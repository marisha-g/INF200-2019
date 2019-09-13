
def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    loop_list = []
    for k in range(n):
        if k % 3 == 1:
            loop_list.append(k ** 2)
    return loop_list


if __name__ == '__main__':
    if squares_by_comp(10) != squares_by_loop(10):
        print('ERROR!')
    else:
        print("squares_by_comp() and squares_by_loop() are the same!")
