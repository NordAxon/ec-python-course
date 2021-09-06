import argparse # <---- imports are always at the top, for easy management
from utils import *


def main(first_name, last_name, all_capital):
    first_name, last_name = change_name_representation(args.first_name, args.surname, args.all_capital)
    age = pair_with_age(first_name, last_name)

if __name__ == "__main__":
    # Sometimes we wish to take the user input also through the terminal.
    # A useful library for doing this easily is argparse.
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--first-name', help='Enter your first name please', required=True)
    parser.add_argument('--surname', help='Enter you surname please')
    parser.add_argument('--all-capital', dest='all_capital', action = 'store_true')
    parser.set_defaults(all_capital=False)
    args = parser.parse_args()
    print(args.first_name, args.surname, args.all_capital)

    main(args.first_name, args.surname, args.all_capital)

