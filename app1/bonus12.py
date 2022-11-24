feet = input('Enter feet and inches: ')
feet_list = feet.split()
feet = float(feet_list[0])
inches = float(feet_list[1])

def converter(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

#message


print(converter(feet))