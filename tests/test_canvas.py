from pygame import display
import pytest
from mock import mock
from engine.canvas import Canvas


class TestCanvas:
    testdata = [([0, 0], [0, 0]), ([-5, -5], [5, 5]), ([500.635, 300.234], [500, 300])]

    @pytest.mark.parametrize("size, expected", testdata)
    @mock.patch('pygame.display')
    def test_should_has_attribs(self, mock_display, size, expected):
        canvas = Canvas(size)
        assert canvas.size == expected
        assert canvas.display == mock_display
        assert canvas.shapes == []
