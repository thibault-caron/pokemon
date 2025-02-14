import os

from .config import *
from .game_state import GameState
from .button import Button

class WelcomeMenu(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokemon.jpg")
        self.caption = "Welcome Menu"
        
        self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'New game', self.new_game)
        self.button2 = Button(WIDTH/2 - 200, 290, 400, 50, 'Continue', self.display_pokedex)
        self.button3 = Button(WIDTH/2 - 200, 380, 400, 50, 'Add Pokemon', self.display_pokemons)
        self.button4 = Button(WIDTH/2 - 200, 470, 400, 50, 'My Pokedex', self.display_pokemons)
        
        self.buttons = [self.button1, self.button2, self.button3, self.button4]
        
    def new_game(self):
        """Go to menu Choose your first pokemon"""
        self.app.state_manager.set_state("choice")
        
    def continue_game(self):
        """Go to menu battle menu"""
        self.app.state_manager.set_state("battle menu")
        
    def display_pokemons(self):
        """Go to pokedex display scene."""
        print("Show all pokemons")

    def display_pokedex(self):
        """Go to pokedex display scene"""
        print("Show my pokedex")

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGHT*0.25)) # Draw menu rectangle
        for button in self.buttons:
            button.process()  # Show buttons