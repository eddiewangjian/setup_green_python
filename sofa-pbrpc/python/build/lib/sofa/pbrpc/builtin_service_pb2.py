# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2
import sofa.pbrpc.rpc_option_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='sofa/pbrpc/builtin_service.proto',
  package='sofa.pbrpc.builtin',
  serialized_pb='\n sofa/pbrpc/builtin_service.proto\x12\x12sofa.pbrpc.builtin\x1a google/protobuf/descriptor.proto\x1a\x1bsofa/pbrpc/rpc_option.proto\"\x0f\n\rHealthRequest\"E\n\x0eHealthResponse\x12\x0e\n\x06health\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\t\"\xf7\x01\n\rServerOptions\x12\x17\n\x0fwork_thread_num\x18\x01 \x01(\x03\x12\x17\n\x0fkeep_alive_time\x18\x02 \x01(\x03\x12\x1f\n\x17max_pending_buffer_size\x18\x03 \x01(\x03\x12\x19\n\x11max_throughput_in\x18\x04 \x01(\x03\x12\x1a\n\x12max_throughput_out\x18\x05 \x01(\x03\x12 \n\x18\x64isable_builtin_services\x18\x06 \x01(\x08\x12\x1c\n\x14\x64isable_list_service\x18\x07 \x01(\x08\x12\x1c\n\x14max_connection_count\x18\x08 \x01(\x03\"\x16\n\x14ServerOptionsRequest\"K\n\x15ServerOptionsResponse\x12\x32\n\x07options\x18\x01 \x01(\x0b\x32!.sofa.pbrpc.builtin.ServerOptions\"J\n\x14UpdateOptionsRequest\x12\x32\n\x07options\x18\x01 \x01(\x0b\x32!.sofa.pbrpc.builtin.ServerOptions\"K\n\x15UpdateOptionsResponse\x12\x32\n\x07options\x18\x01 \x01(\x0b\x32!.sofa.pbrpc.builtin.ServerOptions\"\x15\n\x13ServerStatusRequest\"\xb4\x01\n\x14ServerStatusResponse\x12\x14\n\x0cis_listening\x18\x01 \x01(\x08\x12\x18\n\x10\x63onnection_count\x18\x02 \x01(\x03\x12\x15\n\rservice_count\x18\x03 \x01(\x03\x12\x1d\n\x15pending_message_count\x18\x04 \x01(\x03\x12\x1b\n\x13pending_buffer_size\x18\x05 \x01(\x03\x12\x19\n\x11pending_data_size\x18\x06 \x01(\x03\"\x14\n\x12ListServiceRequest\"\\\n\x13ListServiceResponse\x12\x10\n\x08services\x18\x01 \x03(\t\x12\x33\n\x05\x66iles\x18\x02 \x03(\x0b\x32$.google.protobuf.FileDescriptorProto\"\xd1\x01\n\nMethodStat\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12\x15\n\rsucceed_count\x18\x02 \x01(\x03\x12\x1b\n\x13succeed_avg_time_us\x18\x03 \x01(\x02\x12\x1b\n\x13succeed_max_time_us\x18\x04 \x01(\x03\x12\x14\n\x0c\x66\x61iled_count\x18\x05 \x01(\x03\x12\x1a\n\x12\x66\x61iled_avg_time_us\x18\x06 \x01(\x02\x12\x1a\n\x12\x66\x61iled_max_time_us\x18\x07 \x01(\x03\x12\x0f\n\x07slot_id\x18\x08 \x01(\x03\"\x9e\x01\n\x0bServiceStat\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x16\n\x0eperiod_seconds\x18\x02 \x01(\x03\x12\x15\n\rsucceed_count\x18\x03 \x01(\x03\x12\x14\n\x0c\x66\x61iled_count\x18\x04 \x01(\x03\x12\x34\n\x0cmethod_stats\x18\x05 \x03(\x0b\x32\x1e.sofa.pbrpc.builtin.MethodStat\"D\n\x0bStatRequest\x12\x19\n\x0cservice_name\x18\x01 \x01(\t:\x03\x61ll\x12\x1a\n\x0eperiod_seconds\x18\x02 \x01(\x03:\x02\x36\x30\"a\n\x0cStatResponse\x12\x36\n\rservice_stats\x18\x01 \x03(\x0b\x32\x1f.sofa.pbrpc.builtin.ServiceStat\x12\x19\n\x11server_start_time\x18\x02 \x01(\t2\xc8\x04\n\x0e\x42uiltinService\x12O\n\x06Health\x12!.sofa.pbrpc.builtin.HealthRequest\x1a\".sofa.pbrpc.builtin.HealthResponse\x12\x64\n\rServerOptions\x12(.sofa.pbrpc.builtin.ServerOptionsRequest\x1a).sofa.pbrpc.builtin.ServerOptionsResponse\x12\x64\n\rUpdateOptions\x12(.sofa.pbrpc.builtin.UpdateOptionsRequest\x1a).sofa.pbrpc.builtin.UpdateOptionsResponse\x12\x61\n\x0cServerStatus\x12\'.sofa.pbrpc.builtin.ServerStatusRequest\x1a(.sofa.pbrpc.builtin.ServerStatusResponse\x12\x64\n\x0bListService\x12&.sofa.pbrpc.builtin.ListServiceRequest\x1a\'.sofa.pbrpc.builtin.ListServiceResponse\"\x04\x90\xe2\t\x01\x12I\n\x04Stat\x12\x1f.sofa.pbrpc.builtin.StatRequest\x1a .sofa.pbrpc.builtin.StatResponse\x1a\x05\x80\xe2\t\xb8\x17\x42\t\x80\x01\x01\x88\x01\x01\x90\x01\x01')




