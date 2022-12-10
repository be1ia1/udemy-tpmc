import PySimpleGUI as sg
from datetime import datetime
import functions

sg.theme('DarkTeal2')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button =  sg.Button('Add', key='Add')
list_box = sg.Listbox(functions.get_todos(),
                        key='todos',
                        enable_events=True,
                        size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(datetime.now().strftime("%B %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo 
                functions.write_todos(todos)
                window['todos'].update(todos)
            except IndexError:
                sg.Popup('Please select todo first..', font=('Helvetica', 16))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(todos)
                window['todo'].update('')
            except IndexError:
                sg.Popup('Please select todo first..', font=('Helvetica', 16))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(values['todos'][0][:-1])

        case sg.WIN_CLOSED:
            break



window.close()
