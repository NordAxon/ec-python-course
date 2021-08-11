import argparse

import string_manipulators



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--first-name', help='Enter your first name please', required=True)
    parser.add_argument('--surname', help='Enter you surname please')
    parser.add_argument('--all-capital', dest='all_capital', action = 'store_false')
    parser.set_defaults(feature=True)
    args = parser.parse_args()
    print(args.first_name, args.surname)

    first_name, last_name = string_manipulators.change_name_representation(args.first_name, args.surname, args.all_capital)