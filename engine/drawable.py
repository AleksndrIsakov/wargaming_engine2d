import pygame


class Drawable:
    common_color = "white"

    def __init__(self):
        self.color = Drawable.common_color

    def draw(self):
        screen = pygame.surface.Surface
        name = self.__class__.__name__
        attr = self.__dict__

        debug_info = "Drawing {} {}:".format(self.color, name)
        if name == "Circle":
            pygame.draw.circle(screen, self.color, attr.get("center"), attr.get("radius"))
            debug_info += "({}, {}) with radius {}".format(*attr.get("center"),attr.get("radius"))
        elif name == "Rectangle":
            pygame.draw.rect(screen, self.color, attr.get("points"))
            debug_info += "({}, {}) with height {} and width {})".format(*attr.get("points"))
        elif name == "Triangle":
            pygame.draw.polygon(screen, self.color, attr.get("points"))
            debug_info += "{}, {}, {}".format(*attr.get("points")).replace("[", "(").replace("]", ")")

        print(debug_info)


