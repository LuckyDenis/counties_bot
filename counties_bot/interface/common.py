import dataclasses
import enum


class MessageType(enum.Enum):
    TEXT = enum.auto()


@dataclasses.dataclass(frozen=True)
class BaseMessage:
    chat_id: int
    track_code: str
    msg_type: MessageType = dataclasses.field(init=False)


@dataclasses.dataclass(frozen=True)
class TextMessage(BaseMessage):
    text: str
    msg_type = MessageType.TEXT


@dataclasses.dataclass(frozen=True)
class BaseRenderReq:
    chat_id: int
    track_code: str
    language: str


@dataclasses.dataclass(frozen=True)
class NewUserReq(BaseRenderReq):
    pass
