import os

from config import *

from .battle import Battle
from .battle_menu import GeneratePokemon
from .button import Button
from .display_pokemon import DisplayPokemon
from .game_state import GameState
from .player_pokemon import PlayerPokemon
from .values import pokedex

class PokemonDetails(GameState):
    def __init__(self, app, pokemon_name):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokedex.jpg")
        self.caption = "Show pokemon details"
        self.pokemon = PlayerPokemon(pokemon_name)
        self.chose_pokemon_button = Button(WIDTH / 2 - 50, HEIGHT*0.78, 200, 40, "Choose me", lambda: self.launch_battle(self.pokemon), screen=self.app.screen)
        
        self.back_button = Button(WIDTH*0.048, HEIGHT*0.84, 100, 40, "Back", lambda: self.app.state_manager.set_state("show pokedex"), screen=self.app.screen)

    def launch_battle(self, chosen_pokemon):
        """Launch battle scene"""
        player_pokemon = chosen_pokemon
        if not player_pokemon:
            self.app.state_manager.set_state("choice")
        else:
            wild_pokemon = GeneratePokemon().wild_pokemon
            print(wild_pokemon.get_name())
            battle = Battle(player_pokemon, wild_pokemon)
            self.app.state_manager.set_state("battle", player_pokemon, wild_pokemon, battle)

    def draw(self):
        """Draw welcome menu scene. """
        super().draw()  # Draw background
        
        if self.pokemon:
            pokemon_card = DisplayPokemon(self.pokemon, WIDTH/ 2 - 250, HEIGHT / 2 - 120, 600, 300, app=self.app)
            pokemon_card.draw_pokedex_card()
            self.chose_pokemon_button.process()

        self.back_button.process()
