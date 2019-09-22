from random import randint as a

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def your_guess():
    """
    This function has a input function where you guess a number
    :return: int
    """
    guess = 0  # start value
    while guess < 1:  # you have to guess a number if "guess" is lower that 1
        guess = int(input('Your guess: '))  # guess
    return guess  # returning


def rand_int():
    """
    This function picks a random number
    :return: int
    """
    return a(1, 6) + a(1, 6)  # returning random number


def check_answer(guess, rand):
    """
    This function checks if the guessed number is the same as the random number
    :param guess: int
    :param rand: int
    :return: bool
    """
    return guess == rand  # returning


if __name__ == '__main__':

    answer = False  # start value for answer
    points = 3  # start value for points
    rand = rand_int()  # calling and defining the function, rand_int()

    while not answer and points > 0:  # checking if the game is not finished and you have more than 0 points left
        guess = your_guess()  # calling and defining the function, your_guess()
        answer = check_answer(rand, guess)  # calling and defining the function check_answer()
        if not answer:  # checking if the game is finished or not
            print('Wrong, try again!')
            points -= 1  # if the guessed number is not the same as the random number, 1 point is subtracted

    if points > 0:  # checking if you have more than 0 points
        print('You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(rand))
