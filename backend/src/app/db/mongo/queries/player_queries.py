from bson import ObjectId
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.player import Player
from pymongo.database import Database
import bcrypt
from app.config import settings

SALT_ROUNDS = settings.SALT_ROUNDS


class PlayerQueries:
    """
    Clase para interactuar con la colección de jugadores en la base de datos.
    """

    def __init__(self, db: Database):
        """
        Inicializa la instancia con la base de datos y la colección de jugadores.

        Args:
                db (Database): Instancia de la base de datos MongoDB.
        """
        self.collection = db.players

    async def login(self, player_name: str) -> dict:
        """
        Retrieves the player's password for login verification.

        Args:
            player_name (str): The name of the player attempting to log in.

        Returns:
            dict: A dictionary containing a message and the player's hashed password.
                  If the player is not found, returns None for the password.

        Raises:
            Exception: If there's an error during the database query.
        """
        try:
            player_data = await self.collection.find_one({"name": player_name})

            if not player_data:
                return {"message": "Player not found", "player": None}

            player_data["_id"] = str(player_data["_id"])
            player_password = player_data["password"]

            return {"message": "Login successful", "password": player_password}
        except Exception as e:
            raise Exception(f"An error occurred while retrieving player data: {str(e)}")

    async def register(self, player: Player) -> dict:
        """
        Crea un nuevo jugador en la base de datos.

        Args:
                player (Player): Objeto Player con los datos del jugador a crear.

        Returns:
                dict: Mensaje de éxito o error y los datos del jugador
        """
        try:
            player_dict = player.model_dump()
            hashed_password = bcrypt.hashpw(
                player_dict["password"].encode("utf-8"),
                bcrypt.gensalt(rounds=SALT_ROUNDS),
            )
            player_dict["password"] = hashed_password.decode("utf-8")
            result = await self.collection.insert_one(player_dict)
            player_dict["_id"] = str(result.inserted_id)

            return {
                "message": "Player created successfully",
                "player": player_dict["name"],
            }
        except Exception as e:
            raise Exception(f"An error occurred while creating the player {e}")

    async def get_player_by_name(self, player_name: str) -> dict:
        """
                Obtiene un jugador por su ID.
        Args:
                player_name (str): Nombre del jugador
        Returns:
                Player: Objeto Player con los datos del jugador encontrado, o None si no se encuentra.
        """
        player_data = await self.collection.find_one({"name": player_name})
        if player_data:
            player_data["_id"] = str(player_data["_id"])
            player_data.pop("password")

            return {"message": "Player retrieved successfully", "player": player_data}
        return {"message": "Player not found"}

    async def get_all_players(self) -> dict:
        """
        Obtiene todos los jugadores.

        Returns:
                List[Player]: Lista de objetos Player con los datos de todos los jugadores.
        """
        cursor = self.collection.find()
        players = []
        async for player_data in cursor:
            player_data["_id"] = str(player_data["_id"])
            players.append(Player(**player_data))
        return {"message": "Players retrieved successfully", "players": players}

    async def update_player(self, player_data: dict) -> bool:
        """
        Actualiza los datos de un jugador.

        Args:
                player_data (dict): Diccionario con los nuevos datos del jugador.

        Returns:
                bool: True si se actualizó correctamente, False en caso contrario.
        """
        player_id = player_data.pop("_id", None)
        if not player_id:
            return False

        result = await self.collection.update_one(
            {"_id": ObjectId(player_id)}, {"$set": player_data}
        )
        return result.modified_count > 0

    async def delete_player(self, player_id: str) -> bool:
        """
        Elimina un jugador por su ID.

        Args:
                player_id (str): ID del jugador a eliminar.

        Returns:
                bool: True si se eliminó correctamente, False en caso contrario.
        """
        result = await self.collection.delete_one({"_id": ObjectId(player_id)})
        return result.deleted_count > 0

    async def delete_all_players(self) -> dict:
        """
        Elimina todos los jugadores de la base de datos.

        Returns:
            dict: Un diccionario con un mensaje y el número de jugadores eliminados.
        """
        try:
            result = await self.collection.delete_many({})
            return {
                "message": "All players deleted successfully",
                "deleted_count": result.deleted_count,
            }
        except Exception as e:
            raise Exception(f"An error occurred while deleting all players: {str(e)}")

    async def it_exists(self, player_name: str) -> bool:
        """
        Verifica si un jugador existe por su nombre.

        Args:
                player_name (str): Nombre del jugador.

        Returns:
                bool: True si existe, False en caso contrario.
        """
        player = await self.collection.find_one({"name": player_name})
        return player is not None
