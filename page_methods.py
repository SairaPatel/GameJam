import math
import pygame, sys
from pygame.locals import *

from rocket  import Rocket
from game import Game
from falling_classes import *



#when rocket is flying/playing game, 
def run(win, game):
    
    # SPRITES

    # rocket
    rocket = Rocket(game.rocket_colour, game.width, game.height)
 
    # prototype planet
    planet = Planet(game.green, game.width, game.height)

    # stars
    stars = pygame.sprite.Group()
    for i in range(50):
        star = Star(game.white, game.width, game.height)
        stars.add(star)

    # asteroids
    asteroids = pygame.sprite.Group()
    for i in range(5):
        ast = Asteroid(game.rocket_colour, game.width, game.height)
        asteroids.add(ast)

    # overall sprite group
    sprites = pygame.sprite.Group()
    sprites.add(stars)
    sprites.add(planet)
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

        # UPDATE ROCKET BASED ON KEYS PRESSED
        rocket.updatePos(pygame.key.get_pressed())
    
    #   MAYBE HAVE A SINGLE CLASS: FallingObject - And have Star, Asteroid and Planet inherit it.?
    #	And then (instead of having 3 dif for loops/lines to call updatePos for star, asteroid and planet in the main loop),
    #	just add them all to a single sprite group e.g. (Falling) and loop through all sprites in Falling.sprites() to updatePos for all of them

        # update stars
        for s in stars.sprites():
            s.updatePos(rocket.speed)
    
        # update asteroids
        for a in asteroids.sprites():
            a.updatePos(rocket.speed)

        # update planet pos and planet num
        if planet.updatePos(rocket.speed):
            game.planet_num += 1
            rocket.speed = 5 + game.planet_num
    
        # rocket and asteroid collision
        if len(pygame.sprite.spritecollide(rocket, asteroids, True)) > 0:
            # collision CHANGE THIS (right now a collision goes to main menu but it should actually go to checkpoint)
            game.status = "menu"
            return game
        
        # draw score # AND TEMPORARILY THE PLANET NUM BUT WE WILL REMOVE THAT LATER
        text = game.font.render(str(rocket.score) + "m, PLANET: " + str(game.planet_num), True, game.white)
        textbox = text.get_rect()
        textbox.topleft = (10,10)
        win.blit(text, textbox)

        # update
        sprites.draw(win)  
        game.update()




# IMPLEMENT - called after rocket crashes: 
def checkpoint(win):
    hi = 2




# press start, have stars in background
def menu(win, game):

    # MAIN MENU LOOP
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

            # ANY KEY PRESSED
            if event.type == pygame.KEYDOWN:
                game.status = "game"
                return game


        # draw start message
        text = game.font.render("PRESS ANY KEY TO START", True, game.white)
        textbox = text.get_rect()
        textbox.topleft = (10,10)
        win.blit(text, textbox)

        # update 
        game.update()
