# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/core/app/v1alpha1/app.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from penumbra.core.component.chain.v1alpha1 import chain_pb2 as penumbra_dot_core_dot_component_dot_chain_dot_v1alpha1_dot_chain__pb2
from penumbra.core.component.stake.v1alpha1 import stake_pb2 as penumbra_dot_core_dot_component_dot_stake_dot_v1alpha1_dot_stake__pb2
from penumbra.core.component.shielded_pool.v1alpha1 import shielded_pool_pb2 as penumbra_dot_core_dot_component_dot_shielded__pool_dot_v1alpha1_dot_shielded__pool__pb2
from penumbra.core.component.governance.v1alpha1 import governance_pb2 as penumbra_dot_core_dot_component_dot_governance_dot_v1alpha1_dot_governance__pb2
from penumbra.core.component.ibc.v1alpha1 import ibc_pb2 as penumbra_dot_core_dot_component_dot_ibc_dot_v1alpha1_dot_ibc__pb2
from penumbra.core.component.fee.v1alpha1 import fee_pb2 as penumbra_dot_core_dot_component_dot_fee_dot_v1alpha1_dot_fee__pb2
from penumbra.core.component.dao.v1alpha1 import dao_pb2 as penumbra_dot_core_dot_component_dot_dao_dot_v1alpha1_dot_dao__pb2
from ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$penumbra/core/app/v1alpha1/app.proto\x12\x1apenumbra.core.app.v1alpha1\x1a\x32penumbra/core/component/chain/v1alpha1/chain.proto\x1a\x32penumbra/core/component/stake/v1alpha1/stake.proto\x1a\x42penumbra/core/component/shielded_pool/v1alpha1/shielded_pool.proto\x1a<penumbra/core/component/governance/v1alpha1/governance.proto\x1a.penumbra/core/component/ibc/v1alpha1/ibc.proto\x1a.penumbra/core/component/fee/v1alpha1/fee.proto\x1a.penumbra/core/component/dao/v1alpha1/dao.proto\x1a\'ibc/core/commitment/v1/commitment.proto\"?\n\x0fKeyValueRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05proof\x18\x03 \x01(\x08\"\xa1\x01\n\x10KeyValueResponse\x12\x41\n\x05value\x18\x01 \x01(\x0b\x32\x32.penumbra.core.app.v1alpha1.KeyValueResponse.Value\x12\x32\n\x05proof\x18\x02 \x01(\x0b\x32#.ibc.core.commitment.v1.MerkleProof\x1a\x16\n\x05Value\x12\r\n\x05value\x18\x01 \x01(\x0c\"6\n\x12PrefixValueRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x0e\n\x06prefix\x18\x02 \x01(\t\"1\n\x13PrefixValueResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xe6\x03\n\rAppParameters\x12M\n\x0c\x63hain_params\x18\x01 \x01(\x0b\x32\x37.penumbra.core.component.chain.v1alpha1.ChainParameters\x12G\n\ndao_params\x18\x02 \x01(\x0b\x32\x33.penumbra.core.component.dao.v1alpha1.DaoParameters\x12\\\n\x11governance_params\x18\x03 \x01(\x0b\x32\x41.penumbra.core.component.governance.v1alpha1.GovernanceParameters\x12G\n\nibc_params\x18\x04 \x01(\x0b\x32\x33.penumbra.core.component.ibc.v1alpha1.IbcParameters\x12M\n\x0cstake_params\x18\x05 \x01(\x0b\x32\x37.penumbra.core.component.stake.v1alpha1.StakeParameters\x12G\n\nfee_params\x18\x06 \x01(\x0b\x32\x33.penumbra.core.component.fee.v1alpha1.FeeParameters\"(\n\x14\x41ppParametersRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\"Z\n\x15\x41ppParametersResponse\x12\x41\n\x0e\x61pp_parameters\x18\x01 \x01(\x0b\x32).penumbra.core.app.v1alpha1.AppParameters\"\x8b\x01\n\x0fGenesisAppState\x12\x45\n\x0fgenesis_content\x18\x01 \x01(\x0b\x32*.penumbra.core.app.v1alpha1.GenesisContentH\x00\x12\x1c\n\x12genesis_checkpoint\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11genesis_app_state\"\xc7\x04\n\x0eGenesisContent\x12M\n\rstake_content\x18\x01 \x01(\x0b\x32\x36.penumbra.core.component.stake.v1alpha1.GenesisContent\x12]\n\x15shielded_pool_content\x18\x02 \x01(\x0b\x32>.penumbra.core.component.shielded_pool.v1alpha1.GenesisContent\x12W\n\x12governance_content\x18\x03 \x01(\x0b\x32;.penumbra.core.component.governance.v1alpha1.GenesisContent\x12I\n\x0bibc_content\x18\x04 \x01(\x0b\x32\x34.penumbra.core.component.ibc.v1alpha1.GenesisContent\x12M\n\rchain_content\x18\x05 \x01(\x0b\x32\x36.penumbra.core.component.chain.v1alpha1.GenesisContent\x12I\n\x0b\x64\x61o_content\x18\x06 \x01(\x0b\x32\x34.penumbra.core.component.dao.v1alpha1.GenesisContent\x12I\n\x0b\x66\x65\x65_content\x18\x07 \x01(\x0b\x32\x34.penumbra.core.component.fee.v1alpha1.GenesisContent2\xdd\x02\n\x0cQueryService\x12t\n\rAppParameters\x12\x30.penumbra.core.app.v1alpha1.AppParametersRequest\x1a\x31.penumbra.core.app.v1alpha1.AppParametersResponse\x12\x65\n\x08KeyValue\x12+.penumbra.core.app.v1alpha1.KeyValueRequest\x1a,.penumbra.core.app.v1alpha1.KeyValueResponse\x12p\n\x0bPrefixValue\x12..penumbra.core.app.v1alpha1.PrefixValueRequest\x1a/.penumbra.core.app.v1alpha1.PrefixValueResponse0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.core.app.v1alpha1.app_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _KEYVALUEREQUEST._serialized_start=487
  _KEYVALUEREQUEST._serialized_end=550
  _KEYVALUERESPONSE._serialized_start=553
  _KEYVALUERESPONSE._serialized_end=714
  _KEYVALUERESPONSE_VALUE._serialized_start=692
  _KEYVALUERESPONSE_VALUE._serialized_end=714
  _PREFIXVALUEREQUEST._serialized_start=716
  _PREFIXVALUEREQUEST._serialized_end=770
  _PREFIXVALUERESPONSE._serialized_start=772
  _PREFIXVALUERESPONSE._serialized_end=821
  _APPPARAMETERS._serialized_start=824
  _APPPARAMETERS._serialized_end=1310
  _APPPARAMETERSREQUEST._serialized_start=1312
  _APPPARAMETERSREQUEST._serialized_end=1352
  _APPPARAMETERSRESPONSE._serialized_start=1354
  _APPPARAMETERSRESPONSE._serialized_end=1444
  _GENESISAPPSTATE._serialized_start=1447
  _GENESISAPPSTATE._serialized_end=1586
  _GENESISCONTENT._serialized_start=1589
  _GENESISCONTENT._serialized_end=2172
  _QUERYSERVICE._serialized_start=2175
  _QUERYSERVICE._serialized_end=2524
# @@protoc_insertion_point(module_scope)
