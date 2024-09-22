import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import AsyncMock, patch
from app.main import app


@pytest.fixture
def messenger_client_mock():
    with patch('app.main.messenger_client') as mock:
        mock.send_text_message = AsyncMock(return_value={"message_id": "mid.1234"})
        mock.send_media_message = AsyncMock(return_value={"message_id": "mid.5678"})
        yield mock


@pytest.mark.asyncio
async def test_send_text_message(messenger_client_mock):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://testserver") as ac:
        response = await ac.post(
            "/send_text_message",
            json={
                "recipient_id": "test_recipient_id",
                "message_text": "Hello, World!"
            }
        )

    assert response.status_code == 200
    assert response.json() == {"message_id": "mid.1234"}
    messenger_client_mock.send_text_message.assert_awaited_once_with(
        recipient_id="test_recipient_id",
        message_text="Hello, World!"
    )


@pytest.mark.asyncio
async def test_send_media_message(messenger_client_mock):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://testserver") as ac:
        response = await ac.post(
            "/send_media_message",
            json={
                "recipient_id": "test_recipient_id",
                "media_url": "https://example.com/image.jpg",
                "media_type": "image"
            }
        )

    assert response.status_code == 200
    assert response.json() == {"message_id": "mid.5678"}
    messenger_client_mock.send_media_message.assert_awaited_once_with(
        recipient_id="test_recipient_id",
        media_url="https://example.com/image.jpg",
        media_type="image"
    )
