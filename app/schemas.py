from pydantic import BaseModel, Field


class BaseMessageRequest(BaseModel):
    recipient_id: str = Field(..., description="Facebook ID получателя")


class TextMessageRequest(BaseMessageRequest):
    message_text: str = Field(..., description="Текст сообщения для отправки")


class MediaMessageRequest(BaseMessageRequest):
    media_url: str = Field(..., description="URL медиафайла для отправки")
    media_type: str = Field(..., description="Тип медиа: 'image', 'video', 'audio', 'file'")
