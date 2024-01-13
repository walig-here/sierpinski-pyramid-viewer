from dataclasses import  dataclass
import math


@dataclass
class ColorRgb:
    red: int
    green: int
    blue: int


@dataclass
class Vertex:
    x: float
    y: float
    z: float = 0.0


def crossProcudt3d(a: Vertex, b: Vertex):
    return Vertex(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x)


@dataclass
class Triangle:
    verticies: [Vertex] * 3


@dataclass
class Line:
    verticies: [Vertex] * 2


class Pyramid:
    def __init__(self,
                 position: Vertex,
                 size: float
                 ):
        piramid_h = size / 3 * math.sqrt(6)
        sidewall_h = size / 2 * math.sqrt(3)
        v = [
            Vertex(
                position.x - size / 2.0,
                position.y - piramid_h / 2.0,
                position.z + sidewall_h / 3.0
            ),
            Vertex(
                position.x + size / 2.0,
                position.y - piramid_h / 2.0,
                position.z + sidewall_h / 3.0
            ),
            Vertex(
                position.x,
                position.y + piramid_h / 2.0,
                position.z
            ),
            Vertex(
                position.x,
                position.y - piramid_h / 2.0,
                position.z - sidewall_h * 2.0 / 3.0
            )
        ]

        self.triangles = [
            Triangle([v[0], v[1], v[2]]),
            Triangle([v[0], v[1], v[3]]),
            Triangle([v[0], v[2], v[3]]),
            Triangle([v[1], v[2], v[3]]),
        ]


class Level2Terix:
    def __init__(self, position: Vertex, size: float, levels: int):
        piramid_h = size / 3 * math.sqrt(6)
        sidewall_h = size / 2 * math.sqrt(3)

        #Piramida składowa 1
        if levels > 2:
            self.subpyramid_1 = Level2Terix(
                Vertex(position.x + size / 4, position.y - piramid_h / 4,
                       position.z + sidewall_h / 6),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_1 = Pyramid(
                Vertex(position.x+size/4, position.y-piramid_h/4, position.z+sidewall_h/6),
                size/2
            )

        # Piramida składowa 2
        if levels > 2:
            self.subpyramid_2 = Level2Terix(
                Vertex(position.x - size / 4, position.y - piramid_h / 4, position.z + sidewall_h / 6),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_2 = Pyramid(
                Vertex(position.x - size / 4, position.y - piramid_h / 4,
                       position.z + sidewall_h / 6),
                size / 2
            )

        # Piramida składowa 3
        if levels > 2:
            self.subpyramid_3 = Level2Terix(
                Vertex(position.x, position.y + piramid_h / 4, position.z),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_3 = Pyramid(
                Vertex(position.x, position.y + piramid_h / 4, position.z),
                size / 2
            )

        # Piramida składowa 4
        if levels > 2:
            self.subpyramid_4 = Level2Terix(
                Vertex(position.x, position.y - piramid_h / 4, position.z - sidewall_h / 3),
                size / 2,
                levels-1
            )
        else:
            self.subpyramid_4 = Pyramid(
                Vertex(position.x, position.y - piramid_h / 4, position.z - sidewall_h/3),
                size / 2
            )
