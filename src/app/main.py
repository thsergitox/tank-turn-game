import pygame
from views.menu_view import menu_view
from views.stats_view import stats_view
from views.game_view import game_view

SCREEN_SIZE = (1280, 720)


def main():
    pygame.init()
    pygame.font.init()  # Initialize the font module
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    # Load background image
    background = pygame.image.load("image.jpg").convert()
    background = pygame.transform.scale(background, SCREEN_SIZE)

    running = True
    while running:
        # Menu
        player_names = menu_view(screen, clock, background)
        if not player_names or (player_names[0] is None and player_names[1] is None):
            running = False
            continue

        # Stats
        for player_name in player_names:
            if player_name and not stats_view(screen, clock, background, player_name):
                running = False
                break

        if not running:
            continue

        # Game
        if not game_view(screen, clock, player_names):
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
