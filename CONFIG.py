import pygame
from pygame.locals import *


# Initialisation
pygame.init()
pygame.font.init()

# Game window
WIDTH, HEIGHT = 1000, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# font
FONT = pygame.font.SysFont('Roboto', 35)
FONT_HOVER = pygame.font.SysFont('Roboto', 35, True)


# Colors
BLACK = (0, 0, 0)
GREY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)

# Clock
FPS = pygame.time.Clock()

# Background
BACKGROUND = pygame.image.load("assets/battle_background.webp")
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
