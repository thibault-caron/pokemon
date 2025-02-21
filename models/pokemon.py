from config import *

from .values import all_pokemons, pokedex


class Pokemon:
    """ Class to manage the pokemons."""
    def __init__(self, name, level=5, wild=True):
        """
        Initialization of the class.
        :param name: The pokemon name.
        :param level: The pokemon level.
        :param wild: If true it's a wild pokemon.
        """
        self.__name = name
        self.__id = all_pokemons.data_pokemons[self.get_name()]["id_code"]
        self.__level = level
        self.__xp = 0
        self.__wild = wild

        self.__types = all_pokemons.data_pokemons[self.get_name()]["types"]
        self.__max_hp = self.calculate_max_hp()
        self.__hp = self.__max_hp
        self.__attack = self.calculate_attack()
        self.__evolution = all_pokemons.data_pokemons[self.get_name()]["evolution"]
        self.__front_sprite_path = './assets/sprites/' + self.__name.lower() + '_front.png'
        self.__back_sprite_path = './assets/sprites/' + self.__name.lower() + '_back.png'

    def get_name(self):
        """
        Getter of the pokemon name.
        :return: The name.
        """
        return self.__name
    
    def get_id(self):
        """
        Getter of the pokemon id.
        :return: The id.
        """
        return self.__id
    
    def get_level(self):
        """
        Getter of the pokemon level.
        :return: The level.
        """
        return self.__level
    
    def get_xp(self):
        """
        Getter of the pokemon xp.
        :return: The xp.
        """
        return self.__xp
    
    def get_types(self):
        """
        Getter of the pokemon type.
        :return: The type.
        """
        return self.__types
    
    def get_max_hp(self):
        """
        Getter of the pokemon max hp.
        :return: The max hp.
        """
        return self.__max_hp
    
    def get_hp(self):
        """
        Getter of the pokemon hp.
        :return: The hp.
        """
        return self.__hp
    
    def get_attack(self):
        """
        Getter of the pokemon attack points.
        :return: The attack points.
        """
        return self.__attack
    
    def get_wild(self):
        """
        Getter of the pokemon wild status.
        :return: The wild status.
        """
        return self.__wild
    
    def get_evolution(self):
        """
        Getter of the pokemon evolution.
        :return: The evolution.
        """
        return self.__evolution
    
    def get_front_sprite(self):
        """
        Getter of the pokemon front sprite.
        :return: The front sprite.
        """
        return self.__front_sprite_path
    
    def get_back_sprite(self):
        """
        Getter of the pokemon back sprite.
        :return: The back sprite.
        """
        return self.__back_sprite_path
    
    # Setters
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        """
        Setter of the pokemon id.
        :param id: The new id.
        :return: ∅
        """
        self.__id = id
    
    def set_level(self, level):
        self.__level = level

    def set_xp(self, xp):
        self.__xp = xp

    def set_types(self, types):
        self.__types = types

    def set_hp(self, hp):
        self.__hp = hp

    def set_max_hp(self, max_hp):
        self.__max_hp = max_hp
    
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


    def to_dico(self):
        """Convert Pokemon instance to dictionary"""
        return {
            "name": self.__name,
            "id": self.__id,
            "level": self.__level,
            "xp": self.__xp,
            "types": self.__types,
            "max_hp": self.__max_hp,
            "hp": self.__hp,
            "attack": self.__attack,
            "evolution": self.__evolution,
            "front_sprite": self.__front_sprite_path,
            "back_sprite": self.__back_sprite_path,
        }

    def evolve(self):
        if self.__evolution != []:
            if self.__level >= self.__evolution[0]:
                print(f"{self.__name} is evolving!")
                
                pokedex.remove_pokemon(self)
                self.__name = self.__evolution[1]

                # get evolution data from 'pokemon.json (all_pokemons.data_pokemons)'
                self.__types = all_pokemons.data_pokemons[self.get_name()]["types"]
                self.__max_hp = self.calculate_max_hp()
                self.__hp = self.__max_hp
                self.__attack = self.calculate_attack()
                self.__evolution = all_pokemons.data_pokemons[self.get_name()]["evolution"]
                self.__front_sprite_path = all_pokemons.data_pokemons[self.get_name()]["front_sprite"]
                self.__back_sprite_path = all_pokemons.data_pokemons[self.get_name()]["back_sprite"]

                print(f"{self.__name} has evolved!")

        else:
            print(f"{self.__name} cannot evolve.")

    def level_up(self):
        if self.__xp >= self.__level * 4 and self.__level < 50:
            self.__level += 1
            print(f"{self.__name} has grown to level {self.__level} !")
            self.__attack = self.__attack * 1.02  # Increases attack by 2 % each level
            self.__hp = self.__hp * 1.02  # # Increases HP by 2 % each level
            self.__xp = 0

    def calculate_attack(self):
        """
        Calculate pokemon attack evolution.
        :return:
        """
        if self.__level > 1:
            attack = all_pokemons.data_pokemons[self.get_name()]["attack"] * 1.02 ** self.__level
        else:
            attack = all_pokemons.data_pokemons[self.get_name()]["attack"]
        return round(attack)

    def calculate_max_hp(self):
        """
        Calculate pokemon max HP evolution.
        :return:
        """
        if self.__level > 1:
            max_hp = all_pokemons.data_pokemons[self.get_name()]["hp"] * 1.02 ** self.__level
        else:
            max_hp = all_pokemons.data_pokemons[self.get_name()]["hp"]
        return round(max_hp)
    
    def gain_xp(self, enemy_pokemon):
        """methode to gain hp after victory"""
        xp_source = enemy_pokemon.get_level()
        self.__xp += xp_source


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
