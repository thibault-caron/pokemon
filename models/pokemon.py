import json
from database import Database
from pokedex import Pokedex
from pokemon_dictionary import PokemonDictionary

# data_pokemons = PokemonDictionary().data_pokemons
# my_pokemons = Pokedex.read_json()

class Pokemon:

    def __init__(self, name, level, wild=True):
        self.__name = name
        self.__level = level
        self.__xp = 0
        self.__wild = wild

        # a faire: données à récup dans data_pokemons via le "name"
        self.__types = data_pokemons[self.get_name()]["types"]
        self.__max_hp = data_pokemons[self.get_name()]["hp"]
        self.__hp = self.__max_hp
        self.__attack = data_pokemons[self.get_name()]["attack"]
        self.__evolution = data_pokemons[self.get_name()]["evolution"]
        self.__front_sprite_path = '../assets/sprites/' + self.__name.lower() + '_front.png'
        self.__back_sprite_path = '../assets/sprites/' + self.__name.lower() + '_back.png'
    
    # Getters
    def get_name(self):
        return self.__name
    
    def get_level(self):
        return self.__level
    
    def get_xp(self):
        return self.__xp
    
    def get_types(self):
        return self.__types
    
    def get_max_hp(self):
        return self.__max_hp
    
    def get_hp(self):
        return self.__hp
    
    def get_attack(self):
        return self.__attack
    
    def get_wild(self):
        return self.__wild
    
    def get_evolution(self):
        return self.__evolution
    
    def get_front_sprite(self):
        return self.__front_sprite_path
    
    def get_back_sprite(self):
        return self.__back_sprite_path
    
    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_level(self, level):
        self.__level = level

    def set_xp(self, xp):
        self.__max_hp = xp

    def set_types(self, types):
        self.__types = types

    def set_hp(self, hp):
        self.__hp = hp
    
    def set_attack(self, attack):
        self.__attack = attack
    
    def set_wild(self, wild):
        self.__wild = wild
    
    def set_evolution(self, evolution):
        self.__evolution = evolution
    
    def set_front_sprite(self, front_sprite):
        self.__front_sprite_path = front_sprite

    def set_back_sprite(self, back_sprite):
        self.__back_sprite_path = back_sprite
    
    def evolve(self):
        if self.__evolution != []:
            if self.__level >= self.__evolution[0]:
                self.__name = self.__evolution[1]

                # a faire: recuperer les données de l'evolution dans 'pokemon.json (data_pokemons)'
                self.__types = data_pokemons[self.get_name()]["types"]
                self.__max_hp = data_pokemons[self.get_name()]["hp"]
                self.__hp = self.__max_hp
                self.__attack = data_pokemons[self.get_name()]["attack"]
                self.__evolution = data_pokemons[self.get_name()]["evolution"]
                self.front_sprite_path = data_pokemons[self.get_name()]["front_sprite"]
                self.back_sprite_path = data_pokemons[self.get_name()]["back_sprite"]

                print(f"{self.__name} has evolved!")

                # a faire: retirer l'objet du nom de la pré-evolution à 'my_pokemons' et append celui du nouveau nom à la place 
        else:
            print(f"{self.__name} cannot evolve.")

    def level_up(self):
        if self.__xp >= self.__level * 4:
            self.__level += 1
            print(f"{self.__name} has grown to level {self.__level} !")
            self.__xp = 0
    
    def display_info(self):
        """Display the Pokémon's details"""
        print(f"Name: {self.__name}")
        print(f"Max Hit Points: {self.__max_hp}")
        print(f"Current Hit Points: {self.__hp}")
        print(f"Level: {self.__level}")
        print(f"Attack Power: {self.__attack}")
        print(f"Types: {', '.join(self.__types)}")
        if self.__evolution:
            print(f"Evolves into: {self.__evolution}")
        else:
            print("This Pokémon cannot evolve.")


if __name__ == '__main__':
    data_pokemons = PokemonDictionary().data_pokemons
    test = Pokemon("Pikachu", 1)
    print(test.get_evolution())
