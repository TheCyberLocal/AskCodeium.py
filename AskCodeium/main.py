from fastapi import FastAPI
from api import chat

app = FastAPI()

app.include_router(chat.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
