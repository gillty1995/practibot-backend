from fastapi import APIRouter, Query
from services.chatbot_service import get_openai_response

router = APIRouter()

@router.get("/")
async def chat(
    question: str = Query(..., description="Ask a music-related question"),
    reset: bool = Query(False, description="Reset the conversation history")
):
    response = get_openai_response(question, reset)
    
    if response == "Question cannot be empty.":
        return {"error": response}
    
    return {"response": response}