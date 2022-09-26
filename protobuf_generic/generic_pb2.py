# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgeneric.proto\x12\nd1.generic\"O\n\x0e\x45ncryptRequest\x12\x11\n\tplaintext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\x12\x11\n\tgroup_ids\x18\x03 \x03(\t\"Q\n\x0f\x45ncryptResponse\x12\x12\n\nciphertext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\t\"P\n\x0e\x44\x65\x63ryptRequest\x12\x12\n\nciphertext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\t\"=\n\x0f\x44\x65\x63ryptResponse\x12\x11\n\tplaintext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\x32\x95\x01\n\x07Generic\x12\x44\n\x07\x45ncrypt\x12\x1a.d1.generic.EncryptRequest\x1a\x1b.d1.generic.EncryptResponse\"\x00\x12\x44\n\x07\x44\x65\x63rypt\x12\x1a.d1.generic.DecryptRequest\x1a\x1b.d1.generic.DecryptResponse\"\x00\x42\x96\x01\n!io.cybercrypt.d1.protobuf.genericB\x0cGenericProtoZ;github.com/cybercryptio/d1-service-generic/protobuf/generic\xaa\x02%CyberCrypt.D1.Client.Protobuf.Genericb\x06proto3')



_ENCRYPTREQUEST = DESCRIPTOR.message_types_by_name['EncryptRequest']
_ENCRYPTRESPONSE = DESCRIPTOR.message_types_by_name['EncryptResponse']
_DECRYPTREQUEST = DESCRIPTOR.message_types_by_name['DecryptRequest']
_DECRYPTRESPONSE = DESCRIPTOR.message_types_by_name['DecryptResponse']
EncryptRequest = _reflection.GeneratedProtocolMessageType('EncryptRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTREQUEST,
  '__module__' : 'generic_pb2'
  # @@protoc_insertion_point(class_scope:d1.generic.EncryptRequest)
  })
_sym_db.RegisterMessage(EncryptRequest)

EncryptResponse = _reflection.GeneratedProtocolMessageType('EncryptResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTRESPONSE,
  '__module__' : 'generic_pb2'
  # @@protoc_insertion_point(class_scope:d1.generic.EncryptResponse)
  })
_sym_db.RegisterMessage(EncryptResponse)

DecryptRequest = _reflection.GeneratedProtocolMessageType('DecryptRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECRYPTREQUEST,
  '__module__' : 'generic_pb2'
  # @@protoc_insertion_point(class_scope:d1.generic.DecryptRequest)
  })
_sym_db.RegisterMessage(DecryptRequest)

DecryptResponse = _reflection.GeneratedProtocolMessageType('DecryptResponse', (_message.Message,), {
  'DESCRIPTOR' : _DECRYPTRESPONSE,
  '__module__' : 'generic_pb2'
  # @@protoc_insertion_point(class_scope:d1.generic.DecryptResponse)
  })
_sym_db.RegisterMessage(DecryptResponse)

_GENERIC = DESCRIPTOR.services_by_name['Generic']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.cybercrypt.d1.protobuf.genericB\014GenericProtoZ;github.com/cybercryptio/d1-service-generic/protobuf/generic\252\002%CyberCrypt.D1.Client.Protobuf.Generic'
  _ENCRYPTREQUEST._serialized_start=29
  _ENCRYPTREQUEST._serialized_end=108
  _ENCRYPTRESPONSE._serialized_start=110
  _ENCRYPTRESPONSE._serialized_end=191
  _DECRYPTREQUEST._serialized_start=193
  _DECRYPTREQUEST._serialized_end=273
  _DECRYPTRESPONSE._serialized_start=275
  _DECRYPTRESPONSE._serialized_end=336
  _GENERIC._serialized_start=339
  _GENERIC._serialized_end=488
# @@protoc_insertion_point(module_scope)
