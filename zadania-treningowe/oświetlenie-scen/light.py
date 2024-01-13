from OpenGL.GL import *
from dataclasses import dataclass
from Shapes import ColorRgb, Vertex, crossProcudt3d, Triangle
import math


def getNormalVectorTriangle(triangle: Triangle):
    ab_vec = Vertex(
        triangle.verticies[1].x - triangle.verticies[0].x,
        triangle.verticies[1].y - triangle.verticies[0].y,
        triangle.verticies[1].z - triangle.verticies[0].z
    )
    ac_vec = Vertex(
        triangle.verticies[2].x - triangle.verticies[0].x,
        triangle.verticies[2].y - triangle.verticies[0].y,
        triangle.verticies[2].z - triangle.verticies[0].z
    )
    normal_vector = crossProcudt3d(ab_vec, ac_vec)
    normal_vector_len = math.sqrt(normal_vector.x ** 2 + normal_vector.y ** 2 + normal_vector.z ** 2)
    normal_vector.x /= normal_vector_len
    normal_vector.y /= normal_vector_len
    normal_vector.z /= normal_vector_len
    return normal_vector


# Źródło światła
class LightSource:
    def __init__(self,
                 position: Vertex,
                 light_id: Constant,
                 ambient_color: ColorRgb,
                 diffuse_color: ColorRgb,
                 specular_color: ColorRgb,
                 constant_attenuation: float,
                 linear_attenuation: float,
                 quadratic_attrnuation: float):
        self.light_id = light_id
        self.position = Vertex(0.0, 0.0, 0.0)
        self.setPosition(position)

        glLightfv(self.light_id, GL_AMBIENT,
                  [
                      ambient_color.red/255,
                      ambient_color.blue/255,
                      ambient_color.green/255,
                      1.0
                  ])
        glLightfv(self.light_id, GL_DIFFUSE,
                  [
                      diffuse_color.red/255,
                      diffuse_color.blue/255,
                      diffuse_color.green/255,
                      1.0
                  ])
        glLightfv(self.light_id, GL_SPECULAR,
                  [
                      specular_color.red/255,
                      specular_color.blue/255,
                      specular_color.green/255,
                      1.0
                  ])
        glLightf(self.light_id, GL_CONSTANT_ATTENUATION, constant_attenuation)
        glLightf(self.light_id, GL_LINEAR_ATTENUATION, linear_attenuation)
        glLightf(self.light_id, GL_QUADRATIC_ATTENUATION, quadratic_attrnuation)

    # Zmiana pozycji światła
    def setPosition(self, position: Vertex):
        self.position = position
        glLightfv(self.light_id, GL_POSITION,
                 [
                    self.position.x,
                    self.position.y,
                    self.position.z,
                    1.0
                 ])

    # Włączenie/wyłączenie źródła światła
    def setEnabled(self, enabled: bool):
        if enabled:
            glEnable(self.light_id)
        else:
            glDisable(self.light_id)


# Materiał, z którego wykonany jest renderowany obiekt
class Material:
    def __init__(self,
                 ambient_color: ColorRgb,
                 diffuse_color: ColorRgb,
                 specular_color: ColorRgb,
                 shininess: float):
        # Parametry materiały obiektu
        glMaterialfv(GL_FRONT, GL_AMBIENT,
                     [
                         ambient_color.red/255,
                         ambient_color.green/255,
                         ambient_color.blue/255,
                         1.0
                     ]
                     )
        glMaterialfv(GL_FRONT, GL_DIFFUSE,
                     [
                         diffuse_color.red/255,
                         diffuse_color.green/255,
                         diffuse_color.blue/255,
                         1.0
                     ]
                     )
        glMaterialfv(GL_FRONT, GL_AMBIENT,
                     [
                         specular_color.red/255,
                         specular_color.green/255,
                         specular_color.blue/255,
                         1.0
                     ]
                     )
        glMaterialf(GL_FRONT, GL_SHININESS, shininess)
