from .config import *

class Scene:
    def __init__(self, app, *args, **kwargs):
        
        """Create a new scene (room, level, view)."""
        id = 0
        bg = Color('gray')
        
        self.app = app
        
        # Append the new scene and make it the current scene
        self.app.scenes.append(self)
        self.app.scene = self
        
        # Set the instance id and increment the class id
        self.id = Scene.id
        Scene.id += 1
        self.nodes = []
        self.bg = Scene.bg
        
        self.file = Scene.options['file']

        if self.file != '':
            self.img = pygame.image.load(self.file)
            size = self.app.screen.get_size()
            self.img = pygame.transform.smoothscale(self.img, size)
        self.enter()
        
    def draw(self):
        """Draw all objects in the scene."""
        self.app.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()
        
