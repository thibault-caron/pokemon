import json
from .database import Database

class PokemonDictionary(Database):
    def __init__(self):
        self.path = "./data/pokemons.json"
        self.data_pokemons = self.read_json()
        
    def get_unused_pokemons(self):
        unused_pokemon = []
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["state"] == "unused":
                unused_pokemon.append(self.data_pokemons[pokemon]["name"])
        return unused_pokemon

    def set_used_pokemons(self):
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["state"] == "unused":
               self.data_pokemons[pokemon]["state"] = "used"

data_pokemons = PokemonDictionary().data_pokemons
all_pokemons = PokemonDictionary()


# if __name__ == '__main__':
#     test = PokemonDictionary()
#     print(test.data_pokemons)