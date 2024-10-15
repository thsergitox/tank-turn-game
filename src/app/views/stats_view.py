import pygame
from views.ui_elements import draw_text, draw_rounded_rect
import math

SCREEN_SIZE = (1280, 720)


def show_stats(player_name):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    # Cargar y escalar la imagen de fondo
    background = pygame.image.load("image.jpg").convert()
    background = pygame.transform.scale(background, SCREEN_SIZE)

    # Fuentes
    title_font = pygame.font.Font(None, 74)
    stats_font = pygame.font.Font(None, 50)
    message_font = pygame.font.Font(None, 40)
    button_font = pygame.font.Font(None, 60)

    # Colores
    COLOR_TEXT = pygame.Color("white")
    COLOR_BUTTON = pygame.Color("green")
    COLOR_BUTTON_HOVER = pygame.Color("limegreen")
    COLOR_EXIT = pygame.Color("red")
    COLOR_EXIT_HOVER = pygame.Color("darkred")

    # Botones
    start_button = pygame.Rect(490, 450, 300, 60)
    exit_button = pygame.Rect(490, 550, 300, 60)

    stats = {"Nivel": 3, "Tanque favorito": "Heavy"}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return True
                if exit_button.collidepoint(event.pos):
                    running = False

        screen.blit(background, (0, 0))

        # Para la animación del título
        title_angle = 0
        # Animación del título
        title_surf = title_font.render("Tank Turn Game", True, COLOR_TEXT)
        title_rect = title_surf.get_rect(center=(SCREEN_SIZE[0] // 2, 100))
        rotated_title = pygame.transform.rotate(title_surf, math.sin(title_angle) * 5)
        rotated_rect = rotated_title.get_rect(center=title_rect.center)
        screen.blit(rotated_title, rotated_rect)

        # Título y estadísticas con padding
        padding = 50
        draw_text(
            screen,
            f"Bienvenido, {player_name}",
            title_font,
            COLOR_TEXT,
            pygame.Rect(padding, 250, SCREEN_SIZE[0] - 2 * padding, 100),
        )
        draw_text(
            screen,
            f"Dale click a Iniciar partida",
            message_font,
            COLOR_TEXT,
            pygame.Rect(padding, 450, SCREEN_SIZE[0] - 2 * padding, 100),
        )
        draw_text(
            screen,
            f"para una nueva batalla",
            message_font,
            COLOR_TEXT,
            pygame.Rect(padding, 475, SCREEN_SIZE[0] - 2 * padding, 100),
        )
        draw_text(
            screen,
            "Estadísticas de jugador:",
            stats_font,
            COLOR_TEXT,
            pygame.Rect(SCREEN_SIZE[0] - 450, 175, 400, 50),
        )
        draw_text(
            screen,
            f"Tanque favorito: {stats['Tanque favorito']}",
            stats_font,
            COLOR_TEXT,
            pygame.Rect(SCREEN_SIZE[0] - 450, 275, 400, 50),
        )
        draw_text(
            screen,
            f"Nivel: {stats['Nivel']}",
            stats_font,
            COLOR_TEXT,
            pygame.Rect(SCREEN_SIZE[0] - 450, 375, 400, 50),
        )

        # Botón de iniciar partida
        mouse_pos = pygame.mouse.get_pos()
        start_color = (
            COLOR_BUTTON_HOVER if start_button.collidepoint(mouse_pos) else COLOR_BUTTON
        )
        draw_rounded_rect(screen, start_button, start_color, 10)
        start_text = button_font.render("Iniciar partida", True, COLOR_TEXT)
        screen.blit(start_text, (start_button.x + 20, start_button.y + 10))

        # Botón de salir
        exit_color = (
            COLOR_EXIT_HOVER if exit_button.collidepoint(mouse_pos) else COLOR_EXIT
        )
        draw_rounded_rect(screen, exit_button, exit_color, 10)
        exit_text = button_font.render("Salir", True, COLOR_TEXT)
        screen.blit(exit_text, (exit_button.x + 100, exit_button.y + 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    return False
