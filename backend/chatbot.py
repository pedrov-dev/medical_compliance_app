# backend/chatbot.py
import openai
from backend.config import OPENAI_API_KEY
from backend.chat_memory import get_history, add_message
from backend.vector_db import query_vector
from backend.utils import generate_embedding, preprocess_text
from backend.models import ChatMessage

openai.api_key = OPENAI_API_KEY

def get_chatbot_response(user_id: str, user_input: str) -> ChatMessage:
    # Preprocess input and add to history.
    clean_input = preprocess_text(user_input)
    add_message(user_id, ChatMessage(role="user", message=clean_input))
    
    # Generate embedding of user input for context retrieval.
    embedding = generate_embedding(clean_input)
    context_results = query_vector(embedding)

    # Process retrieved context. Here we extract metadata as context text.
    retrieved_context = ""
    for match in context_results.get("matches", []):
        # For example, assume each match's metadata contains a 'text' field.
        retrieved_context += match['metadata'].get('text', '') + "\n"

    # Construct a prompt that includes conversation history and retrieved context.
    history = get_history(user_id)
    conversation_history = ""
    for msg in history:
        conversation_history += f"{msg.role}: {msg.message}\n"
    
    prompt = (
        "You are a medical compliance assistant. Use the context provided to help answer the query.\n\n"
        "Retrieved Context:\n"
        f"{retrieved_context}\n\n"
        "Conversation History:\n"
        f"{conversation_history}\n\n"
        "Now, respond succinctly and accurately to the user query."
    )
    
    # Generate the answer using OpenAI's chat completion API.
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}],
        temperature=0.2
    )
    answer_text = response.choices[0].message['content'].strip()
    
    # Save the response in memory.
    assistant_msg = ChatMessage(role="assistant", message=answer_text)
    add_message(user_id, assistant_msg)
    return assistant_msg
