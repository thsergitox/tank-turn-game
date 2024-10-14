from pydantic import BaseModel, Field

class Tank(BaseModel):
    """
    Clase que representa un tanque en el juego.
    """
    name: str
    x: int
    y: int
    health: int
    angle: int  

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "name": "Heavy",
                "x": 0,
                "y": 0,
            }
        }
