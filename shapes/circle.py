from shapes.shape import Shape


class Circle(Shape):

    def __init__(self, point: [], radius: int):
        super().__init__()
        self.radius = abs(radius)
        self.center = point