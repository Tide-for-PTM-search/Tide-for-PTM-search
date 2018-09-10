# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: header.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='header.proto',
  package='pb',
  serialized_pb='\n\x0cheader.proto\x12\x02pb\"E\n\x0cModification\x12\x13\n\x0b\x61mino_acids\x18\x01 \x01(\t\x12\r\n\x05\x64\x65lta\x18\x02 \x01(\x01\x12\x11\n\tmax_count\x18\x03 \x01(\x05\"o\n\x08ModTable\x12&\n\x0cvariable_mod\x18\x01 \x03(\x0b\x32\x10.pb.Modification\x12$\n\nstatic_mod\x18\x02 \x03(\x0b\x32\x10.pb.Modification\x12\x15\n\runique_deltas\x18\n \x03(\x01\"\xd2\x08\n\x06Header\x12!\n\x06source\x18\x01 \x03(\x0b\x32\x11.pb.Header.Source\x12&\n\tfile_type\x18\x02 \x02(\x0e\x32\x13.pb.Header.FileType\x12\x39\n\x13raw_proteins_header\x18\x03 \x01(\x0b\x32\x1c.pb.Header.RawProteinsHeader\x12\x32\n\x0fpeptides_header\x18\x04 \x01(\x0b\x32\x19.pb.Header.PeptidesHeader\x12\x30\n\x0espectra_header\x18\x05 \x01(\x0b\x32\x18.pb.Header.SpectraHeader\x12\x30\n\x0eresults_header\x18\x06 \x01(\x0b\x32\x18.pb.Header.ResultsHeader\x12\x36\n\x0f\x61ux_locs_header\x18\x07 \x01(\x0b\x32\x1d.pb.Header.AuxLocationsHeader\x12\x14\n\x0c\x63ommand_line\x18\x08 \x01(\t\x1aH\n\x06Source\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x1a\n\x06header\x18\x02 \x01(\x0b\x32\n.pb.Header\x12\x10\n\x08\x66iletype\x18\x03 \x01(\t\x1a\x13\n\x11RawProteinsHeader\x1a\xe2\x02\n\x0ePeptidesHeader\x12\x10\n\x08min_mass\x18\x03 \x01(\x01\x12\x10\n\x08max_mass\x18\x04 \x01(\x01\x12\x12\n\nmin_length\x18\x05 \x01(\x05\x12\x12\n\nmax_length\x18\x06 \x01(\x05\x12\x0e\n\x06\x65nzyme\x18\x07 \x01(\t\x12\x16\n\x0e\x66ull_digestion\x18\x08 \x01(\x08\x12\x1c\n\x14max_missed_cleavages\x18\x0e \x01(\x05\x12\x1e\n\x16monoisotopic_precursor\x18\r \x01(\x08\x12\x11\n\thas_peaks\x18\n \x01(\x08\x12\x1b\n\x13\x64ownselect_fraction\x18\x0b \x01(\x01\x12\x1a\n\x04mods\x18\x0c \x01(\x0b\x32\x0c.pb.ModTable\x12 \n\nnterm_mods\x18\x0f \x01(\x0b\x32\x0c.pb.ModTable\x12 \n\ncterm_mods\x18\x10 \x01(\x0b\x32\x0c.pb.ModTable\x12\x0e\n\x06\x64\x65\x63oys\x18\t \x01(\x05\x1a\x1f\n\rSpectraHeader\x12\x0e\n\x06sorted\x18\x02 \x01(\x08\x1am\n\rResultsHeader\x12\x13\n\x0bmass_window\x18\x01 \x01(\x01\x12\x13\n\x0btop_matches\x18\x02 \x01(\x05\x12\x32\n\x0fpeptides_header\x18\x03 \x01(\x0b\x32\x19.pb.Header.PeptidesHeader\x1a\x14\n\x12\x41uxLocationsHeader\"r\n\x08\x46ileType\x12\x10\n\x0cRAW_PROTEINS\x10\x00\x12\x0c\n\x08PEPTIDES\x10\x01\x12\x0b\n\x07SPECTRA\x10\x02\x12\n\n\x06PARAMS\x10\x03\x12\r\n\tMOD_TABLE\x10\x04\x12\x0b\n\x07RESULTS\x10\x05\x12\x11\n\rAUX_LOCATIONS\x10\x06')



