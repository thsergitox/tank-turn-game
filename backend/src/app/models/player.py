
from typing import Optional
from .tank import Tank

class Player():

    name: str
    level: int = 1
    password: Optional[str] = None
    current_tank: Optional[Tank] = None

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "Hero",
                "password": "123456",
                "level": 1,
                
                
            }
        }
