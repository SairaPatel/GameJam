import math

import pygame, sys
from pygame.locals import *


# ROCKET CLASS
class Rocket(pygame.sprite.Sprite):
     def __init__(self, colour, width, centre_x, y):
          
          super().__init__()

          # set surface
          self.image = pygame.Surface([width, width*2])
          self.image.fill(colour)
          self.rect = self.image.get_rect()
          self.rect.x = centre_x - math.floor(width/2)
          self.rect.y = y
