# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: definitions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='definitions.proto',
  package='fmuproxy.grpc',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x64\x65\x66initions.proto\x12\rfmuproxy.grpc\"\x9a\x04\n\x10ModelDescription\x12\x13\n\x0b\x66mi_version\x18\x01 \x01(\t\x12\x0c\n\x04guid\x18\x02 \x01(\t\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x12\x0f\n\x07license\x18\x04 \x01(\t\x12\x11\n\tcopyright\x18\x05 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x06 \x01(\t\x12\x0f\n\x07version\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x17\n\x0fgeneration_tool\x18\t \x01(\t\x12 \n\x18generation_date_and_time\x18\n \x01(\t\x12<\n\x12\x64\x65\x66\x61ult_experiment\x18\x0b \x01(\x0b\x32 .fmuproxy.grpc.DefaultExperiment\x12K\n\x1avariable_naming_convention\x18\x0c \x01(\x0e\x32\'.fmuproxy.grpc.VariableNamingConvention\x12\x36\n\x0fmodel_variables\x18\r \x03(\x0b\x32\x1d.fmuproxy.grpc.ScalarVariable\x12\x36\n\x0fmodel_structure\x18\x0e \x01(\x0b\x32\x1d.fmuproxy.grpc.ModelStructure\x12\x1e\n\x16supports_co_simulation\x18\x0f \x01(\x08\x12\x1f\n\x17supports_model_exchange\x18\x10 \x01(\x08\";\n\x10IntegerAttribute\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\x12\r\n\x05start\x18\x03 \x01(\x05\"8\n\rRealAttribute\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\r\n\x05start\x18\x03 \x01(\x01\" \n\x0fStringAttribute\x12\r\n\x05start\x18\x01 \x01(\t\"!\n\x10\x42ooleanAttribute\x12\r\n\x05start\x18\x01 \x01(\x08\"?\n\x14\x45numerationAttribute\x12\x0b\n\x03min\x18\x01 \x01(\x05\x12\x0b\n\x03max\x18\x02 \x01(\x05\x12\r\n\x05start\x18\x03 \x01(\x05\"\xad\x04\n\x0eScalarVariable\x12\x17\n\x0fvalue_reference\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rdeclared_type\x18\x04 \x01(\t\x12\'\n\x07initial\x18\x05 \x01(\x0e\x32\x16.fmuproxy.grpc.Initial\x12+\n\tcausality\x18\x06 \x01(\x0e\x32\x18.fmuproxy.grpc.Causality\x12/\n\x0bvariability\x18\x07 \x01(\x0e\x32\x1a.fmuproxy.grpc.Variability\x12<\n\x11integer_attribute\x18\n \x01(\x0b\x32\x1f.fmuproxy.grpc.IntegerAttributeH\x00\x12\x36\n\x0ereal_attribute\x18\x0b \x01(\x0b\x32\x1c.fmuproxy.grpc.RealAttributeH\x00\x12:\n\x10string_attribute\x18\x0c \x01(\x0b\x32\x1e.fmuproxy.grpc.StringAttributeH\x00\x12<\n\x11\x62oolean_attribute\x18\r \x01(\x0b\x32\x1f.fmuproxy.grpc.BooleanAttributeH\x00\x12\x44\n\x15\x65numeration_attribute\x18\x0e \x01(\x0b\x32#.fmuproxy.grpc.EnumerationAttributeH\x00\x42\x0b\n\tattribute\"`\n\x11\x44\x65\x66\x61ultExperiment\x12\x12\n\nstart_time\x18\x01 \x01(\x01\x12\x11\n\tstop_time\x18\x02 \x01(\x01\x12\x11\n\ttolerance\x18\x03 \x01(\x01\x12\x11\n\tstep_size\x18\x04 \x01(\x01\"j\n\x07Unknown\x12\r\n\x05index\x18\x01 \x01(\r\x12\x14\n\x0c\x64\x65pendencies\x18\x02 \x03(\r\x12:\n\x11\x64\x65pendencies_kind\x18\x03 \x01(\x0e\x32\x1f.fmuproxy.grpc.DependenciesKind\"\x98\x01\n\x0eModelStructure\x12\'\n\x07outputs\x18\x01 \x03(\x0b\x32\x16.fmuproxy.grpc.Unknown\x12+\n\x0b\x64\x65rivatives\x18\x02 \x03(\x0b\x32\x16.fmuproxy.grpc.Unknown\x12\x30\n\x10initial_unknowns\x18\x03 \x03(\x0b\x32\x16.fmuproxy.grpc.Unknown*\xa3\x01\n\tCausality\x12\x13\n\x0fINPUT_CAUSALITY\x10\x00\x12\x14\n\x10OUTPUT_CAUSALITY\x10\x01\x12\x17\n\x13PARAMETER_CAUSALITY\x10\x02\x12\"\n\x1e\x43\x41LCULATED_PARAMETER_CAUSALITY\x10\x03\x12\x13\n\x0fLOCAL_CAUSALITY\x10\x04\x12\x19\n\x15INDEPENDENT_CAUSALITY\x10\x05*\x8d\x01\n\x0bVariability\x12\x18\n\x14\x43ONSTANT_VARIABILITY\x10\x00\x12\x15\n\x11\x46IXED_VARIABILITY\x10\x01\x12\x1a\n\x16\x43ONTINUOUS_VARIABILITY\x10\x02\x12\x18\n\x14\x44ISCRETE_VARIABILITY\x10\x03\x12\x17\n\x13TUNABLE_VARIABILITY\x10\x04*H\n\x07Initial\x12\x11\n\rEXACT_INITIAL\x10\x00\x12\x12\n\x0e\x41PPROX_INITIAL\x10\x01\x12\x16\n\x12\x43\x41LCULATED_INITIAL\x10\x02*w\n\x06Status\x12\r\n\tOK_STATUS\x10\x00\x12\x12\n\x0eWARNING_STATUS\x10\x01\x12\x12\n\x0e\x44ISCARD_STATUS\x10\x02\x12\x10\n\x0c\x45RROR_STATUS\x10\x03\x12\x10\n\x0c\x46\x41TAL_STATUS\x10\x04\x12\x12\n\x0ePENDING_STATUS\x10\x05*^\n\x10\x44\x65pendenciesKind\x12\x12\n\x0e\x44\x45PENDENT_KIND\x10\x00\x12\x11\n\rCONSTANT_KIND\x10\x01\x12\x10\n\x0cTUNABLE_KIND\x10\x02\x12\x11\n\rDISCRETE_KIND\x10\x04*4\n\x18VariableNamingConvention\x12\x08\n\x04\x46LAT\x10\x00\x12\x0e\n\nSTRUCTURED\x10\x01\x42*\n!no.mechatronics.sfi.fmuproxy.grpcB\x05Protob\x06proto3')
)

