from vectors import *
from colors import ColorRgb
import math

from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self,
                 frame,
                 looking_at: Vertex,
                 stands_at_point: Vertex):
        self.__forward_vector = Vector(looking_at, stands_at_point)
        self.__default_vector = Vector(looking_at, stands_at_point)
        self.__up_vector = Vector(Vertex(stands_at_point.x, stands_at_point.y+1, stands_at_point.z), stands_at_point)
        self.zoom_level = 1.0
        self.aspect = frame.get_width()/frame.get_height()

    def getPosition(self):
        return self.__forward_vector.begin

    def rotateUp(self, angle_deg: float):
        self.__forward_vector = rotateVecrtorVertically(self.__forward_vector, angle_deg * math.pi / 180)

    def rotateDown(self, angle_deg: float):
        self.__forward_vector = rotateVecrtorVertically(self.__forward_vector, -angle_deg * math.pi / 180)

    def rotateRight(self, angle_deg: float):
        self.__forward_vector = rotateVecrtorHorizointaly(self.__forward_vector, -angle_deg * math.pi / 180)

    def rotateLeft(self, angle_deg: float):
        self.__forward_vector = rotateVecrtorHorizointaly(self.__forward_vector, angle_deg * math.pi / 180)

    def moveUp(self, distance: float):
        up_vector_normalized = normalize(self.__up_vector)
        up_vector_normalized = multiplyByScalar(up_vector_normalized, distance)
        self.__forward_vector = translateVector(self.__forward_vector, up_vector_normalized)

    def moveDown(self, distance: float):
        up_vector_normalized = normalize(self.__up_vector)
        up_vector_normalized = multiplyByScalar(up_vector_normalized, -distance)
        self.__forward_vector = translateVector(self.__forward_vector, up_vector_normalized)

    def moveRight(self, distance: float):
        right_vector = normalize(crossProcudt3d(self.__forward_vector, self.__up_vector))
        right_vector = multiplyByScalar(right_vector, distance)
        self.__forward_vector = translateVector(self.__forward_vector, right_vector)

    def moveLeft(self, distance: float):
        left_vector = normalize(crossProcudt3d(self.__up_vector, self.__forward_vector))
        left_vector = multiplyByScalar(left_vector, distance)
        self.__forward_vector = translateVector(self.__forward_vector, left_vector)

    def moveForward(self, distance: float):
        forward_vector_normalized = normalize(self.__forward_vector)
        forward_vector_normalized = multiplyByScalar(forward_vector_normalized, distance)
        self.__forward_vector = translateVector(self.__forward_vector, forward_vector_normalized)

    def moveBackward(self, distance: float):
        forward_vector_normalized = normalize(self.__forward_vector)
        forward_vector_normalized = multiplyByScalar(forward_vector_normalized, -distance)
        self.__forward_vector = translateVector(self.__forward_vector, forward_vector_normalized)

    def zoomIn(self, zoom: float):
        self.zoom_level = self.zoom_level - zoom
        if self.zoom_level < 0.001:
            self.zoom_level = 0.001

    def zoomOut(self, zoom: float):
        self.zoom_level = self.zoom_level + zoom
        if self.zoom_level > 1:
            self.zoom_level = 1

    def reset(self):
        self.zoom_level = 1.0
        self.__forward_vector = Vector(self.__default_vector.end, self.__default_vector.begin)

    def refresh(self, display_w, display_h):
        # Zastosowanie perspektywy oraz zoom'u
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45*self.zoom_level, self.aspect, 0.1, 50.0)

        # Ruchy kamery w przestrzeni
        gluLookAt(self.__forward_vector.begin.x, self.__forward_vector.begin.y, self.__forward_vector.begin.z,
                  self.__forward_vector.end.x, self.__forward_vector.end.y, self.__forward_vector.end.z,
                  self.__up_vector.dx, self.__up_vector.dy, self.__up_vector.dz)
