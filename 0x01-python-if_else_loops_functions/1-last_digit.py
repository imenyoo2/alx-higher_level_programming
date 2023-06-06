#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
print(f"Last digit of {number} is {last_dig} ", end="")
if last_dig > 5:
    print("and is greater than 5")
elif last_dig == 0:
    print("and is zero")
elif last_dig < 6 and last_dig != 0:
    print("and is less than 6 and not 0")
