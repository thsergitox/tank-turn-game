import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from behave import given, when, then
from unittest.mock import MagicMock
from app.models.tank import LightTank, StandardTank, HeavyTank


@given("I have selected a {tank_type} tank")
def step_impl(context, tank_type):
    if tank_type == "Light":
        context.tank = LightTank(MagicMock(), 100, 100)
    elif tank_type == "Standard":
        context.tank = StandardTank(MagicMock(), 100, 100)
    elif tank_type == "Heavy":
        context.tank = HeavyTank(MagicMock(), 100, 100)


@when("I check its stats")
def step_impl(context):
    pass


@then("it should have {stat} {value:d}")
def step_impl(context, stat, value):
    if stat == "health":
        assert (
            context.tank.health == value
        ), f"Expected health {value}, got {context.tank.health}"
    elif stat == "damage":
        assert (
            context.tank.damage == value
        ), f"Expected damage {value}, got {context.tank.damage}"
    elif stat == "movement":
        assert (
            context.tank.movement == value
        ), f"Expected movement {value}, got {context.tank.movement}"
