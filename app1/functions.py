import pathlib
import os

FILEPATH = pathlib.Path('todos.txt')

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as fo:
        pass

def get_todos(file=FILEPATH):
    '''Get todos from FILEPATH'''
    with open(file) as fo:
        return fo.readlines()

def write_todos(todos_list, file=FILEPATH):
    with open(file, 'w') as fo:
        fo.writelines(todos_list)

if __name__ == '__main__':
    print(FILEPATH)
