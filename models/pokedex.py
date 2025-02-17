import json
from .database import Database

class Pokedex(Database):
    def __init__(self):
        self.path = "./data/pokedex.json"
        self.data_pokedex = self.read_json()

    def clear_pokedex(self):
        """
        Function used to clear json pokedex.
        :return: ∅
        """
        self.data_pokedex = {}
        with open(self.path, "w") as file:
            file.truncate()   # Use the truncate method to clear the file's content.

            # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
            json.dump(self.data_pokedex, file)

    def add_pokemon(self, pokemon):
        """Function that adds a Pokemon to the Pokedex"""
        pokemon = pokemon.to_dico()
        self.data_pokedex[pokemon["name"]] = pokemon
        
        # Save in JSON file
        with open(self.path, "w") as file:
            json.dump(self.data_pokedex, file, indent=4)

    def remove_pokemon(self, pokemon_name):
        """remove a pokemon from var pokedex if it contains an item with its name"""
        if pokemon_name in self.data_pokedex:
            self.data_pokedex.pop(pokemon_name, None)
                
pokedex = Pokedex()


'''Si c'est défini en dessous pour que ça marche ilfaut le dénir au dessus aussi (ex: PokemonDictionary pas importé, all_pokemons pas défini)'''
# if __name__ == '__main__':
#     from pokemon_dictionary import PokemonDictionary

#     all_pokemons = PokemonDictionary()
#     player_pokedex = Pokedex()
#     player_pokedex.add_pokemon("Mewtwo")

#     print(player_pokedex.data_pokedex)