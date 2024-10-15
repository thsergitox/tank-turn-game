import pygame
from pygame.math import Vector2
import math
from .Bullet import Bullet


class Cannon:
    def __init__(self, pivot):
        self.pivot = Vector2(pivot)
        self.actual_bullet = None
        self.angle = 0
        self.end_point = Vector2(0, 0)

    def start(self):
        self.image_orig = pygame.image.load("images/cannon.png")
        self.image_orig = pygame.transform.scale(
            self.image_orig, [x / 3 for x in self.image_orig.get_size()]
        )

        self.image = self.image_orig
        self.position = self.pivot
        self.rect = self.image.get_rect(midleft=self.position)
        self.cannon_length = self.image.get_size()[0]

    def update(self):
        if self.actual_bullet:
            self.actual_bullet.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_bullet(screen)

    def draw_bullet(self, screen):
        if self.actual_bullet:
            self.actual_bullet.draw(screen)

    def move(self, pivot, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.image_orig, angle)
        self.pivot = Vector2(pivot)
        self.position = self.pivot + Vector2(self.image_orig.get_rect().width / 2, 0)

        offset = self.pivot + (self.position - self.pivot).rotate(-angle)
        self.rect = self.image.get_rect(center=(offset.x, offset.y))

        angle_rad = math.radians(self.angle)
        self.end_point = self.pivot + Vector2(
            self.cannon_length * math.cos(angle_rad),
            -self.cannon_length * math.sin(angle_rad),
        )

    def shoot(self):
        self.actual_bullet = Bullet(self.end_point, self.angle, 1000)
