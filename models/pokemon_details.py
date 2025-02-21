import os

from config import *
from .game_state import GameState
from .button import Button
from .display_pokemon import DisplayPokemon
from .pokemon import PlayerPokemon
from .pokedex import pokedex

class PokemonDetails(GameState):
    def __init__(self, app, pokemon_name):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokedex.jpg")
        self.caption = "Show pokedex"
        self.pokemon_name = pokemon_name
        
        self.back_button = Button(WIDTH*0.048, HEIGHT*0.84, 100, 40, "Back", lambda: self.app.state_manager.set_state("show pokedex"), screen=self.app.screen)

    def draw(self):
        """Draw welcome menu scene. """
        super().draw()  # Draw background
        
        if self.pokemon_name:
            displayed_pokemon = PlayerPokemon(self.pokemon_name)
            pokemon_card = DisplayPokemon(displayed_pokemon, WIDTH/ 2 - 250, HEIGHT / 2 - 120, 600, 300, app=self.app)
            pokemon_card.draw_pokedex_card()

        self.back_button.process()
