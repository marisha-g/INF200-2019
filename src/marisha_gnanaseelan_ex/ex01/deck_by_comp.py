SUITS = ('C', 'S', 'H', 'D')  # type
VALUES = range(1, 14)  # tall


def deck_loop():
    deck = []  # kortstokk
    for suit in SUITS:  # iterer gjennom typer
        for val in VALUES:  # iterer gjennom tall
            deck.append((suit, val))  # legger sammen typer og tall
    return deck  # returnerer kortstokk


def deck_comp():
    return [(suit1, val1) for suit1 in SUITS for val1 in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
    else:
        print("deck_loop and deck_comp are the same!")
