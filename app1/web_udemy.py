import streamlit as st
import functions
 
todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
 
st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')
 
for index, item in enumerate(todos):
    check = st.checkbox(item, key=item)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
 
st.text_input(label='',
              placeholder='Add new todo..',
              on_change=add_todo(),
              key='new_todo')