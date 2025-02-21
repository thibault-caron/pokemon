from config import *

from .pokemon import Pokemon
from .values import pokedex


class PlayerPokemon(Pokemon):
    """ Class to manage the player pokemons."""
    def __init__(self, name):
        """
        Initialization of the class.
        :param name: The pokemon name.
        """
        super().__init__(name)

        self.set_id(pokedex.data_pokedex[self.get_name()]["id"])
        self.set_level(pokedex.data_pokedex[self.get_name()]["level"])
        self.set_xp(pokedex.data_pokedex[self.get_name()]["xp"])
        self.set_wild(False)
        self.set_types(pokedex.data_pokedex[self.get_name()]["types"])
        self.set_max_hp(pokedex.data_pokedex[self.get_name()]["max_hp"])
        self.set_hp(pokedex.data_pokedex[self.get_name()]["hp"])
        self.set_attack(pokedex.data_pokedex[self.get_name()]["attack"])
        self.set_evolution(pokedex.data_pokedex[self.get_name()]["evolution"])
        self.set_front_sprite(pokedex.data_pokedex[self.get_name()]["front_sprite"])
        self.set_back_sprite(pokedex.data_pokedex[self.get_name()]["back_sprite"])