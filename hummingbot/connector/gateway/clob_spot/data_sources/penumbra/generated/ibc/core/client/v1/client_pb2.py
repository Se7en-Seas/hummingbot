# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/client.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fibc/core/client/v1/client.proto\x12\x12ibc.core.client.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"V\n\x15IdentifiedClientState\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12*\n\x0c\x63lient_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"{\n\x18\x43onsensusStateWithHeight\x12\x30\n\x06height\x18\x01 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12-\n\x0f\x63onsensus_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"x\n\x15\x43lientConsensusStates\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12L\n\x10\x63onsensus_states\x18\x02 \x03(\x0b\x32,.ibc.core.client.v1.ConsensusStateWithHeightB\x04\xc8\xde\x1f\x00\"D\n\x06Height\x12\x17\n\x0frevision_number\x18\x01 \x01(\x04\x12\x17\n\x0frevision_height\x18\x02 \x01(\x04:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"!\n\x06Params\x12\x17\n\x0f\x61llowed_clients\x18\x01 \x03(\tB:Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.client_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/types'
  _CONSENSUSSTATEWITHHEIGHT.fields_by_name['height']._options = None
  _CONSENSUSSTATEWITHHEIGHT.fields_by_name['height']._serialized_options = b'\310\336\037\000'
  _CLIENTCONSENSUSSTATES.fields_by_name['consensus_states']._options = None
  _CLIENTCONSENSUSSTATES.fields_by_name['consensus_states']._serialized_options = b'\310\336\037\000'
  _HEIGHT._options = None
  _HEIGHT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _IDENTIFIEDCLIENTSTATE._serialized_start=104
  _IDENTIFIEDCLIENTSTATE._serialized_end=190
  _CONSENSUSSTATEWITHHEIGHT._serialized_start=192
  _CONSENSUSSTATEWITHHEIGHT._serialized_end=315
  _CLIENTCONSENSUSSTATES._serialized_start=317
  _CLIENTCONSENSUSSTATES._serialized_end=437
  _HEIGHT._serialized_start=439
  _HEIGHT._serialized_end=507
  _PARAMS._serialized_start=509
  _PARAMS._serialized_end=542
# @@protoc_insertion_point(module_scope)
