from .config import *

class Menu:
    def __init__(self, app):
        
        self.app = app
        
        self.menu_background = pygame.Surface((WIDTH*0.5, HEIGTH*0.5))
        self.menu_background.fill(FADE_WHITE)
        
    def draw(self):
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGTH*0.25))
        pygame.display.update()