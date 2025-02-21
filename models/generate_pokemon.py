from random import choice, randint

from config import *

from .pokedex import pokedex
from .pokemon import Pokemon, PlayerPokemon
from .pokemon_dictionary import all_pokemons


class GeneratePokemon:
    """ Class to generate pokemons for the battle. """

    def __init__(self):
        """ Initialization of the class. """
        self.player_pokemon = self.select_first_pokemon()
        if self.player_pokemon:
            self.wild_pokemon = self.generate_wild_pokemon(self.player_pokemon)

    def generate_wild_pokemon(self, player_pokemon):
        """
        Choose randomly a pokemon to be the opponent of your pokemon.
        :param player_pokemon: The player pokemon.
        :return: The wild pokemon.
        """

        def generate_wild_pokemon_level():
            """
            Choose randomly the wild pokemon level in a range of +/- 3 levels from the player pokemon level.
            :return: The wild pokemon level.
            """
            min_level = player_pokemon_level - 3
            if min_level < 1:
                min_level = 1

            max_level = player_pokemon_level + 3
            if max_level > 50:
                max_level = 50

            wild_pokemon_level = randint(min_level, max_level)
            return wild_pokemon_level

        def generate_wild_pokemon_name():
            """
            Choose randomly the will pokemon. Random function can use only pokemons that have a minimum level
            equal or inferior to the player pokemon level.
            :return: The wild pokemon name.
            """
            sufficient_level_pokemons = all_pokemons.get_pokemon_by_min_level(player_pokemon_level)

            used_pokemons = all_pokemons.get_pokemon_by_state("used")

            wild_pokemons_list = []
            for used_name in used_pokemons:
                for sufficient_level_name in sufficient_level_pokemons:
                    if used_name == sufficient_level_name:
                        wild_pokemons_list.append(used_name)

            wild_pokemon_name = choice(wild_pokemons_list)
            return wild_pokemon_name

        player_pokemon_level = player_pokemon.get_level()
        return Pokemon(generate_wild_pokemon_name(), generate_wild_pokemon_level())

    def select_first_pokemon(self):
        """
        Select the first pokemon of player pokedex.
        :return: The first pokemon.
        """
        player_pokemon_list = pokedex.list_pokemons()
        if not player_pokemon_list:
            return None
        else:
            first_pokemon = player_pokemon_list[0]
            return PlayerPokemon(first_pokemon)