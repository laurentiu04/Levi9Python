'''
Ex 5:
Write a function that counts the number of vowels in a string.
Example: input "hello world" should return 3
'''

def vowel_count(s):
    return sum([c in 'aeiou' for c in s])

print(vowel_count(input("string: ")))