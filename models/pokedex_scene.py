import os

from config import *
from .game_state import GameState
from .pokemon_dictionary import all_pokemons
from .pokedex import pokedex

class PokedexScene(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokedex.jpg")
        self.caption = "Show pokedex"
        
        self.font = pygame.font.Font("assets/pokemon_classic.ttf", 15)
               
        # self.menu_background = pygame.Surface((WIDTH*0.9, HEIGHT*0.9), pygame.SRCALPHA)
        # self.menu_background.fill(FADE_WHITE)
        
        self.message = ""
        self.message_time = 0
        
    def draw_text(self, text, x, y):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, BLACK)
        self.app.screen.blit(text_surface, (x, y))


    def draw_pokedex(self, x, y):
        list_player_pokemon = pokedex.list_pokemons()
        
        for pokemon in list_player_pokemon:
            self.draw_text(pokemon, x, y)           
            
            y += 30
            
            if y > HEIGHT*0.9 - 30:
                y = HEIGHT*0.05
                y += 30
                x += 270

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        # self.app.screen.blit(self.menu_background, (WIDTH*0.05, HEIGHT*0.05)) # Draw menu rectangle
        self.draw_pokedex(WIDTH*0.26, HEIGHT*0.18)