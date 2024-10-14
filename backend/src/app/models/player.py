
from typing import Optional
from .tank import Tank

class Player():
    xp: int = 0
    target_xp: int = 10
    password: Optional[str] = None

    current_enemy: Optional[Tank] = None

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "Hero",
                "password": "123456",
                
            }
        }
