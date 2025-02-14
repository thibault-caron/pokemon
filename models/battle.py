import random, json
from pokemon import Pokemon
from database import Database

class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        # self.type_chart = Database().read_json()
    # Type effectiveness table (attack multiplier)


    # Method to apply type effectiveness and calculate the attack damage
    def calculate_damage(self, attacker, defender):
        attacker_type = attacker.get_types()[0] 
        defender_type = defender.get_types()[0]
        
        # Check for type effectiveness
        multiplier = 1.0
        for attack_key in type_chart:
            if attacker_type == attack_key:
                for defense_key in type_chart[attack_key]:
                    if defender_type == defense_key:
                        multiplier = type_chart[attack_key][defense_key]
                        print(multiplier)

        # Calculate damage: attack power * type multiplier
        attack = attacker.get_attack()
        damage = attack * multiplier
        print(f"{attacker.get_name()} attacks {defender.get_name()} for {damage} damage (Multiplier: {multiplier})")
        # return damage

    def inflict_damage(self, defender, damage):
        """Method to apply defense and deduct life points"""
        defender.set_hp(defender.get_hp() - damage)
        print(f"{defender.get_name()} takes {damage} damage after defense. Remaining HP: {defender.get_hp()}")

    def determine_winner(self):
        """Method to determine the winner"""
        if self.pokemon1.get_hp() > 0 and self.pokemon2.get_hp() <= 0:
            return self.pokemon1.get_name()
        elif self.pokemon2.get_hp() > 0 and self.pokemon1.get_hp() <= 0:
            return self.pokemon2.get_name()
        else:
            return "Draw"
    
    def get_battle_outcome(self):
        """Method to determine the names of the winner and loser"""
        winner = self.determine_winner()
        if winner == "Draw":
            return "It's a draw!"
        if winner == self.pokemon1.get_name():
            loser = self.pokemon2.get_name()
        else:
            loser = self.pokemon1.get_name()  
        return f"Winner: {winner}, Loser: {loser}"

    def record_encounter(self, pokemon):
        """Method to record encountered Pokémon in the Pokédex"""
        if pokemon.get_name() not in [p.get_name() for p in self.pokedex]:
            self.pokedex.append(pokemon)
            print(f"{pokemon.get_name()} added to Pokédex.")
        else:
            print(f"{pokemon.get_name()} is already in the Pokédex.")


if __name__ == '__main__':
    type_chart = Database().read_json()
    print(type_chart)
    poke1 = Pokemon("Pikachu", 1)
    poke2 = Pokemon("Caterpie", 1)
    test_battle = Battle(poke1, poke2)
    test_battle.calculate_damage(poke1, poke2)
