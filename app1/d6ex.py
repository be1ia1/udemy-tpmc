'''essay_file = 'files/essay.txt'
with open(essay_file) as fo:
    content = fo.readlines()

for string in content:
    print(string.title())'''


'''essay_file = 'files/essay.txt'
with open(essay_file) as fo:
    content = fo.read()

print(len(content))'''


'''members_file = 'files/members.txt'

new_user = input('Add a new member: ')

with open(members_file, 'a') as fo:
    fo.write(new_user)'''

files = ['a', 'b', 'c']
for file in files:
    with open(f'files/{file}.txt') as fo:
        content = fo.read()
        print(content)