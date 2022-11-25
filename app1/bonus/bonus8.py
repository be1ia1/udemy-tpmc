udate = input('Enter today`s date: ')
urate = input('How do you rate your mood today from 1 to 10? ')
print('Let your throughts flow:')
utext = input()

with open(f'files/{udate}.txt', 'w') as fo:
    fo.write(urate + 2 * '\n')
    fo.write(utext)