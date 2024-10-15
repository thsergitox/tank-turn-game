import pytest
import pytest_asyncio
from httpx import AsyncClient
from app.main import app
from asgi_lifespan import LifespanManager


# Create a fixture to manage the lifespan of the app
@pytest_asyncio.fixture
async def client():
    # Use LifespanManager to handle startup and shutdown events
    async with LifespanManager(app):
        # Create an AsyncClient with the app parameter
        async with AsyncClient(app=app, base_url="http://test") as client:
            yield client


@pytest.mark.asyncio
async def test_register_player(client):
    response = await client.post(
        "/api/player/register", json={"username": "sergio", "password": "password"}
    )
    print(response.json())

    assert response.status_code == 200
    assert "Registration successful" in response.json()["message"]
    assert "token" in response.json()


@pytest.mark.asyncio
async def test_login_player(client):
    # Primero, registra al jugador
    await client.post(
        "/api/player/register", json={"username": "sergio", "password": "password"}
    )
    # Luego, intenta iniciar sesión
    response = await client.post(
        "/api/player/login", json={"username": "sergio", "password": "password"}
    )
    assert response.status_code == 200
    assert "Login successful" in response.json()["message"]
    assert "token" in response.json()


@pytest.mark.asyncio
async def test_login_with_wrong_password(client):
    # Primero, registra al jugador
    await client.post(
        "/api/player/register", json={"username": "sergio", "password": "password"}
    )
    # Intenta iniciar sesión con una contraseña incorrecta
    response = await client.post(
        "/api/player/login", json={"username": "sergio", "password": "wrongpassword"}
    )
    assert response.status_code == 400
    assert (
        "Login failed: An error occurred while checking passwords: Invalid password"
        in response.json()["message"]
    )


@pytest.mark.asyncio
async def test_delete_players(client):
    response = await client.delete("/api/player/delete/sergio")
    assert response.status_code == 200
    assert "Player deleted successfully" in response.json()["message"]
