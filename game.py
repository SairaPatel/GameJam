import math
import random

import pygame, sys
from pygame.locals import *

class Game():
    def __init__(self, win_width):
        # window
        self.width = win_width
        self.height = math.floor(win_width*1.5)

        # clock
        self.clock = pygame.time.Clock()
        self.fps = 30


        # colours
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        self.back_colour = pygame.Color(0, 0, 40)
        self.rocket_colour = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)

        # font
        self.font = pygame.font.SysFont("Impact", 30 )

        # game vars
        self.status = "menu"
        self.planet_num = 1
        self.score = 0


        # planet image list
        self.planet_images = ["images/BluePlanet.png", "images/RedPlanet.png", "images/PurplePlanet.png"]

        
        

    def update(self):

        # update display and tick clock
        pygame.display.update()
        self.clock.tick(self.fps)



