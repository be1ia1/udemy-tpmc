from parser_func import get_feet_inches
from converter_func import converter

user_input = input('Enter feet and inches: ')

data = get_feet_inches(user_input)
print(converter(data['feet'], data['inches']))