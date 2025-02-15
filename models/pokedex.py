import json
from .database import Database
from .pokemon_dictionary import PokemonDictionary

class Pokedex(Database):
    def __init__(self):
        self.path = "./data/pokedex.json"
        self.data_pokedex = self.read_json()
        
        self.all_pokemons = PokemonDictionary()

    def clear_pokedex(self):
        """
        Function used to clear json pokedex.
        :return: ∅
        """
        with open(self.path, "w") as file:
            file.truncate()   # Use the truncate method to clear the file's content.

            # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
            json.dump({}, file)

    # def add_pokemon(self, name):
    #     """Function that adds a Pokemon to the Pokedex"""
    #     if name in self.all_pokemons.data_pokemons:
    #         self.data_pokedex[name] = self.all_pokemons.data_pokemons[name]
            
    #         # Save in JSON file
    #         with open(self.path, "w") as file:
    #             json.dump(self.data_pokedex, file, indent=4)

    def add_pokemon(self, pokemon):
        """Function that adds a Pokemon to the Pokedex"""
        pokemon = pokemon.to_dico()
        self.data_pokedex[pokemon["name"]] = pokemon
        
        # Save in JSON file
        with open(self.path, "w") as file:
            json.dump(self.data_pokedex, file, indent=4)
                
pokedex = Pokedex()


'''Si c'est défini en dessous pour que ça marche ilfaut le dénir au dessus aussi (ex: PokemonDictionary pas importé, all_pokemons pas défini)'''
# if __name__ == '__main__':
#     from pokemon_dictionary import PokemonDictionary

#     all_pokemons = PokemonDictionary()
#     player_pokedex = Pokedex()
#     player_pokedex.add_pokemon("Mewtwo")

#     print(player_pokedex.data_pokedex)