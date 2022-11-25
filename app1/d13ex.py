'''def calc_age(year_of_birth, current_year=2022):
    return current_year - year_of_birth

user_input = int(input('What is your year of birth? '))
if calc_age(user_input) >= 120:
    print('You are super star!')
else:
    print(calc_age(user_input))'''

user_input = input('Enter names separated by comas(no spaces): ')
def calc_names(user_input):
    return len(user_input.split(','))

print(calc_names(user_input))