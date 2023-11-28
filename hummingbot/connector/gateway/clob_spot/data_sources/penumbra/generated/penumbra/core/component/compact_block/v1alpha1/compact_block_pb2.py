# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/core/component/compact_block/v1alpha1/compact_block.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from penumbra.crypto.tct.v1alpha1 import tct_pb2 as penumbra_dot_crypto_dot_tct_dot_v1alpha1_dot_tct__pb2
from penumbra.core.component.sct.v1alpha1 import sct_pb2 as penumbra_dot_core_dot_component_dot_sct_dot_v1alpha1_dot_sct__pb2
from penumbra.core.component.chain.v1alpha1 import chain_pb2 as penumbra_dot_core_dot_component_dot_chain_dot_v1alpha1_dot_chain__pb2
from penumbra.core.component.dex.v1alpha1 import dex_pb2 as penumbra_dot_core_dot_component_dot_dex_dot_v1alpha1_dot_dex__pb2
from penumbra.core.component.fee.v1alpha1 import fee_pb2 as penumbra_dot_core_dot_component_dot_fee_dot_v1alpha1_dot_fee__pb2
from penumbra.core.component.shielded_pool.v1alpha1 import shielded_pool_pb2 as penumbra_dot_core_dot_component_dot_shielded__pool_dot_v1alpha1_dot_shielded__pool__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBpenumbra/core/component/compact_block/v1alpha1/compact_block.proto\x12.penumbra.core.component.compact_block.v1alpha1\x1a&penumbra/crypto/tct/v1alpha1/tct.proto\x1a.penumbra/core/component/sct/v1alpha1/sct.proto\x1a\x32penumbra/core/component/chain/v1alpha1/chain.proto\x1a.penumbra/core/component/dex/v1alpha1/dex.proto\x1a.penumbra/core/component/fee/v1alpha1/fee.proto\x1a\x42penumbra/core/component/shielded_pool/v1alpha1/shielded_pool.proto\"\xd4\x04\n\x0c\x43ompactBlock\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12T\n\x0estate_payloads\x18\x02 \x03(\x0b\x32<.penumbra.core.component.compact_block.v1alpha1.StatePayload\x12\x43\n\nnullifiers\x18\x03 \x03(\x0b\x32/.penumbra.core.component.sct.v1alpha1.Nullifier\x12<\n\nblock_root\x18\x04 \x01(\x0b\x32(.penumbra.crypto.tct.v1alpha1.MerkleRoot\x12<\n\nepoch_root\x18\x11 \x01(\x0b\x32(.penumbra.crypto.tct.v1alpha1.MerkleRoot\x12\x18\n\x10proposal_started\x18\x14 \x01(\x08\x12M\n\x0e\x66md_parameters\x18\x64 \x01(\x0b\x32\x35.penumbra.core.component.chain.v1alpha1.FmdParameters\x12O\n\x0cswap_outputs\x18\x05 \x03(\x0b\x32\x39.penumbra.core.component.dex.v1alpha1.BatchSwapOutputData\x12\x1e\n\x16\x61pp_parameters_updated\x18\x06 \x01(\x08\x12\x43\n\ngas_prices\x18\x07 \x01(\x0b\x32/.penumbra.core.component.fee.v1alpha1.GasPrices\"\x96\x05\n\x0cStatePayload\x12Z\n\trolled_up\x18\x01 \x01(\x0b\x32\x45.penumbra.core.component.compact_block.v1alpha1.StatePayload.RolledUpH\x00\x12Q\n\x04note\x18\x02 \x01(\x0b\x32\x41.penumbra.core.component.compact_block.v1alpha1.StatePayload.NoteH\x00\x12Q\n\x04swap\x18\x03 \x01(\x0b\x32\x41.penumbra.core.component.compact_block.v1alpha1.StatePayload.SwapH\x00\x1aM\n\x08RolledUp\x12\x41\n\ncommitment\x18\x01 \x01(\x0b\x32-.penumbra.crypto.tct.v1alpha1.StateCommitment\x1a\x95\x01\n\x04Note\x12\x42\n\x06source\x18\x01 \x01(\x0b\x32\x32.penumbra.core.component.chain.v1alpha1.NoteSource\x12I\n\x04note\x18\x02 \x01(\x0b\x32;.penumbra.core.component.shielded_pool.v1alpha1.NotePayload\x1a\x8b\x01\n\x04Swap\x12\x42\n\x06source\x18\x01 \x01(\x0b\x32\x32.penumbra.core.component.chain.v1alpha1.NoteSource\x12?\n\x04swap\x18\x02 \x01(\x0b\x32\x31.penumbra.core.component.dex.v1alpha1.SwapPayloadB\x0f\n\rstate_payload\"j\n\x18\x43ompactBlockRangeRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\x12\x14\n\x0cstart_height\x18\x02 \x01(\x04\x12\x12\n\nend_height\x18\x03 \x01(\x04\x12\x12\n\nkeep_alive\x18\x04 \x01(\x08\"p\n\x19\x43ompactBlockRangeResponse\x12S\n\rcompact_block\x18\x01 \x01(\x0b\x32<.penumbra.core.component.compact_block.v1alpha1.CompactBlock2\xbb\x01\n\x0cQueryService\x12\xaa\x01\n\x11\x43ompactBlockRange\x12H.penumbra.core.component.compact_block.v1alpha1.CompactBlockRangeRequest\x1aI.penumbra.core.component.compact_block.v1alpha1.CompactBlockRangeResponse0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.core.component.compact_block.v1alpha1.compact_block_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMPACTBLOCK._serialized_start=423
  _COMPACTBLOCK._serialized_end=1019
  _STATEPAYLOAD._serialized_start=1022
  _STATEPAYLOAD._serialized_end=1684
  _STATEPAYLOAD_ROLLEDUP._serialized_start=1296
  _STATEPAYLOAD_ROLLEDUP._serialized_end=1373
  _STATEPAYLOAD_NOTE._serialized_start=1376
  _STATEPAYLOAD_NOTE._serialized_end=1525
  _STATEPAYLOAD_SWAP._serialized_start=1528
  _STATEPAYLOAD_SWAP._serialized_end=1667
  _COMPACTBLOCKRANGEREQUEST._serialized_start=1686
  _COMPACTBLOCKRANGEREQUEST._serialized_end=1792
  _COMPACTBLOCKRANGERESPONSE._serialized_start=1794
  _COMPACTBLOCKRANGERESPONSE._serialized_end=1906
  _QUERYSERVICE._serialized_start=1909
  _QUERYSERVICE._serialized_end=2096
# @@protoc_insertion_point(module_scope)
