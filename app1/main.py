import pathlib
todos_file = pathlib.PureWindowsPath('files/todos.txt')
print(todos_file)

def get_todos(file):
    with open(file) as fo:
        return fo.readlines()

def write_todos(file, todos_list):
    with open(file, 'w') as fo:
        fo.writelines(todos_list)


while True:
    uaction = input('Type add, show, complete, edit or exit: ').strip()
    if uaction.startswith('exit') or uaction.startswith('quit'):
        break

    elif uaction.startswith('show') or uaction.startswith('display'):
        for i,todo in enumerate(get_todos(todos_file), start=1):
            print(f'{i} - {todo}', end='')

    elif uaction.startswith('add'):
        todos = get_todos(todos_file)
        todo = uaction[4:] + '\n'
        todos.append(todo)
        write_todos(todos_file, todos)

    elif uaction.startswith('edit'):
        try:
            todos = get_todos(todos_file)
            num_todo = int(uaction[5:]) - 1
            todos[num_todo] = input('Enter new todo: ') + '\n'
            write_todos(todos_file, todos)
        except ValueError:
            print('Enter number, not string')
            continue

    elif uaction.startswith('complete'):
        try:
            todos = get_todos(todos_file)
            num_todo = int(uaction[9:]) - 1
            poped_todo = todos[num_todo].strip('\n')
            todos.pop(num_todo)
            write_todos(todos_file, todos)
            print(f'Todo "{poped_todo}" was removed from the list..')
        except IndexError:
            print('Out of list..')
            continue
    else:
        print('Use command!')
