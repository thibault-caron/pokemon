import json

class Database:
    def __init__(self):
        self.path = "../pokemons.json"

    def read_json(self):
        """
        Function used to retrieve from a json file, the past operations history and convert there into a dictionary.
        Executed at the beginning of the program.
        :param file: File path of json file.
        :return: A dictionary of operations history.
        """
        with open(self.path, 'r') as input_file:  # Deserializing from a json format.
            data = json.load(input_file)
        return data