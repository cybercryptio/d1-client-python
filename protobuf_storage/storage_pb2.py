# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\nd1.storage\":\n\x0cStoreRequest\x12\x11\n\tplaintext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\"\"\n\rStoreResponse\x12\x11\n\tobject_id\x18\x01 \x01(\t\"$\n\x0fRetrieveRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\">\n\x10RetrieveResponse\x12\x11\n\tplaintext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\"N\n\rUpdateRequest\x12\x11\n\tplaintext\x18\x01 \x01(\x0c\x12\x17\n\x0f\x61ssociated_data\x18\x02 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\t\"\x10\n\x0eUpdateResponse\"\"\n\rDeleteRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\"\x10\n\x0e\x44\x65leteResponse2\x98\x02\n\x07Storage\x12>\n\x05Store\x12\x18.d1.storage.StoreRequest\x1a\x19.d1.storage.StoreResponse\"\x00\x12G\n\x08Retrieve\x12\x1b.d1.storage.RetrieveRequest\x1a\x1c.d1.storage.RetrieveResponse\"\x00\x12\x41\n\x06Update\x12\x19.d1.storage.UpdateRequest\x1a\x1a.d1.storage.UpdateResponse\"\x00\x12\x41\n\x06\x44\x65lete\x12\x19.d1.storage.DeleteRequest\x1a\x1a.d1.storage.DeleteResponse\"\x00\x42\x96\x01\n!io.cybercrypt.d1.protobuf.storageB\x0cStorageProtoZ;github.com/cybercryptio/d1-service-storage/protobuf/storage\xaa\x02%CyberCrypt.D1.Client.Protobuf.Storageb\x06proto3')



_STOREREQUEST = DESCRIPTOR.message_types_by_name['StoreRequest']
_STORERESPONSE = DESCRIPTOR.message_types_by_name['StoreResponse']
_RETRIEVEREQUEST = DESCRIPTOR.message_types_by_name['RetrieveRequest']
_RETRIEVERESPONSE = DESCRIPTOR.message_types_by_name['RetrieveResponse']
_UPDATEREQUEST = DESCRIPTOR.message_types_by_name['UpdateRequest']
_UPDATERESPONSE = DESCRIPTOR.message_types_by_name['UpdateResponse']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_DELETERESPONSE = DESCRIPTOR.message_types_by_name['DeleteResponse']
StoreRequest = _reflection.GeneratedProtocolMessageType('StoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOREREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.StoreRequest)
  })
_sym_db.RegisterMessage(StoreRequest)

StoreResponse = _reflection.GeneratedProtocolMessageType('StoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.StoreResponse)
  })
_sym_db.RegisterMessage(StoreResponse)

RetrieveRequest = _reflection.GeneratedProtocolMessageType('RetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.RetrieveRequest)
  })
_sym_db.RegisterMessage(RetrieveRequest)

RetrieveResponse = _reflection.GeneratedProtocolMessageType('RetrieveResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.RetrieveResponse)
  })
_sym_db.RegisterMessage(RetrieveResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

UpdateResponse = _reflection.GeneratedProtocolMessageType('UpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.UpdateResponse)
  })
_sym_db.RegisterMessage(UpdateResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:d1.storage.DeleteResponse)
  })
_sym_db.RegisterMessage(DeleteResponse)

_STORAGE = DESCRIPTOR.services_by_name['Storage']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.cybercrypt.d1.protobuf.storageB\014StorageProtoZ;github.com/cybercryptio/d1-service-storage/protobuf/storage\252\002%CyberCrypt.D1.Client.Protobuf.Storage'
  _STOREREQUEST._serialized_start=29
  _STOREREQUEST._serialized_end=87
  _STORERESPONSE._serialized_start=89
  _STORERESPONSE._serialized_end=123
  _RETRIEVEREQUEST._serialized_start=125
  _RETRIEVEREQUEST._serialized_end=161
  _RETRIEVERESPONSE._serialized_start=163
  _RETRIEVERESPONSE._serialized_end=225
  _UPDATEREQUEST._serialized_start=227
  _UPDATEREQUEST._serialized_end=305
  _UPDATERESPONSE._serialized_start=307
  _UPDATERESPONSE._serialized_end=323
  _DELETEREQUEST._serialized_start=325
  _DELETEREQUEST._serialized_end=359
  _DELETERESPONSE._serialized_start=361
  _DELETERESPONSE._serialized_end=377
  _STORAGE._serialized_start=380
  _STORAGE._serialized_end=660
# @@protoc_insertion_point(module_scope)