import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from behave import given, when, then
from unittest.mock import MagicMock
from app.models.tank.cannon.Bullet import Bullet


@given("a tank has fired a bullet")
def step_impl(context):
    context.bullet = Bullet(MagicMock(), 100, 100, 45, 50)


@when("the bullet is in flight")
def step_impl(context):
    context.initial_position = context.bullet.position.copy()
    context.bullet.update()


@then("it should follow a parabolic path")
def step_impl(context):
    assert (
        context.bullet.position.y != context.initial_position.y
    ), "Bullet did not change vertical position"
    assert (
        context.bullet.position.x != context.initial_position.x
    ), "Bullet did not change horizontal position"


@given("a bullet is in flight")
def step_impl(context):
    context.bullet = Bullet(MagicMock(), 100, 100, 45, 50)
    context.enemy_tank = MagicMock()


@when("it collides with an enemy tank")
def step_impl(context):
    context.bullet.collide(context.enemy_tank)


@then("it should deal damage to the tank")
def step_impl(context):
    context.enemy_tank.take_damage.assert_called_once()
