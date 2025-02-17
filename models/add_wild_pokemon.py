import os
# config = "../config.py"
from config import *
from .game_state import GameState
from .button import Button
from .display_pokemon import DisplayPokemon
from .pokemon_dictionary import all_pokemons

class AddWildPokemon(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="Pokemon_bg1.webp")
        self.caption = "Welcome Menu"
        
        self.font = pygame.font.Font("assets/pokemon_classic.ttf", 15)
        
        self.menu_background = pygame.Surface((WIDTH*0.9, HEIGHT*0.9), pygame.SRCALPHA)
        self.menu_background.fill(FADE_WHITE)
        
    def draw_text(self, text, x, y):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, BLACK)
        self.app.screen.blit(text_surface, (x, y))


    def draw_unused_pokemon(self, x, y):
        unused_pokemon = all_pokemons.get_unused_pokemons()
    
        for name in unused_pokemon:
            if y <= HEIGHT*0.9 - 30:
                self.draw_text(name, x, y)
                y += 30
            else:
                self.draw_text(name, x, y)
                y = HEIGHT*0.05
                y += 30
                x += 200      

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.app.screen.blit(self.menu_background, (WIDTH*0.05, HEIGHT*0.05)) # Draw menu rectangle
        self.draw_unused_pokemon(WIDTH*0.05 + 50, HEIGHT*0.05 + 30)