import json


class Database:
    """ Class to interact with json files. """
    def __init__(self):
        """ Initialization of the class. """
        self.path = "./data/type_chart.json"

    def read_json(self):
        """
        Function used to retrieve datas from a json file.
        :return: Datas.
        """
        with open(self.path, 'r') as input_file:  # Deserializing from a json format.
            data = json.load(input_file)
        return data
    
    def write_json(self, my_pokemons):
        """
        Function used to write the pokemons in a json file.
        :param my_pokemons: The dictionary of owned pokemons.
        :return: ∅
        """
        json_object = json.dumps(my_pokemons, indent=4)  # Serializing in a json format.

        with open(self.path, "w") as file:  # Write in the json
            file.write(json_object)
