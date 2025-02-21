import os

from config import *

from .battle import Battle
from .button import Button
from .game_state import GameState
from .generate_pokemon import GeneratePokemon


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
        player_pokemon = GeneratePokemon().player_pokemon
        if not player_pokemon:  # If the pokedex is empty after a battle, turn to the choice menu (like a new game).
            self.app.state_manager.set_state("choice")
        else:
            wild_pokemon = GeneratePokemon().wild_pokemon
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

    def draw(self):
        """
        Draw the battle menu scene.
        :return: ∅
        """
        super().draw()
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGHT*0.25))
        for button in self.buttons:
            button.process()
