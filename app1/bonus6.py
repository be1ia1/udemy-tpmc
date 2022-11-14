contents = ['first bla',
            'second bla',
            'third bla']
filenames = ['1.txt',
            '2.txt',
            '3.txt']

for filename, content in zip(filenames, contents):
    with open(f'files//{filename}', 'w') as fo:
        fo.write(content)
