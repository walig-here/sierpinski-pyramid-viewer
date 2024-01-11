from dataclasses import  dataclass
import math


@dataclass
class ColorRgb:
    red: int
    green: int
    blue: int


@dataclass
class Vertex:
    color: ColorRgb
    x: float
    y: float
    z: float = 0.0


@dataclass
class Triangle:
    verticies: [Vertex] * 3


@dataclass
class Line:
    verticies: [Vertex] * 2


class Pyramid:
    def __init__(self, position: Vertex, size: float):
        piramid_h = size / 3 * math.sqrt(6)
        sidewall_h = size / 2 * math.sqrt(3)
        v = [
            Vertex(
                ColorRgb(255, 255, 255),
                position.x - size / 2.0,
                position.y - piramid_h / 2.0,
                position.z + sidewall_h / 3.0
            ),
            Vertex(
                ColorRgb(255, 255, 255),
                position.x + size / 2.0,
                position.y - piramid_h / 2.0,
                position.z + sidewall_h / 3.0
            ),
            Vertex(
                ColorRgb(255, 255, 255),
                position.x,
                position.y + piramid_h / 2.0,
                position.z
            ),
            Vertex(
                ColorRgb(255, 255, 255),
                position.x,
                position.y - piramid_h / 2.0,
                position.z - sidewall_h * 2.0 / 3.0
            )
        ]

        self.triangles = [
            Triangle([v[0], v[1], v[2]]),
            Triangle([v[0], v[1], v[3]]),
            Triangle([v[1], v[2], v[3]]),
            Triangle([v[2], v[2], v[3]])
        ]


class Level2Terix:
    def __init__(self, position: Vertex, size: float, levels: int):
        piramid_h = size / 3 * math.sqrt(6)
        sidewall_h = size / 2 * math.sqrt(3)

        #Piramida składowa 1
        if levels > 2:
            self.subpyramid_1 = Level2Terix(
                Vertex(ColorRgb(0, 0, 0), position.x + size / 4, position.y - piramid_h / 4,
                       position.z + sidewall_h / 6),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_1 = Pyramid(
                Vertex(ColorRgb(0, 0, 0), position.x+size/4, position.y-piramid_h/4, position.z+sidewall_h/6),
                size/2
            )

        # Piramida składowa 2
        if levels > 2:
            self.subpyramid_2 = Level2Terix(
                Vertex(ColorRgb(0, 0, 0), position.x - size / 4, position.y - piramid_h / 4, position.z + sidewall_h / 6),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_2 = Pyramid(
                Vertex(ColorRgb(0, 0, 0), position.x - size / 4, position.y - piramid_h / 4,
                       position.z + sidewall_h / 6),
                size / 2
            )

        # Piramida składowa 3
        if levels > 2:
            self.subpyramid_3 = Level2Terix(
                Vertex(ColorRgb(0, 0, 0), position.x, position.y + piramid_h / 4, position.z),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_3 = Pyramid(
                Vertex(ColorRgb(0, 0, 0), position.x, position.y + piramid_h / 4, position.z),
                size / 2
            )

        # Piramida składowa 4
        if levels > 2:
            self.subpyramid_4 = Level2Terix(
                Vertex(ColorRgb(0, 0, 0), position.x, position.y - piramid_h / 4, position.z - sidewall_h / 3),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_4 = Pyramid(
                Vertex(ColorRgb(0, 0, 0), position.x, position.y - piramid_h / 4, position.z - sidewall_h/3),
                size / 2
            )
