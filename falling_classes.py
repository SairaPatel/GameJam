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

        self.width = 50
        self.height = self.width

        # set surface
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        # set background transparent
        self.image.fill(pygame.Color(0,0,0))
        self.image.set_colorkey(pygame.Color(0,0,0))

        pygame.draw.circle(self.image, colour,self.rect.center, random.randint(5,15))
        self.setPos()

    def setPos(self):
        self.rect.x = random.randint(0, self.win_width)
        self.rect.y = random.randint(0, self.win_height *  0.25)
        
    def updatePos(self, speed):
        # increment y or reset y and x pos if y goes of the screen
        if self.rect.y < self.win_height + self.height:
            self.rect.y += speed
        else:
            self.rect.x = random.randint(0, self.win_width)
            self.rect.y = -1 * self.height


class Planet(pygame.sprite.Sprite):
    def __init__(self, colour, win_width, win_height):
          
        super().__init__()
        self.win_width = win_width
        self.win_height = win_height

        self.width = 100
        self.height = self.width

        # set surface
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()

        # set background transparent
        self.image.fill(pygame.Color(0,0,0))
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.radius = random.randint(20,40)

        pygame.draw.circle(self.image, colour,self.rect.center, self.radius)
        self.setPos()

    def setPos(self):
        self.rect.x = random.randint(0, self.win_width - self.radius)
        self.rect.y = random.randint(0, self.win_height - self.radius)
        

    # updates planet pos and returns true if planet has passed bottom (returns false otherwise)
    def updatePos(self, speed):
        # increment y or reset y and x pos if y goes of the screen
        if self.rect.y < self.win_height + self.height:
            self.rect.y += speed

            return False
        else:
            self.rect.x = random.randint(0, self.win_width - self.radius)
            self.rect.y = -1 * (self.height- self.radius)
            
            return True

            

  