_HEADER_FILETYPE = _descriptor.EnumDescriptor(
  name='FileType',
  full_name='pb.Header.FileType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW_PROTEINS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEPTIDES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECTRA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARAMS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOD_TABLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUX_LOCATIONS', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1197,
  serialized_end=1311,
)


_MODIFICATION = _descriptor.Descriptor(
  name='Modification',
  full_name='pb.Modification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amino_acids', full_name='pb.Modification.amino_acids', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delta', full_name='pb.Modification.delta', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_count', full_name='pb.Modification.max_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=20,
  serialized_end=89,
)


_MODTABLE = _descriptor.Descriptor(
  name='ModTable',
  full_name='pb.ModTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable_mod', full_name='pb.ModTable.variable_mod', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static_mod', full_name='pb.ModTable.static_mod', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_deltas', full_name='pb.ModTable.unique_deltas', index=2,
      number=10, type=1, cpp_type=5, label=3,
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
  serialized_start=91,
  serialized_end=202,
)


_HEADER_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='pb.Header.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='pb.Header.Source.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header', full_name='pb.Header.Source.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filetype', full_name='pb.Header.Source.filetype', index=2,
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
  serialized_start=579,
  serialized_end=651,
)

_HEADER_RAWPROTEINSHEADER = _descriptor.Descriptor(
  name='RawProteinsHeader',
  full_name='pb.Header.RawProteinsHeader',
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
  serialized_start=653,
  serialized_end=672,
)

_HEADER_PEPTIDESHEADER = _descriptor.Descriptor(
  name='PeptidesHeader',
  full_name='pb.Header.PeptidesHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_mass', full_name='pb.Header.PeptidesHeader.min_mass', index=0,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_mass', full_name='pb.Header.PeptidesHeader.max_mass', index=1,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_length', full_name='pb.Header.PeptidesHeader.min_length', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_length', full_name='pb.Header.PeptidesHeader.max_length', index=3,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enzyme', full_name='pb.Header.PeptidesHeader.enzyme', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_digestion', full_name='pb.Header.PeptidesHeader.full_digestion', index=5,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_missed_cleavages', full_name='pb.Header.PeptidesHeader.max_missed_cleavages', index=6,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monoisotopic_precursor', full_name='pb.Header.PeptidesHeader.monoisotopic_precursor', index=7,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_peaks', full_name='pb.Header.PeptidesHeader.has_peaks', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downselect_fraction', full_name='pb.Header.PeptidesHeader.downselect_fraction', index=9,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mods', full_name='pb.Header.PeptidesHeader.mods', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nterm_mods', full_name='pb.Header.PeptidesHeader.nterm_mods', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cterm_mods', full_name='pb.Header.PeptidesHeader.cterm_mods', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decoys', full_name='pb.Header.PeptidesHeader.decoys', index=13,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=675,
  serialized_end=1029,
)

_HEADER_SPECTRAHEADER = _descriptor.Descriptor(
  name='SpectraHeader',
  full_name='pb.Header.SpectraHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sorted', full_name='pb.Header.SpectraHeader.sorted', index=0,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1031,
  serialized_end=1062,
)

_HEADER_RESULTSHEADER = _descriptor.Descriptor(
  name='ResultsHeader',
  full_name='pb.Header.ResultsHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mass_window', full_name='pb.Header.ResultsHeader.mass_window', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top_matches', full_name='pb.Header.ResultsHeader.top_matches', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peptides_header', full_name='pb.Header.ResultsHeader.peptides_header', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1064,
  serialized_end=1173,
)

_HEADER_AUXLOCATIONSHEADER = _descriptor.Descriptor(
  name='AuxLocationsHeader',
  full_name='pb.Header.AuxLocationsHeader',
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
  serialized_start=1175,
  serialized_end=1195,
)

