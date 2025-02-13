from models.config import *
from models.text import Text
from models.scene import Scene
from models.menu import Menu
from models.button import Button

class App:
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
        self.t = Text('Pygame App', pos=(20, 20), app=self)
        
        self.scenes = []

        self.running = True
        
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
        

    def run(self):
        self.scene = Scene(app=self, img_folder = "assets/images", file = "pokemon.jpg", caption='Intro')
        # self.intro = Text('Introduction screen', (20, 20), app=self)
        self.menu1 = Menu(app=self)
        self.button = Button(WIDTH/2 - 200, 200, 400, 50, 'Button One (onePress)', Button.myFunction)
        
        game_state = "welcome_menu"
        
        objects = [self.button]
        
        """Run the main event loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    
            if game_state == "welcome_menu":
                self.scene.draw()
                self.menu1.draw()
            
            for object in objects:
                object.process()
                
            pygame.display.update()
            CLOCK.tick(FPS)

        pygame.quit()

        
if __name__ == '__main__':
    App().run()