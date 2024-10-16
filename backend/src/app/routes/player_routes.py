from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from app.services.player_service import PlayerService, get_player_service
from pydantic import BaseModel
from app.metrics import LOGGEDIN_PLAYERS, REGISTERED_PLAYERS, TOTAL_DAMAGE, TOTAL_GAMES

# Create a router with a prefix for player-related routes
router = APIRouter(prefix="/player")

# Define a Pydantic model for input data
class InputData(BaseModel):
    username: str
    password: str

# Define a Pydantic model for update data
class UpdateData(BaseModel):
    name: str
    damage: int
    result: bool

# Function to validate input data
def is_valid_input_data(data: InputData):
    if data.username and data.password:
        return JSONResponse(
            status_code=400, content={"message": "Username and password are required"}
        )

# Route for player login
@router.post("/login")
async def login(
    request: InputData,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    # Validate input data
    is_valid_input_data(request)
    request = request.dict()
    username = request["username"]
    password = request["password"]

    try:
        # Attempt to login the player
        player = await player_service.login(username, password)
        response = {
            "message": player["message"],
            "token": player["token"],
            "name": player["name"],
        }
        response = JSONResponse(content=response)
        LOGGEDIN_PLAYERS.labels(username).inc()
        return response
    except Exception as e:
        if str(e) == "Player not found":
            return JSONResponse(
                status_code=404,
                content={"message": "Player not found. Please register first."},
            )
        return JSONResponse(
            status_code=400, content={"message": f"Login failed: {str(e)}"}
        )

# Route for player registration
@router.post("/register")
async def register(
    request: InputData,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    # Validate input data
    is_valid_input_data(request)
    request = request.dict()
    username = request["username"]
    password = request["password"]

    try:
        # Attempt to register the player
        player = await player_service.register(username, password)
        print(player)
        response = {"message": "Registration successful", "token": player["token"]}
        response = JSONResponse(content=response)
        REGISTERED_PLAYERS.labels(username).inc()
        return response
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Registration failed: {str(e)}"}
        )

# Route to get all players
@router.get("/all")
async def get_all_players(
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    try:
        # Attempt to get all players
        players = await player_service.get_all_players()
        return players
    except Exception as e:
        return JSONResponse(
            status_code=400, content={"message": f"Failed to get players: {str(e)}"}
        )

# Route to delete a player by username
@router.delete("/delete/{username}")
async def delete_player(
    username: str,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    try:
        # Attempt to delete the player
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

# Route to update player information
@router.post("/update")
async def update_player(
    request: UpdateData,
    response: Response,
    player_service: PlayerService = Depends(get_player_service),
):
    request = request.dict()
    try:
        # Attempt to update the player
        result = await player_service.update_player(request)
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
