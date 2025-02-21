import os

from config import *
from .game_state import GameState
from .pokemon import Pokemon
from .display_pokemon import DisplayPokemon


class ChoiceMenu(GameState):
    """ Class to manage the choice menu scene. """
    def __init__(self, app):
        """
        Initialization of the class.
        :param app: Call of the game main loop.
        """
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokemon.jpg")
        self.caption = "Choose Pokemon Menu"

        starter1 = Pokemon("Pikachu", 5)
        starter2 = Pokemon("Bulbasaur", 5)
        starter3 = Pokemon("Charmander", 5)
        starter4 = Pokemon("Squirtle", 5)

        self.pokemon_cards = [
            DisplayPokemon(starter1, 100, 100, 400, 200, app=self.app),
            DisplayPokemon(starter2, 700, 100, 400, 200, app=self.app),
            DisplayPokemon(starter3, 100, 400, 400, 200, app=self.app),
            DisplayPokemon(starter4, 700, 400, 400, 200, app=self.app),
        ]

    def draw(self):
        """
        Draw the choice menu scene.
        :return: ∅
        """
        super().draw()
        if hasattr(self.app, 'screen'):
            for pokemon_card in self.pokemon_cards:
                pokemon_card.draw_card()
        else:
            print("Error: `self.app` has no attribute `screen`.")
