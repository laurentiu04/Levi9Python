"""
Problem 4: FizzBuzz with a Twist (Functions & Loops)
Create a function custom_fizzbuzz(n) that prints numbers from 1 to n.
For multiples of 3, print "Fizz",
for multiples of 5, print "Buzz",
for multiples of both 3 and 5, print "FizzBuzz".
For all other numbers, print the number itself.

Example: custom_fizzbuzz(5)
Output: 1
2
Fizz
4
Buzz
"""

def custom_fizzbuzz(n):
    try:
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
    except TypeError:
        print("Invalid argument for function custom_fizzbuzz. Argument has to be a positive number.")

custom_fizzbuzz("15")