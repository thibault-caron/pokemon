import os

from .config import *
from .game_state import GameState
from .button import Button

class BattleScene(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="battle_background.webp")
        self.caption = "Battle"
        
    def start_game(self):
        """Start game"""
        self.app.state_manager.set_state("battle")

    def view_pokedex(self):
        """Show pokedex"""
        print("Settings clicked!")

    def exit_game(self):
        """Quitte l'application."""
        self.app.running = False

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background