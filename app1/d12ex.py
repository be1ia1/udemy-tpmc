'''def converter(liter):
    return liter * 0.001

print(converter(1000))'''

import string

user_input = input('Enter a password: ')

def pass_checker(password):
    result = {'lenchk':len(password) >= 8}
    result['digitchk'] = any([char.isdigit() for char in password])
    result['lowerchk'] = any([char in string.ascii_lowercase for char in password])
    result['upperchk'] = any([char in string.ascii_uppercase for char in password])
    answer = 'Strong pasword!' if all(result.values()) else 'Weak password..'
    return answer

print(pass_checker(user_input))