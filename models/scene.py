import os

from .config import *

class Scene:
    """Create a new scene (room, level, view)."""
    id = 0
    bg = Color('gray')
    options = {"file": ""}    
    
    def __init__(self, app, img_folder="images", file="", *args, **kwargs):
                
        self.app = app
        
        # Append the new scene and make it the current scene
        self.app.scenes.append(self)
        self.app.scene = self
        
        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg

        # get background image path
        self.file = os.path.join(img_folder, file) if file else ""
        self.file = os.path.normpath(self.file)
        
        # load and scale background image
        self.img = pygame.image.load(self.file)
        self.img = pygame.transform.smoothscale(self.img, self.app.screen.get_size())
        
    def draw(self):
        screen_size = self.app.screen.get_size()
        
        """Draw all objects in the scene."""
        if self.img:
            resized_img = pygame.transform.smoothscale(self.img, screen_size)  # Resize background
            self.app.screen.blit(resized_img, (0, 0))
        
        for node in self.nodes:
            node.draw()
        
