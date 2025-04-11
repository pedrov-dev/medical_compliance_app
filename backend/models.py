# backend/models.py
from pydantic import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str  # 'user' or 'assistant'
    message: str


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    user_id: str
    responses: List[ChatMessage]
