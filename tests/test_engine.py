import mock
import pygame
from engine.canvas import Canvas
from engine.drawable import Drawable
from shapes.shape import Shape
from engine.engine import Engine2D


class TestEngine:

    @mock.patch('pygame.init')
    @mock.patch('pygame.quit')
    @mock.patch.object(Canvas, '__init__', return_value = None)
    def test_engine_should_add_shapes(self, p_init, p_quit, canvas):
        engine = Engine2D([640, 480])
        engine.canvas = mock.Mock(Canvas)
        shape = mock.Mock(Shape)
        engine.add_shape(shape)
        engine.canvas.add_shape.assert_called_once_with(shape)

    @mock.patch('pygame.init')
    @mock.patch('pygame.quit')
    @mock.patch.object(Canvas, '__init__', return_value=None)
    @mock.patch.object(Drawable, 'common_color')
    @mock.patch('engine.drawable.Drawable.common_color')
    def test_engine_should_change_color(self, p_init, p_quit, canvas, drawable, color):
        color.return_value = "black"
        engine = Engine2D([640, 480])
        engine.change_color("black")
        color.assert_called_once()
        assert Drawable.common_color == "black"


