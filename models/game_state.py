import os

from config import *
from button import Button

class GameState:
    """Create a new scene (room, level, view)."""
    options = {"file": ""}    
    
    def __init__(self, app, img_folder="images", file="", *args, **kwargs):
                
        self.app = app

        # get background image path
        self.file = os.path.join(img_folder, file) if file else ""
        self.file = os.path.normpath(self.file)
        
        # load and scale background image
        self.img = pygame.image.load(self.file)
        self.img = pygame.transform.smoothscale(self.img, self.app.screen.get_size())
        
        # create menu window
        self.menu_background = pygame.Surface((WIDTH*0.5, HEIGHT*0.5), pygame.SRCALPHA)
        self.menu_background.fill(FADE_WHITE)
        
    def draw(self):
        screen_size = self.app.screen.get_size()
        
        """Draw all objects in the scene."""
        if self.img:
            resized_img = pygame.transform.smoothscale(self.img, screen_size)  # Resize background
            self.app.screen.blit(resized_img, (0, 0)) # Draw background
            
