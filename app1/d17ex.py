import PySimpleGUI as sg

feet_input = sg.InputText('', key='feet')
inches_input = sg.InputText('', key='inches')
convert_button = sg.Button('Convert', key='convert')
result_text = sg.Text('', key='text')

window = sg.Window('Converter', layout=[[feet_input],
                                        [inches_input],
                                        [convert_button, result_text]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case sg.WIN_CLOSED:
            break
        case 'convert':
            answer = float(values['feet']) * 0.3048 + float(values['inches']) * 0.0254
            window['text'].update(answer)
window.close()
