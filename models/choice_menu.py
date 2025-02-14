import os

from .config import *
from .game_state import GameState
from .button import Button
from.display_pokemon import DisplayPokemon

class ChoiceMenu(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokemon.jpg")
        self.caption = "Choose Pokemon Menu"
              
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
            DisplayPokemon("Pikachu", 100, 100, 400, 200, app=self.app).draw_card()
            # Button(220, 120, 70, 50, 'New game', self.battle).process()
            DisplayPokemon("Bulbasaur", 700, 100, 400, 200, app=self.app).draw_card()
            DisplayPokemon("Charmander", 100, 400, 400, 200, app=self.app).draw_card()
            DisplayPokemon("Blastoise", 700, 400, 400, 200, app=self.app).draw_card()
        else:
            print("Erreur: `self.app` ne contient pas d'attribut `screen`.")