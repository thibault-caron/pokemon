from .config import *

from .welcome_menu import WelcomeMenu

class GameStateManager:
    def __init__(self, app):
        self.app = app
        self.states = {
            "welcome": WelcomeMenu(self.app),
            # "battle": Battle(self.app),  # À ajouter plus tard
            # "settings": Settings(self.app),  # À ajouter plus tard
        }
        self.current_state = self.states["welcome"]
        
    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        if state in self.states:
            self.current_state = self.states[state]
        else:
            print(f"Erreur: état '{state}' inconnu")