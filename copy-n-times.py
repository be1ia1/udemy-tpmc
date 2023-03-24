with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

'''with open('data.txt') as fo:
    content = fo.readlines()

with open('data.txt', 'a') as fo:
    fo.writelines(content * 2) '''