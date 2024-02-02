import math
import random

import pygame, sys
from pygame.locals import *


# ROCKET CLASS
class Rocket(pygame.sprite.Sprite):
    def __init__(self, colour, win_width, win_height):
          
        super().__init__()

        # dimensions
        self.win_width = win_width
        self.win_height = win_height
        self.width = math.floor(win_width*0.1)

        # set surface
        self.image = pygame.Surface([self.width, self.width*2])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = math.floor(win_width/2) - math.floor(self.width/2)
        self.rect.y = math.floor(win_height*0.75)


        # set game vars
        self.speed = 4
        self.score = 0
        

    def updatePos(self, keys):
        # update rocket x pos based on keys pressed
        if keys[pygame.K_LEFT]:
            if self.rect.x - self.speed > 0:
                self.rect.x -= self.speed
            
        if keys[pygame.K_RIGHT]:
            if self.rect.x + self.speed + self.width < self.win_width:
                self.rect.x += self.speed
     
        # update rocket score always
        self.score += self.speed


   