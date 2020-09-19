import pygame
from pathfinder import *

MENU_SIZE = 50
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH,WIDTH + MENU_SIZE))
pygame.display.set_caption("Pathfinder")
pygame.init()
GRID_SIZE = 50

if __name__ == "__main__":
    pathfinder = Pathfinder(WINDOW, WIDTH, GRID_SIZE, MENU_SIZE, pygame)

    pathfinder.start()

