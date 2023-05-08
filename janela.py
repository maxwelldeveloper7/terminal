from termcolor import colored
import emoji
import os

def limpar_terminal():
    if os.name == 'posix':  # Verifica se é um sistema Unix (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':  # Verifica se é um sistema Windows
        os.system('cls')
        
limpar_terminal()

print(colored(emoji.emojize(':alarm_clock: Ponto Eletrônico | Empresa Fictícia :chart_with_upwards_trend:', language='alias'), 'yellow'))

print(colored('\nMENU:\n', 'green'))
print(colored('1. Registrar', 'cyan'))
print(colored('2. Cadastros', 'cyan'))
print(colored('3. Sair\n', 'cyan'))