'''
Ex 8:
Write a function that prints the multiplication table for a given number n.
Example: exercise_8(3) should print:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
... up to 3 x 10 = 30
'''

from functools import reduce


def multiplications(n:int) -> None:
    [print(f"{n} x {c} = {int(n)*c}") for c in range(1, 11, 1)]

multiplications(input("n: "))