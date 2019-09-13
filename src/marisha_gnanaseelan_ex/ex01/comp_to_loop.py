
function squares_by_loop()

def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]






if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')