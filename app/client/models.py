from enum import Enum
from pydantic import BaseModel
from typing import Union, Optional


class AttachmentType(str, Enum):
    image = 'image'
    video = 'video'
    audio = 'audio'
    file = 'file'


class Recipient(BaseModel):
    id: str


class TextMessage(BaseModel):
    text: str


class AttachmentPayload(BaseModel):
    url: str
    is_reusable: Optional[bool] = True


class Attachment(BaseModel):
    type: AttachmentType
    payload: AttachmentPayload


class AttachmentMessage(BaseModel):
    attachment: Attachment


class MessageRequest(BaseModel):
    recipient: Recipient
    message: Union[TextMessage, AttachmentMessage]
