import pygame
import requests
from views.ui_elements import draw_text
from config import settings

SCREEN_SIZE = (1280, 720)
LOGIN_URL = settings.API_URL + "/player/login"
REGISTER_URL = settings.API_URL + "/player/register"


def menu_view(screen, clock, background):
    """
    Display the menu screen and handle player login/registration.

    Args:
        screen (pygame.Surface): The main display surface.
        clock (pygame.time.Clock): The game clock for controlling frame rate.
        background (pygame.Surface): The background image for the menu.

    Returns:
        tuple: A tuple containing the names of the two players (or None if not logged in).
    """
    pygame.display.set_caption("Tank Turn Game")

    # Initialize fonts
    title_font = pygame.font.Font(None, 100)
    input_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 60)

    # Define colors
    COLOR_INACTIVE = pygame.Color("lightskyblue3")
    COLOR_ACTIVE = pygame.Color("dodgerblue2")
    COLOR_TEXT = pygame.Color("white")
    COLOR_BUTTON = pygame.Color("green")
    COLOR_BUTTON_HOVER = pygame.Color("limegreen")

    # Create input boxes and buttons
    input_boxes, button_boxes = create_ui_elements()

    # Initialize UI state
    colors = [COLOR_INACTIVE] * 4
    active_boxes = [False] * 4
    texts = [""] * 4
    player_names = [None, None]

    # Title animation
    title_angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None

            handle_input_events(
                event, input_boxes, button_boxes, active_boxes, texts, player_names
            )

        # Update colors based on active state
        colors = [COLOR_ACTIVE if active else COLOR_INACTIVE for active in active_boxes]

        # Draw UI
        draw_menu_ui(
            screen,
            background,
            title_font,
            input_font,
            button_font,
            input_boxes,
            button_boxes,
            colors,
            texts,
            title_angle,
        )

        # Update display
        pygame.display.flip()
        clock.tick(30)

        # Check if both players have logged in
        if all(player_names):
            running = False

    return player_names


def create_ui_elements():
    """Create and return input boxes and buttons for the UI."""
    input_boxes = [
        pygame.Rect(190, 250, 300, 60),  # Left side username
        pygame.Rect(190, 350, 300, 60),  # Left side password
        pygame.Rect(790, 250, 300, 60),  # Right side username
        pygame.Rect(790, 350, 300, 60),  # Right side password
    ]
    button_boxes = [
        pygame.Rect(240, 420, 200, 60),  # Left side Login
        pygame.Rect(240, 500, 200, 60),  # Left side Register
        pygame.Rect(840, 420, 200, 60),  # Right side Login
        pygame.Rect(840, 500, 200, 60),  # Right side Register
    ]
    return input_boxes, button_boxes


def handle_input_events(
    event, input_boxes, button_boxes, active_boxes, texts, player_names
):
    """Handle mouse clicks and keyboard input events."""
    if event.type == pygame.MOUSEBUTTONDOWN:
        handle_mouse_click(
            event, input_boxes, button_boxes, active_boxes, texts, player_names
        )
    elif event.type == pygame.KEYDOWN:
        handle_keyboard_input(event, active_boxes, texts)


def handle_mouse_click(
    event, input_boxes, button_boxes, active_boxes, texts, player_names
):
    """Handle mouse click events for input boxes and buttons."""
    for i, box in enumerate(input_boxes):
        active_boxes[i] = box.collidepoint(event.pos)

    for i, box in enumerate(button_boxes):
        if box.collidepoint(event.pos) and texts[i // 2 * 2] and texts[i // 2 * 2 + 1]:
            handle_login_register(i, texts, player_names)


def handle_keyboard_input(event, active_boxes, texts):
    """Handle keyboard input for active input boxes."""
    for i, active in enumerate(active_boxes):
        if active:
            if event.key == pygame.K_RETURN:
                active_boxes[i] = False
            elif event.key == pygame.K_BACKSPACE:
                texts[i] = texts[i][:-1]
            else:
                texts[i] += event.unicode


def handle_login_register(button_index, texts, player_names):
    """Handle login or registration attempts."""
    url = LOGIN_URL if button_index % 2 == 0 else REGISTER_URL
    try:
        response = requests.post(
            url,
            json={
                "username": texts[button_index // 2 * 2],
                "password": texts[button_index // 2 * 2 + 1],
            },
        )
        response.raise_for_status()
        player_names[button_index // 2] = texts[button_index // 2 * 2]
        action = "login" if button_index % 2 == 0 else "register"
        print(f"Player {button_index // 2 + 1} {action} successful.")
    except requests.exceptions.RequestException as e:
        handle_request_exception(e, response if "response" in locals() else None)


def handle_request_exception(e, response):
    """Handle exceptions from login/register requests."""
    if isinstance(e, requests.exceptions.HTTPError):
        if response.status_code == 400:
            print("Bad request. Please check your input.")
        elif response.status_code == 500:
            print("Server error. Please try again later.")
    else:
        print(
            "Failed to connect to the server. Please check the URL or your internet connection."
        )


def draw_menu_ui(
    screen,
    background,
    title_font,
    input_font,
    button_font,
    input_boxes,
    button_boxes,
    colors,
    texts,
    title_angle,
):
    """Draw all UI elements for the menu screen."""
    screen.blit(background, (0, 0))

    # Draw animated title
    draw_animated_title(screen, title_font, title_angle)

    # Draw input boxes and labels
    draw_input_boxes(screen, input_font, input_boxes, colors, texts)

    # Draw buttons
    draw_buttons(screen, button_font, button_boxes)


def draw_animated_title(screen, title_font, title_angle):
    """Draw the animated title of the game."""
    title_surf = title_font.render("Tank Turn Game", True, pygame.Color("white"))
    title_rect = title_surf.get_rect(center=(SCREEN_SIZE[0] // 2, 100))
    rotated_title = pygame.transform.rotate(title_surf, title_angle)
    rotated_rect = rotated_title.get_rect(center=title_rect.center)
    screen.blit(rotated_title, rotated_rect)


def draw_input_boxes(screen, input_font, input_boxes, colors, texts):
    """Draw input boxes and their labels."""
    for i, (box, color, text) in enumerate(zip(input_boxes, colors, texts)):
        txt_surface = input_font.render(text, True, color)
        width = max(300, txt_surface.get_width() + 10)
        input_boxes[i].w = width
        screen.blit(txt_surface, (box.x + 5, box.y + 5))
        pygame.draw.rect(screen, color, box, 2)

    # Draw labels for input boxes
    labels = ["Usuario 1", "Contraseña 1", "Usuario 2", "Contraseña 2"]
    label_positions = [(190, 200), (190, 300), (790, 200), (790, 300)]
    for label, pos in zip(labels, label_positions):
        draw_text(
            screen, label, input_font, pygame.Color("white"), pygame.Rect(*pos, 300, 50)
        )


def draw_buttons(screen, button_font, button_boxes):
    """Draw login and register buttons with hover effect."""
    mouse_pos = pygame.mouse.get_pos()
    for i, box in enumerate(button_boxes):
        button_color = (
            pygame.Color("limegreen")
            if box.collidepoint(mouse_pos)
            else pygame.Color("green")
        )
        pygame.draw.rect(screen, button_color, box)
        button_text = button_font.render(
            "Login" if i % 2 == 0 else "Register", True, pygame.Color("white")
        )
        screen.blit(button_text, (box.x + 35, box.y + 10))
