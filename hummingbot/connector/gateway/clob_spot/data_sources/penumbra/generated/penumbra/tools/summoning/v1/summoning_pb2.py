# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/tools/summoning/v1/summoning.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.keys.v1 import (
    keys_pb2 as penumbra_dot_core_dot_keys_dot_v1_dot_keys__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.num.v1 import (
    num_pb2 as penumbra_dot_core_dot_num_dot_v1_dot_num__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+penumbra/tools/summoning/v1/summoning.proto\x12\x1bpenumbra.tools.summoning.v1\x1a penumbra/core/keys/v1/keys.proto\x1a\x1epenumbra/core/num/v1/num.proto\"\xdc\x03\n\x12ParticipateRequest\x12L\n\x08identify\x18\x01 \x01(\x0b\x32\x38.penumbra.tools.summoning.v1.ParticipateRequest.IdentifyH\x00\x12T\n\x0c\x63ontribution\x18\x02 \x01(\x0b\x32<.penumbra.tools.summoning.v1.ParticipateRequest.ContributionH\x00\x1a;\n\x08Identify\x12/\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1e.penumbra.core.keys.v1.Address\x1a\xdd\x01\n\x0c\x43ontribution\x12\x39\n\x07updated\x18\x01 \x01(\x0b\x32(.penumbra.tools.summoning.v1.CeremonyCrs\x12H\n\rupdate_proofs\x18\x02 \x01(\x0b\x32\x31.penumbra.tools.summoning.v1.CeremonyLinkingProof\x12H\n\rparent_hashes\x18\x03 \x01(\x0b\x32\x31.penumbra.tools.summoning.v1.CeremonyParentHashesB\x05\n\x03msg\"\xa1\x01\n\x0b\x43\x65remonyCrs\x12\r\n\x05spend\x18\x64 \x01(\x0c\x12\x0e\n\x06output\x18\x65 \x01(\x0c\x12\x16\n\x0e\x64\x65legator_vote\x18\x66 \x01(\x0c\x12\x18\n\x10undelegate_claim\x18g \x01(\x0c\x12\x0c\n\x04swap\x18h \x01(\x0c\x12\x12\n\nswap_claim\x18i \x01(\x0c\x12\x1f\n\x17nullifer_derivation_crs\x18j \x01(\x0c\"\xaa\x01\n\x14\x43\x65remonyLinkingProof\x12\r\n\x05spend\x18\x64 \x01(\x0c\x12\x0e\n\x06output\x18\x65 \x01(\x0c\x12\x16\n\x0e\x64\x65legator_vote\x18\x66 \x01(\x0c\x12\x18\n\x10undelegate_claim\x18g \x01(\x0c\x12\x0c\n\x04swap\x18h \x01(\x0c\x12\x12\n\nswap_claim\x18i \x01(\x0c\x12\x1f\n\x17nullifer_derivation_crs\x18j \x01(\x0c\"\xaa\x01\n\x14\x43\x65remonyParentHashes\x12\r\n\x05spend\x18\x64 \x01(\x0c\x12\x0e\n\x06output\x18\x65 \x01(\x0c\x12\x16\n\x0e\x64\x65legator_vote\x18\x66 \x01(\x0c\x12\x18\n\x10undelegate_claim\x18g \x01(\x0c\x12\x0c\n\x04swap\x18h \x01(\x0c\x12\x12\n\nswap_claim\x18i \x01(\x0c\x12\x1f\n\x17nullifer_derivation_crs\x18j \x01(\x0c\"\x9a\x04\n\x13ParticipateResponse\x12M\n\x08position\x18\x01 \x01(\x0b\x32\x39.penumbra.tools.summoning.v1.ParticipateResponse.PositionH\x00\x12X\n\x0e\x63ontribute_now\x18\x02 \x01(\x0b\x32>.penumbra.tools.summoning.v1.ParticipateResponse.ContributeNowH\x00\x12K\n\x07\x63onfirm\x18\x03 \x01(\x0b\x32\x38.penumbra.tools.summoning.v1.ParticipateResponse.ConfirmH\x00\x1a\xa1\x01\n\x08Position\x12\x10\n\x08position\x18\x01 \x01(\r\x12\x1e\n\x16\x63onnected_participants\x18\x02 \x01(\r\x12\x33\n\rlast_slot_bid\x18\x03 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12.\n\x08your_bid\x18\x04 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x1aI\n\rContributeNow\x12\x38\n\x06parent\x18\x01 \x01(\x0b\x32(.penumbra.tools.summoning.v1.CeremonyCrs\x1a\x17\n\x07\x43onfirm\x12\x0c\n\x04slot\x18\x01 \x01(\x04\x42\x05\n\x03msg2\x92\x01\n\x1a\x43\x65remonyCoordinatorService\x12t\n\x0bParticipate\x12/.penumbra.tools.summoning.v1.ParticipateRequest\x1a\x30.penumbra.tools.summoning.v1.ParticipateResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.tools.summoning.v1.summoning_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PARTICIPATEREQUEST']._serialized_start=143
  _globals['_PARTICIPATEREQUEST']._serialized_end=619
  _globals['_PARTICIPATEREQUEST_IDENTIFY']._serialized_start=329
  _globals['_PARTICIPATEREQUEST_IDENTIFY']._serialized_end=388
  _globals['_PARTICIPATEREQUEST_CONTRIBUTION']._serialized_start=391
  _globals['_PARTICIPATEREQUEST_CONTRIBUTION']._serialized_end=612
  _globals['_CEREMONYCRS']._serialized_start=622
  _globals['_CEREMONYCRS']._serialized_end=783
  _globals['_CEREMONYLINKINGPROOF']._serialized_start=786
  _globals['_CEREMONYLINKINGPROOF']._serialized_end=956
  _globals['_CEREMONYPARENTHASHES']._serialized_start=959
  _globals['_CEREMONYPARENTHASHES']._serialized_end=1129
  _globals['_PARTICIPATERESPONSE']._serialized_start=1132
  _globals['_PARTICIPATERESPONSE']._serialized_end=1670
  _globals['_PARTICIPATERESPONSE_POSITION']._serialized_start=1402
  _globals['_PARTICIPATERESPONSE_POSITION']._serialized_end=1563
  _globals['_PARTICIPATERESPONSE_CONTRIBUTENOW']._serialized_start=1565
  _globals['_PARTICIPATERESPONSE_CONTRIBUTENOW']._serialized_end=1638
  _globals['_PARTICIPATERESPONSE_CONFIRM']._serialized_start=1640
  _globals['_PARTICIPATERESPONSE_CONFIRM']._serialized_end=1663
  _globals['_CEREMONYCOORDINATORSERVICE']._serialized_start=1673
  _globals['_CEREMONYCOORDINATORSERVICE']._serialized_end=1819
# @@protoc_insertion_point(module_scope)
