#!/usr/bin/python3

from calculator_1 import add,  subtract, multiply, divide

if __name__ == '__main__':
    a = 10
    b = 5

    result1 = calculator_1.add(a, b)
    result2 = calculator_1.subtract(a, b)
    result3 = calculator_1.multiply(a, b)
    result4 = calculator_1.divide(a, b)

    print(f"the sum of {a} and {b} is: {result1}")
    print(f"the difference between {a} and {b} is: {result2}")
    print(f"the product of {a} and {b} is: {result3}")
    print(f"the division of {a} by {b} is: {result4}")
