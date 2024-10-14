from abc import ABC, abstractmethod
import pygame


class BaseTank(ABC):
    def __init__(self, x, y, color, max_health):
        self.x = x
        self.y = y
        self.color = color
        self.max_health = max_health
        self.health = max_health
        self.angle = 0
        self.size_x, self.size_y = 20, 20

    @abstractmethod
    def shoot(self):
        # TODO: Implement shooting logic
        pass

    def _draw_aim_line(self, angle):
        # TODO: Implement aim line drawing
        pass

    def aim(self, angle):
        self.angle = angle
        self._draw_aim_line(self.angle)

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

    # Combat logic

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()
