import dataclasses
import enum


class MessageType(enum.Enum):
    TEXT = enum.auto()


@dataclasses.dataclass(frozen=True)
class BaseMessage:
    user_id: int
    track_code: str
    msg_type: MessageType = dataclasses.field(init=False)


@dataclasses.dataclass(frozen=True)
class TextMessage(BaseMessage):
    text: str
    msg_type = MessageType.TEXT


@dataclasses.dataclass(frozen=True)
class BaseRenderReq:
    user_id: int
    track_code: str
    language: str


@dataclasses.dataclass(frozen=True)
class NewUserReq(BaseRenderReq):
    pass


@dataclasses.dataclass(frozen=True)
class OldUserAcceptedReq(BaseRenderReq):
    pass


@dataclasses.dataclass(frozen=True)
class OldUserIsNotAcceptedReq(BaseRenderReq):
    pass
