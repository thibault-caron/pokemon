from .config import *
from .pokemon import Pokemon
from .game_state import GameState

class DisplayPokemon:
    def __init__(self, name, x, y, width, height, app, onclickFunction=None, onePress=False):
        self.app = app
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.pokemon = Pokemon(name, level=1)
        
        self.font = pygame.font.Font(None, 30)
    
    
    '''Get pokemon infos'''    
    def get_pokemon_name(self):
        return self.pokemon.get_name()
        
    def get_pokemon_type(self):
        return self.pokemon.get_types()
        
    def get_pokemon_hp(self):
        return self.pokemon.get_hp()
        
    def get_pokemon_level(self):
        return self.pokemon.get_level()
        
    def get_pokemon_attack(self):
        return self.pokemon.get_attack()
    
    def get_pokemon_front_sprite(self):
        return self.pokemon.get_front_sprite()
    
    def get_pokemon_backsprite(self):
        return self.pokemon.get_back_sprite()
    
    '''Draw pokemon info'''
    def draw_text(self, text, x, y):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, (0, 0, 0))
        self.app.screen.blit(text_surface, (x, y))

    def draw_image(self, image_path, x, y):
        """ Allow to draw a sprite """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (self.width, self.height))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")
    
    def draw_pokemon_name(self, x, y):
        self.draw_text(self.get_pokemon_name(), x, y)

    def draw_pokemon_type(self, x, y):
        self.draw_text(", ".join(self.get_pokemon_type()), x, y)

    def draw_pokemon_hp(self, x, y):
        self.draw_text(f"HP: {self.get_pokemon_hp()}", x, y)

    def draw_pokemon_level(self, x, y):
        self.draw_text(f"Level: {self.get_pokemon_level()}", x, y)

    def draw_pokemon_attack(self, x, y):
        self.draw_text(f"Attack: {self.get_pokemon_attack()}", x, y)

    def draw_pokemon_front_sprite(self, x, y):
        self.draw_image(self.get_pokemon_front_sprite(), x, y)

    def draw_pokemon_back_sprite(self, x, y):
        self.draw_image(self.get_pokemon_back_sprite(), x, y)
    
    def draw_card(self):
        self.draw_pokemon_name(100, 100)
        self.draw_pokemon_type(100, 130)
        self.draw_pokemon_hp(100, 160)
        self.draw_pokemon_level(100, 190)
        self.draw_pokemon_attack(100, 220)
        