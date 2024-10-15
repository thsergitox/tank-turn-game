import pygame


def draw_text(surface, text, font, color, rect, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    line_spacing = -2
    font_height = font.size("Tg")[1]
    while text:
        i = 1
        if y + font_height > rect.bottom:
            break
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)
        surface.blit(image, (rect.left, y))
        y += font_height + line_spacing
        text = text[i:]
    return text


def draw_rounded_rect(surface, rect, color, corner_radius):
    """Draw a rectangle with rounded corners"""
    if corner_radius < 0:
        raise ValueError(f"Corner radius ({corner_radius}) must be >= 0")

    rect = pygame.Rect(rect)
    color = pygame.Color(*color)
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pygame.Surface(rect.size, pygame.SRCALPHA)

    circle = pygame.Surface([min(rect.size) * 3] * 2, pygame.SRCALPHA)
    pygame.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = pygame.transform.smoothscale(circle, [corner_radius * 2] * 2)

    radius = corner_radius
    for point in [(radius, 0), (radius, radius), (0, radius)]:
        corner_rect = rect.inflate(-radius * 2, -radius * 2)
        position = (
            corner_rect.bottomright[0] - point[0],
            corner_rect.bottomright[1] - point[1],
        )
        rectangle.blit(circle, position)

    rectangle.fill((0, 0, 0), rect.inflate(-radius * 2, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius * 2))

    rectangle.fill(color, special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MIN)

    surface.blit(rectangle, pos)
