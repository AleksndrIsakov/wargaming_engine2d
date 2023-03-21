from shapes.shape import Shape


class Triangle(Shape):

    def __init__(self, points):
        super().__init__()
        self.points = points
