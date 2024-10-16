from .player_routes import router as player_routes
from fastapi import APIRouter

router = APIRouter()

router.get("/")(lambda: {"message": "Welcome to the API!"})


router.include_router(player_routes)
