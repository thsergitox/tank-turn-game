from abc import abstractmethod
from pygame import Vector2
import pygame
import math

from models.tank.cannon.cannon import Cannon
from core.base_object import BaseObject


class BaseTank(BaseObject):
    def __init__(
        self,
        objectController,
        x,
        y,
        color,
        health,
        damage,
        movement,
        speed,  # Add speed parameter
        size_x=100,
        size_y=70,
    ):
        super().__init__(objectController, x, y, size_x, size_y)

        # Tank properties
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.health = health
        self.actual_health = health
        self.damage = damage
        self.movement = movement
        self.actual_movement = movement  # This is the stamina
        self.speed = speed
        self.angle = 0
        self.is_alive = True

        # Initialize cannon
        self.cannon = Cannon(Vector2(self.center), self.damage)

    def start(self):
        """Initialize the tank and its components."""
        self.cannon.start()

    def update(self):
        """Update the tank's state each frame."""
        self.cannon.update()

    def end(self):
        """Clean up resources when the tank is destroyed."""
        pass

    def shoot(self, target):
        """Fire the cannon at a target."""
        self.cannon.shoot(target)

    def aim(self, direction: int):
        """Adjust the cannon's aim."""
        # Limit angle between 0 and 180 degrees
        self.angle += (self.angle < 180 and direction > 0) - (
            self.angle > 0 and direction < 0
        )
        self.cannon.move(Vector2(self.center), self.angle)

    def move(self, direction: int):
        """Move the tank horizontally."""
        if self.actual_movement > 0 and direction != 0:
            move_amount = direction * self.speed  # Use speed to calculate movement
            if abs(move_amount) <= self.actual_movement:
                self.x += move_amount
                if self.cannon.rect is not None:
                    self.cannon.rect.move_ip(move_amount, 0)
                else:
                    print("Warning: Cannon rect is None. Make sure start() is called.")
                self.actual_movement -= abs(
                    move_amount
                )  # Decrease stamina by amount moved
            else:
                # Move as far as stamina allows
                max_move = (
                    self.actual_movement if direction > 0 else -self.actual_movement
                )
                self.x += max_move
                if self.cannon.rect is not None:
                    self.cannon.rect.move_ip(max_move, 0)
                self.actual_movement = 0

    def recieve_damage(self, damage):
        """Handle incoming damage and check for destruction."""
        print(f"{self.__class__.__name__} receives {damage} damage")
        self.actual_health -= damage
        if self.actual_health <= 0:
            self.die()

    def die(self):
        """Handle the tank's destruction."""
        self.is_alive = False
        print(f"{self.__class__.__name__} has been destroyed!")

    def draw(self, screen):
        """Render the tank on the screen."""
        if not self.is_alive:
            return
        self.cannon.draw(screen)
        pygame.draw.rect(screen, self.color, self)
        self.draw_health_bar(screen)
        self.draw_stamina_bar(screen)

    def draw_health_bar(self, screen):
        """Draw the health bar above the tank."""
        health_bar_width = self.size_x * 0.5
        health_bar_height = 10

        # Calculate health bar position
        frame_bar_x = self.x + self.size_x / 2 - health_bar_width / 2
        frame_bar_y = self.y - 2 * health_bar_height

        # Draw health bar frame
        pygame.draw.rect(
            screen,
            (200, 200, 200),
            (frame_bar_x, frame_bar_y, health_bar_width, health_bar_height),
        )

        # Draw current health
        current_health_width = self.actual_health / self.health * health_bar_width
        pygame.draw.rect(
            screen,
            (0, 240, 0),
            (frame_bar_x, frame_bar_y, current_health_width, health_bar_height),
        )

    def draw_stamina_bar(self, screen):
        """Draw the stamina bar above the tank."""
        stamina_bar_width = self.size_x * 0.5
        stamina_bar_height = 5

        # Calculate stamina bar position
        frame_bar_x = self.x + self.size_x / 2 - stamina_bar_width / 2
        frame_bar_y = (
            self.y - 3 * stamina_bar_height
        )  # Position it above the health bar

        # Draw stamina bar frame
        pygame.draw.rect(
            screen,
            (200, 200, 200),
            (frame_bar_x, frame_bar_y, stamina_bar_width, stamina_bar_height),
        )

        # Draw current stamina
        current_stamina_width = self.actual_movement / self.movement * stamina_bar_width
        pygame.draw.rect(
            screen,
            (40, 40, 240),  # Blue color for stamina
            (frame_bar_x, frame_bar_y, current_stamina_width, stamina_bar_height),
        )

    def reset_movement(self):
        """Reset the tank's movement at the start of its turn."""
        self.actual_movement = self.movement
