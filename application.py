from engine.engine import Engine2D
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle

engine = Engine2D([640, 480])

engine.change_color("red")
engine.add_shape(Rectangle([40, 300, 150, 150]))
engine.add_shape(Circle([115, 200], 60))
engine.add_shape(Triangle([[115, 50], [65, 100], [165, 100]]))
engine.change_color("blue")
engine.add_shape(Rectangle([240, 300, 150, 150]))
engine.add_shape(Circle([315, 200], 60))
engine.add_shape(Triangle([[315, 50], [265, 100], [365, 100]]))
engine.change_color("green")
engine.add_shape(Rectangle([440, 300, 150, 150]))
engine.add_shape(Circle([515, 200], 60))
engine.add_shape(Triangle([[515, 50], [465, 100], [565, 100]]))

engine.draw()
