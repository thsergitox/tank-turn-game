import math
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, point, angle, speed, dmg, target):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect(center=(point.x, point.y))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.vx = speed * math.cos(math.radians(angle))
        self.vy = -speed * math.sin(math.radians(angle))
        self.gravity = 9.8 * speed / 10
        self.is_alive = True
        self.dmg = dmg
        self.target = target

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        dt = 1 / 60
        self.vy += self.gravity * dt
        self.pos.x += self.vx * dt
        self.pos.y += self.vy * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        self.check_collisions()
        self.check_limits()

    def check_collisions(self):
        if self.rect.colliderect(self.target):
            self.target.recieve_damage(self.dmg)
            self.is_alive = False

    def check_limits(self):
        if (
            self.rect.right < 0
            or self.rect.left > 1280
            or self.rect.bottom < 0
            or self.rect.top > 720
        ):
            self.is_alive = False

    def alive(self):
        return self.is_alive
