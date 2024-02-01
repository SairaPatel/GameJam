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

# rocket
rocket = Rocket(game.rocket_colour, math.floor(game.width/10), math.floor(game.width/2), math.floor(game.height*0.75))


# stars
stars = pygame.sprite.Group()
for i in range(50):
    star = Star(game.white, game.width, game.height)
    stars.add(star)


# prototype obstacles
asteroids = pygame.sprite.Group()
for i in range(5):
    ast = Star(game.rocket_colour, game.width, game.height)
    asteroids.add(ast)




# overall sprite group
sprites = pygame.sprite.Group()
sprites.add(stars)
sprites.add(asteroids)
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
    
    # update asteroids
    for a in asteroids.sprites():
        a.updatePos(rocket.speed)
    
    # rocket and asteroid collision
    if len(pygame.sprite.spritecollide(rocket, asteroids, True)) > 0:
        # below is temporary code so we can see that the asteroid collision code is working:
        # change this so that the game ends/checkpoint page shows (rather than displaying COLLISION text)
        text = game.font.render("COLLISION", True, game.white)
        textbox = text.get_rect()
        textbox.topleft = (200,10)
        win.blit(text, textbox)


    # draw score
    text = game.font.render(str(rocket.score) + "m, PLANET: " + str(game.planet_num), True, game.white)
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

