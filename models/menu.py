from .config import *

class Menu:
    def __init__(self, app):
        
        self.app = app
        
        self.menu_background = pygame.Surface((WIDTH*0.5, HEIGTH*0.5), pygame.SRCALPHA)
        self.menu_background.fill(WHITE)
        
    def draw(self):
        self.app.screen.blit(self.menu_background, (WIDTH*0.2, HEIGTH*0.2))
               
        