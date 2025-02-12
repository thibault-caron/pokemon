'''Set all the variable of the game'''

# import pygame
import pygame
from pygame.locals import *

# Set screen size
WIDTH = 1200
HEIGHT = 720
SCREEN_SIZE = WIDTH, HEIGHT
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

# Add background image
BACKGROUND_IMAGE = pygame.image.load("assets/images/pokemon.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, SCREEN_SIZE)

# Set fonts

# Set colors
WHITE = (255, 255, 255)
FADE_WHITE = (255, 255, 255, 20)
BLACK = (0, 0, 0)
GREY = "grey"

# Clock
CLOCK = pygame.time.Clock()

# Set number of refresh per second
FPS = 60