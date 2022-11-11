todos = []
while True:
    uaction = input('Type add, show or exit: ').strip()
    match uaction:
        case 'exit':
            break
        case 'show':
            for i in todos:
                print(i)
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)

