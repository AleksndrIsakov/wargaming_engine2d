import mock
import pygame
from pygame import Surface, Rect

from engine.canvas import Canvas

class TestCanvasShow:

    def test_should_show_canvas(self):
        pygame_mock = mock.Mock(pygame.display)
        surface = mock.Mock(Surface)

        pygame_mock.set_mode([0, 0]).return_value = None
        surface.fill("white").return_value = None

        pygame_mock.set_mode.assert_called_with([0, 0])
        surface.fill.assert_called_with("white")

        canvas = Canvas([0, 0])
        canvas.display = pygame_mock
        canvas.show()





