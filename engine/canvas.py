import pygame
from shapes.shape import Shape


class Canvas:

    def __init__(self, size):
        self.size = [int(abs(size[0])), int(abs(size[1]))]
        self.shapes = []
        self.display = pygame.display

    def show(self):
        screen = self.display.set_mode(self.size)
        screen.fill("white")
        return screen

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)