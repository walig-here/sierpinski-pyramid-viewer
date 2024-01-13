from dataclasses import dataclass
import math
from vectors import *


class Triangle:
    def __init__(self, verticies: [Vertex]*3, normal_vector: Vector):
        self.verticies = verticies
        self.normals = []

        # Wektor normalny wierzchołka v0
        self.normals.append(normal_vector)

        # Wektor normalny wierzchołka v1
        self.normals.append(
            translate(normal_vector, Vector(verticies[1], verticies[0]))
        )

        # Wektor normalny wierzchołka v2
        self.normals.append(
            translate(normal_vector, Vector(verticies[2], verticies[0]))
        )


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
                position.y - piramid_h / 2.0,
                position.z - sidewall_h * 2.0 / 3.0
            ),
            Vertex(
                position.x,
                position.y + piramid_h / 2.0,
                position.z
            )
        ]

        # Wektory normalne trójkątów
        normal_v0v1v2 = crossProcudt3d(Vector(v[2], v[0]), Vector(v[1], v[0]))
        normal_v0v1v3 = crossProcudt3d(Vector(v[1], v[0]), Vector(v[3], v[0]))
        normal_v0v2v3 = crossProcudt3d(Vector(v[3], v[0]), Vector(v[2], v[0]))
        normal_v1v2v3 = crossProcudt3d(Vector(v[2], v[1]), Vector(v[3], v[1]))

        self.triangles = [
            Triangle([v[0], v[1], v[2]], normal_v0v1v2),
            Triangle([v[0], v[1], v[3]], normal_v0v1v3),
            Triangle([v[0], v[2], v[3]], normal_v0v2v3),
            Triangle([v[1], v[2], v[3]], normal_v1v2v3),
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
