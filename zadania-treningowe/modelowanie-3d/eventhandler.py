import enum
import pygame
from pygame.locals import *

class EventHandler:
    def __init__(self, parent_app, renderer):
        self.__renderer = renderer
        self.__application = parent_app

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__application.shutdown()
