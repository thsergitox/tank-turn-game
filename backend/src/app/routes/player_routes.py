from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from app.services.player_service import PlayerService, get_player_service
from pydantic import BaseModel

router = APIRouter(prefix="/player")


class InputData(BaseModel):
    username: str
    password: str


class UpdateData(BaseModel):
    token: str
    # TODO: Add fields to update player data


def is_valid_input_data(data: InputData):
    if data.username and data.password:
        return JSONResponse(
            status_code=400, content={"message": "Username and password are required"}
        )


@router.post("/login")
async def login(
    request: InputData,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    is_valid_input_data(request)
    request = request.dict()
    username = request["username"]
    password = request["password"]

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
    request: InputData,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    is_valid_input_data(request)
    request = request.dict()
    username = request["username"]
    password = request["password"]

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


@router.get("/all")
async def get_all_players(
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    try:
        players = await player_service.get_all_players()
        return players
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Failed to get players: {str(e)}"}
        )


@router.delete("/delete/{username}")
async def delete_player(
    username: str,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    try:
        result = await player_service.delete_player(username)
        if result:
            return JSONResponse(content={"message": "Player deleted successfully"})
        else:
            return JSONResponse(
                status_code=400, content={"message": "Player could not be deleted"}
            )
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Failed to delete player: {str(e)}"}
        )


@router.post("/update")
async def update_player(
    request: UpdateData,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    try:
        result = await player_service.update_player(request.token)
        if result:
            return JSONResponse(content={"message": "Player updated successfully"})
        else:
            return JSONResponse(
                status_code=400,
                content={"message": "Player could not be updated", "result": result},
            )
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Failed to update player: {str(e)}"}
        )
