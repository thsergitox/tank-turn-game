import pygame
from views.ui_elements import draw_text

SCREEN_SIZE = (1280, 720)


def menu():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Tank Turn Game")
    clock = pygame.time.Clock()

    # Cargar y escalar la imagen de fondo
    background = pygame.image.load("image.jpg").convert()
    background = pygame.transform.scale(background, SCREEN_SIZE)

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

    # Cuadros de entrada y botón
    input_box1 = pygame.Rect(490, 250, 300, 60)
    input_box2 = pygame.Rect(490, 350, 300, 60)
    button_box = pygame.Rect(540, 460, 200, 60)

    color1 = COLOR_INACTIVE
    color2 = COLOR_INACTIVE
    active_box1 = False
    active_box2 = False
    text1 = ""
    text2 = ""
    player_name = None

    # Para la animación del título
    title_angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active_box1 = not active_box1
                else:
                    active_box1 = False
                if input_box2.collidepoint(event.pos):
                    active_box2 = not active_box2
                else:
                    active_box2 = False
                if button_box.collidepoint(event.pos) and text1 and text2:
                    player_name = text1
                    return player_name
                color1 = COLOR_ACTIVE if active_box1 else COLOR_INACTIVE
                color2 = COLOR_ACTIVE if active_box2 else COLOR_INACTIVE
            if event.type == pygame.KEYDOWN:
                if active_box1:
                    if event.key == pygame.K_RETURN:
                        active_box1 = False
                    elif event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
                if active_box2:
                    if event.key == pygame.K_RETURN:
                        active_box2 = False
                    elif event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode

        screen.blit(background, (0, 0))

        # Animación del título
        title_surf = title_font.render("Tank Turn Game", True, COLOR_TEXT)
        title_rect = title_surf.get_rect(center=(SCREEN_SIZE[0] // 2, 100))
        rotated_title = pygame.transform.rotate(title_surf, title_angle)
        rotated_rect = rotated_title.get_rect(center=title_rect.center)
        screen.blit(rotated_title, rotated_rect)
        title_angle += 0.05

        # Cuadros de entrada
        txt_surface1 = input_font.render(text1, True, color1)
        txt_surface2 = input_font.render(text2, True, color2)
        width = max(300, txt_surface1.get_width() + 10)
        input_box1.w = width
        input_box2.w = width
        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)

        # Etiquetas para los cuadros de entrada
        draw_text(
            screen, "Usuario", input_font, COLOR_TEXT, pygame.Rect(490, 200, 300, 50)
        )
        draw_text(
            screen, "Contraseña", input_font, COLOR_TEXT, pygame.Rect(490, 300, 300, 50)
        )

        # Botón con efecto hover
        mouse_pos = pygame.mouse.get_pos()
        button_color = (
            COLOR_BUTTON_HOVER if button_box.collidepoint(mouse_pos) else COLOR_BUTTON
        )
        pygame.draw.rect(screen, button_color, button_box)
        button_text = button_font.render("Ingresar", True, COLOR_TEXT)
        screen.blit(button_text, (button_box.x + 35, button_box.y + 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    return None
