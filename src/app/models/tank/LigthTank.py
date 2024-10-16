from .BaseTank import BaseTank

COLOR_LIGHT_TANK = (50, 50, 200)  # Blueish


class LightTank(BaseTank):
    def __init__(self, objectController, x, y):
        super().__init__(
            objectController,
            x,
            y,
            COLOR_LIGHT_TANK,
            health=60,
            damage=20,
            movement=200,
            speed=3,
        )

    def shoot(self, target):
        print("Light tank shoots!")
        super().shoot(target)
        return self.damage
