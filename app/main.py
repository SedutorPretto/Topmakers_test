from fastapi import FastAPI, HTTPException
from .schemas import TextMessageRequest, MediaMessageRequest
from .client.client import MessageClient
from config import PAGE_ACCESS_TOKEN


app = FastAPI()
messenger_client = MessageClient(page_access_token=PAGE_ACCESS_TOKEN)


@app.post('/send_text_message')
async def send_text_message(request: TextMessageRequest):
    try:
        response = await  messenger_client.send_text_message(
            recipient_id=request.recipient_id,
            message_text=request.message_text
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/send_media_message")
async def send_media_message(request: MediaMessageRequest):
    try:
        response = await messenger_client.send_media_message(
            recipient_id=request.recipient_id,
            media_url=request.media_url,
            media_type=request.media_type
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
