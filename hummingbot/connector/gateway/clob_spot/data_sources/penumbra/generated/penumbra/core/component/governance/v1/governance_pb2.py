# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/core/component/governance/v1/governance.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.asset.v1 import (
    asset_pb2 as penumbra_dot_core_dot_asset_dot_v1_dot_asset__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.auction.v1 import (
    auction_pb2 as penumbra_dot_core_dot_component_dot_auction_dot_v1_dot_auction__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.community_pool.v1 import (
    community_pool_pb2 as penumbra_dot_core_dot_component_dot_community__pool_dot_v1_dot_community__pool__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.dex.v1 import (
    dex_pb2 as penumbra_dot_core_dot_component_dot_dex_dot_v1_dot_dex__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.distributions.v1 import (
    distributions_pb2 as penumbra_dot_core_dot_component_dot_distributions_dot_v1_dot_distributions__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.fee.v1 import (
    fee_pb2 as penumbra_dot_core_dot_component_dot_fee_dot_v1_dot_fee__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.funding.v1 import (
    funding_pb2 as penumbra_dot_core_dot_component_dot_funding_dot_v1_dot_funding__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.ibc.v1 import (
    ibc_pb2 as penumbra_dot_core_dot_component_dot_ibc_dot_v1_dot_ibc__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.sct.v1 import (
    sct_pb2 as penumbra_dot_core_dot_component_dot_sct_dot_v1_dot_sct__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.shielded_pool.v1 import (
    shielded_pool_pb2 as penumbra_dot_core_dot_component_dot_shielded__pool_dot_v1_dot_shielded__pool__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.stake.v1 import (
    stake_pb2 as penumbra_dot_core_dot_component_dot_stake_dot_v1_dot_stake__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.keys.v1 import (
    keys_pb2 as penumbra_dot_core_dot_keys_dot_v1_dot_keys__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.num.v1 import (
    num_pb2 as penumbra_dot_core_dot_num_dot_v1_dot_num__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.crypto.decaf377_rdsa.v1 import (
    decaf377_rdsa_pb2 as penumbra_dot_crypto_dot_decaf377__rdsa_dot_v1_dot_decaf377__rdsa__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6penumbra/core/component/governance/v1/governance.proto\x12%penumbra.core.component.governance.v1\x1a\x19google/protobuf/any.proto\x1a\"penumbra/core/asset/v1/asset.proto\x1a\x30penumbra/core/component/auction/v1/auction.proto\x1a>penumbra/core/component/community_pool/v1/community_pool.proto\x1a(penumbra/core/component/dex/v1/dex.proto\x1a<penumbra/core/component/distributions/v1/distributions.proto\x1a(penumbra/core/component/fee/v1/fee.proto\x1a\x30penumbra/core/component/funding/v1/funding.proto\x1a(penumbra/core/component/ibc/v1/ibc.proto\x1a(penumbra/core/component/sct/v1/sct.proto\x1a<penumbra/core/component/shielded_pool/v1/shielded_pool.proto\x1a,penumbra/core/component/stake/v1/stake.proto\x1a penumbra/core/keys/v1/keys.proto\x1a\x1epenumbra/core/num/v1/num.proto\x1a\x34penumbra/crypto/decaf377_rdsa/v1/decaf377_rdsa.proto\"%\n\x14ZKDelegatorVoteProof\x12\r\n\x05inner\x18\x01 \x01(\x0c\"\x89\x01\n\x0eProposalSubmit\x12\x41\n\x08proposal\x18\x01 \x01(\x0b\x32/.penumbra.core.component.governance.v1.Proposal\x12\x34\n\x0e\x64\x65posit_amount\x18\x03 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\"4\n\x10ProposalWithdraw\x12\x10\n\x08proposal\x18\x01 \x01(\x04\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xa7\x01\n\x14ProposalDepositClaim\x12\x10\n\x08proposal\x18\x01 \x01(\x04\x12\x34\n\x0e\x64\x65posit_amount\x18\x02 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12G\n\x07outcome\x18\x03 \x01(\x0b\x32\x36.penumbra.core.component.governance.v1.ProposalOutcome\"\x9f\x01\n\rValidatorVote\x12\x46\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x38.penumbra.core.component.governance.v1.ValidatorVoteBody\x12\x46\n\x08\x61uth_sig\x18\x02 \x01(\x0b\x32\x34.penumbra.crypto.decaf377_rdsa.v1.SpendAuthSignature\"%\n\x13ValidatorVoteReason\x12\x0e\n\x06reason\x18\x01 \x01(\t\"\xa4\x02\n\x11ValidatorVoteBody\x12\x10\n\x08proposal\x18\x01 \x01(\x04\x12\x39\n\x04vote\x18\x02 \x01(\x0b\x32+.penumbra.core.component.governance.v1.Vote\x12\x38\n\x0cidentity_key\x18\x03 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\x12<\n\x0egovernance_key\x18\x04 \x01(\x0b\x32$.penumbra.core.keys.v1.GovernanceKey\x12J\n\x06reason\x18\x05 \x01(\x0b\x32:.penumbra.core.component.governance.v1.ValidatorVoteReason\"\xeb\x01\n\rDelegatorVote\x12\x46\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x38.penumbra.core.component.governance.v1.DelegatorVoteBody\x12\x46\n\x08\x61uth_sig\x18\x02 \x01(\x0b\x32\x34.penumbra.crypto.decaf377_rdsa.v1.SpendAuthSignature\x12J\n\x05proof\x18\x03 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ZKDelegatorVoteProof\"\xdf\x02\n\x11\x44\x65legatorVoteBody\x12\x10\n\x08proposal\x18\x01 \x01(\x04\x12\x16\n\x0estart_position\x18\x02 \x01(\x04\x12\x39\n\x04vote\x18\x03 \x01(\x0b\x32+.penumbra.core.component.governance.v1.Vote\x12,\n\x05value\x18\x04 \x01(\x0b\x32\x1d.penumbra.core.asset.v1.Value\x12\x35\n\x0funbonded_amount\x18\x05 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12<\n\tnullifier\x18\x06 \x01(\x0b\x32).penumbra.core.component.sct.v1.Nullifier\x12\x42\n\x02rk\x18\x07 \x01(\x0b\x32\x36.penumbra.crypto.decaf377_rdsa.v1.SpendVerificationKey\"\xc1\x03\n\x11\x44\x65legatorVoteView\x12S\n\x07visible\x18\x01 \x01(\x0b\x32@.penumbra.core.component.governance.v1.DelegatorVoteView.VisibleH\x00\x12Q\n\x06opaque\x18\x02 \x01(\x0b\x32?.penumbra.core.component.governance.v1.DelegatorVoteView.OpaqueH\x00\x1a\x99\x01\n\x07Visible\x12L\n\x0e\x64\x65legator_vote\x18\x01 \x01(\x0b\x32\x34.penumbra.core.component.governance.v1.DelegatorVote\x12@\n\x04note\x18\x02 \x01(\x0b\x32\x32.penumbra.core.component.shielded_pool.v1.NoteView\x1aV\n\x06Opaque\x12L\n\x0e\x64\x65legator_vote\x18\x01 \x01(\x0b\x32\x34.penumbra.core.component.governance.v1.DelegatorVoteB\x10\n\x0e\x64\x65legator_vote\"\xda\x02\n\x11\x44\x65legatorVotePlan\x12\x10\n\x08proposal\x18\x01 \x01(\x04\x12\x16\n\x0estart_position\x18\x02 \x01(\x04\x12\x39\n\x04vote\x18\x03 \x01(\x0b\x32+.penumbra.core.component.governance.v1.Vote\x12\x43\n\x0bstaked_note\x18\x04 \x01(\x0b\x32..penumbra.core.component.shielded_pool.v1.Note\x12\x1c\n\x14staked_note_position\x18\x05 \x01(\x04\x12\x35\n\x0funbonded_amount\x18\x06 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x12\n\nrandomizer\x18\x07 \x01(\x0c\x12\x18\n\x10proof_blinding_r\x18\x08 \x01(\x0c\x12\x18\n\x10proof_blinding_s\x18\t \x01(\x0c\"D\n\x14\x43ommunityPoolDeposit\x12,\n\x05value\x18\x01 \x01(\x0b\x32\x1d.penumbra.core.asset.v1.Value\"B\n\x12\x43ommunityPoolSpend\x12,\n\x05value\x18\x01 \x01(\x0b\x32\x1d.penumbra.core.asset.v1.Value\"t\n\x13\x43ommunityPoolOutput\x12,\n\x05value\x18\x01 \x01(\x0b\x32\x1d.penumbra.core.asset.v1.Value\x12/\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x1e.penumbra.core.keys.v1.Address\"\x91\x01\n\x04Vote\x12>\n\x04vote\x18\x01 \x01(\x0e\x32\x30.penumbra.core.component.governance.v1.Vote.Vote\"I\n\x04Vote\x12\x14\n\x10VOTE_UNSPECIFIED\x10\x00\x12\x10\n\x0cVOTE_ABSTAIN\x10\x01\x12\x0c\n\x08VOTE_YES\x10\x02\x12\x0b\n\x07VOTE_NO\x10\x03\"\xb0\x04\n\rProposalState\x12M\n\x06voting\x18\x02 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ProposalState.VotingH\x00\x12S\n\twithdrawn\x18\x03 \x01(\x0b\x32>.penumbra.core.component.governance.v1.ProposalState.WithdrawnH\x00\x12Q\n\x08\x66inished\x18\x04 \x01(\x0b\x32=.penumbra.core.component.governance.v1.ProposalState.FinishedH\x00\x12O\n\x07\x63laimed\x18\x05 \x01(\x0b\x32<.penumbra.core.component.governance.v1.ProposalState.ClaimedH\x00\x1a\x08\n\x06Voting\x1a\x1b\n\tWithdrawn\x12\x0e\n\x06reason\x18\x01 \x01(\t\x1aS\n\x08\x46inished\x12G\n\x07outcome\x18\x01 \x01(\x0b\x32\x36.penumbra.core.component.governance.v1.ProposalOutcome\x1aR\n\x07\x43laimed\x12G\n\x07outcome\x18\x01 \x01(\x0b\x32\x36.penumbra.core.component.governance.v1.ProposalOutcomeB\x07\n\x05state\"\xf7\x03\n\x0fProposalOutcome\x12O\n\x06passed\x18\x01 \x01(\x0b\x32=.penumbra.core.component.governance.v1.ProposalOutcome.PassedH\x00\x12O\n\x06\x66\x61iled\x18\x02 \x01(\x0b\x32=.penumbra.core.component.governance.v1.ProposalOutcome.FailedH\x00\x12Q\n\x07slashed\x18\x03 \x01(\x0b\x32>.penumbra.core.component.governance.v1.ProposalOutcome.SlashedH\x00\x1a\x1b\n\tWithdrawn\x12\x0e\n\x06reason\x18\x01 \x01(\t\x1a\x08\n\x06Passed\x1a]\n\x06\x46\x61iled\x12S\n\twithdrawn\x18\x01 \x01(\x0b\x32@.penumbra.core.component.governance.v1.ProposalOutcome.Withdrawn\x1a^\n\x07Slashed\x12S\n\twithdrawn\x18\x01 \x01(\x0b\x32@.penumbra.core.component.governance.v1.ProposalOutcome.WithdrawnB\t\n\x07outcome\"1\n\x05Tally\x12\x0b\n\x03yes\x18\x01 \x01(\x04\x12\n\n\x02no\x18\x02 \x01(\x04\x12\x0f\n\x07\x61\x62stain\x18\x03 \x01(\x04\"\x8c\n\n\x08Proposal\x12\n\n\x02id\x18\x04 \x01(\x04\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12N\n\tsignaling\x18\x05 \x01(\x0b\x32\x39.penumbra.core.component.governance.v1.Proposal.SignalingH\x00\x12N\n\temergency\x18\x06 \x01(\x0b\x32\x39.penumbra.core.component.governance.v1.Proposal.EmergencyH\x00\x12[\n\x10parameter_change\x18\x07 \x01(\x0b\x32?.penumbra.core.component.governance.v1.Proposal.ParameterChangeH\x00\x12\x62\n\x14\x63ommunity_pool_spend\x18\x08 \x01(\x0b\x32\x42.penumbra.core.component.governance.v1.Proposal.CommunityPoolSpendH\x00\x12S\n\x0cupgrade_plan\x18\t \x01(\x0b\x32;.penumbra.core.component.governance.v1.Proposal.UpgradePlanH\x00\x12\\\n\x11\x66reeze_ibc_client\x18\n \x01(\x0b\x32?.penumbra.core.component.governance.v1.Proposal.FreezeIbcClientH\x00\x12`\n\x13unfreeze_ibc_client\x18\x0b \x01(\x0b\x32\x41.penumbra.core.component.governance.v1.Proposal.UnfreezeIbcClientH\x00\x1a\x1b\n\tSignaling\x12\x0e\n\x06\x63ommit\x18\x01 \x01(\t\x1a\x1f\n\tEmergency\x12\x12\n\nhalt_chain\x18\x01 \x01(\x08\x1a\xdd\x02\n\x0fParameterChange\x12W\n\x0eold_parameters\x18\x01 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ChangedAppParametersB\x02\x18\x01\x12W\n\x0enew_parameters\x18\x02 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ChangedAppParametersB\x02\x18\x01\x12N\n\rpreconditions\x18\x03 \x03(\x0b\x32\x37.penumbra.core.component.governance.v1.EncodedParameter\x12H\n\x07\x63hanges\x18\x04 \x03(\x0b\x32\x37.penumbra.core.component.governance.v1.EncodedParameter\x1a\x44\n\x12\x43ommunityPoolSpend\x12.\n\x10transaction_plan\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x1a\x1d\n\x0bUpgradePlan\x12\x0e\n\x06height\x18\x01 \x01(\x04\x1a$\n\x0f\x46reezeIbcClient\x12\x11\n\tclient_id\x18\x01 \x01(\t\x1a&\n\x11UnfreezeIbcClient\x12\x11\n\tclient_id\x18\x01 \x01(\tB\t\n\x07payload\"*\n\x13ProposalInfoRequest\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x04\"J\n\x14ProposalInfoResponse\x12\x1a\n\x12start_block_height\x18\x01 \x01(\x04\x12\x16\n\x0estart_position\x18\x02 \x01(\x04\"*\n\x13ProposalDataRequest\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x04\"\xab\x02\n\x14ProposalDataResponse\x12\x41\n\x08proposal\x18\x01 \x01(\x0b\x32/.penumbra.core.component.governance.v1.Proposal\x12\x1a\n\x12start_block_height\x18\x02 \x01(\x04\x12\x18\n\x10\x65nd_block_height\x18\x03 \x01(\x04\x12\x16\n\x0estart_position\x18\x04 \x01(\x04\x12\x43\n\x05state\x18\x05 \x01(\x0b\x32\x34.penumbra.core.component.governance.v1.ProposalState\x12=\n\x17proposal_deposit_amount\x18\x06 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\".\n\x17ProposalRateDataRequest\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x04\"Y\n\x18ProposalRateDataResponse\x12=\n\trate_data\x18\x01 \x01(\x0b\x32*.penumbra.core.component.stake.v1.RateData\"\'\n\x13ProposalListRequest\x12\x10\n\x08inactive\x18\x02 \x01(\x08\"\xec\x01\n\x14ProposalListResponse\x12\x41\n\x08proposal\x18\x01 \x01(\x0b\x32/.penumbra.core.component.governance.v1.Proposal\x12\x1a\n\x12start_block_height\x18\x02 \x01(\x04\x12\x18\n\x10\x65nd_block_height\x18\x03 \x01(\x04\x12\x16\n\x0estart_position\x18\x04 \x01(\x04\x12\x43\n\x05state\x18\x05 \x01(\x0b\x32\x34.penumbra.core.component.governance.v1.ProposalState\",\n\x15ValidatorVotesRequest\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x04\"\x8d\x01\n\x16ValidatorVotesResponse\x12\x39\n\x04vote\x18\x01 \x01(\x0b\x32+.penumbra.core.component.governance.v1.Vote\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"\xd7\x01\n\x14GovernanceParameters\x12\x1e\n\x16proposal_voting_blocks\x18\x01 \x01(\x04\x12=\n\x17proposal_deposit_amount\x18\x02 \x01(\x0b\x32\x1c.penumbra.core.num.v1.Amount\x12\x1d\n\x15proposal_valid_quorum\x18\x03 \x01(\t\x12\x1f\n\x17proposal_pass_threshold\x18\x04 \x01(\t\x12 \n\x18proposal_slash_threshold\x18\x05 \x01(\t\"h\n\x0eGenesisContent\x12V\n\x11governance_params\x18\x01 \x01(\x0b\x32;.penumbra.core.component.governance.v1.GovernanceParameters\"A\n\x10\x45ncodedParameter\x12\x11\n\tcomponent\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x89\x07\n\x14\x43hangedAppParameters\x12\x41\n\nsct_params\x18\x01 \x01(\x0b\x32-.penumbra.core.component.sct.v1.SctParameters\x12\x61\n\x15\x63ommunity_pool_params\x18\x02 \x01(\x0b\x32\x42.penumbra.core.component.community_pool.v1.CommunityPoolParameters\x12V\n\x11governance_params\x18\x03 \x01(\x0b\x32;.penumbra.core.component.governance.v1.GovernanceParameters\x12\x41\n\nibc_params\x18\x04 \x01(\x0b\x32-.penumbra.core.component.ibc.v1.IbcParameters\x12G\n\x0cstake_params\x18\x05 \x01(\x0b\x32\x31.penumbra.core.component.stake.v1.StakeParameters\x12\x41\n\nfee_params\x18\x06 \x01(\x0b\x32-.penumbra.core.component.fee.v1.FeeParameters\x12_\n\x14\x64istributions_params\x18\x07 \x01(\x0b\x32\x41.penumbra.core.component.distributions.v1.DistributionsParameters\x12M\n\x0e\x66unding_params\x18\x08 \x01(\x0b\x32\x35.penumbra.core.component.funding.v1.FundingParameters\x12^\n\x14shielded_pool_params\x18\t \x01(\x0b\x32@.penumbra.core.component.shielded_pool.v1.ShieldedPoolParameters\x12\x41\n\ndex_params\x18\n \x01(\x0b\x32-.penumbra.core.component.dex.v1.DexParameters\x12M\n\x0e\x61uction_params\x18\x0b \x01(\x0b\x32\x35.penumbra.core.component.auction.v1.AuctionParameters:\x02\x18\x01\"\xb1\x01\n\x17\x43hangedAppParametersSet\x12H\n\x03old\x18\x01 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ChangedAppParameters\x12H\n\x03new\x18\x02 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ChangedAppParameters:\x02\x18\x01\"r\n!VotingPowerAtProposalStartRequest\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x04\x12\x38\n\x0cidentity_key\x18\x03 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\":\n\"VotingPowerAtProposalStartResponse\x12\x14\n\x0cvoting_power\x18\x01 \x01(\x04\"A\n*AllTalliedDelegatorVotesForProposalRequest\x12\x13\n\x0bproposal_id\x18\x02 \x01(\x04\"\xa4\x01\n+AllTalliedDelegatorVotesForProposalResponse\x12;\n\x05tally\x18\x01 \x01(\x0b\x32,.penumbra.core.component.governance.v1.Tally\x12\x38\n\x0cidentity_key\x18\x02 \x01(\x0b\x32\".penumbra.core.keys.v1.IdentityKey\"\x17\n\x15NextProposalIdRequest\"2\n\x16NextProposalIdResponse\x12\x18\n\x10next_proposal_id\x18\x01 \x01(\x04\"/\n\x05Ratio\x12\x11\n\tnumerator\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x04\"X\n\x12\x45ventDelegatorVote\x12\x42\n\x04vote\x18\x01 \x01(\x0b\x32\x34.penumbra.core.component.governance.v1.DelegatorVote\"o\n\x19\x45ventProposalDepositClaim\x12R\n\rdeposit_claim\x18\x01 \x01(\x0b\x32;.penumbra.core.component.governance.v1.ProposalDepositClaim\"X\n\x12\x45ventValidatorVote\x12\x42\n\x04vote\x18\x01 \x01(\x0b\x32\x34.penumbra.core.component.governance.v1.ValidatorVote\"b\n\x15\x45ventProposalWithdraw\x12I\n\x08withdraw\x18\x01 \x01(\x0b\x32\x37.penumbra.core.component.governance.v1.ProposalWithdraw\"\\\n\x13\x45ventProposalSubmit\x12\x45\n\x06submit\x18\x01 \x01(\x0b\x32\x35.penumbra.core.component.governance.v1.ProposalSubmit\"W\n\x12\x45ventEnactProposal\x12\x41\n\x08proposal\x18\x01 \x01(\x0b\x32/.penumbra.core.component.governance.v1.Proposal\"X\n\x13\x45ventProposalFailed\x12\x41\n\x08proposal\x18\x01 \x01(\x0b\x32/.penumbra.core.component.governance.v1.Proposal\"Y\n\x14\x45ventProposalSlashed\x12\x41\n\x08proposal\x18\x01 \x01(\x0b\x32/.penumbra.core.component.governance.v1.Proposal2\xed\t\n\x0cQueryService\x12\x87\x01\n\x0cProposalInfo\x12:.penumbra.core.component.governance.v1.ProposalInfoRequest\x1a;.penumbra.core.component.governance.v1.ProposalInfoResponse\x12\x89\x01\n\x0cProposalList\x12:.penumbra.core.component.governance.v1.ProposalListRequest\x1a;.penumbra.core.component.governance.v1.ProposalListResponse0\x01\x12\x87\x01\n\x0cProposalData\x12:.penumbra.core.component.governance.v1.ProposalDataRequest\x1a;.penumbra.core.component.governance.v1.ProposalDataResponse\x12\x8d\x01\n\x0eNextProposalId\x12<.penumbra.core.component.governance.v1.NextProposalIdRequest\x1a=.penumbra.core.component.governance.v1.NextProposalIdResponse\x12\x8f\x01\n\x0eValidatorVotes\x12<.penumbra.core.component.governance.v1.ValidatorVotesRequest\x1a=.penumbra.core.component.governance.v1.ValidatorVotesResponse0\x01\x12\xb1\x01\n\x1aVotingPowerAtProposalStart\x12H.penumbra.core.component.governance.v1.VotingPowerAtProposalStartRequest\x1aI.penumbra.core.component.governance.v1.VotingPowerAtProposalStartResponse\x12\xce\x01\n#AllTalliedDelegatorVotesForProposal\x12Q.penumbra.core.component.governance.v1.AllTalliedDelegatorVotesForProposalRequest\x1aR.penumbra.core.component.governance.v1.AllTalliedDelegatorVotesForProposalResponse0\x01\x12\x95\x01\n\x10ProposalRateData\x12>.penumbra.core.component.governance.v1.ProposalRateDataRequest\x1a?.penumbra.core.component.governance.v1.ProposalRateDataResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.core.component.governance.v1.governance_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _PROPOSAL_PARAMETERCHANGE.fields_by_name['old_parameters']._options = None
  _PROPOSAL_PARAMETERCHANGE.fields_by_name['old_parameters']._serialized_options = b'\030\001'
  _PROPOSAL_PARAMETERCHANGE.fields_by_name['new_parameters']._options = None
  _PROPOSAL_PARAMETERCHANGE.fields_by_name['new_parameters']._serialized_options = b'\030\001'
  _CHANGEDAPPPARAMETERS._options = None
  _CHANGEDAPPPARAMETERS._serialized_options = b'\030\001'
  _CHANGEDAPPPARAMETERSSET._options = None
  _CHANGEDAPPPARAMETERSSET._serialized_options = b'\030\001'
  _globals['_ZKDELEGATORVOTEPROOF']._serialized_start=782
  _globals['_ZKDELEGATORVOTEPROOF']._serialized_end=819
  _globals['_PROPOSALSUBMIT']._serialized_start=822
  _globals['_PROPOSALSUBMIT']._serialized_end=959
  _globals['_PROPOSALWITHDRAW']._serialized_start=961
  _globals['_PROPOSALWITHDRAW']._serialized_end=1013
  _globals['_PROPOSALDEPOSITCLAIM']._serialized_start=1016
  _globals['_PROPOSALDEPOSITCLAIM']._serialized_end=1183
  _globals['_VALIDATORVOTE']._serialized_start=1186
  _globals['_VALIDATORVOTE']._serialized_end=1345
  _globals['_VALIDATORVOTEREASON']._serialized_start=1347
  _globals['_VALIDATORVOTEREASON']._serialized_end=1384
  _globals['_VALIDATORVOTEBODY']._serialized_start=1387
  _globals['_VALIDATORVOTEBODY']._serialized_end=1679
  _globals['_DELEGATORVOTE']._serialized_start=1682
  _globals['_DELEGATORVOTE']._serialized_end=1917
  _globals['_DELEGATORVOTEBODY']._serialized_start=1920
  _globals['_DELEGATORVOTEBODY']._serialized_end=2271
  _globals['_DELEGATORVOTEVIEW']._serialized_start=2274
  _globals['_DELEGATORVOTEVIEW']._serialized_end=2723
  _globals['_DELEGATORVOTEVIEW_VISIBLE']._serialized_start=2464
  _globals['_DELEGATORVOTEVIEW_VISIBLE']._serialized_end=2617
  _globals['_DELEGATORVOTEVIEW_OPAQUE']._serialized_start=2619
  _globals['_DELEGATORVOTEVIEW_OPAQUE']._serialized_end=2705
  _globals['_DELEGATORVOTEPLAN']._serialized_start=2726
  _globals['_DELEGATORVOTEPLAN']._serialized_end=3072
  _globals['_COMMUNITYPOOLDEPOSIT']._serialized_start=3074
  _globals['_COMMUNITYPOOLDEPOSIT']._serialized_end=3142
  _globals['_COMMUNITYPOOLSPEND']._serialized_start=3144
  _globals['_COMMUNITYPOOLSPEND']._serialized_end=3210
  _globals['_COMMUNITYPOOLOUTPUT']._serialized_start=3212
  _globals['_COMMUNITYPOOLOUTPUT']._serialized_end=3328
  _globals['_VOTE']._serialized_start=3331
  _globals['_VOTE']._serialized_end=3476
  _globals['_VOTE_VOTE']._serialized_start=3403
  _globals['_VOTE_VOTE']._serialized_end=3476
  _globals['_PROPOSALSTATE']._serialized_start=3479
  _globals['_PROPOSALSTATE']._serialized_end=4039
  _globals['_PROPOSALSTATE_VOTING']._serialized_start=3824
  _globals['_PROPOSALSTATE_VOTING']._serialized_end=3832
  _globals['_PROPOSALSTATE_WITHDRAWN']._serialized_start=3834
  _globals['_PROPOSALSTATE_WITHDRAWN']._serialized_end=3861
  _globals['_PROPOSALSTATE_FINISHED']._serialized_start=3863
  _globals['_PROPOSALSTATE_FINISHED']._serialized_end=3946
  _globals['_PROPOSALSTATE_CLAIMED']._serialized_start=3948
  _globals['_PROPOSALSTATE_CLAIMED']._serialized_end=4030
  _globals['_PROPOSALOUTCOME']._serialized_start=4042
  _globals['_PROPOSALOUTCOME']._serialized_end=4545
  _globals['_PROPOSALOUTCOME_WITHDRAWN']._serialized_start=3834
  _globals['_PROPOSALOUTCOME_WITHDRAWN']._serialized_end=3861
  _globals['_PROPOSALOUTCOME_PASSED']._serialized_start=4335
  _globals['_PROPOSALOUTCOME_PASSED']._serialized_end=4343
  _globals['_PROPOSALOUTCOME_FAILED']._serialized_start=4345
  _globals['_PROPOSALOUTCOME_FAILED']._serialized_end=4438
  _globals['_PROPOSALOUTCOME_SLASHED']._serialized_start=4440
  _globals['_PROPOSALOUTCOME_SLASHED']._serialized_end=4534
  _globals['_TALLY']._serialized_start=4547
  _globals['_TALLY']._serialized_end=4596
  _globals['_PROPOSAL']._serialized_start=4599
  _globals['_PROPOSAL']._serialized_end=5891
  _globals['_PROPOSAL_SIGNALING']._serialized_start=5289
  _globals['_PROPOSAL_SIGNALING']._serialized_end=5316
  _globals['_PROPOSAL_EMERGENCY']._serialized_start=5318
  _globals['_PROPOSAL_EMERGENCY']._serialized_end=5349
  _globals['_PROPOSAL_PARAMETERCHANGE']._serialized_start=5352
  _globals['_PROPOSAL_PARAMETERCHANGE']._serialized_end=5701
  _globals['_PROPOSAL_COMMUNITYPOOLSPEND']._serialized_start=5703
  _globals['_PROPOSAL_COMMUNITYPOOLSPEND']._serialized_end=5771
  _globals['_PROPOSAL_UPGRADEPLAN']._serialized_start=5773
  _globals['_PROPOSAL_UPGRADEPLAN']._serialized_end=5802
  _globals['_PROPOSAL_FREEZEIBCCLIENT']._serialized_start=5804
  _globals['_PROPOSAL_FREEZEIBCCLIENT']._serialized_end=5840
  _globals['_PROPOSAL_UNFREEZEIBCCLIENT']._serialized_start=5842
  _globals['_PROPOSAL_UNFREEZEIBCCLIENT']._serialized_end=5880
  _globals['_PROPOSALINFOREQUEST']._serialized_start=5893
  _globals['_PROPOSALINFOREQUEST']._serialized_end=5935
  _globals['_PROPOSALINFORESPONSE']._serialized_start=5937
  _globals['_PROPOSALINFORESPONSE']._serialized_end=6011
  _globals['_PROPOSALDATAREQUEST']._serialized_start=6013
  _globals['_PROPOSALDATAREQUEST']._serialized_end=6055
  _globals['_PROPOSALDATARESPONSE']._serialized_start=6058
  _globals['_PROPOSALDATARESPONSE']._serialized_end=6357
  _globals['_PROPOSALRATEDATAREQUEST']._serialized_start=6359
  _globals['_PROPOSALRATEDATAREQUEST']._serialized_end=6405
  _globals['_PROPOSALRATEDATARESPONSE']._serialized_start=6407
  _globals['_PROPOSALRATEDATARESPONSE']._serialized_end=6496
  _globals['_PROPOSALLISTREQUEST']._serialized_start=6498
  _globals['_PROPOSALLISTREQUEST']._serialized_end=6537
  _globals['_PROPOSALLISTRESPONSE']._serialized_start=6540
  _globals['_PROPOSALLISTRESPONSE']._serialized_end=6776
  _globals['_VALIDATORVOTESREQUEST']._serialized_start=6778
  _globals['_VALIDATORVOTESREQUEST']._serialized_end=6822
  _globals['_VALIDATORVOTESRESPONSE']._serialized_start=6825
  _globals['_VALIDATORVOTESRESPONSE']._serialized_end=6966
  _globals['_GOVERNANCEPARAMETERS']._serialized_start=6969
  _globals['_GOVERNANCEPARAMETERS']._serialized_end=7184
  _globals['_GENESISCONTENT']._serialized_start=7186
  _globals['_GENESISCONTENT']._serialized_end=7290
  _globals['_ENCODEDPARAMETER']._serialized_start=7292
  _globals['_ENCODEDPARAMETER']._serialized_end=7357
  _globals['_CHANGEDAPPPARAMETERS']._serialized_start=7360
  _globals['_CHANGEDAPPPARAMETERS']._serialized_end=8265
  _globals['_CHANGEDAPPPARAMETERSSET']._serialized_start=8268
  _globals['_CHANGEDAPPPARAMETERSSET']._serialized_end=8445
  _globals['_VOTINGPOWERATPROPOSALSTARTREQUEST']._serialized_start=8447
  _globals['_VOTINGPOWERATPROPOSALSTARTREQUEST']._serialized_end=8561
  _globals['_VOTINGPOWERATPROPOSALSTARTRESPONSE']._serialized_start=8563
  _globals['_VOTINGPOWERATPROPOSALSTARTRESPONSE']._serialized_end=8621
  _globals['_ALLTALLIEDDELEGATORVOTESFORPROPOSALREQUEST']._serialized_start=8623
  _globals['_ALLTALLIEDDELEGATORVOTESFORPROPOSALREQUEST']._serialized_end=8688
  _globals['_ALLTALLIEDDELEGATORVOTESFORPROPOSALRESPONSE']._serialized_start=8691
  _globals['_ALLTALLIEDDELEGATORVOTESFORPROPOSALRESPONSE']._serialized_end=8855
  _globals['_NEXTPROPOSALIDREQUEST']._serialized_start=8857
  _globals['_NEXTPROPOSALIDREQUEST']._serialized_end=8880
  _globals['_NEXTPROPOSALIDRESPONSE']._serialized_start=8882
  _globals['_NEXTPROPOSALIDRESPONSE']._serialized_end=8932
  _globals['_RATIO']._serialized_start=8934
  _globals['_RATIO']._serialized_end=8981
  _globals['_EVENTDELEGATORVOTE']._serialized_start=8983
  _globals['_EVENTDELEGATORVOTE']._serialized_end=9071
  _globals['_EVENTPROPOSALDEPOSITCLAIM']._serialized_start=9073
  _globals['_EVENTPROPOSALDEPOSITCLAIM']._serialized_end=9184
  _globals['_EVENTVALIDATORVOTE']._serialized_start=9186
  _globals['_EVENTVALIDATORVOTE']._serialized_end=9274
  _globals['_EVENTPROPOSALWITHDRAW']._serialized_start=9276
  _globals['_EVENTPROPOSALWITHDRAW']._serialized_end=9374
  _globals['_EVENTPROPOSALSUBMIT']._serialized_start=9376
  _globals['_EVENTPROPOSALSUBMIT']._serialized_end=9468
  _globals['_EVENTENACTPROPOSAL']._serialized_start=9470
  _globals['_EVENTENACTPROPOSAL']._serialized_end=9557
  _globals['_EVENTPROPOSALFAILED']._serialized_start=9559
  _globals['_EVENTPROPOSALFAILED']._serialized_end=9647
  _globals['_EVENTPROPOSALSLASHED']._serialized_start=9649
  _globals['_EVENTPROPOSALSLASHED']._serialized_end=9738
  _globals['_QUERYSERVICE']._serialized_start=9741
  _globals['_QUERYSERVICE']._serialized_end=11002
# @@protoc_insertion_point(module_scope)