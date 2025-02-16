import os

from .config import *
from .game_state import GameState
from .button import Button
from .pokemon import Pokemon
from .battle import Battle

class BattleScene(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="battle_background.webp")
        self.caption = "Battle"

        self.player_pokemon = Pokemon("Pikachu", 5)
        self.wild_pokemon = Pokemon("Caterpie", 1)
        self.battle = Battle(self.player_pokemon, self.wild_pokemon)

        self.button1 = Button(50, 650, 200, 50, "Attack", self.attack)
        self.button2 = Button(450, 650, 300, 50, "Change Pokemon", self.change_pokemon)
        self.button3 = Button(950, 650, 200, 50, "Run", self.run)
        self.buttons = [self.button1, self.button2, self.button3]

    def attack(self):
        """ Attack the enemy. """
        victory = self.battle.turn()
        if isinstance(victory, str):
            exit()

    def change_pokemon(self):
        """ Change pokemon in the battle. """
        pass

    def run(self):
        """ Escape from the battle. """
        pass

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
        self.draw_image(self.player_pokemon.get_front_sprite(), x, y)

    def draw_wild_pokemon_sprite(self, x, y):
        """"""
        self.draw_image(self.wild_pokemon.get_front_sprite(), x, y)

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.draw_player_pokemon_sprite(100, 600)
        self.draw_wild_pokemon_sprite(1100, 100)

        for button in self.buttons:
            button.process()  # Show buttons


