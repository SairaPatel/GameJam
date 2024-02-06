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
        self.fps = 45


        # colours
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        self.back_colour = pygame.Color(0, 0, 40)
        self.rocket_colour = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.red = pygame.Color(230,15,15)
        self.blue =pygame.Color(15,120,230)



        self.font = self.getFont(30)
        # game vars
        self.status = "menu"
        self.planet_num = 1
        self.score = 0


        # planet image list
        self.planet_images = []
        for i in range(1, 17):
            self.planet_images.append("images/Planets/planet-" + str(i) + ".png")


        # rocket image list
        self.rocket_num = 0
        self.rocket_images = []
        for i in range(1,4):
            self.rocket_images.append("images/Spaceships/spaceship-" + str(i) + ".png")
        
    def getFont(self, size):
        return pygame.font.SysFont("Impact", size)

    def update(self):

        # update display and tick clock
        pygame.display.update()
        self.clock.tick(self.fps)

    def getRocketImg(self):
        self.rocket_num = self.rocket_num % len(self.rocket_images)
        return self.rocket_images[self.rocket_num]



