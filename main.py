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
 
# prototype planet CHANGE THIS TO ACTUAL PLANET CLASS OBJ
planet = Star(game.green, game.width, game.height)


# stars
stars = pygame.sprite.Group()
for i in range(50):
    star = Star(game.white, game.width, game.height)
    stars.add(star)


# prototype asteroids CHANGE THIS TO ACTUAL ASTEROID CLASS OBJS
asteroids = pygame.sprite.Group()
for i in range(5):
    ast = Star(game.rocket_colour, game.width, game.height)
    asteroids.add(ast)



# overall sprite group
sprites = pygame.sprite.Group()
sprites.add(rocket)
sprites.add(planet)
sprites.add(stars)
sprites.add(asteroids)

    
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
    
#   MAYBE HAVE A SINGLE CLASS: FallingObject - And have Star, Asteroid and Planet inherit it.?
#	And then (instead of having 3 dif for loops/lines to call updatePos for star, asteroid and planet in the main loop),
#	just add them all to a single sprite group e.g. (Falling) and loop through all sprites in Falling.sprites() to updatePos for all of them

    # update stars - 
    for s in stars.sprites():
        s.updatePos(rocket.speed)
    
    # update asteroids
    for a in asteroids.sprites():
        a.updatePos(rocket.speed)

    planet.updatePos(rocket.speed)
    
    # rocket and asteroid collision
    if len(pygame.sprite.spritecollide(rocket, asteroids, True)) > 0:
        # below is temporary code so we can see that the asteroid collision code is working:
        # change this so that the game ends/checkpoint page shows (rather than displaying COLLISION text)
        text = game.font.render("COLLISION", True, game.white)
        textbox = text.get_rect()
        textbox.topleft = (200,10)
        win.blit(text, textbox)

    # update planet num THIS PROBS NEEDS CHANGING? ITS NOT EXACT: MAYBE THIS CODE COULD GO INSIDE THE PLANET CLASS METHOD UpdatePos()
    if planet.rect.y > game.height:
        game.planet_num += 1
        rocket.speed = 5 + game.planet_num/2 # REMOVE THE /2 ONCE THIS IS WORKING PROPERLY

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

