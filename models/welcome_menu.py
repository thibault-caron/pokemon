from .config import *
from .game_state import GameState

class WelcomeMenu(GameState):
    def __init__(self, app, img_folder="images", file="", *args, **kwargs):
        super().__init__(app, img_folder, file, *args, **kwargs)