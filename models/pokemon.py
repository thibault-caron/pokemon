class Pokemon:
    def __init__(self, name, hit_points, level, attack, defense, types, evolves_into=None):
        self._name = name
        self._hit_points = hit_points
        self._level = level
        self._attack = attack
        self._defense = defense
        self._types = types
        self._evolves_into = evolves_into
    
    # Getters
    def get_name(self):
        return self._name
    
    def get_hit_points(self):
        return self._hit_points
    
    def get_level(self):
        return self._level
    
    def get_attack(self):
        return self._attack
    
    def get_defense(self):
        return self._defense
    
    def get_types(self):
        return self._types
    
    def get_evolves_into(self):
        return self._evolves_into
    
    # Setters
    def set_name(self, name):
        self._name = name
    
    def set_hit_points(self, hit_points):
        self._hit_points = hit_points
    
    def set_level(self, level):
        self._level = level
    
    def set_attack(self, attack):
        self._attack = attack
    
    def set_defense(self, defense):
        self._defense = defense
    
    def set_types(self, types):
        self._types = types
    
    def set_evolves_into(self, evolves_into):
        self._evolves_into = evolves_into
    

    def evolve(self):
        if self._evolves_into:
            self._name = self._evolves_into
            print(f"{self._name} has evolved!")
        else:
            print(f"{self._name} cannot evolve.")
    

    def display_info(self):
        """Display Pokémon's details"""
        print(f"Name: {self._name}")
        print(f"Hit Points: {self._hit_points}")
        print(f"Level: {self._level}")
        print(f"Attack Power: {self._attack}")
        print(f"Defense: {self._defense}")
        print(f"Types: {', '.join(self._types)}")
        if self._evolves_into:
            print(f"Evolves into: {self._evolves_into}")
        else:
            print("This Pokémon cannot evolve.")
