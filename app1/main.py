from modules.functions import get_todos, write_todos

from datetime import datetime

now = datetime.now() 
print(f'it is {now.strftime("%B %d, %Y %H:%M:%S")}')

while True:
    uaction = input('Type add, show, complete, edit or exit: ').strip()
    if uaction.startswith('exit') or uaction.startswith('quit'):
        break

    elif uaction.startswith('show') or uaction.startswith('display'):
        for i,todo in enumerate(get_todos(), start=1):
            print(f'{i} - {todo}', end='')

    elif uaction.startswith('add'):
        todos = get_todos()
        todo = uaction[4:].capitalize() + '\n'
        todos.append(todo)
        write_todos(todos)

    elif uaction.startswith('edit'):
        try:
            todos = get_todos()
            num_todo = int(uaction[5:]) - 1
            todos[num_todo] = input('Enter new todo: ').capitalize() + '\n'
            write_todos(todos)
        except ValueError:
            print('Enter number, not string')
            continue

    elif uaction.startswith('complete'):
        try:
            todos = get_todos()
            num_todo = int(uaction[9:]) - 1
            poped_todo = todos[num_todo].strip('\n')
            todos.pop(num_todo)
            write_todos(todos)
            print(f'Todo "{poped_todo}" was removed from the list..')
        except IndexError:
            print('Out of list..')
            continue
    else:
        print('Use command!')
