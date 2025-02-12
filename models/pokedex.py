import json
from database import Database

class Pokedex(Database):
    def __init__(self):
        self.path = "../pokedex.json"

    def clear_pokedex(self):
        """
        Function used to clear json pokedex.
        :return: ∅
        """
        with open("../pokedex.json", "w") as file:
            file.truncate()   # Use the truncate method to clear the file's content.

            # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
            json.dump({}, file)

    def write_json(self, my_pokemons):
        """
        Function used to write the pokemons in the json file.
        :param history: The dictionary of owned pokemons.
        :return: ∅
        """
        json_object = json.dumps(my_pokemons, indent=4)  # Serializing in a json format.

        with open(self.path, "w") as file:  # Write in pokedex.json
            file.write(json_object)