from .BaseTank import BaseTank

COLOR_LIGHT_TANK = (50, 200, 50)  # Greenish


class LightTank(BaseTank):
    def __init__(self, objectController, x, y):
        super().__init__(objectController, x, y, COLOR_LIGHT_TANK, 60)
        self.speed = 5
        self.damage = 20

    def shoot(self):
        print("Light tank shoots!")
        return self.damage
