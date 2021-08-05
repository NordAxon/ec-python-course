
def string_comparison_method(first_string: str, second_string: str) -> str:
    """ This is a string that explains what the method does. It is called docstring.
    In this method we compare two strings to see if the content is the same
    """
    try:
        if first_string.lower() == second_string.lower():
            message = "The strings are saying the same thing! :)"
        else:
            message = "The strings are not saying the same thing.. :("
    except AttributeError:
        message = "Hmm, one of your entries were not a string at all :("

    return message

def main():
    print("I'm in the main method")
    
    a = 100
    b = 1000
    print(a/b)

    string_to_print = string_comparison_method("hello world", "Hello World")
    print(string_to_print)

if __name__ == "__main__":
    main()