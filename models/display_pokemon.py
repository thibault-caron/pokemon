from config import *
from .pokemon import Pokemon
from .button import Button
from .pokedex import pokedex
from .pokemon_dictionary import PokemonDictionary, all_pokemons

class DisplayPokemon():
    def __init__(self, pokemon, x, y, width, height, app, onclickFunction=None, onePress=False):
        # super().__init__(self)
        self.app = app
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.pokemon = pokemon
        
        self.font = pygame.font.Font("assets/pokemon_classic.ttf", 15)
        
        self.button = Button(self.x + 120, self.y + 130, 250, 50, 'Choose me', self.battle, screen=self.app.screen) 
    
    '''Get pokemon infos'''    
    # def get_pokemon_name(self):
    #     return self.pokemon.get_name()
        
    # def get_pokemon_type(self):
    #     types = " ".join(self.pokemon.get_types())
    #     return types
        
    # def get_pokemon_hp(self):
    #     return self.pokemon.get_hp()
        
    # def get_pokemon_level(self):
    #     return self.pokemon.get_level()
        
    # def get_pokemon_attack(self):
    #     return self.pokemon.get_attack()
    
    # def get_pokemon_front_sprite(self):
    #     return self.pokemon.get_front_sprite()
    
    # def get_pokemon_back_sprite(self):
    #     return self.pokemon.get_back_sprite()
    
    '''Draw pokemon info'''
    def draw_text(self, text, x, y):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, WHITE)
        self.app.screen.blit(text_surface, (x, y))

    def draw_image(self, image_path, x, y):
        """ Allow to draw a sprite """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (110, 110))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")
    
    def draw_pokemon_name(self, x, y):
        self.draw_text(self.pokemon.get_name(), x, y)

    def draw_pokemon_type(self, x, y):
        types = " ".join(self.pokemon.get_types())
        self.draw_text(f"Type: {types}", x, y)

    def draw_pokemon_hp(self, x, y):
        self.draw_text(f"HP: {self.pokemon.get_hp()}", x, y)

    def draw_pokemon_max_hp(self, x, y):
        self.draw_text(f"HP: {self.pokemon.get_max_hp()}", x, y)

    def draw_pokemon_level(self, x, y):
        self.draw_text(f"Level: {self.pokemon.get_level()}", x, y)

    def draw_pokemon_xp(self, x, y):
        self.draw_text(f"Level: {self.pokemon.get_xp()}", x, y)

    def draw_pokemon_attack(self, x, y):
        self.draw_text(f"Attack: {self.pokemon.get_attack()}", x, y)

    def draw_pokemon_front_sprite(self, x, y):
        self.draw_image(self.pokemon.get_front_sprite(), x, y)

    def draw_pokemon_back_sprite(self, x, y):
        self.draw_image(self.pokemon.get_back_sprite(), x, y)
        
    def draw_card_background(self, x, y):
        image = pygame.image.load("assets/images/card.png")
        image = pygame.transform.scale(image, (self.width, self.height))
        self.app.screen.blit(image, (x, y))
    
    def draw_card(self):       
        self.draw_card_background(self.x, self.y)
        self.draw_pokemon_name(self.x + 10, self.y + 10)
        self.draw_pokemon_type(self.x + self.width - 235, self.y + 10)
        self.draw_pokemon_hp(self.x + 10, self.y + 35)
        self.draw_pokemon_level(self.x + self.width - 235, self.y + 35)
        self.draw_pokemon_attack(self.x + 10, self.y + 60)
        self.draw_pokemon_front_sprite(self.x + 10, self.y + 100)
        self.button.process()
        
        
    '''Action'''
    def battle(self):
        """Go to battle menu and add chosen pokemon"""
        pokedex.clear_pokedex()
        pokedex.add_pokemon(self.pokemon)  # Add chosen pokemon in pokedex

        self.app.state_manager.set_state("battle menu")  # Change game_state to battle scene
        