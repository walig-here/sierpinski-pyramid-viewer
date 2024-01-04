from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from Shapes import ColorRgb, Triangle, Vertex


class Renderer:
    def __init__(self, frame, backgorund_color: ColorRgb):
        # Lista kształtów do wyrenderowania
        self.shapes_to_render = []

        # Ustalenie koloru ramki (który ma ona po wyczyszczeniu jej bufora). Parametry:
        # * nasycenie czerwonym
        # * nasycenie zielonym
        # * nasycenie niebieskim
        # * przeźroczystość
        glClearColor(backgorund_color.red/255, backgorund_color.green/255, backgorund_color.blue/255, 1.0)

    def drawTriangle(self, triangle : Triangle):
        # Rozpoczęce rysowania trójkąta
        glBegin(GL_TRIANGLES)
        for vertex in triangle.verticies:
            glColor3ub(vertex.color.red, vertex.color.green, vertex.color.blue)
            glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

    def render(self, time):
        # Wyczyszczenie bufora ramki
        glClear(GL_COLOR_BUFFER_BIT)

        for shape in self.shapes_to_render:
            if isinstance(shape, Triangle):
                self.drawTriangle(shape)
        self.shapes_to_render.clear()

        # Wyświetlenie ramki
        glFlush()
        pygame.display.flip()