_HEALTHREQUEST = descriptor.Descriptor(
  name='HealthRequest',
  full_name='sofa.pbrpc.builtin.HealthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=119,
  serialized_end=134,
)


_HEALTHRESPONSE = descriptor.Descriptor(
  name='HealthResponse',
  full_name='sofa.pbrpc.builtin.HealthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='health', full_name='sofa.pbrpc.builtin.HealthResponse.health', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='version', full_name='sofa.pbrpc.builtin.HealthResponse.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_time', full_name='sofa.pbrpc.builtin.HealthResponse.start_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=136,
  serialized_end=205,
)


_SERVEROPTIONS = descriptor.Descriptor(
  name='ServerOptions',
  full_name='sofa.pbrpc.builtin.ServerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='work_thread_num', full_name='sofa.pbrpc.builtin.ServerOptions.work_thread_num', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keep_alive_time', full_name='sofa.pbrpc.builtin.ServerOptions.keep_alive_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_pending_buffer_size', full_name='sofa.pbrpc.builtin.ServerOptions.max_pending_buffer_size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_throughput_in', full_name='sofa.pbrpc.builtin.ServerOptions.max_throughput_in', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_throughput_out', full_name='sofa.pbrpc.builtin.ServerOptions.max_throughput_out', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='disable_builtin_services', full_name='sofa.pbrpc.builtin.ServerOptions.disable_builtin_services', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='disable_list_service', full_name='sofa.pbrpc.builtin.ServerOptions.disable_list_service', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_connection_count', full_name='sofa.pbrpc.builtin.ServerOptions.max_connection_count', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=208,
  serialized_end=455,
)


_SERVEROPTIONSREQUEST = descriptor.Descriptor(
  name='ServerOptionsRequest',
  full_name='sofa.pbrpc.builtin.ServerOptionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=457,
  serialized_end=479,
)


_SERVEROPTIONSRESPONSE = descriptor.Descriptor(
  name='ServerOptionsResponse',
  full_name='sofa.pbrpc.builtin.ServerOptionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='options', full_name='sofa.pbrpc.builtin.ServerOptionsResponse.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=481,
  serialized_end=556,
)


_UPDATEOPTIONSREQUEST = descriptor.Descriptor(
  name='UpdateOptionsRequest',
  full_name='sofa.pbrpc.builtin.UpdateOptionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='options', full_name='sofa.pbrpc.builtin.UpdateOptionsRequest.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=558,
  serialized_end=632,
)


_UPDATEOPTIONSRESPONSE = descriptor.Descriptor(
  name='UpdateOptionsResponse',
  full_name='sofa.pbrpc.builtin.UpdateOptionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='options', full_name='sofa.pbrpc.builtin.UpdateOptionsResponse.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=634,
  serialized_end=709,
)


_SERVERSTATUSREQUEST = descriptor.Descriptor(
  name='ServerStatusRequest',
  full_name='sofa.pbrpc.builtin.ServerStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=711,
  serialized_end=732,
)


