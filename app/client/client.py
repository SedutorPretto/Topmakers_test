import httpx
from .models import Recipient, TextMessage, AttachmentPayload, AttachmentMessage, MessageRequest, Attachment


class MessageClient:
    def __init__(self, page_access_token: str):
        self.page_access_token = page_access_token
        self.api_url = "https://graph.facebook.com/v13.0/me/messages"
        self.headers = {'Content-Type': 'application/json'}

    async def _send_request(self, request_body: MessageRequest):
        params = {'access_token': self.page_access_token}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                params=params,
                json=request_body.model_dump(),
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()

    async def send_text_message(self, recipient_id: str, message_text: str):
        recipient = Recipient(id=recipient_id)
        message = TextMessage(text=message_text)
        request_body = MessageRequest(recipient=recipient, message=message)
        return await self._send_request(request_body)

    async def send_media_message(self, recipient_id: str, media_url: str, media_type: str):
        recipient = Recipient(id=recipient_id)
        attachment_payload = AttachmentPayload(url=media_url)
        attachment = Attachment(type=media_type, payload=attachment_payload)
        message = AttachmentMessage(attachment=attachment)
        request_body = MessageRequest(recipient=recipient, message=message)
        return await self._send_request(request_body)
    