from modules.functions import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button =  sg.Button('Add')
list_box = sg.Listbox(get_todos(),
                        key='todos',
                        enable_events=True,
                        size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                    layout=[[label],[input_box, add_button],[list_box,edit_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo 
            write_todos(todos)
            window['todos'].update(todos)
        case 'todos':
            window['todo'].update(values['todos'][0][:-1])

        case sg.WIN_CLOSED:
            break



window.close()
