from .config import *
from .scene import Scene

class SceneManager:
    def __init__(self, app):
        self.app = app
        self.scene = {}
        self.current_scene = None
        
    # Add a new scene
    def add_scene(self, name, scene):
        self.scene[name] = scene
        
    # Move inbetween scenes
    def change_scene(self, name):
        if name in self.scene:
            self.current_scene = self.scene[name]
    
    # update the current scene        
    def update(self):
        if self.current_scene:
            self.current_scene.update()
    
    
    # Draw the current scene        
    def draw(self):
        if self.current_scene:
            self.current_scene.draw()