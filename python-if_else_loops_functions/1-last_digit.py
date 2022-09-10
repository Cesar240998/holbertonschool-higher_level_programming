#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = repr(number)
last_dig = number_str[-1]
if number > -1:
    last_int = int(last_dig)
else:
    last_int = int(last_dig) * -1

if last_int > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, last_int))
elif last_int == 0:
    print("Last digit of {0} is {1} and is 0".format(number, last_int))
elif last_int < 6:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, last_int))
