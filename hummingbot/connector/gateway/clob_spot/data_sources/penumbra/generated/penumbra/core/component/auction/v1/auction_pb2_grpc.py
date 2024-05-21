# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import grpc.experimental

from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.auction.v1 import (
    auction_pb2 as penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2,
)


class QueryServiceStub(object):
    """Query operations for the auction component.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuctionStateById = channel.unary_unary(
                '/penumbra.core.component.auction.v1.QueryService/AuctionStateById',
                request_serializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdRequest.SerializeToString,
                response_deserializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdResponse.FromString,
                )
        self.AuctionStateByIds = channel.unary_stream(
                '/penumbra.core.component.auction.v1.QueryService/AuctionStateByIds',
                request_serializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdsRequest.SerializeToString,
                response_deserializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdsResponse.FromString,
                )


class QueryServiceServicer(object):
    """Query operations for the auction component.
    """

    def AuctionStateById(self, request, context):
        """Get the current state of an auction by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuctionStateByIds(self, request, context):
        """Get the current state of a group of auctions by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuctionStateById': grpc.unary_unary_rpc_method_handler(
                    servicer.AuctionStateById,
                    request_deserializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdRequest.FromString,
                    response_serializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdResponse.SerializeToString,
            ),
            'AuctionStateByIds': grpc.unary_stream_rpc_method_handler(
                    servicer.AuctionStateByIds,
                    request_deserializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdsRequest.FromString,
                    response_serializer=penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'penumbra.core.component.auction.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class QueryService(object):
    """Query operations for the auction component.
    """

    @staticmethod
    def AuctionStateById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penumbra.core.component.auction.v1.QueryService/AuctionStateById',
            penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdRequest.SerializeToString,
            penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuctionStateByIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/penumbra.core.component.auction.v1.QueryService/AuctionStateByIds',
            penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdsRequest.SerializeToString,
            penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2.AuctionStateByIdsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
