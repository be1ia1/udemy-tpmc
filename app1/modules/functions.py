def get_todos(file='files//todos.txt' ):
    with open(file) as fo:
        return fo.readlines()

def write_todos(todos_list, file='files//todos.txt'):
    with open(file, 'w') as fo:
        fo.writelines(todos_list)

if __name__ == '__main__':
    pass
