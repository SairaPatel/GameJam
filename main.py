import math

import pygame, sys
from pygame.locals import *

from rocket import *



pygame.init()

def draw_text(x, y, string, col, size, window):
     font = pygame.font.SysFont("Impact", size )
     text = font.render(string, True, col)
     textbox = text.get_rect()
     textbox.center = (x, y)
     window.blit(text, textbox)

     return textbox

# COLOURS
white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 40)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)


# SET WINDOW
WIDTH = 400
HEIGHT = math.floor(WIDTH*1.5)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")


# SET CLOCK
clock = pygame.time.Clock()
fps = 30



# SPRITES

# overall sprite group
sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()

# stars
for i in range(50):
    star = Star(white, WIDTH, HEIGHT)
    stars.add(star)

sprites.add(stars)# rocket
rocket = Rocket(red, math.floor(WIDTH/10), math.floor(WIDTH/2), math.floor(HEIGHT*0.75))
sprites.add(rocket)


    
# MAIN GAME LOOP
run = True
while run:
    # clock
    clock.tick(fps)
    
    # update display
    win.fill(blue)

     
    # EVENTS
    for event in pygame.event.get():
        # QUIT GAME
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # KEYS PRESSED
    keys = pygame.key.get_pressed();
    rocket.updatePos(keys[pygame.K_LEFT], keys[pygame.K_RIGHT])
    
    # update stars - CHANGE THIS: create a Stars class, to hold a list of stars and automatically update all their pos with one method call
    for s in stars.sprites():
        s.updatePos(rocket.speed)


    
    # draw score
    rocket.score += rocket.speed

    #draw_text(math.floor(WIDTH/2), math.floor(HEIGHT*0.2), str(rocket.score), white, 30, win)
    font = pygame.font.SysFont("Impact", 30 )
    text = font.render(str(rocket.score), True, white)
    textbox = text.get_rect()
    textbox.center = (100, 100)
    win.blit(text, textbox)

    # update win
    sprites.draw(win)     
    pygame.display.update()


# IMPLEMENT - when rocket is flying/playing game, 
def run(win):
    hi = 2

# IMPLEMENT - called after rocket crashes: 
def checkpoint(win):
    hi = 2
# IMPLEMENT - press start, have stars in background
def main_menu(win):
    hi = 2