_SERVERSTATUSRESPONSE = descriptor.Descriptor(
  name='ServerStatusResponse',
  full_name='sofa.pbrpc.builtin.ServerStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='is_listening', full_name='sofa.pbrpc.builtin.ServerStatusResponse.is_listening', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='connection_count', full_name='sofa.pbrpc.builtin.ServerStatusResponse.connection_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='service_count', full_name='sofa.pbrpc.builtin.ServerStatusResponse.service_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pending_message_count', full_name='sofa.pbrpc.builtin.ServerStatusResponse.pending_message_count', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pending_buffer_size', full_name='sofa.pbrpc.builtin.ServerStatusResponse.pending_buffer_size', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pending_data_size', full_name='sofa.pbrpc.builtin.ServerStatusResponse.pending_data_size', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=735,
  serialized_end=915,
)


_LISTSERVICEREQUEST = descriptor.Descriptor(
  name='ListServiceRequest',
  full_name='sofa.pbrpc.builtin.ListServiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=917,
  serialized_end=937,
)


_LISTSERVICERESPONSE = descriptor.Descriptor(
  name='ListServiceResponse',
  full_name='sofa.pbrpc.builtin.ListServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='services', full_name='sofa.pbrpc.builtin.ListServiceResponse.services', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='files', full_name='sofa.pbrpc.builtin.ListServiceResponse.files', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=939,
  serialized_end=1031,
)


_METHODSTAT = descriptor.Descriptor(
  name='MethodStat',
  full_name='sofa.pbrpc.builtin.MethodStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='method_name', full_name='sofa.pbrpc.builtin.MethodStat.method_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='succeed_count', full_name='sofa.pbrpc.builtin.MethodStat.succeed_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='succeed_avg_time_us', full_name='sofa.pbrpc.builtin.MethodStat.succeed_avg_time_us', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='succeed_max_time_us', full_name='sofa.pbrpc.builtin.MethodStat.succeed_max_time_us', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failed_count', full_name='sofa.pbrpc.builtin.MethodStat.failed_count', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failed_avg_time_us', full_name='sofa.pbrpc.builtin.MethodStat.failed_avg_time_us', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failed_max_time_us', full_name='sofa.pbrpc.builtin.MethodStat.failed_max_time_us', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot_id', full_name='sofa.pbrpc.builtin.MethodStat.slot_id', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1034,
  serialized_end=1243,
)


_SERVICESTAT = descriptor.Descriptor(
  name='ServiceStat',
  full_name='sofa.pbrpc.builtin.ServiceStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_name', full_name='sofa.pbrpc.builtin.ServiceStat.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='period_seconds', full_name='sofa.pbrpc.builtin.ServiceStat.period_seconds', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='succeed_count', full_name='sofa.pbrpc.builtin.ServiceStat.succeed_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failed_count', full_name='sofa.pbrpc.builtin.ServiceStat.failed_count', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='method_stats', full_name='sofa.pbrpc.builtin.ServiceStat.method_stats', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1246,
  serialized_end=1404,
)


_STATREQUEST = descriptor.Descriptor(
  name='StatRequest',
  full_name='sofa.pbrpc.builtin.StatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_name', full_name='sofa.pbrpc.builtin.StatRequest.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("all", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='period_seconds', full_name='sofa.pbrpc.builtin.StatRequest.period_seconds', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=60,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1406,
  serialized_end=1474,
)


_STATRESPONSE = descriptor.Descriptor(
  name='StatResponse',
  full_name='sofa.pbrpc.builtin.StatResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='service_stats', full_name='sofa.pbrpc.builtin.StatResponse.service_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_start_time', full_name='sofa.pbrpc.builtin.StatResponse.server_start_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1476,
  serialized_end=1573,
)

