import pygame
import requests
from views.ui_elements import draw_text
from config import settings

SCREEN_SIZE = (1280, 720)
LOGIN_URL = settings.API_URL + "/player/login"
REGISTER_URL = settings.API_URL + "/player/register"

"""
This module contains the menu_view function which handles the menu screen for the game.

The menu_view function:
- Initializes Pygame and sets up the screen
- Loads and scales the background image
- Sets up fonts and colors for the UI elements
- Creates input boxes for username and password for two players
- Creates buttons for login and register
- Handles user input for button clicks and text input
- Animates the title text
- Returns the player names if both players have logged in or registered, otherwise returns None

Dependencies:
- pygame: For creating the game window and handling events
- requests: For making HTTP requests to the server
- config: For storing the API URL

Constants:
- SCREEN_SIZE: Tuple defining the dimensions of the game window (1280x720)
"""


def menu_view(screen, clock, background):
    pygame.init()
    pygame.display.set_caption("Tank Turn Game")
    # Fuentes
    title_font = pygame.font.Font(None, 100)
    input_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 60)

    # Colores
    COLOR_INACTIVE = pygame.Color("lightskyblue3")
    COLOR_ACTIVE = pygame.Color("dodgerblue2")
    COLOR_TEXT = pygame.Color("white")
    COLOR_BUTTON = pygame.Color("green")
    COLOR_BUTTON_HOVER = pygame.Color("limegreen")

    # Cuadros de entrada y botones para dos jugadores
    input_boxes = [
        pygame.Rect(190, 250, 300, 60),  # Left side
        pygame.Rect(190, 350, 300, 60),  # Left side
        pygame.Rect(790, 250, 300, 60),  # Right side
        pygame.Rect(790, 350, 300, 60),  # Right side
    ]
    button_boxes = [
        pygame.Rect(240, 420, 200, 60),  # Left side Login
        pygame.Rect(240, 500, 200, 60),  # Left side Register
        pygame.Rect(840, 420, 200, 60),  # Right side Login
        pygame.Rect(840, 500, 200, 60),  # Right side Register
    ]

    colors = [COLOR_INACTIVE] * 4
    active_boxes = [False] * 4
    texts = [""] * 4
    player_names = [None, None]

    # Para la animación del título
    title_angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if input_boxes[i].collidepoint(event.pos):
                        active_boxes[i] = not active_boxes[i]
                    else:
                        active_boxes[i] = False
                for i in range(4):
                    if (
                        button_boxes[i].collidepoint(event.pos)
                        and texts[i // 2 * 2]
                        and texts[i // 2 * 2 + 1]
                    ):
                        url = LOGIN_URL if i % 2 == 0 else REGISTER_URL
                        try:
                            response = requests.post(
                                url,
                                json={
                                    "username": texts[i // 2 * 2],
                                    "password": texts[i // 2 * 2 + 1],
                                },
                            )
                            response.raise_for_status()
                            player_names[i // 2] = texts[i // 2 * 2]
                            action = "login" if i % 2 == 0 else "register"
                            print(f"Player {i // 2 + 1} {action} successful.")
                        except requests.exceptions.RequestException as e:
                            if isinstance(e, requests.exceptions.HTTPError):
                                if response.status_code == 400:
                                    print("Bad request. Please check your input.")
                                elif response.status_code == 500:
                                    print("Server error. Please try again later.")
                                continue
                            else:
                                print(
                                    "Failed to connect to the server. Please check the URL or your internet connection."
                                )
                            continue
                colors = [
                    COLOR_ACTIVE if active else COLOR_INACTIVE
                    for active in active_boxes
                ]
            if event.type == pygame.KEYDOWN:
                for i in range(4):
                    if active_boxes[i]:
                        if event.key == pygame.K_RETURN:
                            active_boxes[i] = False
                        elif event.key == pygame.K_BACKSPACE:
                            texts[i] = texts[i][:-1]
                        else:
                            texts[i] += event.unicode

        screen.blit(background, (0, 0))

        # Animación del título
        title_surf = title_font.render("Tank Turn Game", True, COLOR_TEXT)
        title_rect = title_surf.get_rect(center=(SCREEN_SIZE[0] // 2, 100))
        rotated_title = pygame.transform.rotate(title_surf, title_angle)
        rotated_rect = rotated_title.get_rect(center=title_rect.center)
        screen.blit(rotated_title, rotated_rect)
        title_angle += 0.05

        # Cuadros de entrada
        for i in range(4):
            txt_surface = input_font.render(texts[i], True, colors[i])
            width = max(300, txt_surface.get_width() + 10)
            input_boxes[i].w = width
            screen.blit(txt_surface, (input_boxes[i].x + 5, input_boxes[i].y + 5))
            pygame.draw.rect(screen, colors[i], input_boxes[i], 2)

        # Etiquetas para los cuadros de entrada
        draw_text(
            screen, "Usuario 1", input_font, COLOR_TEXT, pygame.Rect(190, 200, 300, 50)
        )
        draw_text(
            screen,
            "Contraseña 1",
            input_font,
            COLOR_TEXT,
            pygame.Rect(190, 300, 300, 50),
        )
        draw_text(
            screen, "Usuario 2", input_font, COLOR_TEXT, pygame.Rect(790, 200, 300, 50)
        )
        draw_text(
            screen,
            "Contraseña 2",
            input_font,
            COLOR_TEXT,
            pygame.Rect(790, 300, 300, 50),
        )

        # Botones con efecto hover
        mouse_pos = pygame.mouse.get_pos()
        for i in range(4):
            button_color = (
                COLOR_BUTTON_HOVER
                if button_boxes[i].collidepoint(mouse_pos)
                else COLOR_BUTTON
            )
            pygame.draw.rect(screen, button_color, button_boxes[i])
            button_text = button_font.render(
                "Login" if i % 2 == 0 else "Register", True, COLOR_TEXT
            )
            screen.blit(button_text, (button_boxes[i].x + 35, button_boxes[i].y + 10))

        pygame.display.flip()
        clock.tick(30)

        # Verificar si ambos jugadores han ingresado
        if all(player_names):
            running = False

    pygame.quit()
    return player_names
