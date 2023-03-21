from unittest import mock

import pytest

from engine.drawable import Drawable
from shapes.rectangle import Rectangle


class TestRectangle:
    testdata = [[0, 0, 0, 0], [-5, -5, -5, -5], [5, 5, 5, 5]]

    @pytest.mark.parametrize("points", testdata)
    def test_should_has_points(self, points):
        assert Rectangle(points).points == points

    def test_inherit_draw(self):
        assert isinstance(mock.Mock(Rectangle), Drawable)