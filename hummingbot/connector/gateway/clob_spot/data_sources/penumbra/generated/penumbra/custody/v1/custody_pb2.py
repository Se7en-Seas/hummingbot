# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: penumbra/custody/v1/custody.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.governance.v1 import (
    governance_pb2 as penumbra_dot_core_dot_component_dot_governance_dot_v1_dot_governance__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.component.stake.v1 import (
    stake_pb2 as penumbra_dot_core_dot_component_dot_stake_dot_v1_dot_stake__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.keys.v1 import (
    keys_pb2 as penumbra_dot_core_dot_keys_dot_v1_dot_keys__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.core.transaction.v1 import (
    transaction_pb2 as penumbra_dot_core_dot_transaction_dot_v1_dot_transaction__pb2,
)
from hummingbot.connector.gateway.clob_spot.data_sources.penumbra.generated.penumbra.crypto.decaf377_rdsa.v1 import (
    decaf377_rdsa_pb2 as penumbra_dot_crypto_dot_decaf377__rdsa_dot_v1_dot_decaf377__rdsa__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!penumbra/custody/v1/custody.proto\x12\x13penumbra.custody.v1\x1a\x36penumbra/core/component/governance/v1/governance.proto\x1a,penumbra/core/component/stake/v1/stake.proto\x1a penumbra/core/keys/v1/keys.proto\x1a.penumbra/core/transaction/v1/transaction.proto\x1a\x34penumbra/crypto/decaf377_rdsa/v1/decaf377_rdsa.proto\"\x92\x01\n\x10\x41uthorizeRequest\x12;\n\x04plan\x18\x01 \x01(\x0b\x32-.penumbra.core.transaction.v1.TransactionPlan\x12\x41\n\x12pre_authorizations\x18\x03 \x03(\x0b\x32%.penumbra.custody.v1.PreAuthorization\"R\n\x11\x41uthorizeResponse\x12=\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32/.penumbra.core.transaction.v1.AuthorizationData\"\xb3\x01\n#AuthorizeValidatorDefinitionRequest\x12I\n\x14validator_definition\x18\x01 \x01(\x0b\x32+.penumbra.core.component.stake.v1.Validator\x12\x41\n\x12pre_authorizations\x18\x03 \x03(\x0b\x32%.penumbra.custody.v1.PreAuthorization\"\x7f\n$AuthorizeValidatorDefinitionResponse\x12W\n\x19validator_definition_auth\x18\x01 \x01(\x0b\x32\x34.penumbra.crypto.decaf377_rdsa.v1.SpendAuthSignature\"\xb4\x01\n\x1d\x41uthorizeValidatorVoteRequest\x12P\n\x0evalidator_vote\x18\x01 \x01(\x0b\x32\x38.penumbra.core.component.governance.v1.ValidatorVoteBody\x12\x41\n\x12pre_authorizations\x18\x03 \x03(\x0b\x32%.penumbra.custody.v1.PreAuthorization\"s\n\x1e\x41uthorizeValidatorVoteResponse\x12Q\n\x13validator_vote_auth\x18\x01 \x01(\x0b\x32\x34.penumbra.crypto.decaf377_rdsa.v1.SpendAuthSignature\"\x8d\x01\n\x10PreAuthorization\x12@\n\x07\x65\x64\x32\x35\x35\x31\x39\x18\x01 \x01(\x0b\x32-.penumbra.custody.v1.PreAuthorization.Ed25519H\x00\x1a\"\n\x07\x45\x64\x32\x35\x35\x31\x39\x12\n\n\x02vk\x18\x01 \x01(\x0c\x12\x0b\n\x03sig\x18\x02 \x01(\x0c\x42\x13\n\x11pre_authorization\"\x1d\n\x1b\x45xportFullViewingKeyRequest\"_\n\x1c\x45xportFullViewingKeyResponse\x12?\n\x10\x66ull_viewing_key\x18\x01 \x01(\x0b\x32%.penumbra.core.keys.v1.FullViewingKey\"S\n\x15\x43onfirmAddressRequest\x12:\n\raddress_index\x18\x01 \x01(\x0b\x32#.penumbra.core.keys.v1.AddressIndex\"I\n\x16\x43onfirmAddressResponse\x12/\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1e.penumbra.core.keys.v1.Address2\xee\x04\n\x0e\x43ustodyService\x12Z\n\tAuthorize\x12%.penumbra.custody.v1.AuthorizeRequest\x1a&.penumbra.custody.v1.AuthorizeResponse\x12\x93\x01\n\x1c\x41uthorizeValidatorDefinition\x12\x38.penumbra.custody.v1.AuthorizeValidatorDefinitionRequest\x1a\x39.penumbra.custody.v1.AuthorizeValidatorDefinitionResponse\x12\x81\x01\n\x16\x41uthorizeValidatorVote\x12\x32.penumbra.custody.v1.AuthorizeValidatorVoteRequest\x1a\x33.penumbra.custody.v1.AuthorizeValidatorVoteResponse\x12{\n\x14\x45xportFullViewingKey\x12\x30.penumbra.custody.v1.ExportFullViewingKeyRequest\x1a\x31.penumbra.custody.v1.ExportFullViewingKeyResponse\x12i\n\x0e\x43onfirmAddress\x12*.penumbra.custody.v1.ConfirmAddressRequest\x1a+.penumbra.custody.v1.ConfirmAddressResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'penumbra.custody.v1.custody_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_AUTHORIZEREQUEST']._serialized_start=297
  _globals['_AUTHORIZEREQUEST']._serialized_end=443
  _globals['_AUTHORIZERESPONSE']._serialized_start=445
  _globals['_AUTHORIZERESPONSE']._serialized_end=527
  _globals['_AUTHORIZEVALIDATORDEFINITIONREQUEST']._serialized_start=530
  _globals['_AUTHORIZEVALIDATORDEFINITIONREQUEST']._serialized_end=709
  _globals['_AUTHORIZEVALIDATORDEFINITIONRESPONSE']._serialized_start=711
  _globals['_AUTHORIZEVALIDATORDEFINITIONRESPONSE']._serialized_end=838
  _globals['_AUTHORIZEVALIDATORVOTEREQUEST']._serialized_start=841
  _globals['_AUTHORIZEVALIDATORVOTEREQUEST']._serialized_end=1021
  _globals['_AUTHORIZEVALIDATORVOTERESPONSE']._serialized_start=1023
  _globals['_AUTHORIZEVALIDATORVOTERESPONSE']._serialized_end=1138
  _globals['_PREAUTHORIZATION']._serialized_start=1141
  _globals['_PREAUTHORIZATION']._serialized_end=1282
  _globals['_PREAUTHORIZATION_ED25519']._serialized_start=1227
  _globals['_PREAUTHORIZATION_ED25519']._serialized_end=1261
  _globals['_EXPORTFULLVIEWINGKEYREQUEST']._serialized_start=1284
  _globals['_EXPORTFULLVIEWINGKEYREQUEST']._serialized_end=1313
  _globals['_EXPORTFULLVIEWINGKEYRESPONSE']._serialized_start=1315
  _globals['_EXPORTFULLVIEWINGKEYRESPONSE']._serialized_end=1410
  _globals['_CONFIRMADDRESSREQUEST']._serialized_start=1412
  _globals['_CONFIRMADDRESSREQUEST']._serialized_end=1495
  _globals['_CONFIRMADDRESSRESPONSE']._serialized_start=1497
  _globals['_CONFIRMADDRESSRESPONSE']._serialized_end=1570
  _globals['_CUSTODYSERVICE']._serialized_start=1573
  _globals['_CUSTODYSERVICE']._serialized_end=2195
# @@protoc_insertion_point(module_scope)