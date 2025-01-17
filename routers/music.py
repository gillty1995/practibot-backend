from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_music_recommendations():
    return {"recommendations": ["Bohemian Rhapsody", "Hotel California", "Imagine"]}