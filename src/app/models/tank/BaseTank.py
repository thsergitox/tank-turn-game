from abc import ABC, abstractmethod
import pygame
import math

from core.base_object import BaseObject


class BaseTank(BaseObject):
    def __init__(self, objectController, x, y, color, health, damage, movement):
        super().__init__(objectController, x, y, 100, 50)
        self.color = color
        self.health = health
        self.actual_health = health
        self.damage = damage
        self.movement = movement
        self.actual_movement = movement
        self.angle = 0

    def start(self):
        pass

    def update(self):
        pass

    def end(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    def aim(self, direction: int):
        # perform rotation arround a pivot point
        # positive direction means left till 180 degrees
        # negative direction means right till 0 degrees
        print(direction)

    def move(self, direction: int):
        if self.actual_movement > 0:
            self.move_ip(direction, 0)
            self.actual_movement -= math.fabs(direction)

    def die(self):
        print(f"{self.__class__.__name__} has been destroyed!")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

    # def draw_health_bar(self, screen):
    #     health_bar_width = 20
    #     health_bar_height = 5
    #     health_bar_x = self.x - health_bar_width / 2
    #     health_bar_y = self.y - 25

    #     pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
