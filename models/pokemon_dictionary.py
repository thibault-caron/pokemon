import json
from database import Database

class PokemonDictionary(Database):
    def __init__(self):
        self.path = "../pokemons.json"
        self.data_pokemons = self.read_json()


if __name__ == '__main__':
    test = PokemonDictionary()
    print(test.data_pokemons)