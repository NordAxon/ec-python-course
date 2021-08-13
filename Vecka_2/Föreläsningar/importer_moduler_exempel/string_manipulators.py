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

    return first_name, surname