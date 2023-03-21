import mock
from pygame import Surface

from engine.canvas import Canvas


class TestCanvasShow:

    @mock.patch('pygame.display.set_mode')
    def test_should_show_canvas(self, mock_display):
        surface = mock.Mock(Surface)
        mock_display.return_value = surface
        canvas = Canvas([0, 0])

        # Check that we got value returned by pygame.display.set_mode
        assert canvas.show() == surface

        # Check that we call fill method with "white" argument
        surface.fill.assert_called_with("white")






