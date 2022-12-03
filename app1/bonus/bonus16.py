import PySimpleGUI as sg
from zip_creator import make_archive


files_select = sg.Text('Select files to compress:')
files_input = sg.InputText('')
files_button = sg.FilesBrowse('Choose', key='files')
folder_select = sg.Text('Select destination folder:')
folder_input = sg.InputText('')
folder_button = sg.FolderBrowse('Choose', key='folder')
output_text = sg.Text('', key='output')


compress_button = sg.Button('Compress')

window = sg.Window('File Zipper', layout=[[files_select,files_input,files_button],
                                            [folder_select,folder_input,folder_button],
                                            [compress_button, output_text]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Compress':
            filepaths = values['files'].split(';')
            folder = values['folder']
            print(filepaths, folder)
            make_archive(filepaths, folder)
            window['output'].update(value='Comression completed!')
        case sg.WIN_CLOSED:
            break


window.close()