_CAUSALITY = _descriptor.EnumDescriptor(
  name='Causality',
  full_name='fmuproxy.grpc.Causality',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPUT_CAUSALITY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_CAUSALITY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAMETER_CAUSALITY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALCULATED_PARAMETER_CAUSALITY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL_CAUSALITY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEPENDENT_CAUSALITY', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1752,
  serialized_end=1915,
)
_sym_db.RegisterEnumDescriptor(_CAUSALITY)

Causality = enum_type_wrapper.EnumTypeWrapper(_CAUSALITY)
_VARIABILITY = _descriptor.EnumDescriptor(
  name='Variability',
  full_name='fmuproxy.grpc.Variability',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONSTANT_VARIABILITY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIXED_VARIABILITY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS_VARIABILITY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCRETE_VARIABILITY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNABLE_VARIABILITY', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1918,
  serialized_end=2059,
)
_sym_db.RegisterEnumDescriptor(_VARIABILITY)

Variability = enum_type_wrapper.EnumTypeWrapper(_VARIABILITY)
_INITIAL = _descriptor.EnumDescriptor(
  name='Initial',
  full_name='fmuproxy.grpc.Initial',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXACT_INITIAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROX_INITIAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALCULATED_INITIAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2061,
  serialized_end=2133,
)
_sym_db.RegisterEnumDescriptor(_INITIAL)

