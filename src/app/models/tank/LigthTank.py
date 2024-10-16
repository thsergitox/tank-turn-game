from .BaseTank import BaseTank

COLOR_LIGHT_TANK = (50, 200, 50)  # Greenish


class LightTank(BaseTank):
    def __init__(self, objectController, x, y):
        super().__init__(
            objectController, x, y, COLOR_LIGHT_TANK, health=60, damage=20, movement=50
        )

    def shoot(self, target):
        super().shoot(target)
        return self.damage
