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

    def set_used_pokemons(self, name):
        """"""
        for pokemon in self.data_pokemons:
            if self.data_pokemons[pokemon]["name"] == name:
                self.data_pokemons[pokemon]["state"] = "used"
                break
        self.data_pokemons = {key: value for key, value in self.data_pokemons.items() if value["state"] == "unused"}        
            
            # print(self.data_pokemons[pokemon]["name"])
            # set_use = self.data_pokemons[pokemon]["name"]
            # print(set_use)
                # if self.data_pokemons[pokemon]["state"] == "unused":
                #     self.data_pokemons[pokemon]["state"] = "used"
                #     name = self.data_pokemons[pokemon]["name"]
            #    for value in unused_pokemon:
            #        print(type(value))
            #        if value == name:
                       
            #            unused_pokemon.pop(value)

all_pokemons = PokemonDictionary()

# if __name__ == '__main__':
#     test = PokemonDictionary()
#     print(test.data_pokemons)