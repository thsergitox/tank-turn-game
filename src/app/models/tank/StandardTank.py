from .BaseTank import BaseTank

COLOR_STANDARD_TANK = (50, 50, 200)  # Blueish


class StandardTank(BaseTank):
    def __init__(self, objectController, x, y):
        super().__init__(objectController, x, y, COLOR_STANDARD_TANK, 100, 30, 35)

    def shoot(self):
        print("Standard tank shoots!")
        return self.damage
