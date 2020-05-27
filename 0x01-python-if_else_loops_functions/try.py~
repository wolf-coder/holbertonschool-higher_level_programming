#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numberAbs = number * - 1
    lastDigit = numberAbs % 10
    lastDigit = lastDigit * -1
else:
    lastDigit = number % 10
if lastDigit > 5:
    last = "and is greater than 5"
elif lastDigit == 0:
    last = "and is 0"
else:
    last = "and is less than 6 and not 0"
print('Last digit of {} is {} {}'.format(number, lastDigit, last))
