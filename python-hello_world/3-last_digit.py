#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
n = n % 10
if n < 0:
    n = n - 10
if n == 0:
    line = ('Last digit of ' + str(n) + ' is ' + str(n) + ' and is 0')
else:
     if n > 5:
         line = ('Last digit of ' + str(n) + ' is ' + str(n) + ' and is greater' + ' than 5')
     elif n < 5:
         line = ('Last digit of ' + str(n) + ' is ' + str(n) + ' and is less' + ' than 6 and not 0')
print(line)
