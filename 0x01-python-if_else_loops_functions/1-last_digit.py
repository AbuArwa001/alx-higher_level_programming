#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
isNeg = 0
last = 0
if number < 0:
    isNeg = 1
    number *= -1
    last = number % 10
if isNeg == 1:
    last *= -1
    number *= -1
else :
    last = number % 10
if last == 0:
    print(f"Last digit of {number} is {last} and is {last}")
elif last > 5 :
    print(f"Last digit of {number} is {last} and is greater than 5")
elif (last < 6) :
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
