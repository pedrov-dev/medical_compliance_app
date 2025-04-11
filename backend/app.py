# backend/app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.models import ChatRequest, ChatResponse, ChatMessage
from backend.chatbot import get_chatbot_response
from typing import List

app = FastAPI(title="Medical Compliance RAG Chatbot")

# Allow CORS for local frontend development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response_msg = get_chatbot_response(request.user_id, request.message)
        # For demonstration, return the full history.
        # Production can return only the latest message or paginate history.
        from backend.chat_memory import get_history
        history: List[ChatMessage] = get_history(request.user_id)
        return ChatResponse(user_id=request.user_id, responses=history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
