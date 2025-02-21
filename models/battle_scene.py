import os

from config import *
from random import random
from .button import Button
from .display_pokemon import DisplayPokemon
from .game_state import GameState


class BattleScene(GameState):
    """ Class to manage the battle scene. """
    def __init__(self, app, player_pokemon, wild_pokemon, battle):
        """
        Initialization of the class.
        :param app: Call of the game main loop.
        :param player_pokemon: The player pokemon.
        :param wild_pokemon: The wild pokemon.
        :param battle: Call the battle between the two pokemons.
        """
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="battle_background.webp")
        self.caption = "Battle"
        self.player_pokemon = player_pokemon
        self.wild_pokemon = wild_pokemon
        self.battle = battle

        self.font = pygame.font.Font("assets/pokemon_classic.ttf", 20)

        self.button1 = Button(50, 650, 200, 50, "Attack", self.attack,
                              screen=self.app.screen)
        self.button2 = Button(450, 650, 300, 50, "Change Pokemon", self.change_pokemon,
                              screen=self.app.screen)
        self.button3 = Button(950, 650, 200, 50, "Run", self.run, screen=self.app.screen)
        self.buttons = [self.button1, self.button2, self.button3]

        self.enemy_display = DisplayPokemon(self.wild_pokemon, 100, 100, WIDTH, HEIGHT, app=self.app)
        self.player_display = DisplayPokemon(self.player_pokemon, 700, 100, WIDTH, HEIGHT, app=self.app)

        self.enemy_card = DisplayPokemon(self.wild_pokemon, WIDTH * 0.15, HEIGHT * 0.25, 400, 105,
                                         app=self.app)
        self.player_card = DisplayPokemon(self.player_pokemon, WIDTH * 0.425, 500, 400, 105,
                                          app=self.app)

        self.battle.damage_player_message = ""
        self.battle.damage_enemy_message = ""
        self.battle.winner_message = ""
        self.winner_message = ""

        self.message_time = 0

    def get_pokemon_front_sprite(self):
        """
        Getter of the player pokemon front sprite.
        :return: The player pokemon front sprite.
        """
        return self.player_pokemon.get_front_sprite()

    def get_pokemon_back_sprite(self):
        """
        Getter of the wild pokemon back sprite
        :return: The wild pokemon back sprite.
        """
        return self.wild_pokemon.get_back_sprite()

    def attack(self):
        """
        Button 'Attack' action.
        :return: ∅
        """
        self.battle.turn()

        # show messages
        self.damage_player_message = self.battle.damage_player_message
        self.damage_enemy_message = self.battle.damage_enemy_message
        self.winner_message = self.battle.winner_message
        self.message_time = pygame.time.get_ticks() + 2200

        self.battle.end_battle()

    def change_pokemon(self):
        """
        Button 'Change Pokemon' action.
        :return: ∅
        """
        pass

    def run(self):
        """
        Button 'Run' action.
        :return: ∅
        """
        escape_attempt = random()
        if escape_attempt > 0.49:  # Set a one in two chance of escape.
            self.app.state_manager.set_state("battle menu")
        else:
            self.player_pokemon.set_hp(self.player_pokemon.get_hp() - (self.wild_pokemon.get_attack() * 0.5))
            print("you failed to escape!")
            if self.battle.end_battle():
                self.app.state_manager.set_state("battle menu")

    def draw_text(self, text, x, y, color=WHITE):
        """
        Allow to draw text.
        :param text: The text to write.
        :param x: Abscissa of the text.
        :param y: Ordinate of the text.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        text_surface = self.font.render(str(text), True, color)
        self.app.screen.blit(text_surface, (x, y))

    def draw_image(self, image_path, x, y):
        """
        Allow to draw a sprite.
        :param image_path: Path of the sprite.
        :param x: Abscissa of the sprite.
        :param y: Ordinate of the sprite.
        :return: ∅
        """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (400, 400))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")

    def draw_player_pokemon_sprite(self, x, y):
        """
        Draw player pokemon sprite.
        :param x: Abscissa of the sprite.
        :param y: Ordinate of the sprite.
        :return: ∅
        """
        self.draw_image(self.get_pokemon_front_sprite(), x, y)

    def draw_wild_pokemon_sprite(self, x, y):
        """
        Draw wild pokemon sprite.
        :param x: Abscissa of the sprite.
        :param y: Ordinate of the sprite.
        :return: ∅
        """
        self.draw_image(self.get_pokemon_back_sprite(), x, y)

    def draw(self):
        """
        Draw the battle scene.
        :return: ∅
        """
        super().draw()

        self.player_display.draw_battle_pokemon_back_sprite(200, HEIGHT - 450)  # Draw sprites
        self.enemy_display.draw_battle_pokemon_front_sprite(WIDTH - 580, 120)
        self.player_card.draw_battle_card()
        self.enemy_card.draw_battle_card()

        for button in self.buttons:
            button.process()

        if pygame.time.get_ticks() < self.message_time:
            if self.damage_player_message:
                self.draw_text(self.damage_player_message, 50, 20)
            if self.damage_enemy_message:
                self.draw_text(self.damage_enemy_message, 50, 90)
            if self.winner_message:
                self.draw_text(self.winner_message, 280, 124, "red")

        if self.winner_message and pygame.time.get_ticks() > self.message_time:
            self.app.state_manager.set_state("battle menu")
