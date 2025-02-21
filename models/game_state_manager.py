from config import *

from .welcome_menu import WelcomeMenu
from .battle_menu import BattleMenu
from .battle_scene import BattleScene
from .choice_menu import ChoiceMenu
from .add_wild_pokemon import AddWildPokemon
from .pokedex_scene import PokedexScene
from .pokemon_details import PokemonDetails


class GameStateManager:
    """ Manage the switch between various screens. """
    def __init__(self, app):
        """
        Initialization of the class.
        :param app: Call of the game main loop.
        """
        self.app = app
        self.states = {}
        
        self.current_state = None
        
        self.set_state("welcome")
        
    def set_state(self, state_name, player_pokemon=None, wild_pokemon=None, battle=None, pokemon_name=None):
        """
        Set the game screen.
        :param state_name: Name of the screen.
        :param player_pokemon: The player pokemon.
        :param wild_pokemon: The wild pokemon.
        :param battle: The battle between the two pokemons.
        :param pokemon_name: The pokemon name.
        :return: ∅
        """

        if state_name == "welcome":
            self.states[state_name] = WelcomeMenu(self.app)
        elif state_name == "choice":
            self.states[state_name] = ChoiceMenu(self.app)
        elif state_name == "show pokedex":
            self.states[state_name] = PokedexScene(self.app)
        elif state_name == "show pokemon details":
            self.states[state_name] = PokemonDetails(self.app, pokemon_name=pokemon_name)
        elif state_name == "battle menu":
            self.states[state_name] = BattleMenu(self.app)
        elif state_name == "add wild pokemon":
            self.states[state_name] = AddWildPokemon(self.app)
        elif state_name == "battle":
            self.states[state_name] = BattleScene(self.app, player_pokemon, wild_pokemon, battle)

        self.current_state = self.states[state_name]

    def get_state(self):
        """
        Getter of the current state.
        :return: ∅
        """
        return self.current_state