import os

from .config import *
from .game_state import GameState
from .button import Button
from.display_pokemon import DisplayPokemon

class BattleScene(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="battle_background.webp")
        self.caption = "Battle"
        self.pokemon_cards = [
            DisplayPokemon("Pikachu", 100, 100, 400, 200, app=self.app),
            DisplayPokemon("Bulbasaur", 700, 100, 400, 200, app=self.app)
        ]
        self.button1 = Button(50, 650, 200, 50, "Attack", self.attack)
        self.button2 = Button(450, 650, 300, 50, "Change Pokemon", self.change_pokemon)
        self.button3 = Button(950, 650, 200, 50, "Run", self.run)
        self.buttons = [self.button1, self.button2, self.button3]

    def attack(self):
        """ Attack the enemy. """
        pass

    def change_pokemon(self):
        """ Change pokemon in the battle. """
        pass

    def run(self):
        """ Escape from the battle. """
        pass

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background

        for button in self.buttons:
            button.process()  # Show buttons

        if hasattr(self.app, 'screen'):
            for pokemon_card in self.pokemon_cards:
                pokemon_card.draw_card()
        else:
            print("Erreur: `self.app` ne contient pas d'attribut `screen`.")