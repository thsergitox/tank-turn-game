from .BaseTank import BaseTank

COLOR_STANDARD_TANK = (50, 200, 50)  # Greenish


class StandardTank(BaseTank):
    def __init__(self, objectController, x, y):
        super().__init__(
            objectController,
            x,
            y,
            COLOR_STANDARD_TANK,
            health=100,
            damage=30,
            movement=150,
            speed=2,
        )

    def shoot(self, target):
        super().shoot(target)
        print("Standard tank shoots!")
        return self.damage
