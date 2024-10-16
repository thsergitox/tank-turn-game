import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from behave import given, when, then
from unittest.mock import MagicMock
from app.core.game_manager import GameManager
from app.models.tank import StandardTank


@given("it is the {turn_type} turn")
def step_impl(context, turn_type):
    context.game_manager = GameManager()
    context.game_manager.current_turn = turn_type
    context.tank = StandardTank(MagicMock(), 100, 100)


@when("I press the {key} key")
def step_impl(context, key):
    if key == "right arrow":
        context.tank.move_right()
    elif key == "spacebar":
        context.tank.shoot()


@then("my tank should {action}")
def step_impl(context, action):
    if action == "move to the right":
        assert context.tank.x > 100, "Tank did not move to the right"
    elif action == "not move":
        assert context.tank.x == 100, "Tank moved when it shouldn't have"
    elif action == "fire a bullet":
        assert context.tank.has_fired, "Tank did not fire a bullet"
    elif action == "not fire a bullet":
        assert not context.tank.has_fired, "Tank fired a bullet when it shouldn't have"
