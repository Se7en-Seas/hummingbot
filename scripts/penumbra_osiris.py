import base64
import logging
import os
import sys
import time
from decimal import Decimal
from pprint import pprint
from typing import Any, List

import numpy as np
import pandas as pd
import requests

from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.dex.v1 import (
    dex_pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.dex.v1.dex_pb2_grpc import (
    QueryService as DexQueryService,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.shielded_pool.v1 import (
    shielded_pool_pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.shielded_pool.v1.shielded_pool_pb2_grpc import (
    QueryService,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.keys.v1 import keys_pb2
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.custody.v1 import custody_pb2
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.custody.v1.custody_pb2_grpc import (
    CustodyService,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.view.v1 import view_pb2
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.view.v1.view_pb2_grpc import (
    ViewService,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.penumbra_constants import (
    TOKEN_ADDRESS_MAP,
    TOKEN_SYMBOL_MAP,
)
from hummingbot.core.data_type.common import OrderType, TradeType
from hummingbot.core.data_type.order_candidate import OrderCandidate
from hummingbot.core.event.events import OrderFilledEvent
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase

LP_NFT_OPEN_PREFIX = 'lpnft_opened_'
LP_NFT_CLOSED_PREFIX = 'lpnft_closed_'

# TODO: Consider setting all manual fees to automatic fees instead (for fee_mode https://buf.build/penumbra-zone/penumbra/docs/main:penumbra.view.v1#penumbra.view.v1.TransactionPlannerRequest)

# The original Osiris bot uses binance feeds, so we aim to do the same here
# https://binance-docs.github.io/apidocs/spot/en/#market-data-endpoints
class PenumbraOsiris(ScriptStrategyBase):
    """
    Adapted from SimplePMM strategy example
    Video: -
    Description:
    The bot will place 1 order around at the midpoint between the bid-ask binances prices in a trading_pair. Every order_refresh_time in seconds,
    the bot will cancel and replace the orders.
    """
    #! Note: Penumbra does not current support websocket connections, so the order book must be refreshed by force in each tick before execution logic can begin
    
    # --- Config knobs for the strategy --- 
    # Account number to trade with
    account_number = 0
    
    # Percetage of reserves to trade (0.1 = 10%)
    reserves1_pct = 0.1
    reserves2_pct = 0.1
    
    # The pair on penumbra to trade
    trading_pair = "penumbra-gm"
    # How the trading pair will be priced according to binance price feeds
    reference_pair = "BTC-USDC"
    # ------------------------------------
    
    bid_spread = 0.001
    ask_spread = 0.001
    order_refresh_time = 60
    order_amount = 0.01
    create_timestamp = 0
    exchange = "penumbra"

    markets = {exchange: {trading_pair}}
    _pclientd_url = 'localhost:8081'
    _gateway_url = 'localhost:15888'

    # Override to skip the ready check which depends on websocket connection
    def tick(self, timestamp: float):
        """
        Clock tick entry point, is run every second (on normal tick setting).
        Checks if all connectors are ready, if so the strategy is ready to trade.

        :param timestamp: current tick timestamp
        """
        self.on_tick()

    def on_tick(self):
        # Only run on tick if order_refresh_time is passed to not consume too many resources
        if self.create_timestamp <= self.current_timestamp - self.order_refresh_time:
            total_loop_time = time.time()
            logging.getLogger().info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Refreshing order book ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            logging.getLogger().info("1. Canceling any outstanding orders...")
            start_time = (time.time())
            self.cancel_all_orders()
            print(f"TOTAL Time to cancel all orders: {(time.time()) - start_time}")
            start_time = (time.time())

            logging.getLogger().info("2. Checking price feeds...")
            bid_ask: List[float] = self.create_proposal()
            print(f"TOTAL Time to get price feeds: {(time.time()) - start_time}")
            logging.getLogger().info(f"3. Best bid: {bid_ask[0]} and ask: {bid_ask[1]}")
            start_time = (time.time())

            logging.getLogger().info("4. Creating liquidity position...")
            self.make_liquidity_position(bid_ask)
            print(f"TOTAL Time to create liquidity position: {(time.time()) - start_time}")

            self.create_timestamp = self.order_refresh_time + self.current_timestamp
            print(
                f"~~~~~~~~~ TOTAL Time to refresh order book: {(time.time()) - total_loop_time} ~~~~~~~~~"
            )

    def create_proposal(self) -> List[float]:
        try:
            bookTicker = requests.get(f"https://api.binance.us/api/v3/ticker/bookTicker?symbol={self.reference_pair.replace('-', '')}").json()
            bid_price = bookTicker['bidPrice']
            ask_price = bookTicker['askPrice']
        except:
            logging.getLogger().error("Error fetching bid/ask from binance, is your IP geolocked?")

        return [Decimal(str(bid_price)), Decimal(str(ask_price))]


    def clamp(self, value, min_value, max_value):
        """Clamps a value between a minimum and maximum value."""
        return max(min_value, min(value, max_value))

    def calculate_pct_reserves(self, reserve1, reserve2, reserves1_pct, reserves2_pct):
        """
        Calculates the amount of reserves to use for trading based on the given percentages and clamps them to 80 bits.
        :param reserve1: The first reserve value.
        :param reserve2: The second reserve value.
        :return: Tuple of reserve amounts (r1, r2).
        """
        max_80_bits = 2**80 - 1
        r1 = self.clamp(int(reserve1 * Decimal(str(reserves1_pct))), 0, max_80_bits)
        r2 = self.clamp(int(reserve2 * Decimal(str(reserves2_pct))), 0, max_80_bits)
        
        return [r1, r2]

    def calculate_half_reserves(self, reserve1, reserve2):
        """
        Calculates half of the given reserves and clamps them to 80 bits.
        :param reserve1: The first reserve value.
        :param reserve2: The second reserve value.
        :return: Tuple of clamped half reserves (r1, r2).
        """

        if reserve1 == None or reserve1 == 0:
            logging.getLogger().error(
                "Not enough r1 reserves available to open a position.")
            raise ValueError("No reserves available to open a position.")
        if reserve2 == None or reserve2 == 0:
            logging.getLogger().error(
                "Not enough r2 reserves available to open a position.")
            raise ValueError("No reserves available to open a position.")

        max_80_bits = 2**80 - 1
        half_reserve1 = self.clamp(reserve1 // 2, 0, max_80_bits)
        half_reserve2 = self.clamp(reserve2 // 2, 0, max_80_bits)

        if half_reserve1 == 0 or half_reserve2 == 0:
            logging.getLogger().error(
                "Not enough reserves available to open a position.")
            raise ValueError("No reserves available to open a position.")

        return [half_reserve1, half_reserve2]

    def int_to_lo_hi(self, value):
        """
        Converts a large integer into lo and hi parts for a 128-bit unsigned integer.
        :param value: The integer to be converted.
        :return: A tuple (lo, hi) representing the low and high parts of the integer.
        """
        # Ensure value fits in 128 bits
        if value.bit_length() > 128:
            raise ValueError("Value is too large to fit in 128 bits")

        # Mask to extract 64 bits.
        mask = (1 << 64) - 1

        # Extract lo and hi values.
        lo = value & mask
        hi = (value >> 64) & mask

        return [lo, hi]

    def hi_low_to_human_readable(self, hi, lo, decimals):
        return ((hi << 64) | lo) / (10**decimals)

    def generate_nonce(self):
        """Generate a 32-byte nonce."""
        nonce_bytes = os.urandom(32)
        return nonce_bytes

    def authorize_tx(self, transaction):
        auth_client = CustodyService()

        auth_request = custody_pb2.AuthorizeRequest()
        auth_request.plan.CopyFrom(transaction.plan)

        auth_response = auth_client.Authorize(request=auth_request,target=self._pclientd_url,insecure=True)

        return auth_response
    
    def witness_and_build_tx(self, client, wit_and_build_req):
        wit_and_build_resp_iterator = client.WitnessAndBuild(request=wit_and_build_req,target=self._pclientd_url,insecure=True)
        wit_and_build_resp = None
        
        while True:
            try:
                # Fetch the next response from the iterator
                wit_and_build_resp = next(wit_and_build_resp_iterator)

                # Check which field is set in the oneof status
                status_field = wit_and_build_resp.WhichOneof("status")

                if status_field == "complete":
                    return wit_and_build_resp.complete.transaction
                elif status_field == "build_progress":
                    print(wit_and_build_resp.build_progress)
                    print("Current progress: ", wit_and_build_resp.build_progress.progress)
                else:
                    print("Unexpected response: ", wit_and_build_resp)
                    return None

            except StopIteration:
                # Handle end of iterator (shouldn't happen if server is streaming)
                print("Fatal error thrown, server disconnected prematurely during witness and build step.")
                break
            except Exception as e:
                print(f"Error processing response: {e}")
                time.sleep(1)
                
    def build_and_broadcast_tx(self, client, broadcast_request):
        # Service will await detection on chain
        broadcast_request.await_detection = True

        logging.getLogger().info("Creating order...")
        broadcast_response_iterator = client.BroadcastTransaction(request=broadcast_request,target=self._pclientd_url,insecure=True, timeout=60)
        broadcast_resp = None
        
        while True:
            try:
                # Fetch the next response from the iterator
                broadcast_resp = next(broadcast_response_iterator)

                # Check which field is set in the oneof status
                status_field = broadcast_resp.WhichOneof("status")

                if status_field == "confirmed":
                    return broadcast_resp.confirmed
                elif status_field == "broadcast_success":
                    print("Broadcasted, but awaiting confirmation...")
                else:
                    print("Unexpected response: ", broadcast_resp)
                    return None

            except StopIteration:
                # Handle end of iterator (shouldn't happen if server is streaming)
                print("Fatal error thrown, server disconnected prematurely during build and broadcast step.")
                break
            except Exception as e:
                print(f"Error processing response: {e}")
                time.sleep(1)

    # https://guide.penumbra.zone/main/pclientd/build_transaction.html
    def make_liquidity_position(self, bid_ask: List[int]):
        try:
            start_time = (time.time())

            client = ViewService()
            transactionPlanRequest = view_pb2.TransactionPlannerRequest()
            
            # Set fee mode to automatic medium tier
            # TODO: Consider configurability
            transactionPlanRequest.auto_fee.fee_tier = 2

            # Assuming you have values for fee, p, q, your_trading_pair, your_reserve1, your_reserve2, and your_nonce
            # Set the TradingFunction directly
            trading_function = transactionPlanRequest.position_opens.add().position.phi

            midPrice = Decimal(bid_ask[0] + bid_ask[1]) / 2
            scaling_factor = Decimal('1000')
            midPrice = midPrice * scaling_factor

            while midPrice < 1:
                scaling_factor = scaling_factor * 1000
                midPrice = midPrice * 1000

            # P is always scaling value
            p_val = self.int_to_lo_hi(int(scaling_factor))

            trading_function.component.p.lo = p_val[0]
            trading_function.component.p.hi = p_val[1]

            q_val = self.int_to_lo_hi(int(midPrice))

            trading_function.component.q.lo = q_val[0]
            trading_function.component.q.hi = q_val[1]

            # Calculate spread:
            difference = scaling_factor * abs(bid_ask[1] - bid_ask[0])
            fraction = difference / midPrice
            # max of 50% fee, min of 100 bps (1%)
            spread = fraction * 100 * 100
            spread = max(100, min(spread, 5000))

            trading_function.component.fee = int(spread)

            # Get asset ids from constants file
            asset_1 = TOKEN_SYMBOL_MAP[self.trading_pair.split('-')[0]]
            asset_2 = TOKEN_SYMBOL_MAP[self.trading_pair.split('-')[1]]

            if asset_1 is None:
                logging.getLogger().error(
                    f"Asset {self.trading_pair.split('-')[0]} not found in constants file"
                )
            if asset_2 is None:
                logging.getLogger().error(
                    f"Asset {self.trading_pair.split('-')[1]} not found in constants file"
                )
            # Asset1 must be < Asset2 according to their lexographic order on byte strings
            # https://buf.build/penumbra-zone/penumbra/docs/db38dcb505fd43769a072925543bc500:penumbra.core.component.dex.v1#penumbra.core.component.dex.v1.TradingFunction
            if asset_1['address'] > asset_2['address']:
                tmp = asset_1
                asset_1 = asset_2
                asset_2 = tmp

            trading_function.pair.asset_1.inner = base64.b64decode(
                asset_1['address'])
            trading_function.pair.asset_2.inner = base64.b64decode(
                asset_2['address'])
            
            print(f"Asset 1: {asset_1['address']}")
            print(f"Asset 2: {asset_2['address']}")

            # Set the PositionState directly
            position_state = transactionPlanRequest.position_opens[0].position.state
            position_state.state = 1

            # Set the Reserves directly
            reserves = transactionPlanRequest.position_opens[0].position.reserves

            # TODO: really should be available balances
            # Get all balances
            b_time = (time.time())
            balances = self.get_all_balances()
            print(f"Sub query time to get balances: {(time.time()) - b_time}")

            res1 = balances[asset_1["symbol"]]['amount'] * 10**balances[asset_1["symbol"]]['decimals']
            res2 = balances[asset_2["symbol"]]['amount'] * 10**balances[asset_2["symbol"]]['decimals']

            #reserve1_int, reserve2_int = self.calculate_half_reserves(res1, res2)
            reserve1, reserve2 = self.calculate_pct_reserves(res1, res2, self.reserves1_pct, self.reserves2_pct)

            reserve1 = self.int_to_lo_hi(int(reserve1))
            reserve2 = self.int_to_lo_hi(int(reserve2))

            reserves.r1.lo = reserve1[0]
            reserves.r1.hi = reserve1[1]
            reserves.r2.lo = reserve2[0]
            reserves.r2.hi = reserve2[1]
            
            # Convert back to human readable and log just to sanity check
            print(
                f"Setting {asset_1['symbol']} in Reserve 1: {self.hi_low_to_human_readable(reserves.r1.hi, reserves.r1.lo, balances[asset_1['symbol']]['decimals'])}")
            print(
                f"Setting {asset_2['symbol']} Reserve 2: {self.hi_low_to_human_readable(reserves.r2.hi, reserves.r2.lo, balances[asset_2['symbol']]['decimals'])}")
            
            # Set other fields of Position
            transactionPlanRequest.position_opens[0].position.close_on_fill = False
            transactionPlanRequest.position_opens[0].position.nonce = self.generate_nonce()

            transactionPlanResponse = client.TransactionPlanner(request=transactionPlanRequest,target=self._pclientd_url,insecure=True)

            print(f"Time to get LP transaction plan: {(time.time()) - start_time}")
            start_time = (time.time())

            # Authorize the tx
            authorized_resp = self.authorize_tx(transactionPlanResponse)

            # Witness & Build
            wit_and_build_req = view_pb2.WitnessAndBuildRequest()
            wit_and_build_req.transaction_plan.CopyFrom(transactionPlanResponse.plan)
            wit_and_build_req.authorization_data.CopyFrom(authorized_resp.data)
            tx_to_broadcast = self.witness_and_build_tx(client, wit_and_build_req)
            
            print(f"Time to get LP auth, witness and build: {(time.time()) - start_time}")
            start_time = (time.time())

            # Broadcast
            broadcast_request = view_pb2.BroadcastTransactionRequest()
            broadcast_request.transaction.CopyFrom(tx_to_broadcast)
            broadcast_response = self.build_and_broadcast_tx(client, broadcast_request)
            
            logging.getLogger().info(f"Order created at block {broadcast_response.detection_height} in tx hash: {broadcast_response.id.inner.hex()}")
            print(f"Time to get LP broadcast: {(time.time()) - start_time}")
            #breakpoint()

        except Exception as e:
            logging.getLogger().error(f"Error making liquidity position: {str(e)}")

    # Cancel & withdraw from all orders
    def cancel_all_orders(self):
        start_time = (time.time())
        active_orders, closed_orders = self.get_orders()
        print(f"Time to get orders: {(time.time()) - start_time}")

        client = ViewService()
        # Iterate over dictionary keys
        order_key_list = list(active_orders.keys())

        for order_key in order_key_list:
            try:
                start_time = (time.time())
                transactionPlanRequest = view_pb2.TransactionPlannerRequest()

                # Set fee mode to automatic medium tier
                # TODO: Consider configurability
                transactionPlanRequest.auto_fee.fee_tier = 2

                # Set the Position directly
                position_close_bech32m = transactionPlanRequest.position_closes.add().position_id
                position_close_bech32m.alt_bech32m = active_orders[order_key]['asset'].denom_metadata.display.split(LP_NFT_OPEN_PREFIX)[1]

                transactionPlanResponse = client.TransactionPlanner(request=transactionPlanRequest,target=self._pclientd_url,insecure=True)

                print(f"Time to get Cancel transaction plan: {(time.time()) - start_time}")
                start_time = (time.time())

                # Authorize the tx
                authorized_resp = self.authorize_tx(transactionPlanResponse)
                print(f"Time to get Cancel authorization: {(time.time()) - start_time}")
                start_time = (time.time())

                # Witness & Build
                wit_and_build_req = view_pb2.WitnessAndBuildRequest()
                wit_and_build_req.transaction_plan.CopyFrom(transactionPlanResponse.plan)
                wit_and_build_req.authorization_data.CopyFrom(authorized_resp.data)
                tx_to_broadcast = self.witness_and_build_tx(client, wit_and_build_req)

                print(f"Time to get Cancel witness and build: {(time.time()) - start_time}")
                start_time = (time.time())

                # Broadcast
                broadcast_request = view_pb2.BroadcastTransactionRequest()
                broadcast_request.transaction.CopyFrom(tx_to_broadcast)

                logging.getLogger().info("Deleting order..")
                broadcast_response = self.build_and_broadcast_tx(client, broadcast_request)
                logging.getLogger().info(
                    f"Order deleted at block {broadcast_response.detection_height} in tx hash: {broadcast_response.id.inner.hex()}"
                )
                print(f"Time to get Cancel broadcast: {(time.time()) - start_time}")

                #breakpoint()

            except Exception as e:
                logging.getLogger().error(f"Error cancelling liquidity position: {str(e)}")


        # Withdraw from positions, iterate over closed orders if there were any, and also attempt to withdraw from any active positions since we just closed them
        # Concat the 2 dictionaries
        all_orders = {**active_orders, **closed_orders}
        all_order_keys = list(all_orders.keys())

        for order_key in all_order_keys:
            try:
                start_time = (time.time())
                transactionPlanRequest = view_pb2.TransactionPlannerRequest()

                # Set fee mode to automatic medium tier
                # TODO: Consider configurability
                transactionPlanRequest.auto_fee.fee_tier = 2

                # Get where current position is (active/closed) to figure out what prefix to use
                if LP_NFT_OPEN_PREFIX in all_orders[order_key]['asset'].denom_metadata.display:
                    prefix = LP_NFT_OPEN_PREFIX
                elif LP_NFT_CLOSED_PREFIX in all_orders[order_key]['asset'].denom_metadata.display:
                    prefix = LP_NFT_CLOSED_PREFIX
                #if order_key in active_orders:
                #    prefix = LP_NFT_OPEN_PREFIX
                #elif order_key in closed_orders:
                #    prefix = LP_NFT_CLOSED_PREFIX
                else:
                    logging.Logger().error(f"Could not find prefix for order id: {order_key}")
                    raise ValueError(f"Could not find prefix for order id: {order_key}")

                # Set the Position directly
                position_withdraw_bech32m = transactionPlanRequest.position_withdraws.add().position_id
                position_withdraw_bech32m.alt_bech32m = all_orders[order_key]['asset'].denom_metadata.display.split(prefix)[1] 

                # Set the remaining Reserves
                transactionPlanRequest.position_withdraws[0].reserves.r1.lo = all_orders[order_key]['position'].reserves.r1.lo
                transactionPlanRequest.position_withdraws[0].reserves.r1.hi = all_orders[order_key]['position'].reserves.r1.hi
                transactionPlanRequest.position_withdraws[0].reserves.r2.lo = all_orders[order_key]['position'].reserves.r2.lo
                transactionPlanRequest.position_withdraws[0].reserves.r2.hi = all_orders[order_key]['position'].reserves.r2.hi

                # Set the trading pair
                transactionPlanRequest.position_withdraws[0].trading_pair.asset_1.inner = bytes.fromhex(all_orders[order_key]['position'].phi.pair.asset_1.inner.hex())
                transactionPlanRequest.position_withdraws[0].trading_pair.asset_2.inner = bytes.fromhex(all_orders[order_key]['position'].phi.pair.asset_2.inner.hex())

                transactionPlanResponse = client.TransactionPlanner(request=transactionPlanRequest,target=self._pclientd_url,insecure=True)

                print(f"Time to get Withdraw transaction plan: {(time.time()) - start_time}")
                start_time = (time.time())

                # Authorize the tx
                authorized_resp = self.authorize_tx(transactionPlanResponse)

                print(f"Time to get Withdraw authorization: {(time.time()) - start_time}")
                start_time = (time.time())

                # Witness & Build
                wit_and_build_req = view_pb2.WitnessAndBuildRequest()
                wit_and_build_req.transaction_plan.CopyFrom(transactionPlanResponse.plan)
                wit_and_build_req.authorization_data.CopyFrom(authorized_resp.data)
                tx_to_broadcast = self.witness_and_build_tx(client, wit_and_build_req)
                
                print(f"Time to get Withdraw witness and build: {(time.time()) - start_time}")
                start_time = (time.time())

                # Broadcast
                broadcast_request = view_pb2.BroadcastTransactionRequest()
                broadcast_request.transaction.CopyFrom(tx_to_broadcast)
                
                logging.getLogger().info("Withdrawing from position..")
                broadcast_response = self.build_and_broadcast_tx(client, broadcast_request)
                logging.getLogger().info(
                    f"Withdrawn from position at block {broadcast_response.detection_height} in tx hash: {broadcast_response.id.inner.hex()}"
                )
                print(f"Time to get Withdraw broadcast: {(time.time()) - start_time}")

            except Exception as e:
                logging.getLogger().error(f"Error withdrawing from liquidity position: {str(e)}")


    def did_fill_order(self, event: OrderFilledEvent):
        msg = (f"{event.trade_type.name} {round(event.amount, 2)} {event.trading_pair} {self.exchange} at {round(event.price, 2)}")
        self.log_with_clock(logging.INFO, msg)
        self.notify_hb_app_with_timestamp(msg)

    def get_all_balances(self, account_number: int = 0):
        # Create new grpc.Channel + client
        client = ViewService()
        request = view_pb2.BalancesRequest()
        request.account_filter.account = account_number
        query_client = QueryService()

        start_time = (time.time())
        logging.getLogger().info("Getting all balances...")
        responses = client.Balances(request=request,target=self._pclientd_url,insecure=True)
        print(f"Time to get Balances: {(time.time()) - start_time}")
        #logging.getLogger().info(f"Time to get Balances: {(time.time()) - start_time}")

        balance_dict = {}

        start_time = (time.time())
        for response in responses:
            #print(response)

            try: 
                balance = {
                    "amount":
                    response.balance_view.known_asset_id.amount.lo,
                    "asset_id":
                        bytes.fromhex(
                            response.balance_view.known_asset_id.metadata.penumbra_asset_id.inner.hex())
                }
            except Exception as e:
                #print("Unkown asset balance found, disregarding...")
                #logging.getLogger().error(f"Unkown asset balance found, disregarding... {str(e)}")
                continue

            # ! You can query denoms directly but this makes things significantly slower (22+ seconds), use constants file for speed
            '''
            denom_req = shielded_pool_pb2.DenomMetadataByIdRequest()
            denom_req.asset_id.inner = balance["asset_id"]

            # Query for metadata from DenomMetadataById
            denom_res = query_client.DenomMetadataById(
                request=denom_req,
                target=self._pclientd_url,
                insecure=True)

            if not denom_res.denom_metadata.denom_units:
                decimals = 0
            else:
                decimals = denom_res.denom_metadata.denom_units[0].exponent

            symbol = denom_res.denom_metadata.display
            '''
            try:
                token_address = base64.b64encode(bytes.fromhex(response.balance_view.known_asset_id.metadata.penumbra_asset_id.inner.hex())).decode('utf-8')

                if token_address not in TOKEN_ADDRESS_MAP:
                    #print("Token not found in TOKEN_ADDRESS_MAP: ", token_address)
                    #logging.getLogger().error(f"Token not found in TOKEN_ADDRESS_MAP: {token_address}")
                    #! This will skip tokens not in the TOKEN_ADDRESS_MAP, so make sure your trading pair is in there
                    continue
            except Exception as e:
                logging.getLogger().error(f"Could not serialize token address, disregarding... {str(e)}")
                continue
            
            #logging.getLogger().info(f"Token found in TOKEN_ADDRESS_MAP: {token_address}")

            decimals = TOKEN_ADDRESS_MAP[token_address]['decimals']
            symbol = TOKEN_ADDRESS_MAP[token_address]['symbol']

            # amount's are uint 128 bit https://buf.build/penumbra-zone/penumbra/docs/300a488c79c9490d86cf09e1eceff593:penumbra.core.num.v1alpha1#penumbra.core.num.v1alpha1.Amount
            balance = Decimal(str(self.hi_low_to_human_readable(response.balance_view.known_asset_id.amount.hi, response.balance_view.known_asset_id.amount.lo, decimals)))
            #logging.getLogger().info(f"Balance for {symbol}: {balance}")

            balance_dict[symbol] = {
                "asset_id_str":
                base64.b64encode(
                    bytes.fromhex(
                        response.balance_view.known_asset_id.metadata.penumbra_asset_id.inner.hex())).decode(
                            'utf-8'),
                "asset_id_bytes":
                bytes.fromhex(response.balance_view.known_asset_id.metadata.penumbra_asset_id.inner.hex()),
                "amount":
                balance,
                "decimals":
                decimals,
            }
            #logging.getLogger().info(f"Running balance dict: {balance_dict[symbol]}")
        print(f"Time to query all denoms & process data: {(time.time()) - start_time}")
        #logging.getLogger().info(f"Time to query all denoms & process data: {(time.time()) - start_time}")

        '''
        example return: 
        {
            'test_usd': {'amount': 7.952016459889115,
                         'asset_id_bytes': b'\xad\xeb\xa6\xef\x04&\x93\xfa0\x82\xf1\x8c'
                                b'X\xc6g\xff\xa4E=]\xb8\xcc\x82\xaa'
                                b'\xddn\x88\x9f\xf5\xb0f\x08',
                        'asset_id_str': 'reum7wQmk/owgvGMWMZn/6RFPV24zIKq3W6In/WwZgg='}
                    }
        }
        '''
        print("Balances: ")
        for key in balance_dict:
            print(key, str(balance_dict[key]['amount']))
            
        #pprint(balance_dict)
        #logging.getLogger().info("Balances: ")
        #logging.getLogger().info(balance_dict)
        return balance_dict

    def get_balance_df(self):
        """
        Returns a data frame for all asset balances for displaying purpose.
        """
        columns: List[str] = [
            "Exchange", "Asset", "Available Balance"
        ]
        data: List[Any] = []

        #! Get all balances first
        all_balances = self.get_all_balances(account_number=self.account_number)

        for asset in self.trading_pair.split('-'):
            balance = 0
            if asset in all_balances:
                balance = all_balances[asset]['amount']

            data.append([
                self.exchange,
                asset,
                float(balance),
            ])

        df = pd.DataFrame(data=data, columns=columns).replace(np.nan,
                                                              '',
                                                              regex=True)
        df.sort_values(by=["Exchange", "Asset"], inplace=True)
        return df

    def get_orders(self):
        client = ViewService()
        query_client = DexQueryService()

        # Get all the cleaned assets
        assets_req = view_pb2.AssetsRequest()
        assets_req.include_lp_nfts = True
        assets = client.Assets(request=assets_req,target=self._pclientd_url,insecure=True)

        cleaned_assets = {}

        for asset in assets:
            # Only get assets with prefix 'lpnft_opened' or 'lpnft_closed'

            denomDisplay = asset.denom_metadata.display

            if str(denomDisplay).startswith(LP_NFT_OPEN_PREFIX) or str(denomDisplay).startswith(LP_NFT_CLOSED_PREFIX):
                asset_id = base64.b64encode(bytes.fromhex(asset.denom_metadata.penumbra_asset_id.inner.hex()))
                cleaned_assets[asset_id] = asset

        # Get all the notes
        notes_req = view_pb2.NotesRequest()
        notes_req.include_spent = False

        notes_resp = client.Notes(request=notes_req,target=self._pclientd_url,insecure=True)

        active_liq_positions = {}
        closed_liq_positions = {}

        for note in notes_resp:
            id_byte_str =  base64.b64encode(bytes.fromhex(note.note_record.note.value.asset_id.inner.hex()))

            # Associate the note with it's relevant asset in cleaned_assets by matching on penumbra_asset_id.inner & id_str
            if id_byte_str in cleaned_assets:
                # Get Position Data
                liq_request = dex_pb2.LiquidityPositionByIdRequest()

                # get the current prefix
                if str(cleaned_assets[id_byte_str].denom_metadata.display).startswith(LP_NFT_OPEN_PREFIX):
                    current_prefix = LP_NFT_OPEN_PREFIX
                elif str(cleaned_assets[id_byte_str].denom_metadata.display).startswith(LP_NFT_CLOSED_PREFIX):
                    current_prefix = LP_NFT_CLOSED_PREFIX
                else:
                    logging.getLogger().error(f"Prefix unsupported: {id_byte_str}")
                    raise ValueError(f"Prefix unsupported: {id_byte_str}")

                liq_request.position_id.alt_bech32m = str(
                    cleaned_assets[id_byte_str].denom_metadata.display).split(
                        current_prefix)[1]

                response = query_client.LiquidityPositionById(request=liq_request,target=self._pclientd_url,insecure=True)

                position = response.data

                # Only add to list if position is open
                if position.state.state == 1:
                    active_liq_positions[id_byte_str] = {
                        'note': note,
                        'asset': cleaned_assets[id_byte_str],
                        'position': response.data
                    }
                elif position.state.state == 2:
                    closed_liq_positions[id_byte_str] = {
                        'note': note,
                        'asset': cleaned_assets[id_byte_str],
                        'position': response.data
                    }
        #print("Active positions: ", active_liq_positions)

        return active_liq_positions, closed_liq_positions

    def active_orders_df(self):
        """
        Return a data frame of all active orders for displaying purpose.
        """
        columns = ["Exchange", "Market", "Status", "Reserves 1", "Reserves 2", "Price"]
        data = []

        open_orders, closed_orders = self.get_orders()
        all_orders = {**open_orders, **closed_orders}
        all_order_keys = list(all_orders.keys())

        for order_key in all_order_keys:
            order = all_orders[order_key]

            state = "Unknown"

            if order['position'].state.state == 1:
                state = "Open"
            elif order['position'].state.state == 2:
                state = "Closed"

            # Get decimals from const
            r1_address = base64.b64encode(bytes.fromhex(order['position'].phi.pair.asset_1.inner.hex())).decode('utf-8')
            r1_decimals = TOKEN_ADDRESS_MAP[r1_address]['decimals']
            reserves_1_num = self.hi_low_to_human_readable(
                order['position'].reserves.r1.hi,
                order['position'].reserves.r1.lo, r1_decimals)

            r2_address = base64.b64encode(bytes.fromhex(order['position'].phi.pair.asset_2.inner.hex())).decode('utf-8')
            r2_decimals = TOKEN_ADDRESS_MAP[r2_address]['decimals']

            reserves_2_num = self.hi_low_to_human_readable(
                order['position'].reserves.r2.hi,
                order['position'].reserves.r2.lo, r2_decimals)

            p_human = self.hi_low_to_human_readable(
                order['position'].phi.component.q.hi,
                order['position'].phi.component.q.lo, r1_decimals)
            q_human = self.hi_low_to_human_readable(
                order['position'].phi.component.p.hi,
                order['position'].phi.component.p.lo, r2_decimals)
            
            # Truncate to 2 decimal places
            price_human = round(p_human / q_human, 2)

            data.append([
                self.exchange,
                self.trading_pair,
                state,
                str(round(float(reserves_1_num),2)) + ' ' + TOKEN_ADDRESS_MAP[r1_address]['symbol'],
                str(round(float(reserves_2_num),2)) + ' ' + TOKEN_ADDRESS_MAP[r2_address]['symbol'],
                f"{price_human} {TOKEN_ADDRESS_MAP[r1_address]['symbol']}/{TOKEN_ADDRESS_MAP[r2_address]['symbol']}"
            ])

        if not data:
            raise ValueError

        df = pd.DataFrame(data=data, columns=columns)
        df.sort_values(by=["Exchange", "Market", "Status"], inplace=True)
        return df

    def format_dataframe(self, df: pd.DataFrame, padding: int = 3) -> str:
        # Find the maximum width for each column and add extra padding
        max_widths = {col: max(df[col].astype(str).apply(len).max(), len(col)) + padding
                      for col in df.columns}

        # Create a formatter for each column that right-aligns the text with the added padding
        formatters = {col: lambda x, w=max_widths[col]: f"{x: >{w}}"
                      for col in df.columns}

        # Convert DataFrame to string using the custom formatters
        return df.to_string(index=False, formatters=formatters)

    def format_status(self) -> str:
        lines = []
        # Assume this method exists and fetches some warning lines
        # warning_lines.extend(self.network_warning(self.get_market_trading_pair_tuples()))

        balance_df = self.get_balance_df()
        lines.extend(["", "  Balances:"] + [
            "    " + line
            for line in self.format_dataframe(balance_df).split("\n")
        ])

        try:
            df = self.active_orders_df()
            lines.extend(["", "  Orders:"] + [
                "    " + line for line in self.format_dataframe(df).split("\n")
            ])
        except ValueError:
            lines.extend(["", "  No active maker orders."])

        return "\n".join(lines)