# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint, choice, sample
import secrets
sSR = secrets.SystemRandom()


def ranpas(n_symb=8):
    pattern1 = '0123456789'
    pattern2 = 'abcdefghijklmnopqrstuvwxyz'
    pattern3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pattern4 = '_!@%*-+'
    password = sample(pattern1+pattern2+pattern3+pattern4, n_symb)
    print(''.join(password))


if __name__ == '__main__':
    ranpas()
    input()
