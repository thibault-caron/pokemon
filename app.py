from config import *
from models import *


class App:
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

        self.state_manager = GameStateManager(self)
        self.state_manager.set_state("welcome")
        
        self.running = True

    def run(self):        
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
    game = App()
    game.run()
