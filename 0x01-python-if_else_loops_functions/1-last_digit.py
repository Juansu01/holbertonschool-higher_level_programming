#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    D = number % 10

else:
    D = number % -10

if D > 5:

    print("Last digit of {:d} is {:d} and is greater than 5".format(number, D))

elif D < 6 and D != 0:
    print("Last digit of {}".format(number), end=' ')
    print("is {:d} and is less than 6 and not 0".format(D))

else:

    print("Last digit of {:d} is {:d} and is 0".format(number, D))
