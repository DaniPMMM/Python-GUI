# importa a biblioteca para interface
from PySimpleGUI import PySimpleGUI as sg


sg.theme('Reddit') #escolhe um tema para a interface


#o comando key armazena os valores e serve para validação posteriormente
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]

]
#nomeia o nome da janela e a variável layout é armazenada dentro desta janela
janela = sg.Window('Cadastro', layout)

#o comando while true impede que o programa pare de funcionar
while True:
    eventos, valores = janela.read() #a variavel evento e valores servem para armezar os valores que estão em key
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'daniel' and valores['senha'] == '12345':
            print("Ebaaaaaaaaaaaaaaaaaaa")