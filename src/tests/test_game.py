import pytest
from unittest.mock import MagicMock
from app.models.tank import LightTank, StandardTank, HeavyTank
from app.core.game_manager import GameManager
from app.models.tank.cannon.Bullet import Bullet


@pytest.fixture
def game_manager():
    return GameManager()


@pytest.fixture
def standard_tank():
    return StandardTank(MagicMock(), 100, 100)


@pytest.fixture
def light_tank():
    return LightTank(MagicMock(), 100, 100)


@pytest.fixture
def heavy_tank():
    return HeavyTank(MagicMock(), 100, 100)


@pytest.fixture
def bullet():
    return Bullet(MagicMock(), 100, 100, 45, 50)


# Tank Movement Tests
def test_tank_movement_during_movement_turn(game_manager, standard_tank):
    game_manager.current_turn = "movement"
    initial_x = standard_tank.x
    standard_tank.move(1)  # Move right
    assert standard_tank.x > initial_x


def test_tank_no_movement_during_shooting_turn(game_manager, standard_tank):
    game_manager.current_turn = "shooting"
    initial_x = standard_tank.x
    standard_tank.move(1)  # Try to move right
    assert standard_tank.x == initial_x


# Tank Shooting Tests
def test_tank_shooting_during_shooting_turn(game_manager, standard_tank):
    game_manager.current_turn = "shooting"
    standard_tank.shoot(MagicMock())
    assert standard_tank.cannon.has_fired


def test_tank_no_shooting_during_movement_turn(game_manager, standard_tank):
    game_manager.current_turn = "movement"
    standard_tank.shoot(MagicMock())
    assert not standard_tank.cannon.has_fired


# Bullet Behavior Tests
def test_bullet_trajectory(bullet):
    initial_position = bullet.position.copy()
    bullet.update()
    assert bullet.position != initial_position


def test_bullet_collision(bullet, standard_tank):
    initial_health = standard_tank.health
    bullet.collide(standard_tank)
    assert standard_tank.health < initial_health


# Tank Types Tests
@pytest.mark.parametrize(
    "tank_class,expected_health,expected_damage,expected_movement",
    [(LightTank, 60, 20, 200), (StandardTank, 100, 30, 150), (HeavyTank, 150, 50, 100)],
)
def test_tank_characteristics(
    tank_class, expected_health, expected_damage, expected_movement
):
    tank = tank_class(MagicMock(), 100, 100)
    assert tank.health == expected_health
    assert tank.damage == expected_damage
    assert tank.movement == expected_movement


# Additional Tests


def test_tank_aim(standard_tank):
    initial_angle = standard_tank.angle
    standard_tank.aim(1)  # Aim up
    assert standard_tank.angle > initial_angle
    standard_tank.aim(-1)  # Aim down
    assert standard_tank.angle < initial_angle


def test_tank_receive_damage(standard_tank):
    initial_health = standard_tank.health
    standard_tank.recieve_damage(20)
    assert standard_tank.health == initial_health - 20


def test_tank_destruction(standard_tank):
    standard_tank.recieve_damage(standard_tank.health)
    assert not standard_tank.is_alive


def test_tank_movement_limit(standard_tank):
    initial_movement = standard_tank.movement
    standard_tank.move(initial_movement + 1)  # Try to move more than allowed
    assert standard_tank.actual_movement == 0
    assert standard_tank.x == 100 + initial_movement  # Moved to the limit


def test_bullet_out_of_bounds(bullet):
    bullet.position.x = -10  # Move bullet out of screen
    bullet.update()
    assert not bullet.active


def test_tank_reset_movement(standard_tank):
    standard_tank.move(50)  # Use some movement
    standard_tank.reset_movement()
    assert standard_tank.actual_movement == standard_tank.movement
