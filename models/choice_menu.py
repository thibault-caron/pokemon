import os

from .config import *
from .game_state import GameState
from .button import Button
from.display_pokemon import DisplayPokemon

class ChoiceMenu(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokemon.jpg")
        self.caption = "Choose Pokemon Menu"
        
        self.pokemon_cards = [
            DisplayPokemon("Pikachu", 100, 100, 400, 200, app=self.app),
            DisplayPokemon("Bulbasaur", 700, 100, 400, 200, app=self.app),
            DisplayPokemon("Charmander", 100, 400, 400, 200, app=self.app),
            DisplayPokemon("Squirtle", 700, 400, 400, 200, app=self.app),
        ]
              
    '''Action'''
    def battle(self):
        """Go to menu battle menu"""
        self.app.state_manager.set_state("battle")

    def settings(self):
        """Affiche les paramètres."""
        print("Settings clicked!")

    def exit_game(self):
        """Quitte l'application."""
        self.app.running = False

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        if hasattr(self.app, 'screen'):
            for pokemon_card in self.pokemon_cards:
                pokemon_card.draw_card()
        else:
            print("Erreur: `self.app` ne contient pas d'attribut `screen`.")