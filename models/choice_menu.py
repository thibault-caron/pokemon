import os

from .config import *
from .game_state import GameState
from .button import Button
from.display_pokemon import DisplayPokemon

class ChoiceMenu(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokemon.jpg")
        self.caption = "Choose Pokemon Menu"
        
        # self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'Start Game', self.start_game)
        # self.button2 = Button(WIDTH/2 - 200, 290, 400, 50, 'Settings', self.settings)
        # self.button3 = Button(WIDTH/2 - 200, 380, 400, 50, 'Exit', self.exit_game)
        
        # self.buttons = [self.button1, self.button2, self.button3]
        
    def start_game(self):
        """Go to menu Choose your first pokemon"""
        self.app.state_manager.set_state("Choose pokemon menu")

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
            DisplayPokemon("Bulbasaur", 600, 900, 400, 200, app=self.app).draw_card()
            DisplayPokemon("Charmander", 900, 100, 400, 200, app=self.app).draw_card()
            DisplayPokemon("Blastoise", 1000, 900, 400, 200, app=self.app).draw_card()
        else:
            print("Erreur: `self.app` ne contient pas d'attribut `screen`.")