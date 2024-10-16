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
    object_controller = ObjectController()
    object_controller.screen = screen
    game_manager = GameManager()

    # Create and initialize players
    player1 = LightTank(object_controller, 100, 500)
    player2 = HeavyTank(object_controller, 1000, 500)
    object_controller.add_object(player1)
    object_controller.add_object(player2)
    player1.start()
    player2.start()

    game_manager.AddPlayer(player1)
    game_manager.AddPlayer(player2)

    object_controller.start()

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
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_manager.NextPhase()

        # Update game state
        object_controller.update()
        game_manager.Update()

        # Check for game over condition
        if not player1.is_alive or not player2.is_alive:
            winner = player_names[1] if not player1.is_alive else player_names[0]
            return show_game_over_screen(screen, winner, clock)

        # Render game objects
        screen.fill("skyblue")
        pygame.draw.rect(screen, "brown", floor)
        object_controller.draw()

        # Render turn information
        current_player = player_names[TURN]
        turn_type = get_turn_type()

        turn_text = f"{current_player} - {turn_type}"
        turn_surface = turn_font.render(turn_text, True, (255, 255, 255))
        turn_rect = turn_surface.get_rect(center=(screen.get_width() // 2, 30))
        screen.blit(turn_surface, turn_rect)

        # Render player names
        player1_surface = player_font.render(player_names[0], True, (255, 255, 255))
        player2_surface = player_font.render(player_names[1], True, (255, 255, 255))
        screen.blit(player1_surface, (10, 10))
        screen.blit(
            player2_surface, (screen.get_width() - player2_surface.get_width() - 10, 10)
        )

        pygame.display.flip()
        clock.tick(60)  # Maintain 60 FPS

    # Clean up
    object_controller.end()
    return False


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


def show_game_over_screen(screen, winner, clock):
    overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Semi-transparent black overlay
    screen.blit(overlay, (0, 0))

    font = pygame.font.Font(None, 74)
    win_text = font.render(f"{winner} Wins!", True, (255, 255, 255))
    win_rect = win_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 50)
    )
    screen.blit(win_text, win_rect)

    button_font = pygame.font.Font(None, 50)
    close_text = button_font.render("Close Game", True, (255, 255, 255))
    close_rect = close_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )
    pygame.draw.rect(screen, (200, 0, 0), close_rect.inflate(20, 10), border_radius=10)
    screen.blit(close_text, close_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_rect.collidepoint(event.pos):
                    return False
        clock.tick(60)

    return False
