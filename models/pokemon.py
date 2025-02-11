class Pokemon:    
    def __init__(self, name, level, types, hp, attack, evolves_into=None):
        self.__name = name
        self.__level = level
        self.__xp = 0
        self.__types = types
        self.__hp = hp
        self.__attack = attack
        self.__savage = True
        self.__evolves_into = evolves_into
    
    # Getters
    def get_name(self):
        return self.__name
    
    def get_level(self):
        return self.__level
    
    def get_xp(self):
        return self.__xp
    
    def get_types(self):
        return self.__types
    
    def get_hp(self):
        return self.__hp
    
    def get_attack(self):
        return self.__attack
    
    def get_savage(self):
        return self.__savage
    
    def get_evolves_into(self):
        return self.__evolves_into
    
    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_level(self, level):
        self.__level = level

    def set_xp(self, xp):
        self.__hp = xp

    def set_types(self, types):
        self.__types = types

    def set_hp(self, hp):
        self.__hp = hp
    
    def set_attack(self, attack):
        self.__attack = attack
    
    def set_savage(self, savage):
        self.__savage = savage
    
    def set_evolves_into(self, evolves_into):
        self.__evolves_into = evolves_into
    

    def evolve(self):
        if self.__evolves_into:
            if self.__level >= self.__evolves_into[0]:
                self.__name = self.__evolves_into[1]
                self.__types = None  # recuperer les données de l'evolution dans 'pokemon.json'
                self.__hp = None
                self.__attack = None
                self.__evolves_into = None
                print(f"{self.__name} has evolved!")
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
        print(f"Hit Points: {self.__hp}")
        print(f"Level: {self.__level}")
        print(f"Attack Power: {self.__attack}")
        print(f"Types: {', '.join(self.__types)}")
        if self.__evolves_into:
            print(f"Evolves into: {self.__evolves_into}")
        else:
            print("This Pokémon cannot evolve.")
