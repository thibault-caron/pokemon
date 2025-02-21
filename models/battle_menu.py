import os

from random import choice, randint

from config import *
from .game_state import GameState
from .battle import Battle
from .button import Button
from .pokemon import Pokemon, PlayerPokemon
from .pokemon_dictionary import all_pokemons
from .pokedex import pokedex


class BattleMenu(GameState):
    """ Class to manage the battle menu. """
    def __init__(self, app, img_folder=os.path.join(os.getcwd(), "assets", "images"),
                 file="start_battle_menu_background.webp"):
        """
        Initialization of the class.
        :param app: Call of the game main loop.
        :param img_folder: Folder of the background image.
        :param file: The background image.
        """
        super().__init__(app, img_folder=img_folder, file=file)
        self.caption = "Battle Menu"
        
        self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'Start Battle', self.start_battle,
                              screen=self.app.screen)
        self.button2 = Button(WIDTH/2 - 200, 335, 400, 50, 'Manage team', self.view_pokedex,
                              screen=self.app.screen)
        self.button3 = Button(WIDTH/2 - 200, 470, 400, 50, 'Exit', self.exit_game,
                              screen=self.app.screen)
        
        self.buttons = [self.button1, self.button2, self.button3]
        
    def start_battle(self):
        """
        Button 'Start Battle' action.
        :return: ∅
        """
        player_pokemon = self.select_first_pokemon()
        if not player_pokemon:  # If the pokedex is empty after a battle, turn to the choice menu (like a new game).
            self.app.state_manager.set_state("choice")
        else:
            wild_pokemon = self.generate_wild_pokemon(player_pokemon)
            print(wild_pokemon.get_name())
            battle = Battle(player_pokemon, wild_pokemon)
            self.app.state_manager.set_state("battle", player_pokemon, wild_pokemon, battle)

    def view_pokedex(self):
        """
        Button 'Manage team' action.
        :return: ∅
        """
        self.app.state_manager.set_state("show pokedex")

    def exit_game(self):
        """
        Button 'Exit' action.
        :return: ∅
        """
        self.app.running = False

    def select_first_pokemon(self):
        """
        Select the first pokemon of player pokedex.
        :return: The first pokemon.
        """
        player_pokemon_list = pokedex.list_pokemons()
        if not player_pokemon_list:
            return None
        else:
            first_pokemon = player_pokemon_list[0]
            return PlayerPokemon(first_pokemon)

    def generate_wild_pokemon(self, player_pokemon):
        """
        Choose randomly a pokemon to be the opponent of your pokemon.
        :param player_pokemon: The player pokemon.
        :return: The wild pokemon.
        """
        def generate_wild_pokemon_level():
            """
            Choose randomly the wild pokemon level in a range of +/- 3 levels from the player pokemon level.
            :return: The wild pokemon level.
            """
            min_level = player_pokemon_level - 3
            if min_level < 1:
                min_level = 1

        max_level = player_pokemon_level + 3
        if max_level > 50:
            max_level = 50

        wild_pokemon_level = randint(min_level, max_level)
        return wild_pokemon_level

        def generate_wild_pokemon_name():
            """
            Choose randomly the will pokemon. Random function can use only pokemons that have a minimum level
            equal or inferior to the player pokemon level.
            :return: The wild pokemon name.
            """
            sufficient_level_pokemons = all_pokemons.get_pokemon_by_min_level(player_pokemon_level)

        used_pokemons = all_pokemons.get_pokemon_by_state("used")

        wild_pokemons_list = []
        for used_name in used_pokemons:
            for sufficient_level_name in sufficient_level_pokemons:
                if used_name == sufficient_level_name:
                    wild_pokemons_list.append(used_name)

        wild_pokemon_name = choice(wild_pokemons_list)
        return wild_pokemon_name

        player_pokemon_level = player_pokemon.get_level()
        return Pokemon(generate_wild_pokemon_name(),
                       generate_wild_pokemon_level())

class BattleMenu(GameState):
    def __init__(self, app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="start_battle_menu_background.webp" ):
        super().__init__(app, img_folder=img_folder, file=file)
        self.caption = "Battle Menu"
        
        self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'Start Battle', self.start_battle, screen=self.app.screen)
        self.button2 = Button(WIDTH/2 - 200, 335, 400, 50, 'Manage team', self.view_pokedex, screen=self.app.screen)
        self.button3 = Button(WIDTH/2 - 200, 470, 400, 50, 'Exit', self.exit_game, screen=self.app.screen)
        
        self.buttons = [self.button1, self.button2, self.button3]
        
    def start_battle(self):
        """Start game."""
        player_pokemon = self.select_first_pokemon()
        if not player_pokemon:
            self.app.state_manager.set_state("choice")
        else:
            wild_pokemon = generate_wild_pokemon(player_pokemon)
            print(wild_pokemon.get_name())
            battle = Battle(player_pokemon, wild_pokemon)
            self.app.state_manager.set_state("battle", player_pokemon, wild_pokemon, battle)

    def view_pokedex(self):
        """Go to pokedex display scene"""
        self.app.state_manager.set_state("show pokedex")

    def exit_game(self):
        """ Exit the game."""
        self.app.running = False

    def select_first_pokemon(self):
        """"""
        player_pokemon_list = pokedex.list_pokemons()
        if not player_pokemon_list:
            return None
        else:
            first_pokemon = player_pokemon_list[0]
            return PlayerPokemon(first_pokemon)

    def draw(self):
        """
        Draw the battle menu scene.
        :return: ∅
        """
        super().draw()
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGHT*0.25))
        for button in self.buttons:
            button.process()
