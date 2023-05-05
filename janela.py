from termcolor import colored
import emoji

print(colored(emoji.emojize(':alarm_clock: Ponto Eletrônico | Empresa Fictícia :chart_with_upwards_trend:', language='alias'), 'yellow'))

print(colored('\nMENU:\n', 'green'))
print(colored('1. Registrar', 'cyan'))
print(colored('2. Cadastros', 'cyan'))
print(colored('3. Sair\n', 'cyan'))