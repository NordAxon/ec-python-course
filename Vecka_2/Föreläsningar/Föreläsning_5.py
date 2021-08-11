import argparse # <---- imports are always at the top, for easy management


def change_name_representation(first_name: str, surname: str, all_capital: bool) -> tuple:
    """In this method the input strings are capitalized and printed

    Args:
        first_name (str): first name to be capitalized
        surname (str): last name to be capitalized
    """
    if all_capital:
        first_name = first_name.upper()
        surname = surname.upper()
    else:
        first_name = first_name.capitalize()
        surname = surname.capitalize()
        print(first_name, surname)

    return first_name, surname


if __name__ == "__main__":
    # Sometimes we wish to take the user input also through the terminal.
    # A useful library for doing this easily is argparse.
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--first-name', help='Enter your first name please', required=True)
    parser.add_argument('--surname', help='Enter you surname please')
    parser.add_argument('--all-capital', dest='all_capital', action = 'store_false')
    parser.set_defaults(feature=True)
    args = parser.parse_args()
    print(args.first_name, args.surname)

    first_name, last_name = change_name_representation(args.first_name, args.surname, args.all_capital)
    