Initial = enum_type_wrapper.EnumTypeWrapper(_INITIAL)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fmuproxy.grpc.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK_STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING_STATUS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCARD_STATUS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_STATUS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FATAL_STATUS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING_STATUS', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2135,
  serialized_end=2254,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_DEPENDENCIESKIND = _descriptor.EnumDescriptor(
  name='DependenciesKind',
  full_name='fmuproxy.grpc.DependenciesKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPENDENT_KIND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSTANT_KIND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TUNABLE_KIND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCRETE_KIND', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2256,
  serialized_end=2350,
)
_sym_db.RegisterEnumDescriptor(_DEPENDENCIESKIND)

DependenciesKind = enum_type_wrapper.EnumTypeWrapper(_DEPENDENCIESKIND)
_VARIABLENAMINGCONVENTION = _descriptor.EnumDescriptor(
  name='VariableNamingConvention',
  full_name='fmuproxy.grpc.VariableNamingConvention',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLAT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRUCTURED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2352,
  serialized_end=2404,
)
_sym_db.RegisterEnumDescriptor(_VARIABLENAMINGCONVENTION)

VariableNamingConvention = enum_type_wrapper.EnumTypeWrapper(_VARIABLENAMINGCONVENTION)
INPUT_CAUSALITY = 0
OUTPUT_CAUSALITY = 1
PARAMETER_CAUSALITY = 2
CALCULATED_PARAMETER_CAUSALITY = 3
LOCAL_CAUSALITY = 4
INDEPENDENT_CAUSALITY = 5
CONSTANT_VARIABILITY = 0
FIXED_VARIABILITY = 1
CONTINUOUS_VARIABILITY = 2
DISCRETE_VARIABILITY = 3
TUNABLE_VARIABILITY = 4
EXACT_INITIAL = 0
APPROX_INITIAL = 1
CALCULATED_INITIAL = 2
OK_STATUS = 0
WARNING_STATUS = 1
DISCARD_STATUS = 2
ERROR_STATUS = 3
FATAL_STATUS = 4
PENDING_STATUS = 5
DEPENDENT_KIND = 0
CONSTANT_KIND = 1
TUNABLE_KIND = 2
DISCRETE_KIND = 4
FLAT = 0
STRUCTURED = 1



_MODELDESCRIPTION = _descriptor.Descriptor(
  name='ModelDescription',
  full_name='fmuproxy.grpc.ModelDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fmi_version', full_name='fmuproxy.grpc.ModelDescription.fmi_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='fmuproxy.grpc.ModelDescription.guid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='fmuproxy.grpc.ModelDescription.model_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='license', full_name='fmuproxy.grpc.ModelDescription.license', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='copyright', full_name='fmuproxy.grpc.ModelDescription.copyright', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='fmuproxy.grpc.ModelDescription.author', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='fmuproxy.grpc.ModelDescription.version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='fmuproxy.grpc.ModelDescription.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation_tool', full_name='fmuproxy.grpc.ModelDescription.generation_tool', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generation_date_and_time', full_name='fmuproxy.grpc.ModelDescription.generation_date_and_time', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_experiment', full_name='fmuproxy.grpc.ModelDescription.default_experiment', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variable_naming_convention', full_name='fmuproxy.grpc.ModelDescription.variable_naming_convention', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_variables', full_name='fmuproxy.grpc.ModelDescription.model_variables', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_structure', full_name='fmuproxy.grpc.ModelDescription.model_structure', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supports_co_simulation', full_name='fmuproxy.grpc.ModelDescription.supports_co_simulation', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supports_model_exchange', full_name='fmuproxy.grpc.ModelDescription.supports_model_exchange', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=575,
)


