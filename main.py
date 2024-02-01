import pygame, sys
from pygame.locals import *

from page_methods import *
from game import Game


pygame.init()


# SET GAME CONTROLLER
game = Game(400)

# CREATE PYGAME WINDOW
win = pygame.display.set_mode((game.width, game.height))
pygame.display.set_caption("Space Game")

# MAIN LOOP
while game.status != "end":

    if game.status == "menu":
        game = menu(win, game)

    elif game.status == "checkpoint":
        game = checkpoint(win, game)

    elif game.status == "game":
        game = run(win, game)