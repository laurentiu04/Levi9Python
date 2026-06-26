"""Problem 1: Password Strength Checker
Write a function check_password_strength(password) that checks if a given password is strong.
A strong password:
 - is at least 8 characters long
 - contains at least one uppercase letter,
 - one lowercase letter
 - and one number.
Return "Strong" if it meets the criteria or "Weak" otherwise.

Example:
Python123 ➔ "Strong"
weakpass ➔ "Weak"
"""

def check_password_strength(password):
    if len(password) < 7:
        return "Weak"
    
    upper_case = False
    lower_case = False
    has_number = False
    
    for c in password:
        char = str(c)
        if upper_case == False and char.isupper():
            upper_case = True
        elif lower_case == False and char.islower():
            lower_case = True
        elif has_number == False and char.isalpha():
            has_number = True
    
    if upper_case and lower_case and has_number:
        return "Strong"
    else:
        return "Weak"
    
print(check_password_strength("weakPass12"))