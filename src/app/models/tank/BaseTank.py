from abc import ABC, abstractmethod
import pygame
import math

from core.base_object import BaseObject


class BaseTank(BaseObject):
    def __init__(self, objectController, x, y, color, health):
        super().__init__(objectController, x, y, 100, 50)
        self.color = color
        self.health = health
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

    def aim(self, angle):
        self.angle = angle

    def move(self, direction):
        if direction == 1:
            self.x += self.speed
        elif direction == -1:
            self.x -= self.speed
        # TODO: Add y direction actualization via Physics Component

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
