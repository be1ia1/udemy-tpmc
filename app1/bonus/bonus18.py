import PySimpleGUI as sg
from zipfile import ZipFile

def extract_archive(archive_path, destination_path):
    with ZipFile(archive_path) as zipobj:
        zipobj.extractall(destination_path)

archive_select = sg.Text('Select archive to extract:')
archive_input = sg.InputText('')
archive_button = sg.FileBrowse('Choose', key='archive')
folder_select = sg.Text('Select destination folder:')
folder_input = sg.InputText('')
folder_button = sg.FolderBrowse('Choose', key='folder')
extract_button = sg.Button('Extract')

window = sg.Window('Archive Extractor', layout=[[archive_select, archive_input, archive_button],
                                                [folder_select, folder_input, folder_button],
                                                [extract_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Extract':
            print(values['archive'])
            print(values['folder'])
            extract_archive(values['archive'], values['folder'])
        case sg.WIN_CLOSED:
            break

window.close()