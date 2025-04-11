# backend/chat_memory.py
from typing import List
from backend.models import ChatMessage

# For simplicity, an in-memory dictionary for chat history.
# Production should use a persistent database.
chat_histories = {}

def get_history(user_id: str) -> List[ChatMessage]:
    return chat_histories.get(user_id, [])

def add_message(user_id: str, message: ChatMessage) -> None:
    if user_id not in chat_histories:
        chat_histories[user_id] = []
    chat_histories[user_id].append(message)
