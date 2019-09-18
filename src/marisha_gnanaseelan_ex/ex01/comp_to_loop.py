
def squares_by_comp(n):
    """
    This function makes squares by using list comprehension
    """
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """
    This function makes squares by using for-loop and if-statement
    :return: list
    """
    loop_list = []  # empty list
    for k in range(n):  # for-loop
        if k % 3 == 1:  # checking if the remainder/modulus of k divided by 3 is equal to 1
            loop_list.append(k ** 2)  # if the if-statement is true, append k**2 to the list
    return loop_list  # returning list


if __name__ == '__main__':
    if squares_by_comp(10) != squares_by_loop(10):
        print('ERROR!')
    else:
        print("squares_by_comp() and squares_by_loop() are the same!")
