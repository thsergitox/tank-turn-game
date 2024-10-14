from fastapi import APIRouter, Depends, Response, JSONResponse
from typing import List
from app.models.player import Player
from app.services.player_service import PlayerService
from app.database.mongo.queries import PlayerQueries
from app.database.mongo.connection import get_database
from pydantic import BaseModel

router = APIRouter(prefix="/player")


class InputData(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(
    login: InputData,
    response: Response,
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    login = login.dict()
    username = login["username"]
    password = login["password"]

    if not username or not password:
        return JSONResponse(
            status_code=400, content={"message": "Username and password are required"}
        )

    try:
        player = await player_service.login(username, password)
        print(player)
        response = {"message": player["message"]}
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=player["token"], httponly=True)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Login failed: {str(e)}"}
        )


@router.post("/register")
async def register(
    login: InputData,
    response: Response,
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    login = login.dict()
    username = login["username"]
    password = login["password"]

    if not username or not password:
        return JSONResponse(
            status_code=400, content={"message": "Username and password are required"}
        )

    try:
        player = await player_service.register(username, password)
        print(player)
        response = {"message": "Registration successful"}
        response = JSONResponse(content=response)
        response.set_cookie(key="access_token", value=player["token"], httponly=True)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Registration failed: {str(e)}"}
        )


@router.get("/logout")
async def logout(response: Response):
    



    return {"message": "Logout successful go to home", "home": "/"}
