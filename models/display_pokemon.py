from math import sin

from config import *

from .button import Button
from .pokedex import pokedex


class DisplayPokemon:
    """ Class to display the pokemons in the screen. """

    def __init__(self, pokemon, x, y, width, height, app, onclickFunction=None, onePress=False):
        """
        Initialization of the class.
        :param pokemon:
        :param x: Abscissa of the image display.
        :param y: Ordinate of the image display.
        :param width: Width of the image display.
        :param height: Height of the image display.
        :param app: Call of the game main loop.
        :param onclickFunction: Set of one click action.
        :param onePress: Set of one press action.
        """
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

        self.mouvement_x = 0
        self.mouvement_y = 0
        self.amplitude_vertical = 0
        self.amplitude_horizontal = 0
        self.speed = 3
        self.time_elapsed = 6

        self.button = Button(self.x + 120, self.y + 130, 250, 50, 'Choose me',
                             self.battle, screen=self.app.screen)

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
            image = pygame.transform.scale(image, (110, 110))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")

    def draw_battle_image(self, image_path, x, y):
        """
        Allow to draw a battle image.
        :param image_path: Path of the image.
        :param x: Abscissa of the image.
        :param y: Ordinate of the image.
        :return: ∅
        """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (400, 400))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")

    def draw_pokedex_image(self, image_path, x, y):
        """
        Allow to draw a pokedex image.
        :param image_path: Path of the image.
        :param x: Abscissa of the image.
        :param y: Ordinate of the image.
        :return: ∅
        """
        try:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (250, 250))
            self.app.screen.blit(image, (x, y))
        except pygame.error as error:
            print(f"Error: there is no image at the path {image_path}: {error}")

    def draw_pokemon_name(self, x, y, color=WHITE):
        """
        Draw the pokemon name.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(self.pokemon.get_name(), x, y, color)

    def draw_pokemon_type(self, x, y, color=WHITE):
        """
        Draw the pokemon type.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        types = "/".join(self.pokemon.get_types())
        self.draw_text(f"Type: {types}", x, y, color)

    def draw_pokemon_hp(self, x, y, color=WHITE):
        """
        Draw the pokemon current hp.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(f"{round(self.pokemon.get_hp())}", x, y, color)

    def draw_pokemon_max_hp(self, x, y, color=WHITE):
        """
        Draw the pokemon max hp.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(f"{self.pokemon.get_max_hp()}", x, y, color)

    def draw_pokemon_level(self, x, y, color=WHITE):
        """
        Draw the pokemon level.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(f"Level: {self.pokemon.get_level()}", x, y, color)

    def draw_pokemon_xp(self, x, y, color=WHITE):
        """
        Draw the pokemon xp.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(f"{self.pokemon.get_xp()}", x, y, color)

    def draw_pokemon_max_xp(self, x, y, color=WHITE):
        """
        Draw the pokemon max xp.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(f"{self.pokemon.get_level() * 4}", x, y, color)

    def draw_pokemon_attack(self, x, y, color=WHITE):
        """
        Draw the pokemon attack.
        :param x: His abscissa.
        :param y: His ordinate.
        :param color: Text color, by default set as white.
        :return: ∅
        """
        self.draw_text(f"Attack: {self.pokemon.get_attack()}", x, y, color)

    def draw_pokemon_front_sprite(self, x, y):
        """
        Draw the pokemon front sprite.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        self.draw_image(self.pokemon.get_front_sprite(), x, y)

    def draw_pokemon_back_sprite(self, x, y):
        """
        Draw the pokemon back sprite.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        self.draw_image(self.pokemon.get_back_sprite(), x, y)

    def draw_battle_pokemon_front_sprite(self, x, y):
        """
        Draw the battle pokemon front sprite.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        self.amplitude_vertical = 5
        self.amplitude_horizontal = 2
        self.time_elapsed += self.speed
        self.mouvement_x = int(self.amplitude_horizontal * sin(self.time_elapsed * 0.08))
        self.mouvement_y = int(self.amplitude_vertical * sin(self.time_elapsed * 0.2))
        self.draw_battle_image(self.pokemon.get_front_sprite(), x + self.mouvement_x, y + self. mouvement_y)

    def draw_battle_pokemon_back_sprite(self, x, y):
        """
        Draw the battle pokemon back sprite.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        self.amplitude_vertical = 2
        self.amplitude_horizontal = 5
        self.time_elapsed += self.speed
        self.mouvement_x = int(self.amplitude_horizontal * sin(self.time_elapsed * 0.1))
        self.mouvement_y = int(self.amplitude_vertical * sin(self.time_elapsed * 0.2))
        self.draw_battle_image(self.pokemon.get_back_sprite(), x + self.mouvement_x, y + self. mouvement_y)

    def draw_pokedex_front_sprite(self, x, y):
        """
        Draw the pokedex pokemon front sprite.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        self.draw_pokedex_image(self.pokemon.get_front_sprite(), x, y)

    def draw_card_background(self, x, y):
        """
        Draw the card background.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        image = pygame.image.load("assets/images/card.png")
        image = pygame.transform.scale(image, (self.width, self.height))
        self.app.screen.blit(image, (x, y))

    def draw_battle_card_background(self, x, y):
        """
        Draw the battle card background.
        :param x: His abscissa.
        :param y: His ordinate.
        :return: ∅
        """
        image = pygame.image.load("assets/images/battle_card.png")
        image = pygame.transform.scale(image, (self.width, self.height))
        self.app.screen.blit(image, (x, y))

    def draw_card(self):
        """
        Draw the pokemon card.
        :return: ∅
        """
        self.draw_card_background(self.x, self.y)
        self.draw_pokemon_name(self.x + 10, self.y + 10)
        self.draw_pokemon_type(self.x + self.width - 235, self.y + 10)
        self.draw_pokemon_hp(self.x + 10, self.y + 35)
        self.draw_pokemon_level(self.x + self.width - 235, self.y + 35)
        self.draw_pokemon_attack(self.x + 10, self.y + 60)
        self.draw_pokemon_front_sprite(self.x + 10, self.y + 100)
        self.button.process()

    def draw_battle_card(self):
        """
        Draw the battle pokemon card.
        :return: ∅
        """
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
        """
        Draw the pokedex pokemon card.
        :return: ∅
        """
        self.draw_card_background(self.x, self.y)
        self.draw_pokemon_name(self.x + 10, self.y + 10)
        self.draw_pokemon_type(self.x + self.width - 265, self.y + 10)
        self.draw_text("HP: ", self.x + 10, self.y + 55)
        self.draw_pokemon_hp(self.x + 60, self.y + 55)
        self.draw_pokemon_level(self.x + self.width - 265, self.y + 55)
        self.draw_pokemon_attack(self.x + 10, self.y + 100)
        self.draw_text("XP: ", self.x + self.width - 265, self.y + 100)
        self.draw_pokemon_xp(self.x + self.width - 215, self.y + 100)
        self.draw_pokedex_front_sprite(self.x + 5, self.y + 110)

    def draw_wild_card(self):
        """
        Draw the wild pokemon card.
        :return: ∅
        """
        self.draw_card_background(self.x, self.y)
        self.draw_pokemon_name(self.x + self.width * 0.35, self.y + 5)
        self.draw_pokemon_type(self.x + self.width * 0.35, self.y + 30)
        self.draw_text("HP: ", self.x + self.width * 0.35, self.y + 55, BLACK)
        self.draw_pokemon_hp(self.x + self.width * 0.35 + 50, self.y + 55, BLACK)
        self.draw_pokemon_attack(self.x + self.width * 0.35, self.y + 80, BLACK)
        self.draw_pokemon_front_sprite(self.x + 10, self.y + 15)

    def battle(self):
        """
        Action when you click in a pokemon card, like in choose menu.
        :return: ∅
        """
        pokedex.clear_pokedex()
        pokedex.add_pokemon(self.pokemon)  # Add chosen pokemon in pokedex

        self.app.state_manager.set_state("battle menu")  # Change game_state to battle menu
