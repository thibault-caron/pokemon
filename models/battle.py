from random import random

from config import *

from .database import Database
from .pokedex import pokedex


class Battle:
    """ Class to manage the battle. """
    def __init__(self, player_pokemon, wild_pokemon):
        """
        Initialization of the class.
        :param player_pokemon: The player pokemon choose for the battle.
        :param wild_pokemon: A wild pokemon encountered.
        """
        self.player_pokemon = player_pokemon
        self.wild_pokemon = wild_pokemon
        self.multiplier = 1.0
        self.type_chart = Database().read_json()
        
        self.damage_player_message = ""
        self.damage_enemy_message = ""
        self.winner_message = ""
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
            for attack_key in self.type_chart:
                if attacker_type == attack_key:
                    for defense_key in self.type_chart[attack_key]:
                        if defender_type == defense_key:
                            return self.type_chart[attack_key][defense_key]

        attacker_type_0 = attacker.get_types()[0]
        defender_type_0 = defender.get_types()[0]
        attack1_1 = single_type_multiplier(attacker_type_0, defender_type_0)

        if len(attacker.get_types()) > 1:  # Check if attacker pokemon have two types.
            attacker_type_1 = attacker.get_types()[1]
            attack2_1 = single_type_multiplier(attacker_type_1, defender_type_0)

            if len(defender.get_types()) > 1:  # Check if defender pokemon have two types.
                defender_type_1 = defender.get_types()[1]
                attack1_2 = single_type_multiplier(attacker_type_0, defender_type_1)
                attack2_2 = single_type_multiplier(attacker_type_1, defender_type_1)

                # for each type of the defender, the attacker attack with its best type
                self.multiplier = max(attack1_1, attack2_1) * max(attack1_2, attack2_2)

            else:
                self.multiplier = max(attack1_1, attack2_1)  # the defender has 1 type, the attacker attack with its best type
        else:
            self.multiplier = attack1_1  # Global multiplier of single type pokemon.
        
        # if self.multiplier < 0.5:
        #     self.multiplier = 0.5
        return self.multiplier

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

        damage = attack * self.calculate_multiplier(attacker, defender) * damage_efficiency

        if damage_efficiency == 1:
            damage_message = f"{attacker.get_name()} attacks {defender.get_name()} for {damage} damage\nMultiplier: {self.multiplier}" 
 
        elif damage_efficiency == 1.5:
            damage_message = f"CRITICAL STRIKE! {attacker.get_name()} attacks {defender.get_name()} for {damage} damage\nMultiplier: {self.multiplier}"

        elif damage_efficiency == 0:
            damage_message = f"{attacker.get_name()} missed its attacks!"
            
        new_hp = defender.get_hp() - damage
        if new_hp < 0:
            new_hp = 0
        defender.set_hp(new_hp)

        return damage, damage_message

    def check_victory(self):
        """
        Check if someone as win the battle this turn.
        :return: The result of the battle turn.
        """
        result = "ongoing"
        if self.player_pokemon.get_hp() > 0 >= self.wild_pokemon.get_hp():
            result = "victory"
            self.winner_message = f"Winner: {self.player_pokemon.get_name()}, Loser: {self.wild_pokemon.get_name()}"
        elif self.wild_pokemon.get_hp() > 0 >= self.player_pokemon.get_hp():
            result = "defeat"
            self.winner_message = f"Winner: {self.wild_pokemon.get_name()}, Loser: {self.player_pokemon.get_name()}"
        else:
            result = "ongoing"
        return result
    
    def end_battle(self):
        """
        Check if battle is finished.
        :return: End battle status.
        """
        end = False

        if self.check_victory() == "victory":
            self.player_pokemon.gain_xp(self.wild_pokemon)
            self.player_pokemon.level_up()
            self.player_pokemon.set_hp(self.player_pokemon.get_max_hp())
            self.player_pokemon.evolve()
            pokedex.add_pokemon(self.player_pokemon)

            # ajouter condition 'si le wild_pokemon (name) n'est pas dans pokedex'
            self.wild_pokemon.set_hp(self.wild_pokemon.get_max_hp())
            pokedex.add_pokemon(self.wild_pokemon)  # Add chosen pokemon in pokedex
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
        player_damage, self.damage_player_message = self.inflict_damage(self.player_pokemon, self.wild_pokemon)  # Player pokemon attack
        
        if self.check_victory() == "ongoing":
            enemy_damage, self.damage_enemy_message = self.inflict_damage(self.wild_pokemon, self.player_pokemon)  # Wild pokemon attack
            
            if self.check_victory() == "defeat":
                victory = self.wild_pokemon.get_name()
        else:
            victory = self.player_pokemon.get_name()
        return victory
