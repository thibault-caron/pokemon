import os

from config import *
from .game_state import GameState
from .button import Button
from .pokemon import Pokemon
from .battle import Battle
from .pokedex import Pokedex

class BattleScene(GameState):
    def __init__(self, app, player_team=[]):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="battle_background.webp")
        self.caption = "Battle"
        pokedex = Pokedex()

        if player_team == [] and pokedex != {}: 
            print(pokedex.data_pokedex)
            print(pokedex.list_pokemons())
            # [next(iter(pokedex))]
            player_pokemon_name = next(iter(pokedex.data_pokedex))
            self.player_pokemon = Pokemon(pokedex.data_pokedex[player_pokemon_name], summoned=True)
            print("player_team = []")
            # self.player_pokemon = Pokemon("Pidgey")
            # print (self.player_pokemon)
        elif pokedex != {}:
            self.player_pokemon = Pokemon(player_team[0])

        self.wild_pokemon = Pokemon("Pidgey")
        # self.wild_pokemon = Pokemon("Pidgey", 1)
        self.battle = Battle(self.player_pokemon, self.wild_pokemon)

        self.font = pygame.font.Font(None, 50)

        self.button1 = Button(50, 650, 200, 50, "Attack", self.attack)
        self.button2 = Button(450, 650, 300, 50, "Change Pokemon", self.change_pokemon)
        self.button3 = Button(950, 650, 200, 50, "Run", self.run)
        self.buttons = [self.button1, self.button2, self.button3]

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
        """ Change pokemon in the battle. ! ne pas changer de state, """
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

    def draw_pokemon_background(self, x, y):
        """"""
        image = pygame.image.load("assets/images/battle_background.webp")
        image = pygame.transform.scale(image, (400, 300))
        self.app.screen.blit(image, (x, y))

    def draw_player_pokemon_sprite(self, x, y):
        """"""
        self.draw_image(self.player_pokemon.get_back_sprite(), x, y)

    def draw_wild_pokemon_sprite(self, x, y):
        """"""
        self.draw_image(self.wild_pokemon.get_front_sprite(), x, y)

    def draw_player_pokemon_name(self, x, y):
        get_pokemon_name = self.player_pokemon.get_name()
        self.draw_text(get_pokemon_name, x, y)

    def draw_wild_pokemon_name(self, x, y):
        get_pokemon_name = self.wild_pokemon.get_name()
        self.draw_text(get_pokemon_name, x, y)

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.draw_pokemon_background(50, 300)
        # self.draw_player_pokemon_sprite(50, 300)
        self.draw_player_pokemon_name(175, 310)

        self.draw_pokemon_background(750, 50)
        # self.draw_wild_pokemon_sprite(750, 50)
        self.draw_wild_pokemon_name(875, 60)

        for button in self.buttons:
            button.process()  # Show buttons


