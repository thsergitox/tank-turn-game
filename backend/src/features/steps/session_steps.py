from behave import given, when, then
from app.main import app
from app.database.mongo.connection import get_database
from app.services.player_service import PlayerService
from httpx import AsyncClient
import pytest

client = AsyncClient(app=app)


@pytest.mark.asyncio
@given('a player with name "{name}" and password "{password}"')
async def step_impl(context, name, password):
    context.player_data = {"username": name, "password": password}


@pytest.mark.asyncio
@when('sent a "{action}" POST request')
async def step_impl(context, action):
    context.action = action
    if action == "register":
        context.response = await client.post(
            "/api/player/register", json=context.player_data
        )
    elif action == "login":
        context.response = await client.post(
            "/api/player/login", json=context.player_data
        )


@pytest.mark.asyncio
@when('sent a "{action}" POST request with wrong password')
async def step_impl(context, action):
    context.action = action
    if action == "login":
        context.response = await client.post(
            "/api/player/login", json=context.player_data
        )


@pytest.mark.asyncio
@then("the player should access successfully")
async def step_impl(context):
    assert context.response.status_code == 200
    if context.action == "register":
        assert "Registration successful" in context.response.json()["message"]
    elif context.action == "login":
        assert "Login successful" in context.response.json()["message"]


@pytest.mark.asyncio
@then("the response should contain a token")
async def step_impl(context):
    assert "token" in context.response.json()


@pytest.mark.asyncio
@then("the player should not access successfully")
async def step_impl(context):
    assert context.response.status_code == 400
    assert "Login failed: Invalid password" in context.response.json()["message"]


@pytest.mark.asyncio
@given('a player with name "{name}" exists in the database')
async def step_impl(context, name):
    # Ensure the player exists in the database
    db = get_database()
    player_service = PlayerService.get_player_service()
    player_service.register(name, "password")
    context.player_name = name


@pytest.mark.asyncio
@when('sent a "delete" DELETE request for "{name}"')
async def step_impl(context, name):
    context.response = await client.delete(f"/api/player/{name}")


@pytest.mark.asyncio
@then("the player should be deleted successfully")
async def step_impl(context):
    assert context.response.status_code == 200
    assert "Player deleted successfully" in context.response.json()["message"]
