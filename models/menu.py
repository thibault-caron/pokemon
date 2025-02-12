from .config import *

class Menu:
    def __init__(self, app):
        
        self.app = app
        
        flags = RESIZABLE
        
        self.menu_background = pygame.Surface((WIDTH*0.5, HEIGTH*0.5), flags)
        self.menu_background.fill(FADE_WHITE)
        self.menu_img = pygame.transform.smoothscale(self.menu_background, self.menu_background.get_size())
        
    def toggle_fullscreen(self):
        """Toggle between full screen and windowed screen."""
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0, 0), self.flags)

    def toggle_resizable(self):
        """Toggle between resizable and fixed-size window."""
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
        """Toggle between frame and noframe window."""
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)
        
    def draw(self):
        # self.app.screen.blit(self.menu_img, (WIDTH*0.2, HEIGTH*0.2))
        # pygame.display.update()
               
        menu_size = self.menu_background.get_size()
        
        """Draw all objects in the scene."""
        if self.menu_img:
            resized_img = pygame.transform.smoothscale(self.menu_img, menu_size)  # Redimensionner l'image
            self.app.screen.blit(resized_img, (WIDTH/2, HEIGTH/2))
        else:
            self.app.screen.fill(self.bg)