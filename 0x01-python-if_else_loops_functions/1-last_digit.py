#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{positive}")
elif number == 0:
    print("{number} is zero")
else:
    print(f"{number} is negative")
