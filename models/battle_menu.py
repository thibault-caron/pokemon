import os

from config import *
from .game_state import GameState
from .button import Button
from .pokedex import pokedex

class BattleMenu(GameState):
    def __init__(self, app):
        super().__init__(app, img_folder=os.path.join(os.getcwd(), "assets", "images"), file="start_battle_menu_background.webp")
        self.caption = "Battle Menu"
        
        self.button1 = Button(WIDTH/2 - 200, 200, 400, 50, 'Start Battle', self.start_battle, screen=self.app.screen)
        self.button2 = Button(WIDTH/2 - 200, 335, 400, 50, 'Settings', self.view_pokedex, screen=self.app.screen)
        self.button3 = Button(WIDTH/2 - 200, 470, 400, 50, 'Exit', self.exit_game, screen=self.app.screen)
        
        self.buttons = [self.button1, self.button2, self.button3]
        
    def start_battle(self):
        """Start game."""
        self.app.state_manager.set_state("battle")

    def view_pokedex(self):
        """Show pokedex."""
        print("Settings clicked!")

    def exit_game(self):
        """ Exit the game."""
        self.app.running = False

    def draw(self):
        """Draw welcome menu scene"""
        super().draw()  # Draw background
        self.app.screen.blit(self.menu_background, (WIDTH*0.25, HEIGHT*0.25)) # Draw menu rectangle
        for button in self.buttons:
            button.process()  # Show buttons