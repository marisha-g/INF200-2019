from random import randint as a

__author__ = 'Marisha Gnanaseelan'
__email__ = 'magn@nmbu.no'


def your_guess():
    guess = 0
    while guess < 1:
        guess = int(input('Your guess: '))
    return guess


def rand_int():
    return a(1, 6) + a(1, 6)


def check_answer(guess, rand):
    return guess == rand


if __name__ == '__main__':

    answer = False
    points = 3
    correct_ans = rand_int()
    while not answer and points > 0:
        estimate = your_guess()
        answer = check_answer(correct_ans, estimate)
        if not answer:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print('You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(correct_ans))
