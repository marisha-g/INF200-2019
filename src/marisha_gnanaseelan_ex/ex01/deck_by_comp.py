SUITS = ('C', 'S', 'H', 'D')  # type
VALUES = range(1, 14)  # numbers


def deck_loop():
    """
    This function creates a deck of cards using for-loops
    :return: list
    """
    deck = []  # deck
    for suit in SUITS:  # iterating through types
        for val in VALUES:  # iterating through numbers
            deck.append((suit, val))  # adding types and numbers
    return deck  # returning deck


def deck_comp():
    """
    This function creates the same list as deck_loop() using a list comprehension
    """
    return [(suit, val) for suit in SUITS for val in VALUES]  # list comprehension of the code above


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
