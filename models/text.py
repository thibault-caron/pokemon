import pygame
from pygame.locals import *

class Text:
    """Create a text object."""

    def __init__(self, text, pos, app, **options):
        super().__init__()
        self.text = text
        self.pos = pos
        self.app = app

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()
        
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        
    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
        
    def draw(self):
        """Draw the text image to the screen."""
        self.app.screen.blit(self.img, self.rect)
        pygame.display.update()
