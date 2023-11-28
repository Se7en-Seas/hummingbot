# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from penumbra.core.app.v1alpha1 import app_pb2 as penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2


class QueryServiceStub(object):
    """Query operations for the overall Penumbra application.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppParameters = channel.unary_unary(
                '/penumbra.core.app.v1alpha1.QueryService/AppParameters',
                request_serializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.AppParametersRequest.SerializeToString,
                response_deserializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.AppParametersResponse.FromString,
                )
        self.KeyValue = channel.unary_unary(
                '/penumbra.core.app.v1alpha1.QueryService/KeyValue',
                request_serializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.KeyValueRequest.SerializeToString,
                response_deserializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.KeyValueResponse.FromString,
                )
        self.PrefixValue = channel.unary_stream(
                '/penumbra.core.app.v1alpha1.QueryService/PrefixValue',
                request_serializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.PrefixValueRequest.SerializeToString,
                response_deserializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.PrefixValueResponse.FromString,
                )


class QueryServiceServicer(object):
    """Query operations for the overall Penumbra application.
    """

    def AppParameters(self, request, context):
        """Gets the app parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeyValue(self, request, context):
        """General-purpose key-value state query API, that can be used to query
        arbitrary keys in the JMT storage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrefixValue(self, request, context):
        """General-purpose prefixed key-value state query API, that can be used to query
        arbitrary prefixes in the JMT storage.
        Returns a stream of `PrefixValueResponse`s.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AppParameters': grpc.unary_unary_rpc_method_handler(
                    servicer.AppParameters,
                    request_deserializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.AppParametersRequest.FromString,
                    response_serializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.AppParametersResponse.SerializeToString,
            ),
            'KeyValue': grpc.unary_unary_rpc_method_handler(
                    servicer.KeyValue,
                    request_deserializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.KeyValueRequest.FromString,
                    response_serializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.KeyValueResponse.SerializeToString,
            ),
            'PrefixValue': grpc.unary_stream_rpc_method_handler(
                    servicer.PrefixValue,
                    request_deserializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.PrefixValueRequest.FromString,
                    response_serializer=penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.PrefixValueResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'penumbra.core.app.v1alpha1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class QueryService(object):
    """Query operations for the overall Penumbra application.
    """

    @staticmethod
    def AppParameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penumbra.core.app.v1alpha1.QueryService/AppParameters',
            penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.AppParametersRequest.SerializeToString,
            penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.AppParametersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeyValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/penumbra.core.app.v1alpha1.QueryService/KeyValue',
            penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.KeyValueRequest.SerializeToString,
            penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.KeyValueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrefixValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/penumbra.core.app.v1alpha1.QueryService/PrefixValue',
            penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.PrefixValueRequest.SerializeToString,
            penumbra_dot_core_dot_app_dot_v1alpha1_dot_app__pb2.PrefixValueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
