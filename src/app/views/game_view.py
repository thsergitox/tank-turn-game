import pygame
from core import ObjectController, GameManager
from models.tank import LightTank

"""
This module contains the game_view function which handles the game screen for the game.

The game_view function:
- Initializes Pygame and sets up the screen
- Loads and scales the background image
- Sets up fonts and colors for the UI elements
- Creates buttons for starting the game and exiting
- Displays the player's statistics
- Handles user input for button clicks

Dependencies:
- pygame: For creating the game window and handling events
- core: For managing game objects and updating the game state
- models.tank: For creating the player's tanks

Constants:
- SCREEN_SIZE: Tuple defining the dimensions of the game window (1280x720)
"""


def game_view(screen, clock):
    object_controller = ObjectController()
    object_controller.screen = screen
    object_controller.start()

    game_manager = GameManager()

    player1 = LightTank(object_controller, 100, 500)
    player2 = LightTank(object_controller, 1000, 500)

    game_manager.AddPlayer(player1)
    game_manager.AddPlayer(player2)

    floor = pygame.Rect(0, 600, screen.get_width(), 120)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_manager.NextPhase()

        object_controller.update()
        game_manager.Update()

        screen.fill("skyblue")
        pygame.draw.rect(screen, "brown", floor)
        object_controller.draw()

        pygame.display.flip()
        clock.tick(60)

    object_controller.end()
    return True  # Or return game result if needed
