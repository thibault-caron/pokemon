import random, json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    # Type effectiveness table (attack multiplier)
    type_chart = json.load(open('coefficient.json'))

    # Method to apply type effectiveness and calculate the attack damage
    def calculate_damage(self, attacker, defender):
        attacker_type = attacker.get_types()[0] 
        defender_type = defender.get_types()[0]
        
        # Check for type effectiveness
        multiplier = 1.0  
        if (attacker_type, defender_type) in self.type_chart:
            multiplier = self.type_chart[(attacker_type, defender_type)]
        elif (defender_type, attacker_type) in self.type_chart:
            multiplier = self.type_chart[(defender_type, attacker_type)]
        
        # Calculate damage: attack power * type multiplier
        attack_power = attacker.get_attack_power()
        damage = attack_power * multiplier
        print(f"{attacker.get_name()} attacks {defender.get_name()} for {damage} damage (Multiplier: {multiplier})")
        return damage

    def apply_defense(self, defender, damage):
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
