from dataclasses import  dataclass


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
