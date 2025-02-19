from config import *

from .welcome_menu import WelcomeMenu
from .battle_menu import BattleMenu
from .battle_scene import BattleScene
from .choice_menu import ChoiceMenu
from .add_wild_pokemon import AddWildPokemon

class GameStateManager:
    def __init__(self, app):
        self.app = app
        self.states = {}
        
        self.current_state = None
        
        self.set_state("welcome")
        
    def set_state(self, state_name, player_pokemon=None, wild_pokemon=None, battle=None):
        """Change d'état en créant l'instance seulement si elle n'existe pas"""
        if state_name not in self.states:
            if state_name == "welcome":
                self.states[state_name] = WelcomeMenu(self.app)
            elif state_name == "choice":
                self.states[state_name] = ChoiceMenu(self.app)
            elif state_name == "battle menu":
                self.states[state_name] = BattleMenu(self.app)
            elif state_name == "add wild pokemon":
                self.states[state_name] = AddWildPokemon(self.app)
            elif state_name == "battle":
                print(wild_pokemon.get_name())
                self.states[state_name] = BattleScene(self.app, player_pokemon, wild_pokemon, battle)

        self.current_state = self.states[state_name]

    def get_state(self):
        return self.current_state