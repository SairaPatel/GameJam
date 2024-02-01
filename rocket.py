import math
import random

import pygame, sys
from pygame.locals import *


# ROCKET CLASS
class Rocket(pygame.sprite.Sprite):
    def __init__(self, colour, width, centre_x, centre_y):
          
        super().__init__()

        # set surface
        self.image = pygame.Surface([width, width*2])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = centre_x - math.floor(width/2)
        self.rect.y = centre_y


        # set game vars
        self.speed = 4
        self.score = 0
        

    def updatePos(self, keys):
        # update rocket x pos based on keys pressed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
     
        # update rocket score always
        self.score += self.speed


   