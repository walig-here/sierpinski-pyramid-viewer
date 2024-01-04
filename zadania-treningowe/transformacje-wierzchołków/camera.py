from Shapes import Vertex, ColorRgb
import math

from OpenGL.GL import *
from OpenGL.GLU import *

class Camera:
    def __init__(self,
                 looking_at_point: Vertex,
                 distance: float,
                 elevation_angle_deg: float,
                 asimuth_angle_deg: float):
        self.__looking_at = looking_at_point
        self.__up_vector = Vertex(ColorRgb(0,0,0), 0, 1, 0)
        self.__elevation = elevation_angle_deg * 2 * math.pi / 360
        self.__asimuth = asimuth_angle_deg * 2 * math.pi / 360
        self.__position = Vertex(ColorRgb(0, 0, 0), 0, 0, 0)
        self.__calculatePosition(distance)
        self.zoom_level = 1.0

    def __getDistance(self):
        return math.sqrt(
            (self.__looking_at.x - self.__position.x) ** 2 +
            (self.__looking_at.y - self.__position.y) ** 2 +
            (self.__looking_at.z - self.__position.z) ** 2
        )

    def __calculatePosition(self, distance: float):
        self.__position.x = distance * math.cos(self.__asimuth) * math.cos(self.__elevation)
        self.__position.y = distance * math.sin(self.__elevation)
        self.__position.z = distance * math.sin(self.__asimuth) * math.cos(self.__elevation)

    def rotateRight(self, angle_deg: float):
        angle_deg = math.fabs(angle_deg)
        self.__asimuth = self.__asimuth + (angle_deg * 2 * math.pi / 360)
        while self.__asimuth >= 2*math.pi:
            self.__asimuth = self.__asimuth - 2*math.pi

    def rotateLeft(self, angle_deg: float):
        angle_deg = math.fabs(angle_deg)
        self.__asimuth = self.__asimuth - (angle_deg * 2 * math.pi / 360)
        while self.__asimuth >= 2*math.pi:
            self.__asimuth = self.__asimuth - 2*math.pi

    def moveUpwards(self, angle_deg: float):
        angle_deg = math.fabs(angle_deg)
        self.__elevation = self.__elevation + (angle_deg * 2 * math.pi / 360)
        while self.__elevation >= 2*math.pi:
            self.__elevation = self.__elevation - 2*math.pi

    def moveDownwards(self, angle_deg: float):
        angle_deg = math.fabs(angle_deg)
        self.__elevation = self.__elevation - (angle_deg * 2 * math.pi / 360)
        while self.__elevation >= 2*math.pi:
            self.__elevation = self.__elevation - 2*math.pi

    def zoomIn(self, zoom: float):
        self.zoom_level = self.zoom_level + zoom
        if self.zoom_level > 2:
            self.zoom_level = 2

    def zoomOut(self, zoom: float):
        self.zoom_level = self.zoom_level - zoom
        if self.zoom_level < 0.1:
            self.zoom_level = 0.1

    def refresh(self, display_w, display_h):
        glLoadIdentity()
        self.__calculatePosition(self.__getDistance())
        if math.pi/2 <= self.__elevation <= math.pi*3/2:
            self.__up_vector.y = -1
        else:
            self.__up_vector.y = 1
        gluLookAt(self.__position.x, self.__position.y, self.__position.z,
                  self.__looking_at.x, self.__looking_at.y, self.__looking_at.z,
                  self.__up_vector.x, self.__up_vector.y, self.__up_vector.z)

        glScalef(self.zoom_level, self.zoom_level, self.zoom_level)
