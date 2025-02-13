import json

class Database:
    def __init__(self):
        self.path = "./data/type_chart.json"

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
    
    def write_json(self, my_pokemons):
        """
        Function used to write the pokemons in the json file.
        :param history: The dictionary of owned pokemons.
        :return: ∅
        """
        json_object = json.dumps(my_pokemons, indent=4)  # Serializing in a json format.

        with open(self.path, "w") as file:  # Write in pokedex.json
            file.write(json_object)
    
if __name__ == '__main__':
    test = Database().read_json()
    print(test)