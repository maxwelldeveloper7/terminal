import csv
import datetime
import getpass

def registrar_ponto():
    nome = input("Digite seu nome: ")
    hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tipo_ponto = input("Digite 'e' para entrada ou 's' para saída: ")

    with open("registros.csv", "a", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, hora_atual, tipo_ponto])
    
    print("Ponto registrado com sucesso!")

def exibir_registros():
    nome = input("Digite seu nome: ")

    with open("registros.csv", "r") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        registros = [registro for registro in leitor if registro[0] == nome]

    if registros:
        print("Registros:")
        for registro in registros:
            print(f"Data/Hora: {registro[1]} - Tipo: {registro[2]}")
    else:
        print("Nenhum registro encontrado para esse nome.")

def autenticar():
    # usuario = input("Usuário: ")
    # senha = getpass.getpass("Senha: ")

    # Lógica para autenticação do usuário
    # ...

    return True  # Retorna True se a autenticação for bem-sucedida, ou False caso contrário

def menu_principal():
    while True:
        print("\n===== Sistema de Ponto Eletrônico =====")
        print("1. Registrar ponto")
        print("2. Exibir registros")
        print("3. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            registrar_ponto()
        elif opcao == "2":
            exibir_registros()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    autenticado = autenticar()

    if autenticado:
        menu_principal()
    else:
        print("Falha na autenticação. Encerrando o programa.")

if __name__ == "__main__":
    main()