_INTEGERATTRIBUTE = _descriptor.Descriptor(
  name='IntegerAttribute',
  full_name='fmuproxy.grpc.IntegerAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='fmuproxy.grpc.IntegerAttribute.min', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='fmuproxy.grpc.IntegerAttribute.max', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='fmuproxy.grpc.IntegerAttribute.start', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=636,
)


_REALATTRIBUTE = _descriptor.Descriptor(
  name='RealAttribute',
  full_name='fmuproxy.grpc.RealAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='fmuproxy.grpc.RealAttribute.min', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='fmuproxy.grpc.RealAttribute.max', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='fmuproxy.grpc.RealAttribute.start', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=638,
  serialized_end=694,
)


_STRINGATTRIBUTE = _descriptor.Descriptor(
  name='StringAttribute',
  full_name='fmuproxy.grpc.StringAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='fmuproxy.grpc.StringAttribute.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=728,
)


_BOOLEANATTRIBUTE = _descriptor.Descriptor(
  name='BooleanAttribute',
  full_name='fmuproxy.grpc.BooleanAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='fmuproxy.grpc.BooleanAttribute.start', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=730,
  serialized_end=763,
)


_ENUMERATIONATTRIBUTE = _descriptor.Descriptor(
  name='EnumerationAttribute',
  full_name='fmuproxy.grpc.EnumerationAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='fmuproxy.grpc.EnumerationAttribute.min', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='fmuproxy.grpc.EnumerationAttribute.max', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='fmuproxy.grpc.EnumerationAttribute.start', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=828,
)


_SCALARVARIABLE = _descriptor.Descriptor(
  name='ScalarVariable',
  full_name='fmuproxy.grpc.ScalarVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value_reference', full_name='fmuproxy.grpc.ScalarVariable.value_reference', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='fmuproxy.grpc.ScalarVariable.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='fmuproxy.grpc.ScalarVariable.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='declared_type', full_name='fmuproxy.grpc.ScalarVariable.declared_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial', full_name='fmuproxy.grpc.ScalarVariable.initial', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='causality', full_name='fmuproxy.grpc.ScalarVariable.causality', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variability', full_name='fmuproxy.grpc.ScalarVariable.variability', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integer_attribute', full_name='fmuproxy.grpc.ScalarVariable.integer_attribute', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='real_attribute', full_name='fmuproxy.grpc.ScalarVariable.real_attribute', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_attribute', full_name='fmuproxy.grpc.ScalarVariable.string_attribute', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean_attribute', full_name='fmuproxy.grpc.ScalarVariable.boolean_attribute', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enumeration_attribute', full_name='fmuproxy.grpc.ScalarVariable.enumeration_attribute', index=11,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='attribute', full_name='fmuproxy.grpc.ScalarVariable.attribute',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=831,
  serialized_end=1388,
)


_DEFAULTEXPERIMENT = _descriptor.Descriptor(
  name='DefaultExperiment',
  full_name='fmuproxy.grpc.DefaultExperiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='fmuproxy.grpc.DefaultExperiment.start_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_time', full_name='fmuproxy.grpc.DefaultExperiment.stop_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tolerance', full_name='fmuproxy.grpc.DefaultExperiment.tolerance', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step_size', full_name='fmuproxy.grpc.DefaultExperiment.step_size', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1390,
  serialized_end=1486,
)


_UNKNOWN = _descriptor.Descriptor(
  name='Unknown',
  full_name='fmuproxy.grpc.Unknown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='fmuproxy.grpc.Unknown.index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='fmuproxy.grpc.Unknown.dependencies', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies_kind', full_name='fmuproxy.grpc.Unknown.dependencies_kind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1488,
  serialized_end=1594,
)


