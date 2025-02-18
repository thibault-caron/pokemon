import os

from config import *
from .game_state import GameState
from .button import Button
from .pokemon import Pokemon, PlayerPokemon
from .battle import Battle
from .display_pokemon import DisplayPokemon
from .pokedex import pokedex

class BattleScene(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="battle_background.webp")
        self.caption = "Battle"


        # get player_poke name
        pp_name = ""
        pp_list = pokedex.list_pokemons()
        pp_name = pp_list[0]
        print(pp_name)
        print(pokedex.data_pokedex[pp_name]["types"])
        self.player_pokemon = PlayerPokemon(pp_name)
        self.wild_pokemon = Pokemon("Caterpie", 1)
        self.battle = Battle(self.player_pokemon, self.wild_pokemon)
        
        self.font = pygame.font.Font(None, 50)

        self.button1 = Button(50, 650, 200, 50, "Attack", self.attack, screen=self.app.screen)
        self.button2 = Button(450, 650, 300, 50, "Change Pokemon", self.change_pokemon, screen=self.app.screen)
        self.button3 = Button(950, 650, 200, 50, "Run", self.run, screen=self.app.screen)
        self.buttons = [self.button1, self.button2, self.button3]
        
        self.enemy_display = DisplayPokemon(self.wild_pokemon, 100, 100, WIDTH, HEIGHT, app=self.app)
        self.player_display = DisplayPokemon(self.player_pokemon, 700, 100, WIDTH, HEIGHT, app=self.app)
        
        self.enemy_card = DisplayPokemon(self.wild_pokemon, WIDTH * 0.25, HEIGHT * 0.25, 400, 105, app=self.app)
        self.player_card= DisplayPokemon(self.player_pokemon, WIDTH * 0.425, 500, 400, 105, app=self.app)

    def get_pokemon_front_sprite(self):
        """"""
        return self.player_pokemon.get_front_sprite()

    def get_pokemon_back_sprite(self):
        """"""
        return self.wild_pokemon.get_back_sprite()

    def attack(self):
        """ Attack the enemy. """
        self.battle.turn()
        if self.battle.end_battle():
            self.app.state_manager.set_state("battle menu")

    def change_pokemon(self):
        """ Change pokemon in the battle. """
        pass

    def run(self):
        """ Escape from the battle. """
        pass

    def draw_text(self, text, x, y):
        """ Allow to draw text """
        text_surface = self.font.render(str(text), True, BLACK)
        self.app.screen.blit(text_surface, (x, y))

    def draw_image(self, image_path, x, y):
        """ Allow to draw a sprite """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (400, 400))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")

    def draw_player_pokemon_sprite(self, x, y):
        """"""
        self.draw_image(self.get_pokemon_front_sprite(), x, y)

    def draw_wild_pokemon_sprite(self, x, y):
        """"""
        self.draw_image(self.get_pokemon_back_sprite(), x, y)

    # def draw_player_pokemon_name(self, x, y):
    #     get_pokemon_name = self.player_pokemon.get_name()
    #     self.draw_text(get_pokemon_name, x, y)

    # def draw_wild_pokemon_name(self, x, y):
    #     get_pokemon_name = self.wild_pokemon.get_name()
    #     self.draw_text(get_pokemon_name, x, y)

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        
        self.player_display.draw_battle_pokemon_back_sprite(200, HEIGHT - 450) # Draw sprites
        self.enemy_display.draw_battle_pokemon_front_sprite(WIDTH - 580, 120)
        self.player_card.draw_battle_card()
        self.enemy_card.draw_battle_card()

        for button in self.buttons:
            button.process()  # Show buttons
