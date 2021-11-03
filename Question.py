import PySimpleGUI as sg

i = 0
answers = []
sg.theme('Dark')
layout = [  [sg.Text('Question 1.')],
            [sg.Text('A: Antwoord 1'), sg.Text('B: Antwoord 2'),],
            [sg.Text('C: Antwoord 3'), sg.Text('D: Antwoord 4')],
            [sg.Button(button_text="A", key="A"), sg.Button(button_text="B", key="B"),
             sg.Button(button_text="C", key="C"), sg.Button(button_text="D",key="D")],

            [sg.Text('Question 2.')],
            [sg.Text('A: Antwoord 1'), sg.Text('B: Antwoord 2'),],
            [sg.Text('C: Antwoord 3'), sg.Text('D: Antwoord 4')],
            [sg.Button(button_text="A", key="A1"), sg.Button(button_text="B", key="B1"),
             sg.Button(button_text="C", key="C1"), sg.Button(button_text="D", key="D1")],

            [sg.Text('Question 3.')],
            [sg.Text('A: Antwoord 1'), sg.Text('B: Antwoord 2'),],
            [sg.Text('C: Antwoord 3'), sg.Text('D: Antwoord 4')],
            [sg.Button(button_text="A", key="A2"), sg.Button(button_text="B", key="B2"),
             sg.Button(button_text="C", key="C2"), sg.Button(button_text="D", key="D2")],

            [sg.Text('Question 4.')],
            [sg.Text('A: Antwoord 1'), sg.Text('B: Antwoord 2'),],
            [sg.Text('C: Antwoord 3'), sg.Text('D: Antwoord 4')],
            [sg.Button(button_text="A", key="A3"), sg.Button(button_text="B", key="B3"),
             sg.Button(button_text="C", key="C3"), sg.Button(button_text="D", key="D3")],
            ]
# Create the Window
window = sg.Window('Hoodlum', layout, resizable=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if i != 17:
        answers.append(event)
        print('The button clicked was "{}"'.format(event))
        i = i + 1
    print(answers)

window.close()
