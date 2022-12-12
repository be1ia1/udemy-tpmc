import streamlit as st
import functions

if 'new_todo' not in st.session_state:
   st.session_state.new_todo = ''

todos = functions.get_todos()

def update_new_todo():
    if st.session_state.new_todo != '':
        todos.append(st.session_state.new_todo + '\n')
        st.session_state['new_todo'] = ''
        functions.write_todos(todos)

st.title('My Todo App')

st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')

st.text_input(label='todo', label_visibility='hidden',
              placeholder='Add new todo..',
              on_change=update_new_todo(),
              key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
 
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()