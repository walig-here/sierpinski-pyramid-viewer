import itertools

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from light import *
from Shapes import *
from camera import Camera


# Mechanizm renderowania obiektów
class Renderer:
    def __init__(self, frame, backgorund_color: ColorRgb):
        # Stworzenie kamery
        self.viewer = Camera(
            frame,
            Vertex(0, 0, 0),
            Vertex(0, 0, 2)
        )

        # Lista kształtów do wyrenderowania
        self.shapes_to_render = []

        # Ustalenie koloru ramki (który ma ona po wyczyszczeniu jej bufora). Parametry:
        # * nasycenie czerwonym
        # * nasycenie zielonym
        # * nasycenie niebieskim
        # * przeźroczystość
        glClearColor(backgorund_color.red/255, backgorund_color.green/255, backgorund_color.blue/255, 1.0)

        # Włączenie bufora głębi
        glEnable(GL_DEPTH_TEST)

        # Definicja meteriału renderowanych obiektów
        self.material = Material(
            Light(ColorRgb(255, 255, 255), 1.0),    # kolor ambient
            Light(ColorRgb(255, 255, 255), 1.0),    # kolor diffuse
            Light(ColorRgb(255, 255, 255), 1.0),    # kolor specular
            50.0                                    # połyskliwość
        )

        # Włączenie oświetlenia
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)

        # Definicja źródła światła punktowego
        self.point_light = PointLight(
            Vertex(-0.5, 0.1, 0),
            GL_LIGHT1,
            Light(ColorRgb(255, 0, 0), 0.01),
            Light(ColorRgb(255, 0, 0), 0.8),
            Light(ColorRgb(255, 255, 255), 1.0),
            0,
            0.05,
            0.01
        )
        self.point_light.setEnabled(True)

        # Definicja źródła światała kierunkowego
        self.directional_light = DirectionalLight(
            Vector(Vertex(-1, 0, 0), Vertex(0, 0, 0)),      # biegnie w kierunku
            GL_LIGHT0,
            Light(ColorRgb(255, 255, 255), 1.0),                # barwa diffuse
            Light(ColorRgb(255, 255, 255), 0.01),            # barwa ambient
            Light(ColorRgb(255, 255, 255), 1.0)             # barwa specular
        )
        self.directional_light.setEnabled(True)

        # Czy renderować wektory normalne?
        self.render_normals = False

    def drawTriangle(self, triangle: Triangle):
        # Rozpoczęce rysowania trójkąta
        glBegin(GL_TRIANGLES)
        for (vertex, normal) in itertools.zip_longest(triangle.verticies, triangle.normals):
            glNormal3f(normal.dx, normal.dy, normal.dz)
            glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

        if self.render_normals:
            glBegin(GL_LINES)
            for normal in triangle.normals:
                glVertex3f(normal.begin.x, normal.begin.y, normal.begin.z)
                glVertex3f(normal.end.x, normal.end.y, normal.end.z)
            glEnd()

    def drawPoint(self, vertex: Vertex):
        glBegin(GL_POINTS)
        glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

    def drawLine(self, line : Line):
        glBegin(GL_LINES)
        for vertex in line.verticies:
            glVertex3f(vertex.dx, vertex.dy, vertex.dz)
        glEnd()

    def drawPyramid(self, pyramid: Pyramid):
        for triangle in pyramid.triangles:
            self.drawTriangle(triangle)

    def drawLevel2Tetrix(self, tetrix: Level2Terix):
        # Piramida składowa 1
        if isinstance(tetrix.subpyramid_1, Pyramid):
            self.drawPyramid(tetrix.subpyramid_1)
        else:
            self.drawLevel2Tetrix(tetrix.subpyramid_1)

        # Piramida składowa 2
        if isinstance(tetrix.subpyramid_2, Pyramid):
            self.drawPyramid(tetrix.subpyramid_2)
        else:
            self.drawLevel2Tetrix(tetrix.subpyramid_2)

        # Piramida składowa 3
        if isinstance(tetrix.subpyramid_3, Pyramid):
            self.drawPyramid(tetrix.subpyramid_3)
        else:
            self.drawLevel2Tetrix(tetrix.subpyramid_3)

        # Piramida składowa 4
        if isinstance(tetrix.subpyramid_4, Pyramid):
            self.drawPyramid(tetrix.subpyramid_4)
        else:
            self.drawLevel2Tetrix(tetrix.subpyramid_4)

    def render(self, time):
        # Wyczyszczenie buforów kolorów oraz głębi
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Ruch kamery
        self.viewer.refresh(pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height())

        # Ruch obiektu
        glMatrixMode(GL_MODELVIEW)
        glRotatef(0.5, 0, 1, 0)  # Obracanie obiektu

        # Renderowanie zleconych primitywów
        for shape in self.shapes_to_render:
            if isinstance(shape, Triangle):
                self.drawTriangle(shape)
            elif isinstance(shape, Vertex):
                self.drawPoint(shape)
            elif isinstance(shape, Line):
                self.drawLine(shape)
            elif isinstance(shape, Pyramid):
                self.drawPyramid(shape)
            elif isinstance(shape, Level2Terix):
                self.drawLevel2Tetrix(shape)
        self.shapes_to_render.clear()



        # Wyświetlenie ramki
        glFlush()
        pygame.display.flip()
