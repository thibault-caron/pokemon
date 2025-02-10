class Pokemon:
    # Set coefficient
    coefficient = {
       "normal" :{
           "immunes":["Ghost"],
           "weaknesses":["Rock","Steel"],
           "strengths":[]
       },
       "Fire" : {
           "immunes":[],
           "weaknesses":["Fire","Water","Rock","Dragon"],
           "strengths":["Grass","Ice","Bug","Steel"]
       },
       "Water" : {
           "immunes":[],
           "weaknesses":["Water","Grass","Dragon"],
           "strengths":["Fire","Ground","Rock"]
       },
       "Electric" : {
           "immunes":["Ground"],
           "weaknesses":["Electric","Grass","Dragon"],
           "strengths":["Water","Flying"]
       },
       "Grass" : {
          "immunes":[],
          "weaknesses":["Fire","Grass","Poison","Flying","Bug","Dragon","Steel"],
          "strengths":["Water","Ground","Rock"] 
       },
       "Ice" : {
           "immunes":[],
           "weaknesses":["Fire","Water","Ice","Steel"],
           "strengths":["Grass","Ground","Flying","Dragon"]
       },
       "Fighting" : {
           "immunes":["Ghost"],
           "weaknesses":["Poison","Flying","Psychic","Bug","Fairy"],
           "strengths":["Normal","Ice","Rock","Dark","Steel"]
       },
       "Poison" : {
           "immunes":["Steel"],
           "weaknesses":["Poison","Ground","Rock","Ghost"],
           "strengths":["Grass","Fairy"]
       },
       "Ground" : {
           "immunes":["Flying"],
           "weaknesses":["Grass","Bug"],
           "strengths":["Fire","Electric","Poison","Rock","Steel"]
       },
       "Flying" : {
           "immunes":[],
           "weaknesses":["Electric","Rock","Steel"],
           "strengths":["Grass","Fighting","Bug"]
       },
       "Psychic" : {
           "immunes":["Dark"],
           "weaknesses":["Psychic","Steel"],
           "strengths":["Fighting","Poison"]
       },
       "Bug" : {
           "immunes":[],
           "weaknesses":["Fire","Fighting","Poison","Flying","Ghost","Steel","Fairy"],
           "strengths":["Grass","Psychic","Dark"]
       },
       "Rock" : {
           "immunes":[],
           "weaknesses":["Fighting","Ground","Steel"],
           "strengths":["Fire","Ice","Flying","Bug"]
       },
       "Ghost" : {
           "immunes":["Normal"],
           "weaknesses":["Dark"],
           "strengths":["Psychic","Ghost"]
       },
       "Dragon" : {
           "immunes":["Fairy"],
           "weaknesses":["Steel"],
           "strengths":["Dragon"]
       },
       "Dark" : {
           "immunes":[],
           "weaknesses":["Fighting","Dark","Fairy"],
           "strengths":["Psychic","Ghost"]
       },
       "Steel" : {
           "immunes":[],
           "weaknesses":["Fire","Water","Electric","Steel"],
           "strengths":["Ice","Rock","Fairy"]
       },
       "Fairy" : {
           "immunes":[],
           "weaknesses":["Fire","Poison","Steel"],
           "strengths":["Fighting","Dragon","Dark"]
       }
       
    }
    
    def __init__(self, name, level, hit_points, attack, defense, types, evolves_into=None):
        self._name = name
        self._level = level
        self._hit_points = hit_points
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
        """Display the Pokémon's details"""
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
