from config import *

from .database import Database


class PokemonDictionary(Database):
    """ Class to manage the pokemons not in the pokedex. """
    def __init__(self):
        """ Initialization of the class. """
        super().__init__()
        self.path = "./data/pokemons.json"
        self.data_pokemons = self.read_json()
        
    def get_pokemon_by_state(self, state):
        """
        Get all the pokemon with a requested state.
        :param state: The state of the pokemons (used or unused).
        :return: The list of pokemons.
        """
        pokemons_list = []
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["state"] == state:
                pokemons_list.append(self.data_pokemons[pokemon]["name"])
        return pokemons_list

    def get_pokemon_by_min_level(self, enemy_level):
        """
        Select only the pokemons who have a minimum level equal or inferior to the player pokemon level.
        :param enemy_level: The player pokemon level.
        :return: A list of pokemons that meet this expectation.
        """
        pokemons_list = []
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["min_level"] <= enemy_level:
                pokemons_list.append(self.data_pokemons[pokemon]["name"])
        return pokemons_list

    def set_pokemon_used(self, name):
        """
        Change state of a pokemon to used.
        ;param name: The pokemon name.
        :return: ∅
        """
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["name"] == name:
                self.data_pokemons[pokemon]["state"] = "used"
