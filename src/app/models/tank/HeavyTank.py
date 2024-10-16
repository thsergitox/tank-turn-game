from .BaseTank import BaseTank

COLOR_HEAVY_TANK = (200, 50, 50)  # Redish


class HeavyTank(BaseTank):
    def __init__(self, objectController, x, y):
        super().__init__(objectController, x, y, COLOR_HEAVY_TANK, 150, 50, 25)

    def shoot(self, target):
        super().shoot(target)
        print("Heavy tank shoots!")
        return self.damage
