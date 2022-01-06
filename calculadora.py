import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Yes

aux1 = 0
aux2 = 0
resultado = 0
operacao = ''

sg.theme('DarkBlue16')   # Adicionando a cor/tema
# Layout da janela com todas as coisas que vão compor ele.
layout = [  
            [sg.Button('       1       '), sg.Button('       2       '), sg.Button('       3       '), sg.Button('       /       ')],
            [sg.Button('       4       '), sg.Button('       5       '), sg.Button('       6       '), sg.Button('       x      ')],
            [sg.Button('       7       '), sg.Button('       8       '), sg.Button('       9       '), sg.Button('       -       ')],
            [sg.Button('       0       '), sg.Button('        .       '), sg.Button('       =       '), sg.Button('       +      ')],
            [sg.Button('Close')] ]

# Criando a janela
window = sg.Window('Calculadora', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # Se o usuario fechar a janela ou clicar em close
        break

    if event == '       1       ':
        aux1 = aux2
        aux2 = 1
    if event == '       2       ':
        aux1 = aux2
        aux2 = 2
    if event == '       3       ':
        aux1 = aux2
        aux2 = 3
    if event == '       4       ':
        aux1 = aux2
        aux2 = 4
    if event == '       5       ':
        aux1 = aux2
        aux2 = 5
    if event == '       6       ':
        aux1 = aux2
        aux2 = 6
    if event == '       7       ':
        aux1 = aux2
        aux2 = 7
    if event == '       8       ':
        aux1 = aux2
        aux2 = 8
    if event == '       9       ':
        aux1 = aux2
        aux2 = 9
    if event == '       0       ':
        aux1 = aux2
        aux2 = 0


    if event == '       +      ':
        operacao = '+'
    if event == '       -       ':
        operacao = '-'
    if event == '       x      ':
        operacao = 'x'
    if event == '       /       ':
        operacao = '/'
    
    
    if event == '       =       ':
        if operacao == '+':
            resultado = aux1 + aux2
        if operacao == '-':
            resultado = aux1 - aux2
        if operacao == 'x':
            resultado = aux1 * aux2
        if operacao == '/':
            resultado = aux1 / aux2
        sg.popup_no_border(resultado)
        aux1 = 0
        aux2 = 0
        resultado = 0
        operacao = ''

window.close()