# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: index.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bindex.proto\x12\x08\x64\x31.index\"2\n\nAddRequest\x12\x10\n\x08keywords\x18\x01 \x03(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\"\r\n\x0b\x41\x64\x64Response\" \n\rSearchRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"%\n\x0eSearchResponse\x12\x13\n\x0bidentifiers\x18\x02 \x03(\t\"5\n\rDeleteRequest\x12\x10\n\x08keywords\x18\x01 \x03(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\"\x10\n\x0e\x44\x65leteResponse2\xbb\x01\n\x05Index\x12\x34\n\x03\x41\x64\x64\x12\x14.d1.index.AddRequest\x1a\x15.d1.index.AddResponse\"\x00\x12=\n\x06Search\x12\x17.d1.index.SearchRequest\x1a\x18.d1.index.SearchResponse\"\x00\x12=\n\x06\x44\x65lete\x12\x17.d1.index.DeleteRequest\x1a\x18.d1.index.DeleteResponse\"\x00\x42\x91\x01\n\x1fio.cybercrypt.d1.protobuf.indexB\nIndexProtoZ<github.com/cybercryptio/d1-service-generic/v2/protobuf/index\xaa\x02#CyberCrypt.D1.Client.Protobuf.Indexb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.cybercrypt.d1.protobuf.indexB\nIndexProtoZ<github.com/cybercryptio/d1-service-generic/v2/protobuf/index\252\002#CyberCrypt.D1.Client.Protobuf.Index'
  _ADDREQUEST._serialized_start=25
  _ADDREQUEST._serialized_end=75
  _ADDRESPONSE._serialized_start=77
  _ADDRESPONSE._serialized_end=90
  _SEARCHREQUEST._serialized_start=92
  _SEARCHREQUEST._serialized_end=124
  _SEARCHRESPONSE._serialized_start=126
  _SEARCHRESPONSE._serialized_end=163
  _DELETEREQUEST._serialized_start=165
  _DELETEREQUEST._serialized_end=218
  _DELETERESPONSE._serialized_start=220
  _DELETERESPONSE._serialized_end=236
  _INDEX._serialized_start=239
  _INDEX._serialized_end=426
# @@protoc_insertion_point(module_scope)