_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='pb.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='pb.Header.source', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_type', full_name='pb.Header.file_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_proteins_header', full_name='pb.Header.raw_proteins_header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peptides_header', full_name='pb.Header.peptides_header', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spectra_header', full_name='pb.Header.spectra_header', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results_header', full_name='pb.Header.results_header', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux_locs_header', full_name='pb.Header.aux_locs_header', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_line', full_name='pb.Header.command_line', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HEADER_SOURCE, _HEADER_RAWPROTEINSHEADER, _HEADER_PEPTIDESHEADER, _HEADER_SPECTRAHEADER, _HEADER_RESULTSHEADER, _HEADER_AUXLOCATIONSHEADER, ],
  enum_types=[
    _HEADER_FILETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=205,
  serialized_end=1311,
)

_MODTABLE.fields_by_name['variable_mod'].message_type = _MODIFICATION
_MODTABLE.fields_by_name['static_mod'].message_type = _MODIFICATION
_HEADER_SOURCE.fields_by_name['header'].message_type = _HEADER
_HEADER_SOURCE.containing_type = _HEADER;
_HEADER_RAWPROTEINSHEADER.containing_type = _HEADER;
_HEADER_PEPTIDESHEADER.fields_by_name['mods'].message_type = _MODTABLE
_HEADER_PEPTIDESHEADER.fields_by_name['nterm_mods'].message_type = _MODTABLE
_HEADER_PEPTIDESHEADER.fields_by_name['cterm_mods'].message_type = _MODTABLE
_HEADER_PEPTIDESHEADER.containing_type = _HEADER;
_HEADER_SPECTRAHEADER.containing_type = _HEADER;
_HEADER_RESULTSHEADER.fields_by_name['peptides_header'].message_type = _HEADER_PEPTIDESHEADER
_HEADER_RESULTSHEADER.containing_type = _HEADER;
_HEADER_AUXLOCATIONSHEADER.containing_type = _HEADER;
_HEADER.fields_by_name['source'].message_type = _HEADER_SOURCE
_HEADER.fields_by_name['file_type'].enum_type = _HEADER_FILETYPE
_HEADER.fields_by_name['raw_proteins_header'].message_type = _HEADER_RAWPROTEINSHEADER
_HEADER.fields_by_name['peptides_header'].message_type = _HEADER_PEPTIDESHEADER
_HEADER.fields_by_name['spectra_header'].message_type = _HEADER_SPECTRAHEADER
_HEADER.fields_by_name['results_header'].message_type = _HEADER_RESULTSHEADER
_HEADER.fields_by_name['aux_locs_header'].message_type = _HEADER_AUXLOCATIONSHEADER
_HEADER_FILETYPE.containing_type = _HEADER;
DESCRIPTOR.message_types_by_name['Modification'] = _MODIFICATION
DESCRIPTOR.message_types_by_name['ModTable'] = _MODTABLE
DESCRIPTOR.message_types_by_name['Header'] = _HEADER

class Modification(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODIFICATION

  # @@protoc_insertion_point(class_scope:pb.Modification)

class ModTable(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MODTABLE

  # @@protoc_insertion_point(class_scope:pb.ModTable)

class Header(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Source(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEADER_SOURCE

    # @@protoc_insertion_point(class_scope:pb.Header.Source)

  class RawProteinsHeader(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEADER_RAWPROTEINSHEADER

    # @@protoc_insertion_point(class_scope:pb.Header.RawProteinsHeader)

  class PeptidesHeader(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEADER_PEPTIDESHEADER

    # @@protoc_insertion_point(class_scope:pb.Header.PeptidesHeader)

  class SpectraHeader(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEADER_SPECTRAHEADER

    # @@protoc_insertion_point(class_scope:pb.Header.SpectraHeader)

  class ResultsHeader(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEADER_RESULTSHEADER

    # @@protoc_insertion_point(class_scope:pb.Header.ResultsHeader)

  class AuxLocationsHeader(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEADER_AUXLOCATIONSHEADER

    # @@protoc_insertion_point(class_scope:pb.Header.AuxLocationsHeader)
  DESCRIPTOR = _HEADER

  # @@protoc_insertion_point(class_scope:pb.Header)


# @@protoc_insertion_point(module_scope)
