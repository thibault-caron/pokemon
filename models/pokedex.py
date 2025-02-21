import json

from config import *

from .database import Database


class Pokedex(Database):
    """ Class to manage the pokedex. """
    def __init__(self):
        """ Initialization of the class. """
        super().__init__()
        self.path = "./data/pokedex.json"
        self.data_pokedex = self.read_json()

    def clear_pokedex(self):
        """
        Clear json pokedex.
        :return: ∅
        """
        self.data_pokedex = {}
        with open(self.path, "w") as file:
            file.truncate()   # Use the truncate method to clear the file's content.

            # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
            json.dump(self.data_pokedex, file)

    def add_pokemon(self, pokemon):
        """
        Add a pokemon to the pokedex.
        :param pokemon: The pokemon.
        :return: ∅
        """
        pokemon = pokemon.to_dico()
        self.data_pokedex[pokemon["name"]] = pokemon
        
        # Save in JSON file
        with open(self.path, "w") as file:
            json.dump(self.data_pokedex, file, indent=4)

    def remove_pokemon(self, pokemon):
        """
        Remove a pokemon from the pokedex.
        :param pokemon: The pokemon.
        :return: ∅
        """
        print("start remove")
        pokemon_name = pokemon.get_name()
        print(pokemon_name)
        if pokemon_name in self.data_pokedex:
            print(f"Removing {pokemon_name} from pokedex")
            self.data_pokedex.pop(pokemon_name, None)

        # Save in JSON file
        with open(self.path, "w") as file:
            json.dump(self.data_pokedex, file, indent=4)

    def list_pokemons(self):
        """
        Create a list of the pokemons names.
        :return: The list.
        """
        return list(self.data_pokedex.keys())
