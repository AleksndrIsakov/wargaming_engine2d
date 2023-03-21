import pytest
from engine.canvas import Canvas


class TestCanvas:
    testdata = [([0, 0], [0, 0]), ([-5, -5], [5, 5]), ([500.635, 300.234], [500, 300])]

    @pytest.mark.parametrize("size, expected", testdata)
    def test_should_has_size(self, size, expected):
        assert Canvas(size).size == expected
