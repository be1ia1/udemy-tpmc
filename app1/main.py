import pathlib
todos_file = pathlib.PureWindowsPath('files/todos.txt')
print(todos_file)

while True:
    uaction = input('Type add, show, complete, edit or exit: ').strip()
    match uaction:
        case 'exit' | 'quit':
            break
        case 'show' | 'display':
            with open(todos_file) as fo:
                todos = fo.readlines()
            for i,todo in enumerate(todos, start=1):
                print(f'{i} - {todo}', end='')
        case 'add':
            todo = input('Enter a todo: ').title() + "\n"
            with open(todos_file) as fo:
                todos = fo.readlines()
            todos.append(todo)
            with open(todos_file, 'w') as fo:
                fo.writelines(todos)
        case 'edit':
            num_todo = int(input('Enter todo number: ')) - 1
            todos[num_todo] = input('Enter new todo: ')
        case 'complete':
            num_todo = int(input('Enter todo number: ')) - 1
            todos.pop(num_todo)
        case _:
            print('Use command!')