_MODELSTRUCTURE = _descriptor.Descriptor(
  name='ModelStructure',
  full_name='fmuproxy.grpc.ModelStructure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='fmuproxy.grpc.ModelStructure.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derivatives', full_name='fmuproxy.grpc.ModelStructure.derivatives', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_unknowns', full_name='fmuproxy.grpc.ModelStructure.initial_unknowns', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1597,
  serialized_end=1749,
)

_MODELDESCRIPTION.fields_by_name['default_experiment'].message_type = _DEFAULTEXPERIMENT
_MODELDESCRIPTION.fields_by_name['variable_naming_convention'].enum_type = _VARIABLENAMINGCONVENTION
_MODELDESCRIPTION.fields_by_name['model_variables'].message_type = _SCALARVARIABLE
_MODELDESCRIPTION.fields_by_name['model_structure'].message_type = _MODELSTRUCTURE
_SCALARVARIABLE.fields_by_name['initial'].enum_type = _INITIAL
_SCALARVARIABLE.fields_by_name['causality'].enum_type = _CAUSALITY
_SCALARVARIABLE.fields_by_name['variability'].enum_type = _VARIABILITY
_SCALARVARIABLE.fields_by_name['integer_attribute'].message_type = _INTEGERATTRIBUTE
_SCALARVARIABLE.fields_by_name['real_attribute'].message_type = _REALATTRIBUTE
_SCALARVARIABLE.fields_by_name['string_attribute'].message_type = _STRINGATTRIBUTE
_SCALARVARIABLE.fields_by_name['boolean_attribute'].message_type = _BOOLEANATTRIBUTE
_SCALARVARIABLE.fields_by_name['enumeration_attribute'].message_type = _ENUMERATIONATTRIBUTE
_SCALARVARIABLE.oneofs_by_name['attribute'].fields.append(
  _SCALARVARIABLE.fields_by_name['integer_attribute'])
_SCALARVARIABLE.fields_by_name['integer_attribute'].containing_oneof = _SCALARVARIABLE.oneofs_by_name['attribute']
_SCALARVARIABLE.oneofs_by_name['attribute'].fields.append(
  _SCALARVARIABLE.fields_by_name['real_attribute'])
_SCALARVARIABLE.fields_by_name['real_attribute'].containing_oneof = _SCALARVARIABLE.oneofs_by_name['attribute']
_SCALARVARIABLE.oneofs_by_name['attribute'].fields.append(
  _SCALARVARIABLE.fields_by_name['string_attribute'])
_SCALARVARIABLE.fields_by_name['string_attribute'].containing_oneof = _SCALARVARIABLE.oneofs_by_name['attribute']
_SCALARVARIABLE.oneofs_by_name['attribute'].fields.append(
  _SCALARVARIABLE.fields_by_name['boolean_attribute'])
_SCALARVARIABLE.fields_by_name['boolean_attribute'].containing_oneof = _SCALARVARIABLE.oneofs_by_name['attribute']
_SCALARVARIABLE.oneofs_by_name['attribute'].fields.append(
  _SCALARVARIABLE.fields_by_name['enumeration_attribute'])
