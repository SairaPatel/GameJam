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
    rocket = Rocket(game.getRocketImg(), game.width, game.height, game.planet_num + 4)
 
    # prototype planet
    planet = Planet(game.planet_images, game.width, game.height, game.planet_num)

    # stars
    stars = pygame.sprite.Group()
    for i in range(100):
        star = Star(game.width, game.height)
        stars.add(star)

    # asteroids
    asteroids = pygame.sprite.Group()
    for i in range(4):
        ast = Asteroid(game.rocket_colour, game.width, game.height)
        asteroids.add(ast)

    # big planet
    bigPlanetGroup = pygame.sprite.GroupSingle()
    bigPlanetGroup.add(BigPlanet(game.width, game.height, game.planet_images, game.planet_num))

    #  power up
    powerUpGroup = pygame.sprite.GroupSingle()
    powerUpGroup.add(PowerUp(game.width, game.height))

    # shield corner icon
    shieldIcon = pygame.image.load("images/Powerups/shield.png").convert_alpha()
    widthToHeight = shieldIcon.get_rect().height/shieldIcon.get_rect().width
    shieldIcon = pygame.transform.scale(shieldIcon, (math.floor(game.width/20), math.floor(game.width/20 * widthToHeight)))

    # overall sprite group
    sprites = pygame.sprite.Group()
    sprites.add(planet)
    sprites.add(stars)
    sprites.add(powerUpGroup)
    sprites.add(bigPlanetGroup)
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
        i = 0
        while i < len(asteroids.sprites()):

            a = asteroids.sprites()[i]
            i += 1

            # update pos
            a.updatePos(rocket.speed)

             # remove overlapping asteroids
            asteroidsWithoutA = asteroids.copy() 
            asteroidsWithoutA.remove(a)

            # get and remove overlapping asteroids
            overlapping = pygame.sprite.spritecollide(a, asteroidsWithoutA, True)
            asteroids.remove(overlapping)

            # add new asteroid
            for i in range(len(overlapping)):
                newA = Asteroid(game.rocket_colour, game.width, game.height)
                asteroids.add(newA)
                sprites.add(newA)

        # update big planet
        if bigPlanetGroup.sprite is not None:
            if bigPlanetGroup.sprite.updatePos(rocket.speed):
                bigPlanetGroup.sprite.kill()
           

        # update planet pos and planet num
        if planet.updatePos(rocket.speed, game.planet_num):
            game.planet_num += 1
            rocket.speed = 5 + game.planet_num
            planet.setImage(game.planet_num)
    
        # rocket and asteroid collision
        i = 0
        while i < len(asteroids.sprites()):
            if pygame.sprite.collide_mask(rocket, asteroids.sprites()[i]) is not None:
                if not rocket.shielded:
                    game.status = "checkpoint"
                    return game
                else:
                    rocket.shielded = False
                    asteroids.sprites()[i].setPos()
            i += 1

        # update powerup pos
        powerUpGroup.sprite.updatePos(rocket.speed)

        # power up and rocket collision
        if pygame.sprite.spritecollide(rocket, powerUpGroup, False):
            rocket.powerUp(powerUpGroup.sprite.power)


            # generate new powerup
            powerUpGroup.sprite.setPower()
            powerUpGroup.sprite.setPos()
           
        # display shield corner icon
        if rocket.shielded:
            win.blit(shieldIcon, (5, game.height - shieldIcon.get_rect().height - 5))
        
        # update score
        game.score += rocket.speed

        # draw sprites
        sprites.draw(win)  


        # draw score and planet num        
        text = game.font.render(str(game.score) + "m", True, game.white)
        textbox = text.get_rect()
        textbox.topleft = (10,10)
        win.blit(text, textbox)

        text = game.font.render("PLANETS: " + str(game.planet_num), True, game.white)
        textbox = text.get_rect()
        textbox.topright = (game.width - 10, 10)
        win.blit(text, textbox)

        # update
        game.update()




# IMPLEMENT - called after rocket crashes: 
def checkpoint(win, game):

      # sprite group
    sprites = pygame.sprite.Group()

    # stars
    stars = pygame.sprite.Group()
    for i in range(100):
        star = Star( game.width, game.height)
        sprites.add(star)


     # MAIN MENU LOOP
    run = True
    while run:
    
        # update display
        win.fill(game.back_colour)
        sprites.draw(win)

        # EVENTS
        for event in pygame.event.get():
            # QUIT GAME
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # ANY KEY PRESSED
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.status = "menu"
                    return Game(game.width)

                elif event.key == pygame.K_RIGHT:
                    game.status = "game"
                    return game


        # draw title
        text = game.getFont(60).render("CHECKPOINT", True, game.white)
        textbox = text.get_rect()
        textbox.centerx = math.floor(game.width/2)
        textbox.centery = math.floor(game.height*0.2)
        win.blit(text, textbox)


        # update 
        game.update()




# press start, have stars in background
def menu(win, game):


     # sprite group
    sprites = pygame.sprite.Group()

    # stars
    stars = pygame.sprite.Group()
    for i in range(100):
        star = Star( game.width, game.height)
        sprites.add(star)

    # planet
    sprites.add(BigPlanet(game.width, game.height, game.planet_images, game.planet_num))

    # rocket
    rocket = Rocket(game.getRocketImg(), game.width, game.height, 0)
    sprites.add(rocket)



    # MAIN MENU LOOP
    run = True
    while run:
    
        # update display
        win.fill(game.back_colour)
        sprites.draw(win)

        # EVENTS
        for event in pygame.event.get():
            # QUIT GAME
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # ANY KEY PRESSED
            if event.type == pygame.KEYDOWN:

                # update rocket image
                if event.key == K_LEFT:
                    game.rocket_num +=  len(game.rocket_images) -1 
                    rocket.imageName = game.getRocketImg()
                    print(game.rocket_num)
                    rocket.setImage()
                
                if event.key == K_RIGHT:
                    game.rocket_num += 1
                    rocket.imageName = game.getRocketImg()
                    rocket.setImage()

                # start game
                elif event.key == K_SPACE:
                    game.status = "game"
                    return game
            


        # draw title
        text = game.getFont(60).render("MAIN MENU", True, game.white)
        textbox = text.get_rect()
        textbox.centerx = math.floor(game.width/2)
        textbox.centery = math.floor(game.height*0.2)
        win.blit(text, textbox)

        # draw start message
        text = game.getFont(20).render("Press SPACEBAR to start", True, game.white)
        textbox = text.get_rect()
        textbox.centery = math.floor(game.height*0.5)
        textbox.centerx = math.floor(game.width/2)
        win.blit(text, textbox)

         # draw left right arrow message
        text = game.getFont(15).render("Use arrow keys to change spaceship", True, game.white)
        textbox = text.get_rect()
        textbox.bottomleft = (0, math.floor(game.height*0.9))
        textbox.centerx = math.floor(game.width/2)
        win.blit(text, textbox)


        # update 
        game.update()

