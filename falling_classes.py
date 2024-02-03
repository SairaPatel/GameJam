import math
import random

from game import Game
import pygame, sys
from pygame.locals import *


class Star(pygame.sprite.Sprite):
    def __init__(self, colour, win_width, win_height):
          
        super().__init__()
        self.win_width = win_width
        self.win_height = win_height

        self.width = random.randrange(3,8,2)
        self.height = self.width

        # set surface
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        # set background transparent
        self.image.fill(pygame.Color(0,0,0))
        self.image.set_colorkey(pygame.Color(0,0,0))

        # draw star lines
        if random.randint(0, 3) >= 1:
            # cross
            pygame.draw.line(self.image, colour, (self.rect.centerx, 0), (self.rect.centerx, self.height))
            pygame.draw.line(self.image, colour, (0, self.rect.centery), (self.width,self.rect.centery))
        else:
            # dot
            pygame.draw.line(self.image, colour, self.rect.center, self.rect.center)
          
        self.setPos()


    def setPos(self):
        # set position to random x and random y
        self.rect.x = random.randint(0, self.win_width)
        self.rect.y = random.randint(0, self.win_height)

    def updatePos(self, speed):
        # increment y or reset y and x pos if y goes of the screen
        if self.rect.y < self.win_height + self.height:
            self.rect.y += speed
        else:
            self.rect.x = random.randint(0, self.win_width)
            self.rect.y = -1 * self.height


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, colour, win_width, win_height):
          
        super().__init__()
        self.win_width = win_width
        self.win_height = win_height

        
        # set surface
        self.image = pygame.image.load("asteroid.png").convert_alpha()
        self.rect = self.image.get_rect()


        self.width = self.rect.width
        self.height = self.rect.height

        self.image = pygame.transform.scale(self.image, (math.floor(self.width * 0.5), math.floor(self.height*0.5)))

        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.setPos()

    def setPos(self):
         self.rect.x = random.randint(0, self.win_width - self.width)
         self.rect.y = random.randint(-2 * self.win_height, math.floor(-0.5 * self.win_height))
        
    def updatePos(self, speed):
        # increment y or reset y and x pos if y goes of the screen
        if self.rect.y < self.win_height + self.height:
            self.rect.y += speed
        else:
            self.setPos()


class Planet(pygame.sprite.Sprite):
    def __init__(self, colour, win_width, win_height, planet_num):
          
        super().__init__()
        self.win_width = win_width
        self.win_height = win_height

        self.width = 30
        self.height = self.width

        # set surface
        self.image = pygame.image.load("images/Earth.png").convert_alpha()
        self.rect = self.image.get_rect()


        self.width = self.rect.width
        self.height = self.rect.height

        self.image = pygame.transform.scale(self.image, (math.floor(self.width * 2), math.floor(self.height*2)))

        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        # set surface


        self.rect = self.image.get_rect()
        self.radius = math.floor(self.width/2)


        self.setPos(planet_num)

    def setPos(self, planet_num):
        self.rect.x = random.randint(0, self.win_width - self.radius)
        self.rect.y = math.floor(-4 * planet_num * (self.height- self.radius))
            
        

    # updates planet pos and returns true if planet has passed bottom (returns false otherwise)
    def updatePos(self, speed, planet_num):
        # increment y or reset y and x pos if y goes of the screen
        if self.rect.y < self.win_height + self.height:
            self.rect.y += math.floor(speed* 0.8)

            return False
        else:
            self.setPos(planet_num)

            return True

            

  
