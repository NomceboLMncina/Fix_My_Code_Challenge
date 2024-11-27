#!/usr/bin/python3
""" FizzBuzz: Print numbers with substitutions for multiples of 3 and 5
"""
import sys


def fizzbuzz(limit):
    """
    FizzBuzz function prints numbers from 1 to limit, with substitutions for multiples of 3 and 5.

    - For multiples of three, print "Fizz" instead of the number.
    - For multiples of five, print "Buzz" instead of the number.
    - For numbers that are multiples of both three and five, print "FizzBuzz".
    """
    if limit < 1:
        return

    results = []
    for num in range(1, limit + 1):
        if (num % 3) == 0 and (num % 5) == 0:
            results.append("FizzBuzz")
        elif (num % 3) == 0:
            results.append("Fizz")
        elif (num % 5) == 0:
            results.append("Buzz")
        else:
            results.append(str(num))
    print(" ".join(results))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
