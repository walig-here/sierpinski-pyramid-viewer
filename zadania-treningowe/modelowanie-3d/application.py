
from renderer import Renderer
from Shapes import ColorRgb, Triangle, Vertex, Line
from eventhandler import EventHandler
import pygame
from pygame.locals import *
import math


class Application:
    def __init__(self, name, scr_w, scr_h):
        pygame.init()
        pygame.display.set_caption(name)

        self.__frame = pygame.display.set_mode((scr_w, scr_h), DOUBLEBUF|OPENGL)
        self.__renderer = Renderer(self.__frame, ColorRgb(0, 0, 0))

        self.__event_handler = EventHandler(self, self.__renderer)
        self.__clock = pygame.time.Clock()

    def shutdown(self):
        pygame.quit()
        quit(0)

    def run(self):
        while True:
            # Obsługa zdarzeń
            self.__event_handler.handleEvents()

            # Wierzchołeki
            v = [
                Vertex(ColorRgb(255, 255, 255), 0.75, 0.00, 0.00),
                Vertex(ColorRgb(255, 255, 255), 0.00, 0.00, -0.75),
                Vertex(ColorRgb(255, 255, 255), 0.00, 0.75, 0.00),
                Vertex(ColorRgb(255, 255, 255), 0.75, 0.75, -0.75)
            ]

            self.__renderer.shapes_to_render.append(Triangle([v[0], v[2], v[3]]))
            self.__renderer.shapes_to_render.append(Triangle([v[0], v[1], v[2]]))
            self.__renderer.shapes_to_render.append(Triangle([v[0], v[1], v[3]]))
            self.__renderer.shapes_to_render.append(Triangle([v[1], v[2], v[3]]))

            # Renderowanie
            self.__renderer.render(1)

            # limit do 60 fps
            # src: https://www.pygame.org/docs/
            self.__clock.tick(60)
