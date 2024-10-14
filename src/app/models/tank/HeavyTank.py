from .BaseTank import BaseTank

COLOR_HEAVY_TANK = (200, 50, 50)  # Redish


class HeavyTank(BaseTank):
    def __init__(self, x, y):
        super().__init__(x, y, COLOR_HEAVY_TANK, 150)
        self.speed = 1.4
        self.damage = 50

    def shoot(self):
        print("Heavy tank shoots!")
        return self.damage
