from engine.canvas import Canvas
from engine.drawable import Drawable
import pygame


class Engine2D:

    def __init__(self, size):
        self.canvas = Canvas(size)
        pygame.init()

    def __del__(self):
        pygame.quit()

    def change_color(self, color):
        Drawable.common_color = color

    def add_shape(self, shape):
        self.canvas.add_shape(shape)

    def draw(self):
        pygame.surface.Surface = self.canvas.show()

        # Loop until the user clicks the close button.
        clock = pygame.time.Clock()
        done = False
        while not done:
            clock.tick(3)

            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            for shape in self.canvas.shapes:
                shape.draw()

            pygame.display.flip()
