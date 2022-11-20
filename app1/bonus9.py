import string

password = input('Enter new password: ')

result = {'lenchk':len(password) >= 8}
result['digitchk'] = any([char.isdigit() for char in password])
result['lowerchk'] = any([char in string.ascii_lowercase for char in password])
result['upperchk'] = any([char in string.ascii_uppercase for char in password])
    
print(result)

print('Strong pasword!') if all(result.values()) else print('Weak password..')
