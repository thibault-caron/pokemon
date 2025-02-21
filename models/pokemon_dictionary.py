from config import *

from .database import Database


class PokemonDictionary(Database):
    """ """
    def __init__(self):
        self.path = "./data/pokemons.json"
        self.data_pokemons = self.read_json()
        
    def get_pokemon_by_state(self, state):
        pokemons_list = []
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["state"] == state:
                pokemons_list.append(self.data_pokemons[pokemon]["name"])
        return pokemons_list

    def get_pokemon_by_min_level(self, enemy_level):
        pokemons_list = []
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["min_level"] <= enemy_level:
                pokemons_list.append(self.data_pokemons[pokemon]["name"])
        return pokemons_list

    def set_pokemon_used(self, name):
        """"""
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["name"] == name:
                self.data_pokemons[pokemon]["state"] = "used"
