from engine.engine import Engine2D
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

screen_size = [640, 480]

colors = ["red", "blue", "green"]
rectangle_data = ([40, 300, 150, 150], [240, 300, 150, 150], [440, 300, 150, 150])
circle_data = (([115, 200], 60), ([315, 200], 60), ([515, 200], 60))
triangle_data = (([[115, 50], [65, 100], [165, 100]]), ([[315, 50], [265, 100], [365, 100]]), ([[515, 50], [465, 100], [565, 100]]))

engine = Engine2D(screen_size)
for i in range(3):
    engine.change_color(colors[i])
    engine.add_shape(Rectangle(rectangle_data[i]))
    engine.add_shape(Circle(*circle_data[i]))
    engine.add_shape(Triangle(triangle_data[i]))

engine.draw()
