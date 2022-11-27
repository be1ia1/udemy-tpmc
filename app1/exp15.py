'''
import glob

myfiles = glob.glob('files/*.txt')

for file in myfiles:
    with open(file) as fo:
        print(fo.read())
'''

'''
import csv

with open('files//weather.csv') as fo:
    data = list(csv.reader(fo))
    for line in data[1:]:
        if line[0] == 'New York':
            print('I love New York!!')
'''

'''
import shutil

shutil.make_archive('output', 'zip', 'files')
'''

import webbrowser
query = 'python+website'
search_str = 'https://google.com/search?q=' + query
print(search_str)
webbrowser.open(search_str)