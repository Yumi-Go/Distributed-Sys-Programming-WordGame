from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResultReply(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class LetterRequest(_message.Message):
    __slots__ = ["letter"]
    LETTER_FIELD_NUMBER: _ClassVar[int]
    LETTER: str
    def __init__(self, letter: _Optional[str] = ...) -> None: ...
