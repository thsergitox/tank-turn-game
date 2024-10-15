from views.menu_view import menu
from views.stats_view import show_stats
from core import ObjectController
from models.tank import *
import pygame

CLOCK = None
SCREEN_SIZE = (1280, 720)
RUNNING = True

OBJECT_CONTROLLER = ObjectController()

PLAYER1 = LightTank(OBJECT_CONTROLLER, 100, 500)
PLAYER2 = LightTank(OBJECT_CONTROLLER, 1000, 500)

FLOOR = pygame.Rect(0, 600, 1280, 120)


def start():
    global OBJECT_CONTROLLER, CLOCK
    pygame.init()
    OBJECT_CONTROLLER.screen = pygame.display.set_mode(SCREEN_SIZE)
    CLOCK = pygame.time.Clock()
    OBJECT_CONTROLLER.start()


def update():
    global RUNNING, CLOCK, OBJECT_CONTROLLER
    while RUNNING:
        OBJECT_CONTROLLER.screen.fill("skyblue")
        pygame.draw.rect(OBJECT_CONTROLLER.screen, "brown", FLOOR)

        OBJECT_CONTROLLER.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False

        pygame.display.update()
        CLOCK.tick(60)


def end():
    OBJECT_CONTROLLER.end()
    pygame.quit()


if __name__ == "__main__":
    player_name = menu()
    if player_name:
        if show_stats(player_name):
            if RUNNING:
                start()
                update()
                end()
