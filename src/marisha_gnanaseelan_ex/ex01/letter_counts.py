def letter_freq(txt):
    frequencies = {}  # empty dictionary
    txt_lower = txt.lower()  # all letters are made into lowercase letters

    for i in txt_lower:
        keys = frequencies.keys()  # list of all the keys in the dictionary
        if i in keys:  # checks if the letter, digit or symbol is in the dictionary keys
            frequencies[i] += 1  # if the if-statement is true then the value to the corresponding key is added by 1
        else:
            frequencies[i] = 1  # if the if-statement is false then the value to the corresponding key is 1
    return frequencies  # returning


if __name__ == '__main__':
    txt = input('Please enter text to analyse: ')
    frequencies = letter_freq(txt)
    for letter, count in sorted(frequencies.items()):  # sorting so the letters are printed in alphabetical order
        print('{:3}{:10}'.format(letter, count))
