from Shapes import Vertex, ColorRgb
import math

from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self,
                 frame,
                 looking_at_point: Vertex,
                 stands_at_point: Vertex):
        self.__looking_at = looking_at_point
        self.__up_vector = Vertex(0, 1, 0)
        self.__position = stands_at_point
        self.zoom_level = 1.0
        self.aspect = frame.get_width()/frame.get_height()

    def rotateRight(self, angle_deg: float):
        forward_vec = Vertex(
            (self.__looking_at.x - self.__position.x),
            (self.__looking_at.y - self.__position.y),
            (self.__looking_at.z - self.__position.z)
        )
        self.__looking_at.x = self.__looking_at.x + (forward_vec.y * self.__up_vector.z - forward_vec.z * self.__up_vector.y) * angle_deg
        self.__looking_at.y = self.__looking_at.y - (forward_vec.y * self.__up_vector.x - forward_vec.x * self.__up_vector.z) * angle_deg
        self.__looking_at.z = self.__looking_at.z + (forward_vec.x * self.__up_vector.y - forward_vec.y * self.__up_vector.x) * angle_deg

    def rotateLeft(self, angle_deg: float):
        forward_vec = Vertex(
            (self.__looking_at.x - self.__position.x),
            (self.__looking_at.y - self.__position.y),
            (self.__looking_at.z - self.__position.z)
        )
        self.__looking_at.x = self.__looking_at.x - (forward_vec.y * self.__up_vector.z - forward_vec.z * self.__up_vector.y) * angle_deg
        self.__looking_at.y = self.__looking_at.y - (forward_vec.y * self.__up_vector.x - forward_vec.x * self.__up_vector.z) * angle_deg
        self.__looking_at.z = self.__looking_at.z - (forward_vec.x * self.__up_vector.y - forward_vec.y * self.__up_vector.x) * angle_deg

    def moveRight(self, distance: float):
        forward_vec = Vertex(
            (self.__looking_at.x - self.__position.x),
            (self.__looking_at.y - self.__position.y),
            (self.__looking_at.z - self.__position.z)
        )
        self.__looking_at.x = self.__looking_at.x + (forward_vec.y*self.__up_vector.z - forward_vec.z*self.__up_vector.y) * distance
        self.__looking_at.y = self.__looking_at.y + (forward_vec.y*self.__up_vector.x - forward_vec.x*self.__up_vector.z) * distance
        self.__looking_at.z = self.__looking_at.z + (forward_vec.x*self.__up_vector.y - forward_vec.y*self.__up_vector.x) * distance

        self.__position.x = self.__position.x + (forward_vec.y * self.__up_vector.z - forward_vec.z * self.__up_vector.y) * distance
        self.__position.y = self.__position.y + (forward_vec.y * self.__up_vector.x - forward_vec.x * self.__up_vector.z) * distance
        self.__position.z = self.__position.z + (forward_vec.x * self.__up_vector.y - forward_vec.y * self.__up_vector.x) * distance

    def moveLeft(self, distance: float):
        forward_vec = Vertex(
            (self.__looking_at.x - self.__position.x),
            (self.__looking_at.y - self.__position.y),
            (self.__looking_at.z - self.__position.z)
        )
        self.__looking_at.x = self.__looking_at.x - (forward_vec.y*self.__up_vector.z - forward_vec.z*self.__up_vector.y) * distance
        self.__looking_at.y = self.__looking_at.y - (forward_vec.y*self.__up_vector.x - forward_vec.x*self.__up_vector.z) * distance
        self.__looking_at.z = self.__looking_at.z - (forward_vec.x*self.__up_vector.y - forward_vec.y*self.__up_vector.x) * distance

        self.__position.x = self.__position.x - (forward_vec.y * self.__up_vector.z - forward_vec.z * self.__up_vector.y) * distance
        self.__position.y = self.__position.y - (forward_vec.y * self.__up_vector.x - forward_vec.x * self.__up_vector.z) * distance
        self.__position.z = self.__position.z - (forward_vec.x * self.__up_vector.y - forward_vec.y * self.__up_vector.x) * distance

    def moveForward(self, distance: float):
        self.__position.x = self.__position.x + distance * (self.__looking_at.x - self.__position.x)
        self.__position.y = self.__position.y + distance * (self.__looking_at.y - self.__position.y)
        self.__position.z = self.__position.z + distance * (self.__looking_at.z - self.__position.z)

    def moveBackward(self, distance: float):
        self.__position.x = self.__position.x - distance * (self.__looking_at.x - self.__position.x)
        self.__position.y = self.__position.y - distance * (self.__looking_at.y - self.__position.y)
        self.__position.z = self.__position.z - distance * (self.__looking_at.z - self.__position.z)

    def zoomIn(self, zoom: float):
        self.zoom_level = self.zoom_level - zoom

    def zoomOut(self, zoom: float):
        self.zoom_level = self.zoom_level + zoom
        if self.zoom_level < 0.1:
            self.zoom_level = 0.1

    def reset(self):
        self.zoom_level = 1.0
        self.__looking_at = Vertex(0, 0, 0)

    def refresh(self, display_w, display_h):
        # Zastosowanie perspektywy oraz zoom'u
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45*self.zoom_level, self.aspect, 0.1, 50.0)

        # Ruchy kamery w przestrzeni
        gluLookAt(self.__position.x, self.__position.y, self.__position.z,
                  self.__looking_at.x, self.__looking_at.y, self.__looking_at.z,
                  self.__up_vector.x, self.__up_vector.y, self.__up_vector.z)