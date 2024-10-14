from abc import ABC, abstractmethod
import pygame
import math


class BaseTank(ABC):
    def __init__(self, x, y, color, health):
        self.x = x
        self.y = y
        self.color = color
        self.health = health
        self.angle = 0
        self.size_x, self.size_y = 20, 20

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
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size_x, self.size_y))

    # def draw_health_bar(self, screen):
    #     health_bar_width = 20
    #     health_bar_height = 5
    #     health_bar_x = self.x - health_bar_width / 2
    #     health_bar_y = self.y - 25

    #     pygame.draw.rect(screen, (0, 255, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
