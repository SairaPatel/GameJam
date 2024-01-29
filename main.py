import math

import pygame, sys
from pygame.locals import *

from classes import *

pygame.init()

# SET WINDOW
WIDTH = 400
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")


# COLOURS
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 40)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)


# SET CLOCK
clock = pygame.time.Clock()
fps = 30



# SPRITES

# rocket
rocket = Rocket(red, math.floor(WIDTH/10), math.floor(WIDTH/2), math.floor(HEIGHT/2))


# overall sprite group
sprites = pygame.sprite.Group()
sprites.add(rocket)

# MAIN GAME LOOP
run = True
while run:
     # clock
     clock.tick(fps)

     
     # EVENTS
     for event in pygame.event.get():
          # QUIT GAME
          if event.type == QUIT:
               pygame.quit()
               sys.exit()

          

     # update display
     win.fill(blue)
     sprites.draw(win)     
     pygame.display.update()

