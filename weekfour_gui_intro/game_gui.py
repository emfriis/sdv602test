import PySimpleGUI as sg

scene1 = [
    [sg.Text('scenetitle')],
    [sg.Text('scenedesc')], 
    [sg.Button('option1_1'), sg.Button('option1_2')]
]
window = sg.Window('windowtitle1', scene1)

def scene1_1():
    scene1_1 = [
        [sg.Text('scenetitle')],
        [sg.Text('scenedesc')], 
        [sg.Button('option1_1_1'), sg.Button('option1_1_2')]
    ]
    return sg.Window('windowtitle1_1', scene1_1)

def scene1_2():
    scene1_2 = [
        [sg.Text('scenetitle')],
        [sg.Text('scenedesc')], 
        [sg.Button('option1_2_1'), sg.Button('option1_2_2')]
    ]
    return sg.Window('windowtitle1_2', scene1_2)

def scene1_1_1():
    scene1_1_1 = [
        [sg.Text('scenetitle')],
        [sg.Text('scenedesc')], 
        [sg.Button('exit')]
    ]
    return sg.Window('windowtitle1_1_1', scene1_1_1)

def scene1_1_2():
    scene1_1_2 = [
        [sg.Text('scenetitle')],
        [sg.Text('scenedesc')], 
        [sg.Button('exit')]
    ]
    return sg.Window('windowtitle1_1_2', scene1_1_2)

def scene1_2_1():
    scene1_2_1 = [
        [sg.Text('scenetitle')],
        [sg.Text('scenedesc')], 
        [sg.Button('exit')]
    ]
    return sg.Window('windowtitle1_2_1', scene1_2_1)

def scene1_2_2():
    scene1_2_2 = [
        [sg.Text('scenetitle')],
        [sg.Text('scenedesc')], 
        [sg.Button('exit')]
    ]
    return sg.Window('windowtitle1_2_2', scene1_2_2)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'exit':
        break
    if event == 'option1_1':
        window = scene1_1()  
    if event == 'option1_2':
        window = scene1_2()
    if event == 'option1_1_1':
        window = scene1_1_1()
    if event == 'option1_1_2':
        window = scene1_1_2()
    if event == 'option1_2_1':
        window = scene1_2_1()
    if event == 'option1_2_2':
        window = scene1_2_2()