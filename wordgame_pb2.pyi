from abc import ABC

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor


class PhraseRequest(_message.Message, ABC):
    __slots__ = ["file_name"]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME: str
    def __init__(self, file_name: _Optional[str] = ...) -> None: ...


class PhraseResultReply(_message.Message, ABC):
    __slots__ = ["phrase"]
    PHRASE_FIELD_NUMBER: _ClassVar[int]
    PHRASE: str
    def __init__(self, phrase: _Optional[str] = ...) -> None: ...


class InitRequest(_message.Message, ABC):
    __slots__ = ["init_request_phrase"]
    INIT_REQUEST_PHRASE_FIELD_NUMBER: _ClassVar[int]
    INIT_REQUEST_PHRASE: str
    def __init__(self, init_request_phrase: _Optional[str] = ...) -> None: ...


class InitResultReply(_message.Message, ABC):
    __slots__ = ["init_result_phrase"]
    INIT_RESULT_PHRASE_FIELD_NUMBER: _ClassVar[int]
    INIT_RESULT_PHRASE: str
    def __init__(self, init_result_phrase: _Optional[str] = ...) -> None: ...


class LetterRequest(_message.Message, ABC):
    __slots__ = ["chosen_phrase", "initialized_phrase", "letter"]
    CHOSEN_PHRASE_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_PHRASE: str

    INITIALIZED_PHRASE_FIELD_NUMBER: _ClassVar[int]
    INITIALIZED_PHRASE: str

    LETTER_FIELD_NUMBER: _ClassVar[int]
    LETTER: str

    def __init__(self, chosen_phrase: _Optional[str] = ..., initialized_phrase: _Optional[str] = ..., letter: _Optional[str] = ...) -> None: ...


class LetterResultReply(_message.Message, ABC):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...



