import pandas as pd
from argparse import ArgumentParser
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

class PokemonHandler:

    def __init__(self):
        p = Path(__file__).resolve().parents[2] / 'week_3\lectures\Pokemon.csv'
        self.df = pd.read_csv(p)

        self._preprocess()

    def _preprocess(self):
        " Removes unneccessary columns"
        self.df = self.df[['Name', 'Attack', 'HP', 'Speed', 'Defense']]

    def _print_stats(self, pokemon):
        pokemon = self.df[self.df['Name'] == pokemon]
        print(pokemon)


    def compare(self, pokemon1, pokemon2):

        # Check valid pokemon namespace
        names = self.df['Name'].values
        if pokemon1 in names and pokemon2 in names:
            self._print_stats(pokemon1)
            self._print_stats(pokemon2)
        else:
            print('Did not find both pokemon in the data')
            return

    def visualize(self, pokemon1, pokemon2):

        pokemon_rows = self.df[self.df['Name'].isin([pokemon1, pokemon2])]
        melt = pokemon_rows.melt(id_vars='Name')

        plt.figure()
        sns.barplot(x='variable', y = 'value', hue='Name' ,data=melt)
        plt.show()


def pokemon_program(pokemon1, pokemon2, visualize):

    pokemon_handler = PokemonHandler()
    pokemon_handler.compare(pokemon1, pokemon2)

    if visualize:
        pokemon_handler.visualize(pokemon1, pokemon2)



if __name__ == '__main__':
    """ Compare pokemon example"""

    parser = ArgumentParser()
    parser.add_argument('--pokemon1', type=str, required=True)
    parser.add_argument('--pokemon2', type=str, required=True)
    parser.add_argument('--visualize', action='store_true', required=False, default=False)

    args = parser.parse_args()
    pokemon_program(args.pokemon1, args.pokemon2, args.visualize)




