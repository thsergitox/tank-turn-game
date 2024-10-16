import pygame
from core import ObjectController, GameManager
from core.game_manager import PHASE, EPhase, TURN, PLAYERS
from models.tank import LightTank, HeavyTank

"""
Game view module: Handles game screen, initializes objects, and manages game loop.
"""


def game_view(screen, clock, player_names):
    """
    Main game loop and rendering function.

    Args:
        screen (pygame.Surface): The main display surface.
        clock (pygame.time.Clock): The game clock for controlling frame rate.
        player_names (list): List containing the names of the two players.

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

    # Font for turn information and player names
    turn_font = pygame.font.Font(None, 36)
    player_font = pygame.font.Font(None, 24)

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

        # Render turn information
        current_player = player_names[TURN]
        turn_type = get_turn_type()  # Use a function to get the current turn type

        turn_text = f"{current_player} - {turn_type}"
        turn_surface = turn_font.render(turn_text, True, (255, 255, 255))
        turn_rect = turn_surface.get_rect(center=(screen.get_width() // 2, 30))
        screen.blit(turn_surface, turn_rect)

        # Render player names
        player1_surface = player_font.render(player_names[0], True, (255, 255, 255))
        player2_surface = player_font.render(player_names[1], True, (255, 255, 255))
        screen.blit(player1_surface, (10, 10))  # Top-left corner
        screen.blit(
            player2_surface, (screen.get_width() - player2_surface.get_width() - 10, 10)
        )  # Top-right corner

        # Update display
        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

    # Clean up
    object_controller.end()
    return True


def get_turn_type():
    """Get the current turn type based on the global PHASE."""
    global PHASE
    if PHASE == EPhase.MOVEMENT:
        return "Move"
    elif PHASE == EPhase.AIM:
        return "Aim"
    elif PHASE == EPhase.SHOOT:
        return "Shoot"
    elif PHASE == EPhase.WAITING_SHOOT:
        return "Waiting"
    else:
        return "Unknown"
