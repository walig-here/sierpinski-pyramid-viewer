
from renderer import Renderer
from Shapes import *
from colors import ColorRgb
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

    def run(self, tertrix_levels: int):
        while True:
            # Obsługa zdarzeń
            self.__event_handler.handleEvents()

            # Zlecenie renderowania piramidy Sierpińskiego
            pyramid = Level2Terix(Vertex(0, 0, 0), 1.25, tertrix_levels)
            self.__renderer.shapes_to_render.append(pyramid)
            self.__renderer.render(1)

            # limit do 60 fps
            # src: https://www.pygame.org/docs/
            self.__clock.tick(60)
