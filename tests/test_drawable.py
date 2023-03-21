import sys
from io import StringIO
import mock

from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle


class TestDrawable:

    @mock.patch('pygame.draw.rect')
    @mock.patch('pygame.surface.Surface')
    def test_should_call_draw_rectangle(self, draw_shape, surface):
        rectangle = Rectangle([0, 0, 0, 0])
        rectangle.draw()
        surface.assert_called_once()

    @mock.patch('pygame.draw.circle')
    @mock.patch('pygame.surface.Surface')
    def test_should_call_draw_circle(self, draw_shape, surface):
        circle = Circle([0, 0], 0)
        circle.draw()
        surface.assert_called_once()

    @mock.patch('pygame.draw.polygon')
    @mock.patch('pygame.surface.Surface')
    def test_should_call_draw_triangle(self, draw_shape, surface):
        triangle = Triangle([0, 0, 0, 0])
        triangle.draw()
        surface.assert_called_once()
