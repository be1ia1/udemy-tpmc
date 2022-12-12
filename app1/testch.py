import streamlit as st
import functions

todos = ['first task', 'second task', 'third task']

todo1 = st.checkbox(todos[0], key='todo1')
todo2 = st.checkbox(todos[1], key='todo2')
todo3 = st.checkbox(todos[2], key='todo3')

print(st.session_state)

if todo2:
    st.write('you select 2')

if 'new_todo' not in st.session_state:
   st.session_state.new_todo = ''

st.title('My Todo App')

st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')


'''for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    print(index, checkbox)
 
    if checkbox:
        todos.pop(index)'''


def update_new_todo():
    if st.session_state.new_todo != '':
        todos.append(st.session_state.new_todo + '\n')
        st.session_state['new_todo'] = ''
        functions.write_todos(todos)



st.text_input(label='todo', label_visibility='hidden',
              placeholder='Add new todo..',
              on_change=update_new_todo(),
              key='new_todo')

