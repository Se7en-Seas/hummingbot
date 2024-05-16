# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/util/tendermint_proxy/v1/tendermint_proxy.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tendermint.crypto import proof_pb2 as tendermint_dot_crypto_dot_proof__pb2
from tendermint.p2p import types_pb2 as tendermint_dot_p2p_dot_types__pb2
from tendermint.types import (
    block_pb2 as tendermint_dot_types_dot_block__pb2,
    types_pb2 as tendermint_dot_types_dot_types__pb2,
    validator_pb2 as tendermint_dot_types_dot_validator__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8penumbra/util/tendermint_proxy/v1/tendermint_proxy.proto\x12!penumbra.util.tendermint_proxy.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dtendermint/crypto/proof.proto\x1a\x1atendermint/p2p/types.proto\x1a\x1ctendermint/types/block.proto\x1a\x1ctendermint/types/types.proto\x1a tendermint/types/validator.proto\"+\n\x0cGetTxRequest\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\r\n\x05prove\x18\x02 \x01(\x08\"\x88\x01\n\rGetTxResponse\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x0e\n\x06height\x18\x02 \x01(\x04\x12\r\n\x05index\x18\x03 \x01(\x04\x12>\n\ttx_result\x18\x04 \x01(\x0b\x32+.penumbra.util.tendermint_proxy.v1.TxResult\x12\n\n\x02tx\x18\x05 \x01(\x0c\"s\n\x08TxResult\x12\x0b\n\x03log\x18\x01 \x01(\t\x12\x12\n\ngas_wanted\x18\x02 \x01(\x04\x12\x10\n\x08gas_used\x18\x03 \x01(\x04\x12\x34\n\x04tags\x18\x04 \x03(\x0b\x32&.penumbra.util.tendermint_proxy.v1.Tag\"0\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\r\n\x05index\x18\x03 \x01(\x08\"9\n\x17\x42roadcastTxAsyncRequest\x12\x0e\n\x06params\x18\x01 \x01(\x0c\x12\x0e\n\x06req_id\x18\x02 \x01(\x04\"Q\n\x18\x42roadcastTxAsyncResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\"8\n\x16\x42roadcastTxSyncRequest\x12\x0e\n\x06params\x18\x01 \x01(\x0c\x12\x0e\n\x06req_id\x18\x02 \x01(\x04\"P\n\x17\x42roadcastTxSyncResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\"\x12\n\x10GetStatusRequest\"\xbc\x01\n\x11GetStatusResponse\x12\x32\n\tnode_info\x18\x01 \x01(\x0b\x32\x1f.tendermint.p2p.DefaultNodeInfo\x12>\n\tsync_info\x18\x02 \x01(\x0b\x32+.penumbra.util.tendermint_proxy.v1.SyncInfo\x12\x33\n\x0evalidator_info\x18\x03 \x01(\x0b\x32\x1b.tendermint.types.Validator\"\xa7\x01\n\x08SyncInfo\x12\x19\n\x11latest_block_hash\x18\x01 \x01(\x0c\x12\x17\n\x0flatest_app_hash\x18\x02 \x01(\x0c\x12\x1b\n\x13latest_block_height\x18\x03 \x01(\x04\x12\x35\n\x11latest_block_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x63\x61tching_up\x18\t \x01(\x08\"M\n\x10\x41\x42\x43IQueryRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\r\n\x05prove\x18\x04 \x01(\x08\"\xc0\x01\n\x11\x41\x42\x43IQueryResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\r\n\x05index\x18\x05 \x01(\x03\x12\x0b\n\x03key\x18\x06 \x01(\x0c\x12\r\n\x05value\x18\x07 \x01(\x0c\x12.\n\tproof_ops\x18\x08 \x01(\x0b\x32\x1b.tendermint.crypto.ProofOps\x12\x0e\n\x06height\x18\t \x01(\x03\x12\x11\n\tcodespace\x18\n \x01(\tJ\x04\x08\x02\x10\x03\")\n\x17GetBlockByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\"o\n\x18GetBlockByHeightResponse\x12+\n\x08\x62lock_id\x18\x01 \x01(\x0b\x32\x19.tendermint.types.BlockID\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tendermint.types.Block2\xa7\x06\n\x16TendermintProxyService\x12x\n\tGetStatus\x12\x33.penumbra.util.tendermint_proxy.v1.GetStatusRequest\x1a\x34.penumbra.util.tendermint_proxy.v1.GetStatusResponse\"\x00\x12\x8d\x01\n\x10\x42roadcastTxAsync\x12:.penumbra.util.tendermint_proxy.v1.BroadcastTxAsyncRequest\x1a;.penumbra.util.tendermint_proxy.v1.BroadcastTxAsyncResponse\"\x00\x12\x8a\x01\n\x0f\x42roadcastTxSync\x12\x39.penumbra.util.tendermint_proxy.v1.BroadcastTxSyncRequest\x1a:.penumbra.util.tendermint_proxy.v1.BroadcastTxSyncResponse\"\x00\x12l\n\x05GetTx\x12/.penumbra.util.tendermint_proxy.v1.GetTxRequest\x1a\x30.penumbra.util.tendermint_proxy.v1.GetTxResponse\"\x00\x12x\n\tABCIQuery\x12\x33.penumbra.util.tendermint_proxy.v1.ABCIQueryRequest\x1a\x34.penumbra.util.tendermint_proxy.v1.ABCIQueryResponse\"\x00\x12\x8d\x01\n\x10GetBlockByHeight\x12:.penumbra.util.tendermint_proxy.v1.GetBlockByHeightRequest\x1a;.penumbra.util.tendermint_proxy.v1.GetBlockByHeightResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.util.tendermint_proxy.v1.tendermint_proxy_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETTXREQUEST']._serialized_start=281
  _globals['_GETTXREQUEST']._serialized_end=324
  _globals['_GETTXRESPONSE']._serialized_start=327
  _globals['_GETTXRESPONSE']._serialized_end=463
  _globals['_TXRESULT']._serialized_start=465
  _globals['_TXRESULT']._serialized_end=580
  _globals['_TAG']._serialized_start=582
  _globals['_TAG']._serialized_end=630
  _globals['_BROADCASTTXASYNCREQUEST']._serialized_start=632
  _globals['_BROADCASTTXASYNCREQUEST']._serialized_end=689
  _globals['_BROADCASTTXASYNCRESPONSE']._serialized_start=691
  _globals['_BROADCASTTXASYNCRESPONSE']._serialized_end=772
  _globals['_BROADCASTTXSYNCREQUEST']._serialized_start=774
  _globals['_BROADCASTTXSYNCREQUEST']._serialized_end=830
  _globals['_BROADCASTTXSYNCRESPONSE']._serialized_start=832
  _globals['_BROADCASTTXSYNCRESPONSE']._serialized_end=912
  _globals['_GETSTATUSREQUEST']._serialized_start=914
  _globals['_GETSTATUSREQUEST']._serialized_end=932
  _globals['_GETSTATUSRESPONSE']._serialized_start=935
  _globals['_GETSTATUSRESPONSE']._serialized_end=1123
  _globals['_SYNCINFO']._serialized_start=1126
  _globals['_SYNCINFO']._serialized_end=1293
  _globals['_ABCIQUERYREQUEST']._serialized_start=1295
  _globals['_ABCIQUERYREQUEST']._serialized_end=1372
  _globals['_ABCIQUERYRESPONSE']._serialized_start=1375
  _globals['_ABCIQUERYRESPONSE']._serialized_end=1567
  _globals['_GETBLOCKBYHEIGHTREQUEST']._serialized_start=1569
  _globals['_GETBLOCKBYHEIGHTREQUEST']._serialized_end=1610
  _globals['_GETBLOCKBYHEIGHTRESPONSE']._serialized_start=1612
  _globals['_GETBLOCKBYHEIGHTRESPONSE']._serialized_end=1723
  _globals['_TENDERMINTPROXYSERVICE']._serialized_start=1726
  _globals['_TENDERMINTPROXYSERVICE']._serialized_end=2533
# @@protoc_insertion_point(module_scope)
