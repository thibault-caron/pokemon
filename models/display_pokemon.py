from config import *
from .button import Button
from .pokedex import pokedex
from .pokemon_dictionary import all_pokemons

class DisplayPokemon():
    def __init__(self, pokemon, x, y, width, height, app, onclickFunction=None, onePress=False):
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
 
    '''Draw pokemon info'''
    def draw_text(self, text, x, y, color = WHITE):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, color)
        self.app.screen.blit(text_surface, (x, y))

    def draw_image(self, image_path, x, y):
        """ Allow to draw a sprite """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (110, 110))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")
            
    def draw_battle_image(self, image_path, x, y):
        """ Allow to draw a sprite """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (400, 400))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")
            
    def draw_pokedex_image(self, image_path, x, y):
        """ Allow to draw a sprite """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (250, 250))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")
    
    def draw_pokemon_name(self, x, y, color = WHITE):
        self.draw_text(self.pokemon.get_name(), x, y, color)

    def draw_pokemon_type(self, x, y, color = WHITE):
        types = "/".join(self.pokemon.get_types())
        self.draw_text(f"Type: {types}", x, y, color)

    def draw_pokemon_hp(self, x, y, color = WHITE):
        self.draw_text(f"{round(self.pokemon.get_hp())}", x, y, color)

    def draw_pokemon_max_hp(self, x, y, color = WHITE):
        self.draw_text(f"{self.pokemon.get_max_hp()}", x, y, color)

    def draw_pokemon_level(self, x, y, color = WHITE):
        self.draw_text(f"Level: {self.pokemon.get_level()}", x, y, color)

    def draw_pokemon_xp(self, x, y, color = WHITE):
        self.draw_text(f"{self.pokemon.get_xp()}", x, y, color)
        
    def draw_pokemon_max_xp(self, x, y, color = WHITE):
        self.draw_text(f"{self.pokemon.get_level()*4}", x, y, color)

    def draw_pokemon_attack(self, x, y, color = WHITE):
        self.draw_text(f"Attack: {self.pokemon.get_attack()}", x, y, color)

    def draw_pokemon_front_sprite(self, x, y, color = WHITE):
        self.draw_image(self.pokemon.get_front_sprite(), x, y)

    def draw_pokemon_back_sprite(self, x, y):
        self.draw_image(self.pokemon.get_back_sprite(), x, y)
        
    def draw_battle_pokemon_front_sprite(self, x, y):
        self.draw_battle_image(self.pokemon.get_front_sprite(), x, y)

    def draw_battle_pokemon_back_sprite(self, x, y):
        self.draw_battle_image(self.pokemon.get_back_sprite(), x, y)
        
    def draw_pokedex_front_sprite(self, x, y):
        self.draw_pokedex_image(self.pokemon.get_front_sprite(), x, y)
        
    def draw_card_background(self, x, y):
        image = pygame.image.load("assets/images/card.png")
        image = pygame.transform.scale(image, (self.width, self.height))
        self.app.screen.blit(image, (x, y))
        
    def draw_battle_card_background(self, x, y):
        image = pygame.image.load("assets/images/battle_card.png")
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
        
    def draw_battle_card(self):       
        self.draw_battle_card_background(self.x, self.y)
        self.draw_pokemon_name(self.x + 30, self.y + 10, BLACK)
        self.draw_pokemon_level(self.x + self.width - 160, self.y + 10, BLACK)
        if self.pokemon.get_hp() >= 100:
            self.draw_text("HP: ", self.x + 30, self.y + 35, BLACK)
            self.draw_pokemon_hp(self.x + 80, self.y + 35, BLACK)
        elif self.pokemon.get_hp() < 100:
            self.draw_text("HP: ", self.x + 30, self.y + 35, BLACK)
            self.draw_pokemon_hp(self.x + 95, self.y + 35, BLACK)
        self.draw_text("/", self.x + 125, self.y + 35, BLACK)
        self.draw_pokemon_max_hp(self.x + 135, self.y + 35, BLACK)
        self.draw_text("XP: ", self.x + 30, self.y + 60, BLACK)
        self.draw_pokemon_xp(self.x + 110, self.y + 60, BLACK) 
        self.draw_text("/", self.x + 125, self.y + 60, BLACK)
        self.draw_pokemon_max_xp(self.x + 140, self.y + 60, BLACK)
        
    def draw_pokedex_card(self):       
        self.draw_card_background(self.x, self.y)
        self.draw_pokemon_name(self.x + 10, self.y + 10)
        self.draw_pokemon_type(self.x + self.width - 265, self.y + 10)
        self.draw_pokemon_hp(self.x + 10, self.y + 55)
        self.draw_pokemon_level(self.x + self.width - 265, self.y + 55)
        self.draw_pokemon_attack(self.x + 10, self.y + 100)
        self.draw_pokedex_front_sprite(self.x + 5, self.y + 110)    
        
    '''Action'''
    def battle(self):
        """Go to battle menu and add chosen pokemon"""
        pokedex.clear_pokedex()
        pokedex.add_pokemon(self.pokemon)  # Add chosen pokemon in pokedex

        self.app.state_manager.set_state("battle menu")  # Change game_state to battle scene
        