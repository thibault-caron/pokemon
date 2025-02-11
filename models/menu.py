from .config import *

class Menu:
    def __init__(self, app):
        
        self.app = app
        
    def menu_background(self, app):
        menu_background = pygame.Surface((WIDTH*0.5, HEIGTH*0.5), pygame.SRCALPHA)
        menu_background.fill(WHITE)
        app.screen.blit(menu_background, (WIDTH*0.2, HEIGTH*0.2))
               
        