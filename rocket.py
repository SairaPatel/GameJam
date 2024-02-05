import math
import random

import pygame, sys
from pygame.locals import *


# ROCKET CLASS
class Rocket(pygame.sprite.Sprite):
    def __init__(self, imgName, win_width, win_height, speed):
          
        super().__init__()

        #dimensions
        self.win_width = win_width
        self.win_height = win_height
        #self.width = math.floor(win_width*0.1)

        
        # set surface
        self.imageName = imgName
        self.setImage()

        # set game vars
        self.speed = speed

        self.shielded = False 
        
    def setImage(self):

        self.image = pygame.image.load(self.imageName).convert_alpha()
        self.rect = self.image.get_rect()


        self.width = self.rect.width
        self.height = self.rect.height

        widthToHeight = self.height/self.width
        self.image = pygame.transform.scale(self.image, (math.floor(self.win_width/10), math.floor(self.win_width/10 * widthToHeight)))

        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        
        self.rect.bottomleft = (0, math.floor(self.win_height*0.7))
        self.rect.x = math.floor(self.win_width/2) - math.floor(self.width/2)

    def updatePos(self, keys):
        # update rocket x pos based on keys pressed
        if keys[pygame.K_LEFT]:
            if self.rect.x - self.speed > 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = 0
            
        if keys[pygame.K_RIGHT]:
            if self.rect.x + self.speed + self.width < self.win_width:
                self.rect.x += self.speed
            else:
                self.rect.x = self.win_width - self.width
     
    def powerUp(self, power):
        

        # powerup
        if power == "grow":
            
            self.image = pygame.image.load(self.imageName).convert_alpha()
            self.image = pygame.transform.scale(self.image, (math.floor(self.image.get_rect().width *  3), math.floor(self.image.get_rect().height*3)))
            self.image = pygame.transform.scale(self.image, (math.floor(self.width *1.1), math.floor(self.height*1.1)))

        elif power == "shrink":
            self.image = pygame.image.load(self.imageName).convert_alpha()
            self.image = pygame.transform.scale(self.image, (math.floor(self.image.get_rect().width *  3), math.floor(self.image.get_rect().height*3)))
            self.image = pygame.transform.scale(self.image, (math.floor(self.width /1.1), math.floor(self.height/1.1)))

        elif power == "shield":
            self.shielded = True

        # update dimensions
        self.width = self.image.get_rect().width
        self.height =self.image.get_rect().height





