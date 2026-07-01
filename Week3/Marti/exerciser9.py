'''
Ex 9:
Write a function that calculates the factorial of a number.
Example: input=5 should return 120 (5*4*3*2*1)
'''

def fact(n:int) -> int:
    res = 1
    for e in range(2, int(n)+1, 1):
        res *= e

    return res

print(fact(input("n: ")))