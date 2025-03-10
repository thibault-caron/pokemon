import os

from config import *
from .game_state import GameState
from .button import Button
from .display_pokemon import DisplayPokemon
from .player_pokemon import PlayerPokemon
from .values import pokedex


class PokedexScene(GameState):
    """ Class to manage the pokedex scene. """
    def __init__(self, app):
        """
        Initialization of the class.
        :param app: Call of the game main loop.
        """
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="pokedex.jpg")
        self.caption = "Show pokedex"
        
        self.font = pygame.font.Font("assets/pokemon_classic.ttf", 15)
        
        self.back_welcome_button = Button(WIDTH*0.25, HEIGHT*0.04, 250, 40, "Start menu",
                                          lambda: self.app.state_manager.set_state("welcome"), screen=self.app.screen)
        
        self.back_battle_button = Button(WIDTH*0.55, HEIGHT*0.04, 250, 40, "Battle menu",
                                         lambda: self.app.state_manager.set_state("battle menu"),
                                         screen=self.app.screen)
        self.buttons = []
        self.message = ""
        self.message_time = 0

    def draw_text(self, text, x, y):
        """
        Allow to draw text.
        :param text: The text to write.
        :param x: Abscissa of the text.
        :param y: Ordinate of the text.
        :return: ∅
        """
        text_surface = self.font.render(str(text), True, BLACK)
        self.app.screen.blit(text_surface, (x, y))

    def draw_pokedex(self, x, y):
        """
        Draw the pokedex.
        :param x: Abscissa of the pokedex.
        :param y: Ordinate of the pokedex.
        :return: ∅
        """
        list_player_pokemon = pokedex.list_pokemons()
        self.buttons.clear()

        for pokemon_name in list_player_pokemon:
            button = Button(x, y, 180, 30, pokemon_name, lambda name=pokemon_name:
                            self.display_details(name), screen=self.app.screen)
            self.buttons.append(button)

            y += 40

            if y > HEIGHT*0.9 - 40:
                y = HEIGHT*0.05
                y += 30
                x += 270

    def display_details(self, pokemon_name):
        """
        Display the details of one of the pokedex pokemon's.
        :param pokemon_name: Name of the pokemon.
        :return: ∅
        """
        displayed_pokemon = PlayerPokemon(pokemon_name)
        DisplayPokemon(displayed_pokemon, 100, 100, 400, 200, app=self.app)
        self.app.state_manager.set_state("show pokemon details", pokemon_name=pokemon_name)

    def draw(self):
        """
        Draw the pokedex scene.
        :return: ∅
        """
        super().draw()
        
        self.draw_pokedex(WIDTH*0.26, HEIGHT*0.19)

        self.back_welcome_button.process()
        self.back_battle_button.process()
        
        for button in self.buttons:
            button.process()
