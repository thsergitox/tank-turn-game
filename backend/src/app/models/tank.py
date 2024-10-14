from pydantic import BaseModel

class Tank(BaseModel):
    """
    Clase que representa un tanque en el juego.
    """

    name: str
    health: int
    attack: int
    defense: int
    speed: int
    level: int
    xp: int
    target_xp: int
 
    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "Tank",
                "health": 100,
                "attack": 10,
                "defense": 5,
                "speed": 5,
                "level": 1,
                "xp": 0,
                "target_xp": 10,
                "current_enemy": None,
                "password": "123456",
            }
        }
