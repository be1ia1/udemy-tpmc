def get_feet_inches(user_input):
    feet_list = user_input.split()
    return {'feet': float(feet_list[0]),
            'inches': float(feet_list[1])}
    