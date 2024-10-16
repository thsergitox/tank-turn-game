import pygame
from views.menu_view import menu
from views.stats_view import show_stats
from core import ObjectController
from models.tank import *
from core import ObjectController, GameManager

CLOCK = None
SCREEN_SIZE = (1280, 720)
RUNNING = True

OBJECT_CONTROLLER = ObjectController()

GAME_MANAGER = GameManager()

PLAYER1 = LightTank(OBJECT_CONTROLLER, 100, 500)
PLAYER2 = LightTank(OBJECT_CONTROLLER, 1000, 500)

GAME_MANAGER.AddPlayer(PLAYER1)
GAME_MANAGER.AddPlayer(PLAYER2)

FLOOR = pygame.Rect(0, 600, 1280, 120)


def start():
    global OBJECT_CONTROLLER, CLOCK
    pygame.init()
    OBJECT_CONTROLLER.screen = pygame.display.set_mode(SCREEN_SIZE)
    CLOCK = pygame.time.Clock()
    OBJECT_CONTROLLER.start()
    OBJECT_CONTROLLER.start()


def update():
    global RUNNING, CLOCK, OBJECT_CONTROLLER
    while RUNNING:
        OBJECT_CONTROLLER.update()
        GAME_MANAGER.Update()

        OBJECT_CONTROLLER.screen.fill("skyblue")
        pygame.draw.rect(OBJECT_CONTROLLER.screen, "brown", FLOOR)
        OBJECT_CONTROLLER.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAME_MANAGER.NextPhase()

        pygame.display.update()
        pygame.display.update()
        CLOCK.tick(60)


def end():
    OBJECT_CONTROLLER.end()
    OBJECT_CONTROLLER.end()
    OBJECT_CONTROLLER.end()
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
