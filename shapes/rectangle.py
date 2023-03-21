from shapes.shape import Shape


class Rectangle(Shape):

    def __init__(self, points):
        super().__init__()
        self.points = points