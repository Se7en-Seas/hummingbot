# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/core/component/stake/v1/stake.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.asset.v1 import (
    asset_pb2 as penumbra_dot_core_dot_asset_dot_v1_dot_asset__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.sct.v1 import (
    sct_pb2 as penumbra_dot_core_dot_component_dot_sct_dot_v1_dot_sct__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.keys.v1 import (
    keys_pb2 as penumbra_dot_core_dot_keys_dot_v1_dot_keys__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.num.v1 import (
    num_pb2 as penumbra_dot_core_dot_num_dot_v1_dot_num__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,penumbra/core/component/stake/v1/stake.proto\x12 penumbra.core.component.stake.v1\x1a\"penumbra/core/asset/v1/asset.proto\x1a(penumbra/core/component/sct/v1/sct.proto\x1a penumbra/core/keys/v1/keys.proto\x1a\x1epenumbra/core/num/v1/num.proto\"\'\n\x16ZKUndelegateClaimProof\x12\r\n\x05inner\x18\x01 \x01(\x0c\"\xc2\x02\n\tValidator\x12\x38\n\x0cidentity_key\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x15\n\rconsensus_key\x18\x02 \x01(\x0c\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x08 \x01(\x08\x12H\n\x0f\x66unding_streams\x18\x06 \x03(\x0b\x32/.penumbra.core.component.stake.v1.FundingStream\x12\x17\n\x0fsequence_number\x18\x07 \x01(\r\x12<\n\x0egovernance_key\x18\t \x01(\x0b\x32$.penumbra.core.keys.v1.GovernanceKey\"K\n\rValidatorList\x12:\n\x0evalidator_keys\x18\x01 \x03(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"\xa0\x02\n\rFundingStream\x12O\n\nto_address\x18\x01 \x01(\x0b\x32\x39.penumbra.core.component.stake.v1.FundingStream.ToAddressH\x00\x12\\\n\x11to_community_pool\x18\x02 \x01(\x0b\x32?.penumbra.core.component.stake.v1.FundingStream.ToCommunityPoolH\x00\x1a.\n\tToAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08rate_bps\x18\x02 \x01(\r\x1a#\n\x0fToCommunityPool\x12\x10\n\x08rate_bps\x18\x02 \x01(\rB\x0b\n\trecipient\"\xd9\x01\n\x08RateData\x12\x38\n\x0cidentity_key\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x17\n\x0b\x65poch_index\x18\x02 \x01(\x04\x42\x02\x18\x01\x12;\n\x15validator_reward_rate\x18\x04 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12=\n\x17validator_exchange_rate\x18\x05 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\"\x95\x01\n\x0c\x42\x61seRateData\x12\x13\n\x0b\x65poch_index\x18\x01 \x01(\x04\x12\x36\n\x10\x62\x61se_reward_rate\x18\x02 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x38\n\x12\x62\x61se_exchange_rate\x18\x03 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\"\x87\x02\n\x0fValidatorStatus\x12\x38\n\x0cidentity_key\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12?\n\x05state\x18\x02 \x01(\x0b\x32\x30.penumbra.core.component.stake.v1.ValidatorState\x12\x32\n\x0cvoting_power\x18\x03 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x45\n\rbonding_state\x18\x04 \x01(\x0b\x32..penumbra.core.component.stake.v1.BondingState\"\xb2\x02\n\x0c\x42ondingState\x12N\n\x05state\x18\x01 \x01(\x0e\x32?.penumbra.core.component.stake.v1.BondingState.BondingStateEnum\x12\x1c\n\x10unbonds_at_epoch\x18\x02 \x01(\x04\x42\x02\x18\x01\x12\x19\n\x11unbonds_at_height\x18\x03 \x01(\x04\"\x98\x01\n\x10\x42ondingStateEnum\x12\"\n\x1e\x42ONDING_STATE_ENUM_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x42ONDING_STATE_ENUM_BONDED\x10\x01\x12 \n\x1c\x42ONDING_STATE_ENUM_UNBONDING\x10\x02\x12\x1f\n\x1b\x42ONDING_STATE_ENUM_UNBONDED\x10\x03\"\xf0\x02\n\x0eValidatorState\x12R\n\x05state\x18\x01 \x01(\x0e\x32\x43.penumbra.core.component.stake.v1.ValidatorState.ValidatorStateEnum\"\x89\x02\n\x12ValidatorStateEnum\x12$\n VALIDATOR_STATE_ENUM_UNSPECIFIED\x10\x00\x12 \n\x1cVALIDATOR_STATE_ENUM_DEFINED\x10\x01\x12!\n\x1dVALIDATOR_STATE_ENUM_INACTIVE\x10\x02\x12\x1f\n\x1bVALIDATOR_STATE_ENUM_ACTIVE\x10\x03\x12\x1f\n\x1bVALIDATOR_STATE_ENUM_JAILED\x10\x04\x12#\n\x1fVALIDATOR_STATE_ENUM_TOMBSTONED\x10\x05\x12!\n\x1dVALIDATOR_STATE_ENUM_DISABLED\x10\x06\"\xd1\x01\n\rValidatorInfo\x12>\n\tvalidator\x18\x01 \x01(\x0b\x32+.penumbra.core.component.stake.v1.Validator\x12\x41\n\x06status\x18\x02 \x01(\x0b\x32\x31.penumbra.core.component.stake.v1.ValidatorStatus\x12=\n\trate_data\x18\x03 \x01(\x0b\x32*.penumbra.core.component.stake.v1.RateData\"g\n\x13ValidatorDefinition\x12>\n\tvalidator\x18\x01 \x01(\x0b\x32+.penumbra.core.component.stake.v1.Validator\x12\x10\n\x08\x61uth_sig\x18\x02 \x01(\x0c\"\xcf\x01\n\x08\x44\x65legate\x12>\n\x12validator_identity\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x13\n\x0b\x65poch_index\x18\x02 \x01(\x04\x12\x35\n\x0funbonded_amount\x18\x03 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x37\n\x11\x64\x65legation_amount\x18\x04 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\"\x96\x02\n\nUndelegate\x12>\n\x12validator_identity\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x1d\n\x11start_epoch_index\x18\x02 \x01(\x04\x42\x02\x18\x01\x12\x35\n\x0funbonded_amount\x18\x03 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x37\n\x11\x64\x65legation_amount\x18\x04 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x39\n\nfrom_epoch\x18\x05 \x01(\x0b\x32%.penumbra.core.component.sct.v1.Epoch\"e\n\x0fUndelegateClaim\x12\x43\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x35.penumbra.core.component.stake.v1.UndelegateClaimBody\x12\r\n\x05proof\x18\x02 \x01(\x0c\"\x97\x02\n\x13UndelegateClaimBody\x12>\n\x12validator_identity\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x1d\n\x11start_epoch_index\x18\x02 \x01(\x04\x42\x02\x18\x01\x12:\n\x07penalty\x18\x03 \x01(\x0b\x32).penumbra.core.component.stake.v1.Penalty\x12\x45\n\x12\x62\x61lance_commitment\x18\x04 \x01(\x0b\x32).penumbra.core.asset.v1.BalanceCommitment\x12\x1e\n\x16unbonding_start_height\x18\x05 \x01(\x04\"\xd6\x02\n\x13UndelegateClaimPlan\x12>\n\x12validator_identity\x18\x01 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x1d\n\x11start_epoch_index\x18\x02 \x01(\x04\x42\x02\x18\x01\x12:\n\x07penalty\x18\x04 \x01(\x0b\x32).penumbra.core.component.stake.v1.Penalty\x12\x36\n\x10unbonding_amount\x18\x05 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x18\n\x10\x62\x61lance_blinding\x18\x06 \x01(\x0c\x12\x18\n\x10proof_blinding_r\x18\x07 \x01(\x0c\x12\x18\n\x10proof_blinding_s\x18\x08 \x01(\x0c\x12\x1e\n\x16unbonding_start_height\x18\t \x01(\x04\"\x99\x01\n\x11\x44\x65legationChanges\x12?\n\x0b\x64\x65legations\x18\x01 \x03(\x0b\x32*.penumbra.core.component.stake.v1.Delegate\x12\x43\n\rundelegations\x18\x02 \x03(\x0b\x32,.penumbra.core.component.stake.v1.Undelegate\"H\n\x06Uptime\x12\x1a\n\x12\x61s_of_block_height\x18\x01 \x01(\x04\x12\x12\n\nwindow_len\x18\x02 \x01(\r\x12\x0e\n\x06\x62itvec\x18\x03 \x01(\x0c\"S\n\x14\x43urrentConsensusKeys\x12;\n\x0e\x63onsensus_keys\x18\x01 \x03(\x0b\x32#.penumbra.core.keys.v1.ConsensusKey\"\x18\n\x07Penalty\x12\r\n\x05inner\x18\x01 \x01(\x0c\"S\n\x17GetValidatorInfoRequest\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"c\n\x18GetValidatorInfoResponse\x12G\n\x0evalidator_info\x18\x01 \x01(\x0b\x32/.penumbra.core.component.stake.v1.ValidatorInfo\"-\n\x14ValidatorInfoRequest\x12\x15\n\rshow_inactive\x18\x02 \x01(\x08\"`\n\x15ValidatorInfoResponse\x12G\n\x0evalidator_info\x18\x01 \x01(\x0b\x32/.penumbra.core.component.stake.v1.ValidatorInfo\"R\n\x16ValidatorStatusRequest\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"\\\n\x17ValidatorStatusResponse\x12\x41\n\x06status\x18\x01 \x01(\x0b\x32\x31.penumbra.core.component.stake.v1.ValidatorStatus\"\x87\x01\n\x17ValidatorPenaltyRequest\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x19\n\x11start_epoch_index\x18\x03 \x01(\x04\x12\x17\n\x0f\x65nd_epoch_index\x18\x04 \x01(\x04\"V\n\x18ValidatorPenaltyResponse\x12:\n\x07penalty\x18\x01 \x01(\x0b\x32).penumbra.core.component.stake.v1.Penalty\"W\n\x1b\x43urrentValidatorRateRequest\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"X\n\x1c\x43urrentValidatorRateResponse\x12\x38\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32*.penumbra.core.component.stake.v1.RateData\"R\n\x16ValidatorUptimeRequest\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"S\n\x17ValidatorUptimeResponse\x12\x38\n\x06uptime\x18\x01 \x01(\x0b\x32(.penumbra.core.component.stake.v1.Uptime\"\xc7\x02\n\x0fStakeParameters\x12\x1c\n\x10unbonding_epochs\x18\x01 \x01(\x04\x42\x02\x18\x01\x12\x1e\n\x16\x61\x63tive_validator_limit\x18\x02 \x01(\x04\x12\x18\n\x10\x62\x61se_reward_rate\x18\x03 \x01(\x04\x12$\n\x1cslashing_penalty_misbehavior\x18\x04 \x01(\x04\x12!\n\x19slashing_penalty_downtime\x18\x05 \x01(\x04\x12 \n\x18signed_blocks_window_len\x18\x06 \x01(\x04\x12\x1d\n\x15missed_blocks_maximum\x18\x07 \x01(\x04\x12\x39\n\x13min_validator_stake\x18\x08 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x17\n\x0funbonding_delay\x18\t \x01(\x04\"\x9a\x01\n\x0eGenesisContent\x12G\n\x0cstake_params\x18\x01 \x01(\x0b\x32\x31.penumbra.core.component.stake.v1.StakeParameters\x12?\n\nvalidators\x18\x02 \x03(\x0b\x32+.penumbra.core.component.stake.v1.Validator\"\xab\x01\n\x17\x45ventTombstoneValidator\x12\x17\n\x0f\x65vidence_height\x18\x01 \x01(\x04\x12\x16\n\x0e\x63urrent_height\x18\x02 \x01(\x04\x12\x38\n\x0cidentity_key\x18\x04 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\x0c\x12\x14\n\x0cvoting_power\x18\x06 \x01(\x04\x32\xd5\x06\n\x0cQueryService\x12\x89\x01\n\x10GetValidatorInfo\x12\x39.penumbra.core.component.stake.v1.GetValidatorInfoRequest\x1a:.penumbra.core.component.stake.v1.GetValidatorInfoResponse\x12\x82\x01\n\rValidatorInfo\x12\x36.penumbra.core.component.stake.v1.ValidatorInfoRequest\x1a\x37.penumbra.core.component.stake.v1.ValidatorInfoResponse0\x01\x12\x86\x01\n\x0fValidatorStatus\x12\x38.penumbra.core.component.stake.v1.ValidatorStatusRequest\x1a\x39.penumbra.core.component.stake.v1.ValidatorStatusResponse\x12\x89\x01\n\x10ValidatorPenalty\x12\x39.penumbra.core.component.stake.v1.ValidatorPenaltyRequest\x1a:.penumbra.core.component.stake.v1.ValidatorPenaltyResponse\x12\x95\x01\n\x14\x43urrentValidatorRate\x12=.penumbra.core.component.stake.v1.CurrentValidatorRateRequest\x1a>.penumbra.core.component.stake.v1.CurrentValidatorRateResponse\x12\x86\x01\n\x0fValidatorUptime\x12\x38.penumbra.core.component.stake.v1.ValidatorUptimeRequest\x1a\x39.penumbra.core.component.stake.v1.ValidatorUptimeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.core.component.stake.v1.stake_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _RATEDATA.fields_by_name['epoch_index']._options = None
  _RATEDATA.fields_by_name['epoch_index']._serialized_options = b'\030\001'
  _BONDINGSTATE.fields_by_name['unbonds_at_epoch']._options = None
  _BONDINGSTATE.fields_by_name['unbonds_at_epoch']._serialized_options = b'\030\001'
  _UNDELEGATE.fields_by_name['start_epoch_index']._options = None
  _UNDELEGATE.fields_by_name['start_epoch_index']._serialized_options = b'\030\001'
  _UNDELEGATECLAIMBODY.fields_by_name['start_epoch_index']._options = None
  _UNDELEGATECLAIMBODY.fields_by_name['start_epoch_index']._serialized_options = b'\030\001'
  _UNDELEGATECLAIMPLAN.fields_by_name['start_epoch_index']._options = None
  _UNDELEGATECLAIMPLAN.fields_by_name['start_epoch_index']._serialized_options = b'\030\001'
  _STAKEPARAMETERS.fields_by_name['unbonding_epochs']._options = None
  _STAKEPARAMETERS.fields_by_name['unbonding_epochs']._serialized_options = b'\030\001'
  _globals['_ZKUNDELEGATECLAIMPROOF']._serialized_start=226
  _globals['_ZKUNDELEGATECLAIMPROOF']._serialized_end=265
  _globals['_VALIDATOR']._serialized_start=268
  _globals['_VALIDATOR']._serialized_end=590
  _globals['_VALIDATORLIST']._serialized_start=592
  _globals['_VALIDATORLIST']._serialized_end=667
  _globals['_FUNDINGSTREAM']._serialized_start=670
  _globals['_FUNDINGSTREAM']._serialized_end=958
  _globals['_FUNDINGSTREAM_TOADDRESS']._serialized_start=862
  _globals['_FUNDINGSTREAM_TOADDRESS']._serialized_end=908
  _globals['_FUNDINGSTREAM_TOCOMMUNITYPOOL']._serialized_start=910
  _globals['_FUNDINGSTREAM_TOCOMMUNITYPOOL']._serialized_end=945
  _globals['_RATEDATA']._serialized_start=961
  _globals['_RATEDATA']._serialized_end=1178
  _globals['_BASERATEDATA']._serialized_start=1181
  _globals['_BASERATEDATA']._serialized_end=1330
  _globals['_VALIDATORSTATUS']._serialized_start=1333
  _globals['_VALIDATORSTATUS']._serialized_end=1596
  _globals['_BONDINGSTATE']._serialized_start=1599
  _globals['_BONDINGSTATE']._serialized_end=1905
  _globals['_BONDINGSTATE_BONDINGSTATEENUM']._serialized_start=1753
  _globals['_BONDINGSTATE_BONDINGSTATEENUM']._serialized_end=1905
  _globals['_VALIDATORSTATE']._serialized_start=1908
  _globals['_VALIDATORSTATE']._serialized_end=2276
  _globals['_VALIDATORSTATE_VALIDATORSTATEENUM']._serialized_start=2011
  _globals['_VALIDATORSTATE_VALIDATORSTATEENUM']._serialized_end=2276
  _globals['_VALIDATORINFO']._serialized_start=2279
  _globals['_VALIDATORINFO']._serialized_end=2488
  _globals['_VALIDATORDEFINITION']._serialized_start=2490
  _globals['_VALIDATORDEFINITION']._serialized_end=2593
  _globals['_DELEGATE']._serialized_start=2596
  _globals['_DELEGATE']._serialized_end=2803
  _globals['_UNDELEGATE']._serialized_start=2806
  _globals['_UNDELEGATE']._serialized_end=3084
  _globals['_UNDELEGATECLAIM']._serialized_start=3086
  _globals['_UNDELEGATECLAIM']._serialized_end=3187
  _globals['_UNDELEGATECLAIMBODY']._serialized_start=3190
  _globals['_UNDELEGATECLAIMBODY']._serialized_end=3469
  _globals['_UNDELEGATECLAIMPLAN']._serialized_start=3472
  _globals['_UNDELEGATECLAIMPLAN']._serialized_end=3814
  _globals['_DELEGATIONCHANGES']._serialized_start=3817
  _globals['_DELEGATIONCHANGES']._serialized_end=3970
  _globals['_UPTIME']._serialized_start=3972
  _globals['_UPTIME']._serialized_end=4044
  _globals['_CURRENTCONSENSUSKEYS']._serialized_start=4046
  _globals['_CURRENTCONSENSUSKEYS']._serialized_end=4129
  _globals['_PENALTY']._serialized_start=4131
  _globals['_PENALTY']._serialized_end=4155
  _globals['_GETVALIDATORINFOREQUEST']._serialized_start=4157
  _globals['_GETVALIDATORINFOREQUEST']._serialized_end=4240
  _globals['_GETVALIDATORINFORESPONSE']._serialized_start=4242
  _globals['_GETVALIDATORINFORESPONSE']._serialized_end=4341
  _globals['_VALIDATORINFOREQUEST']._serialized_start=4343
  _globals['_VALIDATORINFOREQUEST']._serialized_end=4388
  _globals['_VALIDATORINFORESPONSE']._serialized_start=4390
  _globals['_VALIDATORINFORESPONSE']._serialized_end=4486
  _globals['_VALIDATORSTATUSREQUEST']._serialized_start=4488
  _globals['_VALIDATORSTATUSREQUEST']._serialized_end=4570
  _globals['_VALIDATORSTATUSRESPONSE']._serialized_start=4572
  _globals['_VALIDATORSTATUSRESPONSE']._serialized_end=4664
  _globals['_VALIDATORPENALTYREQUEST']._serialized_start=4667
  _globals['_VALIDATORPENALTYREQUEST']._serialized_end=4802
  _globals['_VALIDATORPENALTYRESPONSE']._serialized_start=4804
  _globals['_VALIDATORPENALTYRESPONSE']._serialized_end=4890
  _globals['_CURRENTVALIDATORRATEREQUEST']._serialized_start=4892
  _globals['_CURRENTVALIDATORRATEREQUEST']._serialized_end=4979
  _globals['_CURRENTVALIDATORRATERESPONSE']._serialized_start=4981
  _globals['_CURRENTVALIDATORRATERESPONSE']._serialized_end=5069
  _globals['_VALIDATORUPTIMEREQUEST']._serialized_start=5071
  _globals['_VALIDATORUPTIMEREQUEST']._serialized_end=5153
  _globals['_VALIDATORUPTIMERESPONSE']._serialized_start=5155
  _globals['_VALIDATORUPTIMERESPONSE']._serialized_end=5238
  _globals['_STAKEPARAMETERS']._serialized_start=5241
  _globals['_STAKEPARAMETERS']._serialized_end=5568
  _globals['_GENESISCONTENT']._serialized_start=5571
  _globals['_GENESISCONTENT']._serialized_end=5725
  _globals['_EVENTTOMBSTONEVALIDATOR']._serialized_start=5728
  _globals['_EVENTTOMBSTONEVALIDATOR']._serialized_end=5899
  _globals['_QUERYSERVICE']._serialized_start=5902
  _globals['_QUERYSERVICE']._serialized_end=6755
# @@protoc_insertion_point(module_scope)