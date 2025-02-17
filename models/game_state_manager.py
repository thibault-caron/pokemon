from config import *

from .welcome_menu import WelcomeMenu
from .battle_menu import BattleMenu
from .battle_scene import BattleScene
from .choice_menu import ChoiceMenu
from .add_wild_pokemon import AddWildPokemon

class GameStateManager:
    def __init__(self, app):
        self.app = app
        self.states = {
            "welcome": WelcomeMenu(self.app),
            "choice": ChoiceMenu(self.app),
            "battle menu": BattleMenu(self.app),
            "add wild pokemon": AddWildPokemon(self.app),
            "battle": BattleScene(self.app)
        }
        self.current_state = self.states["welcome"]
        
    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        if state in self.states:
            self.current_state = self.states[state]
        else:
            print(f"Error: state '{state}' is unknown")