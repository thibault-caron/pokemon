import os

from config import *
from .game_state import GameState
from .button import Button
from .pokemon_dictionary import all_pokemons
from .pokedex import pokedex

class WelcomeMenu(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokemon.jpg")
        self.caption = "Welcome Menu"
        self.radius = 10
        
        self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'New game', self.new_game, screen=self.app.screen)
        self.button2 = Button(WIDTH/2 - 200, 290, 400, 50, 'Continue', self.continue_game, screen=self.app.screen)
        self.button3 = Button(WIDTH/2 - 200, 380, 400, 50, 'Add Wild Pokemon', self.add_wild_pokemon, screen=self.app.screen)
        self.button4 = Button(WIDTH/2 - 200, 470, 400, 50, 'My Pokedex', self.display_pokedex, screen=self.app.screen)
        
        self.buttons = [self.button1, self.button2, self.button3, self.button4]
        
    def new_game(self):
        """Go to menu Choose your first pokemon"""
        self.app.state_manager.set_state("choice")
        
    def continue_game(self):
        """Go to menu battle menu"""
        if pokedex.data_pokedex == {}:
            self.app.state_manager.set_state("choice")
        else:
            self.app.state_manager.set_state("battle menu")
        
    def add_wild_pokemon(self):
        """Go to wild pokemon display scene."""
        self.app.state_manager.set_state("add wild pokemon")

    def display_pokedex(self):
        """Go to pokedex display scene"""
        self.app.state_manager.set_state("show pokedex")

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGHT*0.25)) # Draw menu rectangle
        for button in self.buttons:
            button.process()  # Show buttons