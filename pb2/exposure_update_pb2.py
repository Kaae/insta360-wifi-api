# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exposure_update.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import options_pb2 as options__pb2
try:
  photo__pb2 = options__pb2.photo__pb2
except AttributeError:
  photo__pb2 = options__pb2.photo_pb2
try:
  video__pb2 = options__pb2.video__pb2
except AttributeError:
  video__pb2 = options__pb2.video_pb2
try:
  battery__pb2 = options__pb2.battery__pb2
except AttributeError:
  battery__pb2 = options__pb2.battery_pb2
try:
  storage__pb2 = options__pb2.storage__pb2
except AttributeError:
  storage__pb2 = options__pb2.storage_pb2
try:
  button__press__pb2 = options__pb2.button__press__pb2
except AttributeError:
  button__press__pb2 = options__pb2.button_press_pb2
try:
  flicker__pb2 = options__pb2.flicker__pb2
except AttributeError:
  flicker__pb2 = options__pb2.flicker_pb2
try:
  sensor__pb2 = options__pb2.sensor__pb2
except AttributeError:
  sensor__pb2 = options__pb2.sensor_pb2
try:
  chargebox__pb2 = options__pb2.chargebox__pb2
except AttributeError:
  chargebox__pb2 = options__pb2.chargebox_pb2
try:
  battery__pb2 = options__pb2.battery__pb2
except AttributeError:
  battery__pb2 = options__pb2.battery_pb2
try:
  offset__state__pb2 = options__pb2.offset__state__pb2
except AttributeError:
  offset__state__pb2 = options__pb2.offset_state_pb2
try:
  window__crop__info__pb2 = options__pb2.window__crop__info__pb2
except AttributeError:
  window__crop__info__pb2 = options__pb2.window_crop_info_pb2
import exposure_pb2 as exposure__pb2

from options_pb2 import *
from exposure_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='exposure_update.proto',
  package='insta360.messages',
  syntax='proto3',
  serialized_options=b'\242\002\005INSPB',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x65xposure_update.proto\x12\x11insta360.messages\x1a\roptions.proto\x1a\x0e\x65xposure.proto\"\xcc\x01\n\x1aNotificationExposureUpdate\x12\x36\n\rfunction_mode\x18\x01 \x01(\x0e\x32\x1f.insta360.messages.FunctionMode\x12:\n\x0estill_exposure\x18\x02 \x01(\x0b\x32\".insta360.messages.ExposureOptions\x12:\n\x0evideo_exposure\x18\x03 \x01(\x0b\x32\".insta360.messages.ExposureOptionsB\x08\xa2\x02\x05INSPBP\x00P\x01\x62\x06proto3'
  ,
  dependencies=[options__pb2.DESCRIPTOR,exposure__pb2.DESCRIPTOR,],
  public_dependencies=[options__pb2.DESCRIPTOR,exposure__pb2.DESCRIPTOR,])




_NOTIFICATIONEXPOSUREUPDATE = _descriptor.Descriptor(
  name='NotificationExposureUpdate',
  full_name='insta360.messages.NotificationExposureUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='function_mode', full_name='insta360.messages.NotificationExposureUpdate.function_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='still_exposure', full_name='insta360.messages.NotificationExposureUpdate.still_exposure', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='video_exposure', full_name='insta360.messages.NotificationExposureUpdate.video_exposure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=76,
  serialized_end=280,
)

_NOTIFICATIONEXPOSUREUPDATE.fields_by_name['function_mode'].enum_type = options__pb2._FUNCTIONMODE
_NOTIFICATIONEXPOSUREUPDATE.fields_by_name['still_exposure'].message_type = exposure__pb2._EXPOSUREOPTIONS
_NOTIFICATIONEXPOSUREUPDATE.fields_by_name['video_exposure'].message_type = exposure__pb2._EXPOSUREOPTIONS
DESCRIPTOR.message_types_by_name['NotificationExposureUpdate'] = _NOTIFICATIONEXPOSUREUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationExposureUpdate = _reflection.GeneratedProtocolMessageType('NotificationExposureUpdate', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONEXPOSUREUPDATE,
  '__module__' : 'exposure_update_pb2'
  # @@protoc_insertion_point(class_scope:insta360.messages.NotificationExposureUpdate)
  })
_sym_db.RegisterMessage(NotificationExposureUpdate)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
