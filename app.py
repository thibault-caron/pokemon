from config import *
from models import *


class App:
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        # flags = RESIZABLE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

        self.state_manager = GameStateManager(self)
        self.state_manager.set_state("welcome")
        
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
