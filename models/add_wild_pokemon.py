import os
import time
from config import *
from .game_state import GameState
from .button import Button
from .pokemon import Pokemon
from .display_pokemon import DisplayPokemon
from .pokemon_dictionary import all_pokemons

class AddWildPokemon(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="Pokemon_bg1.webp")
        self.caption = "Add wild pokemon"
        
        self.font = pygame.font.Font("assets/pokemon_classic.ttf", 15)
        
        self.buttons = []
        self.back_button = Button(WIDTH*0.95, HEIGHT*0.95, 40, 40, "Back", lambda: self.app.state_manager.set_state("welcome"), screen=self.app.screen)

        self.menu_background = pygame.Surface((WIDTH*0.9, HEIGHT*0.9), pygame.SRCALPHA)
        self.menu_background.fill(FADE_WHITE)
        
        self.message = ""
        self.message_time = 0
        
    def draw_text(self, text, x, y):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, BLACK)
        self.app.screen.blit(text_surface, (x, y))


    def draw_unused_pokemon(self, x, y):
        unused_pokemons = all_pokemons.get_pokemon_by_state("unused")
        self.buttons.clear()
        
        for name in unused_pokemons:
            button = Button(x, y, 180, 30, name, lambda name=name: self.change_state(name), screen=self.app.screen)
            self.buttons.append(button)
            
            y += 70
            
            if y > HEIGHT*0.9 - 70:
                y = HEIGHT*0.05
                y += 30
                x += 270      

    def change_state(self, name):
        """"""
        all_pokemons.set_pokemon_used(name)
        all_pokemons.write_json(all_pokemons.data_pokemons)
        self.draw_unused_pokemon(WIDTH*0.05 + 50, HEIGHT*0.05 + 30) # draw buttons with wild avaible pokemons names
        self.display_text(name)
        
    def display_text(self, name):
        self.message = f"{name} has been released in the wild"
        self.message_time = pygame.time.get_ticks() + 5000

    def display_wild_details(self, pokemon_name):
        """"""
        displayed_pokemon = Pokemon(pokemon_name)
        pokemon_card = DisplayPokemon(displayed_pokemon, WIDTH-350, HEIGHT-250, 350, 110, app=self.app)
        pokemon_card.draw_wild_card()

    def process_hover(self, button):
        mousePos = pygame.mouse.get_pos()
        
        if button.buttonRect.collidepoint(mousePos):
            self.display_wild_details(button.text)

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.app.screen.blit(self.menu_background, (WIDTH*0.05, HEIGHT*0.05)) # Draw menu rectangle
        self.draw_unused_pokemon(WIDTH*0.05 + 50, HEIGHT*0.05 + 30)

        self.back_button.process()
        
        for button in self.buttons:
            button.process()
            self.process_hover(button)
            
        if pygame.time.get_ticks() < self.message_time:
            self.draw_text(self.message, WIDTH*0.05 + 50, HEIGHT*0.9 - 20)