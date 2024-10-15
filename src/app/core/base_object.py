from abc import abstractmethod

import pygame


class BaseObject(pygame.Rect):
    def __init__(self, object_controller, x, y, width, height):
        super().__init__(x, y, width, height)
        object_controller.list.append(self)

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def end(self):
        pass
