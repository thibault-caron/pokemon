"""
Authors : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON.
Date : 20/02/2025 11h05
Aim of the program :
    Execute a pokemon game with PyGame.
Inputs : ∅
Output : Pokemon battle game using the graphical interface PyGame.
"""

from config import *
from models import *


class App:
    """ Main class of the game. """
    def __init__(self):
        """ Initialize pygame and the application. """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

        self.state_manager = GameStateManager(self)
        self.state_manager.set_state("welcome")
        
        self.running = True

    def run(self):        
        """ Run the main event loop. """
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    
            self.state_manager.get_state().draw()  # Draw the welcome menu when the game starts.
                
            pygame.display.update()
            CLOCK.tick(FPS)

        pygame.quit()

        
if __name__ == '__main__':  # The program will be run only if executed directly, not if it is called by another program.
    game = App()
    game.run()
