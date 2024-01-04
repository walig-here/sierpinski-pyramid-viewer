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
    def __int__(self, position: Vertex, size: float):
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

        self.lines = [
            Line([v[0], v[1]]),
            Line([v[0], v[2]]),
            Line([v[0], v[3]]),
            Line([v[1], v[2]]),
            Line([v[1], v[3]]),
            Line([v[2], v[3]])
        ]
