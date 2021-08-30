from argparse import ArgumentParser

def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word = word[i] + "_"
    return new_word



if __name__ == '__main__':
    # parser = ArgumentParser()
    # parser.add_argument('--phrase', required=True, type=str)
    # args = parser.parse_args()

    # phrase = args.phrase

    phrase = 'hello'
    print(add_underscores(phrase))