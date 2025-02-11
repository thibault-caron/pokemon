class Pokemon:    
    def __init__(self, name, level, hit_points, attack, defense, types, evolves_into=None):
        self.__name = name
        self.__level = level
        self.__hit_points = hit_points
        self.__attack = attack
        self.__defense = defense
        self.__types = types
        self.__evolves_into = evolves_into
    
    # Getters
    def get_name(self):
        return self.__name
    
    def get_hit_points(self):
        return self.__hit_points
    
    def get_level(self):
        return self.__level
    
    def get_attack(self):
        return self.__attack
    
    def get_defense(self):
        return self.__defense
    
    def get_types(self):
        return self.__types
    
    def get_evolves_into(self):
        return self.__evolves_into
    
    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_hit_points(self, hit_points):
        self.__hit_points = hit_points
    
    def set_level(self, level):
        self.__level = level
    
    def set_attack(self, attack):
        self.__attack = attack
    
    def set_defense(self, defense):
        self.__defense = defense
    
    def set_types(self, types):
        self.__types = types
    
    def set_evolves_into(self, evolves_into):
        self.__evolves_into = evolves_into
    

    def evolve(self):
        if self.__evolves_into:
            self.__name = self.__evolves_into
            print(f"{self.__name} has evolved!")
        else:
            print(f"{self.__name} cannot evolve.")
    

    def display_info(self):
        """Display the Pokémon's details"""
        print(f"Name: {self.__name}")
        print(f"Hit Points: {self.__hit_points}")
        print(f"Level: {self.__level}")
        print(f"Attack Power: {self.__attack}")
        print(f"Defense: {self.__defense}")
        print(f"Types: {', '.join(self.__types)}")
        if self.__evolves_into:
            print(f"Evolves into: {self.__evolves_into}")
        else:
            print("This Pokémon cannot evolve.")
