
def pair_with_age(first_name, last_name):
    # öppnar en fil
    # läser från filen
    # returnerar
    return 26

def change_name_representation(first_name: str, surname: str, all_capital: bool) -> tuple:
    """In this method the input strings are capitalized and printed

    Args:
        first_name (str): first name to be capitalized
        surname (str): last name to be capitalized
    """
    if all_capital:
        first_name = first_name.upper()
        surname = surname.upper()
        print(first_name, surname)
    else:
        first_name = first_name.capitalize()
        surname = surname.capitalize()
        print(first_name, surname)


    return first_name, surname