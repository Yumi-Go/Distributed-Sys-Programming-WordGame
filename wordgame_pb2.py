# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/wordgame.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protos/wordgame.proto\x12\x08wordgame\"\"\n\rPhraseRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"#\n\x11PhraseResultReply\x12\x0e\n\x06phrase\x18\x01 \x01(\t\"*\n\x0bInitRequest\x12\x1b\n\x13init_request_phrase\x18\x01 \x01(\t\"-\n\x0fInitResultReply\x12\x1a\n\x12init_result_phrase\x18\x01 \x01(\t\"R\n\rLetterRequest\x12\x15\n\rchosen_phrase\x18\x01 \x01(\t\x12\x1a\n\x12initialized_phrase\x18\x02 \x01(\t\x12\x0e\n\x06letter\x18\x03 \x01(\t\"#\n\x11LetterResultReply\x12\x0e\n\x06result\x18\x01 \x01(\t\"8\n\x11GameResultRequest\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\x12\x12\n\nphrase_len\x18\x02 \x01(\x05\"&\n\x0fGameResultReply\x12\x13\n\x0bgame_result\x18\x01 \x01(\t2\xa6\x02\n\x04Game\x12\x46\n\x0c\x43hoosePhrase\x12\x17.wordgame.PhraseRequest\x1a\x1b.wordgame.PhraseResultReply\"\x00\x12\x46\n\x10InitializePhrase\x12\x15.wordgame.InitRequest\x1a\x19.wordgame.InitResultReply\"\x00\x12\x46\n\x0c\x43hangeLetter\x12\x17.wordgame.LetterRequest\x1a\x1b.wordgame.LetterResultReply\"\x00\x12\x46\n\nGameResult\x12\x1b.wordgame.GameResultRequest\x1a\x19.wordgame.GameResultReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.wordgame_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PHRASEREQUEST._serialized_start=35
  _PHRASEREQUEST._serialized_end=69
  _PHRASERESULTREPLY._serialized_start=71
  _PHRASERESULTREPLY._serialized_end=106
  _INITREQUEST._serialized_start=108
  _INITREQUEST._serialized_end=150
  _INITRESULTREPLY._serialized_start=152
  _INITRESULTREPLY._serialized_end=197
  _LETTERREQUEST._serialized_start=199
  _LETTERREQUEST._serialized_end=281
  _LETTERRESULTREPLY._serialized_start=283
  _LETTERRESULTREPLY._serialized_end=318
  _GAMERESULTREQUEST._serialized_start=320
  _GAMERESULTREQUEST._serialized_end=376
  _GAMERESULTREPLY._serialized_start=378
  _GAMERESULTREPLY._serialized_end=416
  _GAME._serialized_start=419
  _GAME._serialized_end=713
# @@protoc_insertion_point(module_scope)
