mint = 0
maxt = 100

def get_state(temperature):
    if temperature <= mint:
       answer = 'Solid'
    elif mint < temperature < maxt:
        answer = 'Liquid'
    elif temperature > maxt:
        answer = 'Gaz'
    return answer