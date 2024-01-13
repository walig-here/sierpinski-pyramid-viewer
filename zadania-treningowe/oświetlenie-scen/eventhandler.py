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
        if keys_pressed[pygame.K_w]:
            self.__renderer.viewer.moveForward(0.01)
        elif keys_pressed[pygame.K_s]:
            self.__renderer.viewer.moveBackward(0.01)
        elif keys_pressed[pygame.K_d]:
            self.__renderer.viewer.moveRight(0.01)
        elif keys_pressed[pygame.K_a]:
            self.__renderer.viewer.moveLeft(0.01)
        elif keys_pressed[pygame.K_RIGHT]:
            self.__renderer.viewer.rotateRight(0.01)
        elif keys_pressed[pygame.K_LEFT]:
            self.__renderer.viewer.rotateLeft(0.01)
        elif keys_pressed[pygame.K_LSHIFT]:
            self.__renderer.viewer.zoomIn(0.01)
        elif keys_pressed[pygame.K_LCTRL]:
            self.__renderer.viewer.zoomOut(0.01)
        elif keys_pressed[pygame.K_SPACE]:
            self.__renderer.viewer.reset()
