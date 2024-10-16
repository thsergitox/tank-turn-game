from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    name: str
    password: Optional[str] = None
    total_damage: Optional[int] = 0
    total_wins: Optional[int] = 0
    total_losses: Optional[int] = 0

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "player1",
                "password": "password",
                "total_damage": 0,
                "total_wins": 0,
                "total_losses": 0,
            }
        }
