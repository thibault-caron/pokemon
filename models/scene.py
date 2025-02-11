import os

from .config import *

class Scene:
    """Create a new scene (room, level, view)."""
    id = 0
    bg = WHITE
    options = {"file": ""}    
    
    def __init__(self, app, *args, **kwargs):
                
        self.app = app
        
        # Append the new scene and make it the current scene
        self.app.scenes.append(self)
        self.app.scene = self
        
        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
        
        self.file = kwargs.get("file", "")

        if self.file:
            try:
                self.img = pygame.image.load(self.file)
                self.img = pygame.transform.smoothscale(self.img, self.app.screen.get_size())
            except pygame.error as error:
                print(f"The background image could not been loaded : {error}")
                self.img = None
        else:
            print("No image folder specified")
            self.img = None

            
        self.enter()
        
    def draw(self):
        screen_size = self.app.screen.get_size()
        
        """Draw all objects in the scene."""
        if self.img:
            resized_img = pygame.transform.smoothscale(self.img, screen_size)
            self.app.screen.blit(resized_img, (0, 0))
        else:
            self.app.screen.fill(self.bg)
        
        for node in self.nodes:
            node.draw()
            
        pygame.display.flip()
        
    def enter(self):
        """Method called to enter a scene"""
        print(f"Entering scene {self.id}")
        
