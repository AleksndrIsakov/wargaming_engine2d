from unittest import mock

import pytest

from engine.drawable import Drawable
from shapes.triangle import Triangle


class TestTriangle:
    testdata = [([0, 0], [0, 0], [0, 0]), ([115, 50], [65, 100], [165, 100]), ([-115, -50], [-65, -100], [-165, -100])]

    @pytest.mark.parametrize("points", testdata)
    def test_should_has_points(self, points):
        assert Triangle(points).points == points

    def test_inherit_draw(self):
        assert isinstance(mock.Mock(Triangle), Drawable)