import os

from config import *
from .game_state import GameState
from .display_pokemon import DisplayPokemon
from .button import Button
from .pokemon import PlayerPokemon
from .pokedex import pokedex

class PokedexDetails(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokedex.jpg")
        self.caption = "Show pokedex details"
        self.pokemon_name = ""

    def draw_pokemon(self, name):
        pokemon_name = PlayerPokemon(name).get_name()
        # self.pokemon_name = pokemon_drawn.get_name()
        pokemon_display = DisplayPokemon(pokemon_name, 100, 100, 400, 200, app=self.app)
        return pokemon_display

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        
        self.draw_pokemon(self.pokemon_name).draw_card()