# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_file.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import file_type_pb2 as file__type__pb2

from file_type_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_file.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eget_file.proto\x12\x11insta360.messages\x1a\x0f\x66ile_type.proto\"9\n\x07GetFile\x12.\n\tfile_type\x18\x01 \x01(\x0e\x32\x1b.insta360.messages.FileType\"+\n\x0bGetFileResp\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x42\x08\xa2\x02\x05INSPBP\x00\x62\x06proto3'
  ,
  dependencies=[file__type__pb2.DESCRIPTOR,],
  public_dependencies=[file__type__pb2.DESCRIPTOR,])




_GETFILE = _descriptor.Descriptor(
  name='GetFile',
  full_name='insta360.messages.GetFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_type', full_name='insta360.messages.GetFile.file_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=111,
)


_GETFILERESP = _descriptor.Descriptor(
  name='GetFileResp',
  full_name='insta360.messages.GetFileResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='insta360.messages.GetFileResp.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='insta360.messages.GetFileResp.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=156,
)

_GETFILE.fields_by_name['file_type'].enum_type = file__type__pb2._FILETYPE
DESCRIPTOR.message_types_by_name['GetFile'] = _GETFILE
DESCRIPTOR.message_types_by_name['GetFileResp'] = _GETFILERESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFile = _reflection.GeneratedProtocolMessageType('GetFile', (_message.Message,), {
  'DESCRIPTOR' : _GETFILE,
  '__module__' : 'get_file_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.GetFile)
  })
_sym_db.RegisterMessage(GetFile)

GetFileResp = _reflection.GeneratedProtocolMessageType('GetFileResp', (_message.Message,), {
  'DESCRIPTOR' : _GETFILERESP,
  '__module__' : 'get_file_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.GetFileResp)
  })
_sym_db.RegisterMessage(GetFileResp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
