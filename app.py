import os

from models.config import *
from models.text import Text
from models.scene import Scene
from models.game_state_manager import GameStateManager
from models.button import Button
from models.database import Database
from models.pokemon import Pokemon
from models.battle import Battle


class App:
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        # flags = RESIZABLE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
        # self.t = Text('Pygame App', pos=(20, 20), app=self)

        self.state_manager = GameStateManager(self)
        
        self.running = True
        
    # def toggle_fullscreen(self):
    #     """Toggle between full screen and windowed screen."""
    #     self.flags ^= FULLSCREEN
    #     pygame.display.set_mode((0, 0), self.flags)

    # def toggle_resizable(self):
    #     """Toggle between resizable and fixed-size window."""
    #     self.flags ^= RESIZABLE
    #     pygame.display.set_mode(self.rect.size, self.flags)

    # def toggle_frame(self):
    #     """Toggle between frame and noframe window."""
    #     self.flags ^= NOFRAME
    #     pygame.display.set_mode(self.rect.size, self.flags)
        

    def run(self):
        # menu1_img_path = os.path.join(os.getcwd(), "assets", "images", "pokemon.jpg")
        # self.menu1 = GameState(app=self, file=menu1_img_path, caption="Main Menu")
        # self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'Button One', Button.myFunction)
        # self.button2 = Button(WIDTH/2 - 200, 290, 400, 50, 'Button Two', Button.myFunction)
        # self.button3 = Button(WIDTH/2 - 200, 380, 400, 50, 'Button Three', Button.myFunction)
        # self.button4 = Button(WIDTH/2 - 200, 470, 400, 50, 'Button Four', Button.myFunction)
        
        # objects = [self.button1, self.button2, self.button3, self.button4]
        
        # game_state = "welcome_menu"
        
        """Run the main event loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    
            self.state_manager.get_state().draw()
                
            pygame.display.update()
            CLOCK.tick(FPS)

        pygame.quit()

        
if __name__ == '__main__':
    App().run()
