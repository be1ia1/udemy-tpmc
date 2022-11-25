def get_average():
    with open('files/data.txt') as fo:
        temp_content = fo.readlines()[1:]
    temperatures = [float(x) for x in temp_content]
    return sum(temperatures) / len(temp_content)

print(get_average())