_SCALARVARIABLE.fields_by_name['enumeration_attribute'].containing_oneof = _SCALARVARIABLE.oneofs_by_name['attribute']
_UNKNOWN.fields_by_name['dependencies_kind'].enum_type = _DEPENDENCIESKIND
_MODELSTRUCTURE.fields_by_name['outputs'].message_type = _UNKNOWN
_MODELSTRUCTURE.fields_by_name['derivatives'].message_type = _UNKNOWN
_MODELSTRUCTURE.fields_by_name['initial_unknowns'].message_type = _UNKNOWN
DESCRIPTOR.message_types_by_name['ModelDescription'] = _MODELDESCRIPTION
DESCRIPTOR.message_types_by_name['IntegerAttribute'] = _INTEGERATTRIBUTE
DESCRIPTOR.message_types_by_name['RealAttribute'] = _REALATTRIBUTE
DESCRIPTOR.message_types_by_name['StringAttribute'] = _STRINGATTRIBUTE
DESCRIPTOR.message_types_by_name['BooleanAttribute'] = _BOOLEANATTRIBUTE
DESCRIPTOR.message_types_by_name['EnumerationAttribute'] = _ENUMERATIONATTRIBUTE
DESCRIPTOR.message_types_by_name['ScalarVariable'] = _SCALARVARIABLE
DESCRIPTOR.message_types_by_name['DefaultExperiment'] = _DEFAULTEXPERIMENT
DESCRIPTOR.message_types_by_name['Unknown'] = _UNKNOWN
DESCRIPTOR.message_types_by_name['ModelStructure'] = _MODELSTRUCTURE
DESCRIPTOR.enum_types_by_name['Causality'] = _CAUSALITY
DESCRIPTOR.enum_types_by_name['Variability'] = _VARIABILITY
DESCRIPTOR.enum_types_by_name['Initial'] = _INITIAL
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['DependenciesKind'] = _DEPENDENCIESKIND
DESCRIPTOR.enum_types_by_name['VariableNamingConvention'] = _VARIABLENAMINGCONVENTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModelDescription = _reflection.GeneratedProtocolMessageType('ModelDescription', (_message.Message,), dict(
  DESCRIPTOR = _MODELDESCRIPTION,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.ModelDescription)
  ))
_sym_db.RegisterMessage(ModelDescription)

IntegerAttribute = _reflection.GeneratedProtocolMessageType('IntegerAttribute', (_message.Message,), dict(
  DESCRIPTOR = _INTEGERATTRIBUTE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.IntegerAttribute)
  ))
_sym_db.RegisterMessage(IntegerAttribute)

RealAttribute = _reflection.GeneratedProtocolMessageType('RealAttribute', (_message.Message,), dict(
  DESCRIPTOR = _REALATTRIBUTE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.RealAttribute)
  ))
_sym_db.RegisterMessage(RealAttribute)

StringAttribute = _reflection.GeneratedProtocolMessageType('StringAttribute', (_message.Message,), dict(
  DESCRIPTOR = _STRINGATTRIBUTE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.StringAttribute)
  ))
_sym_db.RegisterMessage(StringAttribute)

BooleanAttribute = _reflection.GeneratedProtocolMessageType('BooleanAttribute', (_message.Message,), dict(
  DESCRIPTOR = _BOOLEANATTRIBUTE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.BooleanAttribute)
  ))
_sym_db.RegisterMessage(BooleanAttribute)

EnumerationAttribute = _reflection.GeneratedProtocolMessageType('EnumerationAttribute', (_message.Message,), dict(
  DESCRIPTOR = _ENUMERATIONATTRIBUTE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.EnumerationAttribute)
  ))
_sym_db.RegisterMessage(EnumerationAttribute)

ScalarVariable = _reflection.GeneratedProtocolMessageType('ScalarVariable', (_message.Message,), dict(
  DESCRIPTOR = _SCALARVARIABLE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.ScalarVariable)
  ))
_sym_db.RegisterMessage(ScalarVariable)

DefaultExperiment = _reflection.GeneratedProtocolMessageType('DefaultExperiment', (_message.Message,), dict(
  DESCRIPTOR = _DEFAULTEXPERIMENT,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.DefaultExperiment)
  ))
_sym_db.RegisterMessage(DefaultExperiment)

Unknown = _reflection.GeneratedProtocolMessageType('Unknown', (_message.Message,), dict(
  DESCRIPTOR = _UNKNOWN,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.Unknown)
  ))
_sym_db.RegisterMessage(Unknown)

ModelStructure = _reflection.GeneratedProtocolMessageType('ModelStructure', (_message.Message,), dict(
  DESCRIPTOR = _MODELSTRUCTURE,
  __module__ = 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:fmuproxy.grpc.ModelStructure)
  ))
_sym_db.RegisterMessage(ModelStructure)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!no.mechatronics.sfi.fmuproxy.grpcB\005Proto'))
# @@protoc_insertion_point(module_scope)
