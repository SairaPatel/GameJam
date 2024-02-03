import math
import random

import pygame, sys
from pygame.locals import *


# ROCKET CLASS
class Rocket(pygame.sprite.Sprite):
    def __init__(self, colour, win_width, win_height, speed):
          
        super().__init__()

        #dimensions
        self.win_width = win_width
        self.win_height = win_height
        #self.width = math.floor(win_width*0.1)

        
        # set surface
        self.image = pygame.image.load("images/RocketWhite.png").convert_alpha()
        self.rect = self.image.get_rect()


        self.width = self.rect.width
        self.height = self.rect.height

        self.image = pygame.transform.scale(self.image, (math.floor(self.width *  3), math.floor(self.height*3)))

        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        
        self.rect.x = math.floor(win_width/2) - math.floor(self.width/2)
        self.rect.y = math.floor(win_height*0.75)


        # set game vars
        self.speed = speed

        self.shielded = False 
        

    def updatePos(self, keys):
        # update rocket x pos based on keys pressed
        if keys[pygame.K_LEFT]:
            if self.rect.x - self.speed > 0:
                self.rect.x -= self.speed
            
        if keys[pygame.K_RIGHT]:
            if self.rect.x + self.speed + self.width < self.win_width:
                self.rect.x += self.speed
     
    def powerUp(self, power):
        if power == "grow":
            self.image = pygame.transform.scale(self.image, (math.floor(self.width *1.2), math.floor(self.height*1.2)))
        elif power == "shrink":
            self.image = pygame.transform.scale(self.image, (math.floor(self.width /1.2), math.floor(self.height/1.2)))

        elif power == "shield":
            self.shielded = True