_SERVEROPTIONSRESPONSE.fields_by_name['options'].message_type = _SERVEROPTIONS
_UPDATEOPTIONSREQUEST.fields_by_name['options'].message_type = _SERVEROPTIONS
_UPDATEOPTIONSRESPONSE.fields_by_name['options'].message_type = _SERVEROPTIONS
_LISTSERVICERESPONSE.fields_by_name['files'].message_type = google.protobuf.descriptor_pb2._FILEDESCRIPTORPROTO
_SERVICESTAT.fields_by_name['method_stats'].message_type = _METHODSTAT
_STATRESPONSE.fields_by_name['service_stats'].message_type = _SERVICESTAT
DESCRIPTOR.message_types_by_name['HealthRequest'] = _HEALTHREQUEST
DESCRIPTOR.message_types_by_name['HealthResponse'] = _HEALTHRESPONSE
DESCRIPTOR.message_types_by_name['ServerOptions'] = _SERVEROPTIONS
DESCRIPTOR.message_types_by_name['ServerOptionsRequest'] = _SERVEROPTIONSREQUEST
DESCRIPTOR.message_types_by_name['ServerOptionsResponse'] = _SERVEROPTIONSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateOptionsRequest'] = _UPDATEOPTIONSREQUEST
DESCRIPTOR.message_types_by_name['UpdateOptionsResponse'] = _UPDATEOPTIONSRESPONSE
DESCRIPTOR.message_types_by_name['ServerStatusRequest'] = _SERVERSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ServerStatusResponse'] = _SERVERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['ListServiceRequest'] = _LISTSERVICEREQUEST
DESCRIPTOR.message_types_by_name['ListServiceResponse'] = _LISTSERVICERESPONSE
DESCRIPTOR.message_types_by_name['MethodStat'] = _METHODSTAT
DESCRIPTOR.message_types_by_name['ServiceStat'] = _SERVICESTAT
DESCRIPTOR.message_types_by_name['StatRequest'] = _STATREQUEST
DESCRIPTOR.message_types_by_name['StatResponse'] = _STATRESPONSE

class HealthRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEALTHREQUEST
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.HealthRequest)

class HealthResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEALTHRESPONSE
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.HealthResponse)

class ServerOptions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVEROPTIONS
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ServerOptions)

class ServerOptionsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVEROPTIONSREQUEST
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ServerOptionsRequest)

class ServerOptionsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVEROPTIONSRESPONSE
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ServerOptionsResponse)

class UpdateOptionsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEOPTIONSREQUEST
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.UpdateOptionsRequest)

class UpdateOptionsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UPDATEOPTIONSRESPONSE
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.UpdateOptionsResponse)

class ServerStatusRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERSTATUSREQUEST
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ServerStatusRequest)

class ServerStatusResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERSTATUSRESPONSE
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ServerStatusResponse)

class ListServiceRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTSERVICEREQUEST
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ListServiceRequest)

class ListServiceResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LISTSERVICERESPONSE
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ListServiceResponse)

class MethodStat(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METHODSTAT
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.MethodStat)

class ServiceStat(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVICESTAT
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.ServiceStat)

class StatRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATREQUEST
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.StatRequest)

class StatResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATRESPONSE
  
  # @@protoc_insertion_point(class_scope:sofa.pbrpc.builtin.StatResponse)


_BUILTINSERVICE = descriptor.ServiceDescriptor(
  name='BuiltinService',
  full_name='sofa.pbrpc.builtin.BuiltinService',
  file=DESCRIPTOR,
  index=0,
  options=descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), '\200\342\t\270\027'),
  serialized_start=1576,
  serialized_end=2160,
  methods=[
  descriptor.MethodDescriptor(
    name='Health',
    full_name='sofa.pbrpc.builtin.BuiltinService.Health',
    index=0,
    containing_service=None,
    input_type=_HEALTHREQUEST,
    output_type=_HEALTHRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='ServerOptions',
    full_name='sofa.pbrpc.builtin.BuiltinService.ServerOptions',
    index=1,
    containing_service=None,
    input_type=_SERVEROPTIONSREQUEST,
    output_type=_SERVEROPTIONSRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='UpdateOptions',
    full_name='sofa.pbrpc.builtin.BuiltinService.UpdateOptions',
    index=2,
    containing_service=None,
    input_type=_UPDATEOPTIONSREQUEST,
    output_type=_UPDATEOPTIONSRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='ServerStatus',
    full_name='sofa.pbrpc.builtin.BuiltinService.ServerStatus',
    index=3,
    containing_service=None,
    input_type=_SERVERSTATUSREQUEST,
    output_type=_SERVERSTATUSRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='ListService',
    full_name='sofa.pbrpc.builtin.BuiltinService.ListService',
    index=4,
    containing_service=None,
    input_type=_LISTSERVICEREQUEST,
    output_type=_LISTSERVICERESPONSE,
    options=descriptor._ParseOptions(descriptor_pb2.MethodOptions(), '\220\342\t\001'),
  ),
  descriptor.MethodDescriptor(
    name='Stat',
    full_name='sofa.pbrpc.builtin.BuiltinService.Stat',
    index=5,
    containing_service=None,
    input_type=_STATREQUEST,
    output_type=_STATRESPONSE,
    options=None,
  ),
])

class BuiltinService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _BUILTINSERVICE
class BuiltinService_Stub(BuiltinService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _BUILTINSERVICE

# @@protoc_insertion_point(module_scope)
