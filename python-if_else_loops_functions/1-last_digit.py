#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ns = repr(number)
last_dig = ns[-1]
if number > -1:
    la = int(last_dig)
else:
    la = int(last_dig) * -1

if la > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(ns, la))
elif la == 0:
    print("Last digit of {0} is {1} and is 0".format(ns, la))
elif la < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(ns, la))
