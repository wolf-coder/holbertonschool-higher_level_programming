#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last = abs(number) % 10
if number < 0:
    Last = Last * (-1)
if Last > 5:
    str = 'and is greater than 5'
elif Last == 0:
    str = 'and is 0'
else:
    str = 'and is less than 6 and not 0'
print("Last digit of {} is {} {}".format(number, Last, str))
