from abc import abstractmethod
from pygame import Vector2
import math
import pygame
import math

from models.tank.cannon.cannon import Cannon
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
        self.pivot_aim_line_x = self.x + self.size_x * 0.75
        self.pivot_aim_line_y = self.y + self.size_y * 0.5
        self.aim_line_length = self.size_x * 0.65
        self.width_aim_line = int(self.size_x * 0.35)
        self.cannon = Cannon(Vector2(self.center), self.damage)
        self.is_alive = True

    def start(self):
        self.cannon.start()

    def update(self):
        self.cannon.update()

    def end(self):
        pass

    def shoot(self, target):
        self.cannon.shoot(target)

    def aim(self, direction: int):
        self.angle += (self.angle < 180 and direction > 0) - (
            self.angle > 0 and direction < 0
        )
        self.cannon.move(Vector2(self.center), self.angle)

    def move(self, direction: int):
        if self.actual_movement > 0:
            self.move_ip(direction, 0)
            self.cannon.rect.move_ip(direction, 0)
            self.cannon.move(Vector2(self.center), self.angle)
            self.actual_movement -= math.fabs(direction)

    def recieve_damage(self, damage):
        print(f"{self.__class__.__name__} recieves {damage} damage")
        self.actual_health -= damage
        if self.actual_health <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        print(f"{self.__class__.__name__} has been destroyed!")

    def draw(self, screen):
        if not self.is_alive:
            return
        self.cannon.draw(screen)
        pygame.draw.rect(screen, self.color, self)
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        health_bar_width = 20
        health_bar_height = 5

        # Fixed frame
        frame_bar_x = self.x + self.size_x / 2 - health_bar_width / 2
        frame_bar_y = self.y - 2 * health_bar_height

        # Draw frame
        pygame.draw.rect(
            screen,
            (200, 200, 200),
            (frame_bar_x, frame_bar_y, health_bar_width, health_bar_height),
        )

        # Health bar
        health_bar_width = self.health / self.max_health * health_bar_width

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (frame_bar_x, frame_bar_y, health_bar_width, health_bar_height),
        )

        # Aim line
        pygame.draw.line(
            screen,
            self.color,
            (self.pivot_aim_line_x, self.pivot_aim_line_y),  # Start position (pivot)
            (
                self.pivot_aim_line_x + self.aim_line_length * math.cos(self.angle),
                self.pivot_aim_line_y - self.aim_line_length * math.sin(self.angle),
            ),
            self.width_aim_line,
        )

    # Combat logic
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
