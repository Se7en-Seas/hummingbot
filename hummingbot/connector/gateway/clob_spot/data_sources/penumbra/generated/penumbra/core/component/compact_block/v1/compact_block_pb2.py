# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/core/component/compact_block/v1/compact_block.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.dex.v1 import (
    dex_pb2 as penumbra_dot_core_dot_component_dot_dex_dot_v1_dot_dex__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.fee.v1 import (
    fee_pb2 as penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.sct.v1 import (
    sct_pb2 as penumbra_dot_core_dot_component_dot_sct_dot_v1_dot_sct__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.shielded_pool.v1 import (
    shielded_pool_pb2 as penumbra_dot_core_dot_component_dot_shielded__pool_dot_v1_dot_shielded__pool__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.crypto.tct.v1 import (
    tct_pb2 as penumbra_dot_crypto_dot_tct_dot_v1_dot_tct__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<penumbra/core/component/compact_block/v1/compact_block.proto\x12(penumbra.core.component.compact_block.v1\x1a(penumbra/core/component/dex/v1/dex.proto\x1a(penumbra/core/component/fee/v1/fee.proto\x1a(penumbra/core/component/sct/v1/sct.proto\x1a<penumbra/core/component/shielded_pool/v1/shielded_pool.proto\x1a penumbra/crypto/tct/v1/tct.proto\"\x8a\x05\n\x0c\x43ompactBlock\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12N\n\x0estate_payloads\x18\x02 \x03(\x0b\x32\x36.penumbra.core.component.compact_block.v1.StatePayload\x12=\n\nnullifiers\x18\x03 \x03(\x0b\x32).penumbra.core.component.sct.v1.Nullifier\x12\x36\n\nblock_root\x18\x04 \x01(\x0b\x32\".penumbra.crypto.tct.v1.MerkleRoot\x12\x36\n\nepoch_root\x18\x05 \x01(\x0b\x32\".penumbra.crypto.tct.v1.MerkleRoot\x12\x18\n\x10proposal_started\x18\x06 \x01(\x08\x12O\n\x0e\x66md_parameters\x18\x07 \x01(\x0b\x32\x37.penumbra.core.component.shielded_pool.v1.FmdParameters\x12I\n\x0cswap_outputs\x18\x08 \x03(\x0b\x32\x33.penumbra.core.component.dex.v1.BatchSwapOutputData\x12\x1e\n\x16\x61pp_parameters_updated\x18\t \x01(\x08\x12=\n\ngas_prices\x18\n \x01(\x0b\x32).penumbra.core.component.fee.v1.GasPrices\x12\x41\n\x0e\x61lt_gas_prices\x18\x64 \x03(\x0b\x32).penumbra.core.component.fee.v1.GasPrices\x12\x13\n\x0b\x65poch_index\x18\x0b \x01(\x04\"\xaa\x04\n\x0cStatePayload\x12@\n\x06source\x18\x01 \x01(\x0b\x32\x30.penumbra.core.component.sct.v1.CommitmentSource\x12T\n\trolled_up\x18\x02 \x01(\x0b\x32?.penumbra.core.component.compact_block.v1.StatePayload.RolledUpH\x00\x12K\n\x04note\x18\x03 \x01(\x0b\x32;.penumbra.core.component.compact_block.v1.StatePayload.NoteH\x00\x12K\n\x04swap\x18\x04 \x01(\x0b\x32;.penumbra.core.component.compact_block.v1.StatePayload.SwapH\x00\x1aG\n\x08RolledUp\x12;\n\ncommitment\x18\x01 \x01(\x0b\x32\'.penumbra.crypto.tct.v1.StateCommitment\x1aK\n\x04Note\x12\x43\n\x04note\x18\x02 \x01(\x0b\x32\x35.penumbra.core.component.shielded_pool.v1.NotePayload\x1a\x41\n\x04Swap\x12\x39\n\x04swap\x18\x02 \x01(\x0b\x32+.penumbra.core.component.dex.v1.SwapPayloadB\x0f\n\rstate_payload\"X\n\x18\x43ompactBlockRangeRequest\x12\x14\n\x0cstart_height\x18\x02 \x01(\x04\x12\x12\n\nend_height\x18\x03 \x01(\x04\x12\x12\n\nkeep_alive\x18\x04 \x01(\x08\"j\n\x19\x43ompactBlockRangeResponse\x12M\n\rcompact_block\x18\x01 \x01(\x0b\x32\x36.penumbra.core.component.compact_block.v1.CompactBlock\"%\n\x13\x43ompactBlockRequest\x12\x0e\n\x06height\x18\x01 \x01(\x04\"e\n\x14\x43ompactBlockResponse\x12M\n\rcompact_block\x18\x01 \x01(\x0b\x32\x36.penumbra.core.component.compact_block.v1.CompactBlock2\xbf\x02\n\x0cQueryService\x12\x9e\x01\n\x11\x43ompactBlockRange\x12\x42.penumbra.core.component.compact_block.v1.CompactBlockRangeRequest\x1a\x43.penumbra.core.component.compact_block.v1.CompactBlockRangeResponse0\x01\x12\x8d\x01\n\x0c\x43ompactBlock\x12=.penumbra.core.component.compact_block.v1.CompactBlockRequest\x1a>.penumbra.core.component.compact_block.v1.CompactBlockResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.core.component.compact_block.v1.compact_block_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_COMPACTBLOCK']._serialized_start=329
  _globals['_COMPACTBLOCK']._serialized_end=979
  _globals['_STATEPAYLOAD']._serialized_start=982
  _globals['_STATEPAYLOAD']._serialized_end=1536
  _globals['_STATEPAYLOAD_ROLLEDUP']._serialized_start=1304
  _globals['_STATEPAYLOAD_ROLLEDUP']._serialized_end=1375
  _globals['_STATEPAYLOAD_NOTE']._serialized_start=1377
  _globals['_STATEPAYLOAD_NOTE']._serialized_end=1452
  _globals['_STATEPAYLOAD_SWAP']._serialized_start=1454
  _globals['_STATEPAYLOAD_SWAP']._serialized_end=1519
  _globals['_COMPACTBLOCKRANGEREQUEST']._serialized_start=1538
  _globals['_COMPACTBLOCKRANGEREQUEST']._serialized_end=1626
  _globals['_COMPACTBLOCKRANGERESPONSE']._serialized_start=1628
  _globals['_COMPACTBLOCKRANGERESPONSE']._serialized_end=1734
  _globals['_COMPACTBLOCKREQUEST']._serialized_start=1736
  _globals['_COMPACTBLOCKREQUEST']._serialized_end=1773
  _globals['_COMPACTBLOCKRESPONSE']._serialized_start=1775
  _globals['_COMPACTBLOCKRESPONSE']._serialized_end=1876
  _globals['_QUERYSERVICE']._serialized_start=1879
  _globals['_QUERYSERVICE']._serialized_end=2198
# @@protoc_insertion_point(module_scope)
