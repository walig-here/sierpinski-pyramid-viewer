import math
from dataclasses import  dataclass


@dataclass
class Vertex:
    x: float
    y: float
    z: float


class Vector:
    def __init__(self, end: Vertex, begin: Vertex):
        self.dx = end.x - begin.x
        self.dy = end.y - begin.y
        self.dz = end.z - begin.z

        # Punkt końcowy wektora
        self.end = Vertex(end.x, end.y, end.z)

        # Punkt początkowy wektora
        self.begin = Vertex(begin.x, begin.y, begin.z)

    def getLength(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2 + self.dz ** 2)


def crossProcudt3d(a: Vector, b: Vector):
    result = Vector(a.end, a.begin)

    result.dx = a.dy * b.dz - a.dz * b.dy
    result.dy = a.dz * b.dx - a.dx * b.dz
    result.dz = a.dx * b.dy - a.dy * b.dx

    result.end.x = result.begin.x + result.dx
    result.end.y = result.begin.y + result.dy
    result.end.z = result.begin.z + result.dz

    return result


def translate(a: Vector, t: Vector):
    result = Vector(a.end, a.begin)

    result.begin.x = a.begin.x + t.dx
    result.begin.y = a.begin.y + t.dy
    result.begin.z = a.begin.z + t.dz

    result.end.x = a.end.x + t.dx
    result.end.y = a.end.y + t.dy
    result.end.z = a.end.z + t.dz

    return result


def multiplyByScalar(a: Vector, scalar: float):
    result = Vector(a.end, a.begin)
    result.dx = a.dx * scalar
    result.dy = a.dy * scalar
    result.dz = a.dz * scalar

    result.end.x = result.begin.x + result.dx
    result.end.y = result.begin.y + result.dy
    result.end.z = result.begin.z + result.dz

    return result


def normalize(a: Vector):
    return multiplyByScalar(a, 1/a.getLength())
