import math

import pygame, sys
from pygame.locals import *

from rocket import *



pygame.init()


# SET GAME CONTROLLER
game = Game(400)


win = pygame.display.set_mode((game.width, game.height))
pygame.display.set_caption("Space Game")


# SPRITES

# overall sprite group
sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()

# stars
for i in range(50):
    star = Star(white, WIDTH, HEIGHT)
    stars.add(star)

sprites.add(stars)

# rocket
rocket = Rocket(red, math.floor(WIDTH/10), math.floor(WIDTH/2), math.floor(HEIGHT*0.75))
sprites.add(rocket)


    
# MAIN GAME LOOP
run = True
while run:
    
    
    # update display
    win.fill(game.back_colour)

     
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


    
    # increase score
    rocket.score += rocket.speed

    # draw score
    text = game.font.render(str(rocket.score), True, game.white)
    textbox = text.get_rect()
    textbox.topleft = (10,10)
    win.blit(text, textbox)

    # update
    sprites.draw(win)  
    game.update()


# IMPLEMENT - when rocket is flying/playing game, 
def run(win):
    hi = 2

# IMPLEMENT - called after rocket crashes: 
def checkpoint(win):
    hi = 2
# IMPLEMENT - press start, have stars in background
def main_menu(win):
    hi = 2

