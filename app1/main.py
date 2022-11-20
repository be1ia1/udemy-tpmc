import pathlib
todos_file = pathlib.PureWindowsPath('files/todos.txt')
print(todos_file)

while True:
    uaction = input('Type add, show, complete, edit or exit: ').strip()
    if uaction.startswith('exit') or uaction.startswith('quit'):
        break

    elif uaction.startswith('show') or uaction.startswith('display'):
        with open(todos_file) as fo:
            todos = fo.readlines()
        for i,todo in enumerate(todos, start=1):
            print(f'{i} - {todo}', end='')

    elif uaction.startswith('add'):
        with open(todos_file) as fo:
            todos = fo.readlines()
        todo = uaction[4:] + '\n'
        todos.append(todo)
        with open(todos_file, 'w') as fo:
            fo.writelines(todos)

    elif uaction.startswith('edit'):
        try:
            with open(todos_file) as fo:
                current_todos = fo.readlines()
            num_todo = int(uaction[5:]) - 1
            current_todos[num_todo] = input('Enter new todo: ') + '\n'
            with open(todos_file, 'w') as fo:
                fo.writelines(current_todos)
        except ValueError:
            print('Enter number, not string')
            continue

    elif uaction.startswith('complete'):
        try:
            with open(todos_file) as fo:
                current_todos = fo.readlines()
            num_todo = int(uaction[9:]) - 1
            poped_todo = current_todos[num_todo].strip('\n')
            current_todos.pop(num_todo)
            with open(todos_file, 'w') as fo:
                fo.writelines(current_todos)
            print(f'Todo "{poped_todo}" was removed from the list..')
        except IndexError:
            print('Out of list..')
            continue
    else:
        print('Use command!')
