# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/core/component/fee/v1alpha1/fee.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from penumbra.core.num.v1alpha1 import num_pb2 as penumbra_dot_core_dot_num_dot_v1alpha1_dot_num__pb2
from penumbra.core.asset.v1alpha1 import asset_pb2 as penumbra_dot_core_dot_asset_dot_v1alpha1_dot_asset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.penumbra/core/component/fee/v1alpha1/fee.proto\x12$penumbra.core.component.fee.v1alpha1\x1a$penumbra/core/num/v1alpha1/num.proto\x1a(penumbra/core/asset/v1alpha1/asset.proto\"r\n\x03\x46\x65\x65\x12\x32\n\x06\x61mount\x18\x01 \x01(\x0b\x32\".penumbra.core.num.v1alpha1.Amount\x12\x37\n\x08\x61sset_id\x18\x02 \x01(\x0b\x32%.penumbra.core.asset.v1alpha1.AssetId\"~\n\tGasPrices\x12\x19\n\x11\x62lock_space_price\x18\x01 \x01(\x04\x12!\n\x19\x63ompact_block_space_price\x18\x02 \x01(\x04\x12\x1a\n\x12verification_price\x18\x03 \x01(\x04\x12\x17\n\x0f\x65xecution_price\x18\x04 \x01(\x04\"\x0f\n\rFeeParameters\"\x9e\x01\n\x0eGenesisContent\x12G\n\nfee_params\x18\x01 \x01(\x0b\x32\x33.penumbra.core.component.fee.v1alpha1.FeeParameters\x12\x43\n\ngas_prices\x18\x02 \x01(\x0b\x32/.penumbra.core.component.fee.v1alpha1.GasPricesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.core.component.fee.v1alpha1.fee_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FEE._serialized_start=168
  _FEE._serialized_end=282
  _GASPRICES._serialized_start=284
  _GASPRICES._serialized_end=410
  _FEEPARAMETERS._serialized_start=412
  _FEEPARAMETERS._serialized_end=427
  _GENESISCONTENT._serialized_start=430
  _GENESISCONTENT._serialized_end=588
# @@protoc_insertion_point(module_scope)