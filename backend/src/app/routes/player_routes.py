from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from app.services.player_service import PlayerService
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
        response = {"message": player["message"], "token": player["token"]}
        response = JSONResponse(content=response)
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
        response = {"message": "Registration successful", "token": player["token"]}
        response = JSONResponse(content=response)
        return response
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Registration failed: {str(e)}"}
        )


@router.get("/logout")
async def logout(response: Response):
    return {"message": "Logout successful go to home", "home": "/"}


@router.get("/all")
async def get_all_players(
    response: Response,
    player_service: PlayerService = Depends(PlayerService.get_player_service),
):
    try:
        players = await player_service.get_all_players()
        return players
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Failed to get players: {str(e)}"}
        )