import pygame
from models.tank import *

CLOCK = None
SCREEN_SIZE = (1280, 720)
SCREEN = None
RUNNING = True


def start():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    CLOCK = pygame.time.Clock()


def update():
    global RUNNING, CLOCK, SCREEN
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        SCREEN.fill("skyblue")
        # Test draw tanks
        tank = LightTank(100, 100)
        tank.draw(SCREEN)

        pygame.display.flip()
        CLOCK.tick(60)


def end():
    pygame.quit()


if __name__ == "__main__":
    start()
    update()
    end()
