import enum
import math

import pygame
from pygame.locals import *
from camera import Camera
from renderer import Renderer

class EventHandler:
    def __init__(self, parent_app, renderer: Renderer):
        self.__renderer = renderer
        self.__application = parent_app

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__application.shutdown()

        degrees_per_frame = 1
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            self.__renderer.viewer.zoomIn(0.01)
        elif keys_pressed[pygame.K_DOWN]:
            self.__renderer.viewer.zoomOut(0.01)