import mock
from engine.canvas import Canvas
from shapes.shape import Shape


class TestCanvasAddShape:

    @classmethod
    def setup_method(self):
        self.shape = mock.Mock(Shape)
        self.canvas = Canvas([0, 0])

    def test_should_add_shape(self):
        self.canvas.add_shape(self.shape)
        assert self.canvas.shapes[0] == self.shape

    def test_should_add_shapes(self):
        count = 100
        for i in range(count):
            self.canvas.add_shape(self.shape)

        assert len(self.canvas.shapes) == count
