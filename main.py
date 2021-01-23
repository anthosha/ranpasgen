# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint, choice, sample
import secrets
sSR = secrets.SystemRandom()


def ranpas(n_symb=8):
    pattern = 'abcdefghijklmnopqrstuvwxyz0123456789_!@%*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = sample(pattern, n_symb)
    print(''.join(password))


if __name__ == '__main__':
    ranpas()
    input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
