import pygame

from random import random
from .pokemon import Pokemon
from .database import Database
from .pokedex import pokedex
from .display_pokemon import DisplayPokemon

class Battle:
    """ Class to manage the battle. """
    def __init__(self, player_pokemon, wild_pokemon):
        """
        Initialisation of the class.
        :param player_pokemon: The player pokemon choose for the battle.
        :param wild_pokemon: A wild pokemon encountered.
        """
        self.player_pokemon = player_pokemon
        self.wild_pokemon = wild_pokemon
        self.multiplier = 1.0
        
        self.message = ""
        self.message_time = 0

    def calculate_multiplier(self, attacker, defender):
        """
        Calculate attack multiplier.
        :param attacker: Pokemon attacking.
        :param defender: Pokemon defending.
        :return: Global attack multiplier.
        """
        def single_type_multiplier(attacker_type, defender_type):
            """
            Check the multiplier of one single type couple.
            :param attacker_type: The attacker type.
            :param defender_type: The defender type.
            :return: Single type couple multiplier.
            """
            for attack_key in type_chart:
                if attacker_type == attack_key:
                    for defense_key in type_chart[attack_key]:
                        if defender_type == defense_key:
                            return type_chart[attack_key][defense_key]

        attacker_type_0 = attacker.get_types()[0]
        defender_type_0 = defender.get_types()[0]
        multiplier_1 = single_type_multiplier(attacker_type_0, defender_type_0)

        if len(attacker.get_types()) > 1:  # Check if attacker pokemon have two types.
            attacker_type_1 = attacker.get_types()[1]
            defender_type_1 = defender.get_types()[1]
            multiplier_2 = single_type_multiplier(attacker_type_1, defender_type_1)
            self.multiplier = multiplier_1 * multiplier_2  # Global multiplier of two types pokemon.
        else:
            self.multiplier = multiplier_1  # Global multiplier of a single type pokemon.

    def inflict_damage(self, attacker, defender):
        """
        Inflict damages to the defender.
        :param attacker: Pokemon attacking.
        :param defender: Pokemon defending.
        :return: ∅
        """
        attack = attacker.get_attack()
        random_power = random()
        if random_power < 0.11:
            damage_efficiency = 0
        elif random_power > 0.90:
            damage_efficiency = 1.5
        else:
            damage_efficiency = 1

        damage = attack * self.multiplier * damage_efficiency

        if damage_efficiency == 1:
            self.message = f"{attacker.get_name()} attacks {defender.get_name()} for {damage} damage\nMultiplier: {self.multiplier}" 
 
        elif damage_efficiency == 1.5:
            self.message = f"CRITICAL STRIKE! {attacker.get_name()} attacks {defender.get_name()} for {damage} damage\nMultiplier: {self.multiplier}"

        elif damage_efficiency == 0:
            self.message = f"{attacker.get_name()} missed its attacks!"
            

        defender.set_hp(defender.get_hp() - damage)
        self.message = f"{defender.get_name()} takes {damage} damage after defense. Remaining HP: {defender.get_hp()}"

    def check_victory(self):
        """
        Check if someone as win the battle this turn.
        :return: The result of the battle turn.
        """
        result = "ongoing"
        if self.player_pokemon.get_hp() > 0 >= self.wild_pokemon.get_hp():
            result = "victory"
            self.message = f"Winner: {self.player_pokemon.get_name()}, Loser: {self.wild_pokemon.get_name()}"
        elif self.wild_pokemon.get_hp() > 0 >= self.player_pokemon.get_hp():
            result = "defeat"
            self.message = f"Winner: {self.wild_pokemon.get_name()}, Loser: {self.player_pokemon.get_name()}"
        else:
            result = "ongoing"
        return result
    
    def end_battle(self):
        end = False

        if self.check_victory() == "victory":
            self.player_pokemon.gain_xp(self.wild_pokemon)
            self.player_pokemon.level_up()
            # ajouter condition 'si le pokemon (name) n'est pas dans pokedex
            self.wild_pokemon.set_hp(self.wild_pokemon.get_max_hp())
            pokedex.add_pokemon(self.wild_pokemon) # Add chosen pokemon in pokedex
            # self.app.state_manager.set_state("battle menu")
            end = True
        
        elif self.check_victory() == "defeat":
            pokedex.remove_pokemon(self.player_pokemon)
            # self.app.state_manager.set_state("battle menu")
            end = True
        
        return end

    def turn(self):
        """
        Play a battle turn.
        :return: The victory.
        """
        victory = None
        self.inflict_damage(self.player_pokemon, self.wild_pokemon)  # Player pokemon attack
        if self.check_victory() == "ongoing":
            self.inflict_damage(self.wild_pokemon, self.player_pokemon)  # Wild pokemon attack
            if self.check_victory() == "defeat":
                victory = self.wild_pokemon.get_name()
        else:
            victory = self.player_pokemon.get_name()
        return victory

if __name__ == '__main__':

    type_chart = Database().read_json()
    poke1 = Pokemon("Pikachu", 1)
    poke2 = Pokemon("Caterpie", 1)
    test_battle = Battle(poke1, poke2)

    victory = 0
    n = 1
    while not isinstance(victory, str):
        print(f"\nTour {n}")
        victory = test_battle.turn()
        n += 1
