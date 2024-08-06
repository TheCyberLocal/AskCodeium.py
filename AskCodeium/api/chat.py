from fastapi import APIRouter, HTTPException
from models.chat_thread import ChatThread
from services.codeium_service import CodeiumService

router = APIRouter()
chat_threads = {}

@router.post("/createChat")
def create_chat():
    chat_thread = ChatThread()
    chat_threads[chat_thread.thread_id] = chat_thread
    return {"thread_id": chat_thread.thread_id}

@router.post("/chat/{thread_id}")
async def chat(thread_id: str, query: str):
    if thread_id not in chat_threads:
        raise HTTPException(status_code=404, detail="Thread not found")
    chat_thread = chat_threads[thread_id]
    response = await CodeiumService.send_request(chat_thread, query)
    return {"response": response}

@router.post("/chat/{thread_id}/clearHistory")
def clear_history(thread_id: str):
    if thread_id not in chat_threads:
        raise HTTPException(status_code=404, detail="Thread not found")
    chat_threads[thread_id].clear_history()
    return {"status": "History cleared"}
