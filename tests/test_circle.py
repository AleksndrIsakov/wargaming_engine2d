import mock
import pytest

from engine.drawable import Drawable
from shapes.circle import Circle


class TestCircle:
    testdata = [([0, 0], 0, 0), ([10, 10], -5, 5), ([-5, -5], 5, 5)]

    @pytest.mark.parametrize("point,radius,expected", testdata)
    def test_should_has_radius(self, point, radius, expected):
        assert Circle(point, radius).radius == expected

    @pytest.mark.parametrize("point,radius,expected", testdata)
    def test_should_has_points(self, point, radius, expected):
        assert Circle(point, radius).center == point

    def test_should_be_drawable(self):
        assert isinstance(mock.Mock(Circle), Drawable)