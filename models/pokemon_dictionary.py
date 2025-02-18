import json
from .database import Database

class PokemonDictionary(Database):
    def __init__(self):
        self.path = "./data/pokemons.json"
        self.data_pokemons = self.read_json()
        
    def get_unused_pokemon(self):
        unused_pokemons_list = []
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["state"] == "unused":
                unused_pokemons_list.append(self.data_pokemons[pokemon]["name"])
        return unused_pokemons_list

    def set_pokemon_used(self, name):
        """"""
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["name"] == name:
                self.data_pokemons[pokemon]["state"] = "used"
        #         break
        # self.data_pokemons = {key: value for key, value in self.data_pokemons.items() if value["state"] == "unused"}        

all_pokemons = PokemonDictionary()