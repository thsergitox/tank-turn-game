import unittest
from unittest.mock import MagicMock
from app.models.tank import StandardTank, LightTank, HeavyTank


class TestTank(unittest.TestCase):
    def test_standard_tank_stats(self):
        tank = StandardTank(MagicMock(), 100, 100)
        self.assertEqual(tank.health, 100)
        self.assertEqual(tank.damage, 30)
        self.assertEqual(tank.movement, 150)

    def test_light_tank_stats(self):
        tank = LightTank(MagicMock(), 100, 100)
        self.assertEqual(tank.health, 60)
        self.assertEqual(tank.damage, 20)
        self.assertEqual(tank.movement, 200)

    def test_heavy_tank_stats(self):
        tank = HeavyTank(MagicMock(), 100, 100)
        self.assertEqual(tank.health, 150)
        self.assertEqual(tank.damage, 50)
        self.assertEqual(tank.movement, 100)

    def test_tank_movement(self):
        tank = StandardTank(MagicMock(), 100, 100)
        initial_x = tank.x
        tank.move_right()
        self.assertGreater(tank.x, initial_x)

    def test_tank_shooting(self):
        tank = StandardTank(MagicMock(), 100, 100)
        tank.shoot()
        self.assertTrue(tank.has_fired)  # TODO: Implementar esto


if __name__ == "__main__":
    unittest.main()
