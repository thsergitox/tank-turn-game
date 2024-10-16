import pygame
from core import ObjectController, GameManager
from models.tank import LightTank, HeavyTank

"""
Game view module: Handles game screen, initializes objects, and manages game loop.
"""


def game_view(screen, clock):
    """
    Main game loop and rendering function.

    Args:
        screen (pygame.Surface): The main display surface.
        clock (pygame.time.Clock): The game clock for controlling frame rate.

    Returns:
        bool: True if the game completed successfully, False otherwise.
    """
    # Initialize game objects
    object_controller = ObjectController()
    object_controller.screen = screen
    object_controller.start()

    game_manager = GameManager()

    # Create and initialize players
    player1 = LightTank(object_controller, 100, 500)
    player2 = HeavyTank(object_controller, 1000, 500)
    player1.start()
    player2.start()

    game_manager.AddPlayer(player1)
    game_manager.AddPlayer(player2)

    # Create floor
    floor = pygame.Rect(0, 600, screen.get_width(), 120)

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_manager.NextPhase()

        # Update game state
        object_controller.update()
        game_manager.Update()

        # Render game objects
        screen.fill("skyblue")
        pygame.draw.rect(screen, "brown", floor)
        object_controller.draw()

        # Update display
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

    # Clean up
    object_controller.end()
    return True
