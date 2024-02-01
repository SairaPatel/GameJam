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
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
     
        self.score += self.speed


    
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
        self.rect.x = random.randint(0, self.win_width)
        self.rect.y = random.randint(0, self.win_height)

    def updatePos(self, speed):
        if self.rect.y < self.win_height + self.height:
            self.rect.y += speed
        else:
            self.rect.x = random.randint(0, self.win_width)
            self.rect.y = -1 * self.height

   

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

        #font
        self.font = pygame.font.SysFont("Impact", 30 )

        # game vars
        self.status = "menu"
        self.planet_num = 1
        

    def update(self):

        # update display and tick clock
        pygame.display.update()
        self.clock.tick(self.fps)


