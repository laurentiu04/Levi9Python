'''
Ex 3:
Write a function that takes a list of numbers and returns only the even numbers.
Example: input [1, 2, 3, 4, 5, 6] should return [2, 4, 6]
'''

def even_nums(list):
    return filter(lambda x: not x%2, list)

for x in even_nums(input("list: ")):
    print(x)