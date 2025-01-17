from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import music, chatbot, contact

app = FastAPI(
    title="Music Chatbot Backend",
    description="An API to provide music practice tips and recommendations.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

app.include_router(music.router, prefix="/api/v1/music", tags=["Music"])
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot"])
app.include_router(contact.router, prefix="/api/v1", tags=["Contact"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Music Chatbot Backend!"}