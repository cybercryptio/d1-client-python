# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authz.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61uthz.proto\x12\x08\x64\x31.authz\"*\n\x15GetPermissionsRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\"+\n\x16GetPermissionsResponse\x12\x11\n\tgroup_ids\x18\x01 \x03(\t\";\n\x14\x41\x64\x64PermissionRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\"\x17\n\x15\x41\x64\x64PermissionResponse\">\n\x17RemovePermissionRequest\x12\x11\n\tobject_id\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\"\x1a\n\x18RemovePermissionResponse2\x8f\x02\n\x05\x41uthz\x12U\n\x0eGetPermissions\x12\x1f.d1.authz.GetPermissionsRequest\x1a .d1.authz.GetPermissionsResponse\"\x00\x12R\n\rAddPermission\x12\x1e.d1.authz.AddPermissionRequest\x1a\x1f.d1.authz.AddPermissionResponse\"\x00\x12[\n\x10RemovePermission\x12!.d1.authz.RemovePermissionRequest\x1a\".d1.authz.RemovePermissionResponse\"\x00\x42\x8e\x01\n\x1fio.cybercrypt.d1.protobuf.authzB\nAuthzProtoZ9github.com/cybercryptio/d1-service-generic/protobuf/authz\xaa\x02#CyberCrypt.D1.Client.Protobuf.Authzb\x06proto3')



_GETPERMISSIONSREQUEST = DESCRIPTOR.message_types_by_name['GetPermissionsRequest']
_GETPERMISSIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetPermissionsResponse']
_ADDPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['AddPermissionRequest']
_ADDPERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['AddPermissionResponse']
_REMOVEPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['RemovePermissionRequest']
_REMOVEPERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['RemovePermissionResponse']
GetPermissionsRequest = _reflection.GeneratedProtocolMessageType('GetPermissionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPERMISSIONSREQUEST,
  '__module__' : 'authz_pb2'
  # @@protoc_insertion_point(class_scope:d1.authz.GetPermissionsRequest)
  })
_sym_db.RegisterMessage(GetPermissionsRequest)

GetPermissionsResponse = _reflection.GeneratedProtocolMessageType('GetPermissionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPERMISSIONSRESPONSE,
  '__module__' : 'authz_pb2'
  # @@protoc_insertion_point(class_scope:d1.authz.GetPermissionsResponse)
  })
_sym_db.RegisterMessage(GetPermissionsResponse)

AddPermissionRequest = _reflection.GeneratedProtocolMessageType('AddPermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPERMISSIONREQUEST,
  '__module__' : 'authz_pb2'
  # @@protoc_insertion_point(class_scope:d1.authz.AddPermissionRequest)
  })
_sym_db.RegisterMessage(AddPermissionRequest)

AddPermissionResponse = _reflection.GeneratedProtocolMessageType('AddPermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDPERMISSIONRESPONSE,
  '__module__' : 'authz_pb2'
  # @@protoc_insertion_point(class_scope:d1.authz.AddPermissionResponse)
  })
_sym_db.RegisterMessage(AddPermissionResponse)

RemovePermissionRequest = _reflection.GeneratedProtocolMessageType('RemovePermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPERMISSIONREQUEST,
  '__module__' : 'authz_pb2'
  # @@protoc_insertion_point(class_scope:d1.authz.RemovePermissionRequest)
  })
_sym_db.RegisterMessage(RemovePermissionRequest)

RemovePermissionResponse = _reflection.GeneratedProtocolMessageType('RemovePermissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPERMISSIONRESPONSE,
  '__module__' : 'authz_pb2'
  # @@protoc_insertion_point(class_scope:d1.authz.RemovePermissionResponse)
  })
_sym_db.RegisterMessage(RemovePermissionResponse)

_AUTHZ = DESCRIPTOR.services_by_name['Authz']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.cybercrypt.d1.protobuf.authzB\nAuthzProtoZ9github.com/cybercryptio/d1-service-generic/protobuf/authz\252\002#CyberCrypt.D1.Client.Protobuf.Authz'
  _GETPERMISSIONSREQUEST._serialized_start=25
  _GETPERMISSIONSREQUEST._serialized_end=67
  _GETPERMISSIONSRESPONSE._serialized_start=69
  _GETPERMISSIONSRESPONSE._serialized_end=112
  _ADDPERMISSIONREQUEST._serialized_start=114
  _ADDPERMISSIONREQUEST._serialized_end=173
  _ADDPERMISSIONRESPONSE._serialized_start=175
  _ADDPERMISSIONRESPONSE._serialized_end=198
  _REMOVEPERMISSIONREQUEST._serialized_start=200
  _REMOVEPERMISSIONREQUEST._serialized_end=262
  _REMOVEPERMISSIONRESPONSE._serialized_start=264
  _REMOVEPERMISSIONRESPONSE._serialized_end=290
  _AUTHZ._serialized_start=293
  _AUTHZ._serialized_end=564
# @@protoc_insertion_point(module_scope)
