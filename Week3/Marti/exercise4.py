'''
Ex 4:
Write a function that reverses a string and returns a list with each letter.
Example: input "hello" should return ["o", "l", "l", "e", "h"]
'''

def reverse_str(s):
    return list(reversed([_ for _ in s]))

print(reverse_str(input("string: ")))