from OpenGL.GL import *
from dataclasses import dataclass
from Shapes import Triangle
from vectors import *
from colors import ColorRgb
import math


@dataclass
class Light:
    color: ColorRgb
    strength: float


# Źródło światła
class PointLight:
    def __init__(self,
                 position: Vertex,
                 light_id: Constant,
                 ambient_color: Light,
                 diffuse_color: Light,
                 specular_color: Light,
                 constant_attenuation: float,
                 linear_attenuation: float,
                 quadratic_attrnuation: float):
        self.light_id = light_id
        self.position = Vertex(0.0, 0.0, 0.0)
        self.setPosition(position)
        self.enabled = False

        glLightfv(self.light_id, GL_AMBIENT,
                  [
                      ambient_color.color.red/255 * ambient_color.strength,
                      ambient_color.color.green/255 * ambient_color.strength,
                      ambient_color.color.blue/255 * ambient_color.strength,
                      1.0
                  ])
        glLightfv(self.light_id, GL_DIFFUSE,
                  [
                      diffuse_color.color.red/255 * diffuse_color.strength,
                      diffuse_color.color.green/255 * diffuse_color.strength,
                      diffuse_color.color.blue/255 * diffuse_color.strength,
                      1.0
                  ])
        glLightfv(self.light_id, GL_SPECULAR,
                  [
                      specular_color.color.red/255 * specular_color.strength,
                      specular_color.color.green/255 * specular_color.strength,
                      specular_color.color.blue/255 * specular_color.strength,
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
        self.enabled = enabled
        if enabled:
            glEnable(self.light_id)
        else:
            glDisable(self.light_id)

    def getEnabled(self):
        return self.enabled


class DirectionalLight:
    def __init__(self,
                 points_towards: Vector,
                 light_id: Constant,
                 diffuse_color: Light,
                 ambient_color: Light,
                 specular_color: Light):
        self.light_id = light_id
        self.direction = Vector(Vertex(0, 0, 0), Vertex(0, 0, 0))
        self.setDirection(points_towards)
        self.enabled = False

        glLightfv(self.light_id, GL_DIFFUSE,
                  [
                      diffuse_color.color.red/255 * diffuse_color.strength,
                      diffuse_color.color.green/255 * diffuse_color.strength,
                      diffuse_color.color.blue/255 * diffuse_color.strength,
                      1.0
                  ])
        glLightfv(self.light_id, GL_AMBIENT,
                  [
                      ambient_color.color.red / 255 * ambient_color.strength,
                      ambient_color.color.green / 255 * ambient_color.strength,
                      ambient_color.color.blue / 255 * ambient_color.strength,
                      1.0
                  ])
        glLightfv(self.light_id, GL_SPECULAR,
                  [
                      specular_color.color.red / 255 * specular_color.strength,
                      specular_color.color.green / 255 * specular_color.strength,
                      specular_color.color.blue / 255 * specular_color.strength,
                      1.0
                  ])

    # Zmiana kierunku światła
    def setDirection(self, points_towards: Vector):
        self.direction = multiplyByScalar(normalize(points_towards), -1)
        glLightfv(self.light_id, GL_POSITION,
                  [
                      self.direction.dx,
                      self.direction.dy,
                      self.direction.dz,
                      0.0
                  ])

    # Włączenie/wyłączenie źródła światła
    def setEnabled(self, enabled: bool):
        self.enabled = enabled
        if enabled:
            glEnable(self.light_id)
        else:
            glDisable(self.light_id)

    def getEnabled(self):
        return self.enabled


# Materiał, z którego wykonany jest renderowany obiekt
class Material:
    def __init__(self,
                 ambient_color: Light,
                 diffuse_color: Light,
                 specular_color: Light,
                 shininess: float):
        # Parametry materiały obiektu
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT,
                     [
                         ambient_color.color.red/255 * ambient_color.strength,
                         ambient_color.color.green/255 * ambient_color.strength,
                         ambient_color.color.blue/255 * ambient_color.strength,
                         1.0
                     ]
                     )
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE,
                     [
                         diffuse_color.color.red / 255 * ambient_color.strength,
                         diffuse_color.color.green / 255 * ambient_color.strength,
                         diffuse_color.color.blue / 255 * ambient_color.strength,
                         1.0
                     ]
                     )
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT,
                     [
                         specular_color.color.red / 255 * ambient_color.strength,
                         specular_color.color.green / 255 * ambient_color.strength,
                         specular_color.color.blue / 255 * ambient_color.strength,
                         1.0
                     ]
                     )
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
