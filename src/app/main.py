import pygame
from core import ObjectController

CLOCK = None
SCREEN_SIZE = (1280, 720)
SCREEN = None
RUNNING = True

OBJECT_CONTROLLER = ObjectController()

FLOOR = pygame.Rect(0, 600, 1280, 120)

def start():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    CLOCK = pygame.time.Clock()
    OBJECT_CONTROLLER.start()

def update():
    global RUNNING, CLOCK, SCREEN
    while RUNNING:
        SCREEN.fill("skyblue")
        pygame.draw.rect(SCREEN, "green", FLOOR)
        
        OBJECT_CONTROLLER.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        
        pygame.display.update()
        
        pygame.display.update()
        CLOCK.tick(60)


def end():
    OBJECT_CONTROLLER.end()
    OBJECT_CONTROLLER.end()
    pygame.quit()


if __name__ == "__main__":
    start()
    update()
    end()
