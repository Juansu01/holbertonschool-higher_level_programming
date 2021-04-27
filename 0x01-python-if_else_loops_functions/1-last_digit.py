#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    lastD = number % 10

else:
    lastD = number % -10

if lastD > 5:

    print("Last digit of {:d} is {:d} and is greater than 5".format(number, lastD))

elif lastD < 6 and lastD != 0:

    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, lastD))

else:

    print("Last digit of {:d} is {:d} and is 0".format(number, lastD))
