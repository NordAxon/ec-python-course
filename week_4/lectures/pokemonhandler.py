import pandas as pd
from argparse import ArgumentParser
import seaborn as sns

class PokemonHandler:

    def __init__(self, pokemon1, pokemon2):
        # Attribute
        self.df = pd.read_csv('C:\Users\AlexanderHagelborn\code\ec-python-course\week_3\lectures\Pokemon.csv')
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

        # Method call
        self._preprocess()

    def _preprocess(self):
        """In this function we want to do any processing necessary for the dataframe to look like we want it to"""
        
        # We want to drop the Legendary row because we don't want it
        raise NotImplementedError

    def _get_pokemon(self):
        "Return a dataframe with only pokemon1 and pokemon 2"

        raise NotImplementedError

    def _print_stats(self):
        " Print the HP, Attack, Defense, Special Attack, Special Defense and Speed of a pokemon"
        raise NotImplementedError

    def visualize(self):
        "PLot a barplot comparing the pokemon"
        raise NotImplementedError

    
    def compare(self):
        "Do all comparisons"
        raise NotImplementedError
        


def pokemon_program(pokemon1, pokemon2, visualize):

    pokemon_handler = PokemonHandler(pokemon1, pokemon2)
    pokemon_handler.compare(visualize)

    if visualize:
        pokemon_handler.visualize()


if __name__ == '__main__':
    """ Compare pokemon example"""

    parser = ArgumentParser()
    parser.add_argument('--pokemon1', type=str, required=True)
    parser.add_argument('--pokemon2', type=str, required=True)
    parser.add_argument('--visualize', action='store_true', required=False, default=False)

    args = parser.parse_args()

    pokemon_program(args.pokemon1, args.pokemon2, args.visualize)



