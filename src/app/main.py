import pygame
from views.menu_view import menu_view
from views.stats_view import stats_view
from views.game_view import game_view

SCREEN_SIZE = (1280, 720)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    # Load background image once
    background = pygame.image.load("image.jpg").convert()
    background = pygame.transform.scale(background, SCREEN_SIZE)

    while True:
        # Menu
        players = menu_view(screen, clock, background)
        if not players or (players[0] is None and players[1] is None):
            break

        # Stats
        if not all(
            stats_view(screen, clock, background, player)
            for player in players
            if player
        ):
            break

        # Game
        game_result = game_view(screen, clock)
        if not game_result:
            break

    pygame.quit()


if __name__ == "__main__":
    main()
