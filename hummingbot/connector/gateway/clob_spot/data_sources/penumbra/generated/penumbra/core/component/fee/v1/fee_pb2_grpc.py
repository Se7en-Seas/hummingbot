# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import grpc.experimental

from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.fee.v1 import (
    fee_pb2 as penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2,
)


class QueryServiceStub(object):
    """Query operations for the fee component.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CurrentGasPrices = channel.unary_unary(
                '/penumbra.core.component.fee.v1.QueryService/CurrentGasPrices',
                request_serializer=penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2.CurrentGasPricesRequest.SerializeToString,
                response_deserializer=penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2.CurrentGasPricesResponse.FromString,
                )


class QueryServiceServicer(object):
    """Query operations for the fee component.
    """

    def CurrentGasPrices(self, request, context):
        """Get the current gas prices.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CurrentGasPrices': grpc.unary_unary_rpc_method_handler(
                    servicer.CurrentGasPrices,
                    request_deserializer=penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2.CurrentGasPricesRequest.FromString,
                    response_serializer=penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2.CurrentGasPricesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'penumbra.core.component.fee.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class QueryService(object):
    """Query operations for the fee component.
    """

    @staticmethod
    def CurrentGasPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penumbra.core.component.fee.v1.QueryService/CurrentGasPrices',
            penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2.CurrentGasPricesRequest.SerializeToString,
            penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2.CurrentGasPricesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)