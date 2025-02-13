from .config import *

class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state
        
    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        self.current_state = state