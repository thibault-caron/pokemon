from .config import *

class Menu:
    def __init__(self, app):
        
        self.app = app
        
        self.menu_background = pygame.Surface((WIDTH*0.5, HEIGHT*0.5), pygame.SRCALPHA)
        self.menu_background.fill(FADE_WHITE)
        
    def draw(self):
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGHT*0.25))
