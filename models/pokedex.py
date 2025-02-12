import json
from database import Database

class Pokedex(Database):
    def __init__(self):
        self.path = "pokedex.json"

    def clear_pokedex(self):
        """
        Function used to clear json pokedex.
        :return: ∅
        """
        with open(self.path, "w") as file:
            file.truncate()   # Use the truncate method to clear the file's content.

            # Rewrote "{}" in the empty file to avoid an error, in which the file was not recognized as a json format.
            json.dump({}, file)