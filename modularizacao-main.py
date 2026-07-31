from exercicios_01.main_01 import main_01 as executar_01
from exercicios_02.main_02 import main_02 as executar_02


def main():
    while True:
        print("\n Menu Principal ")
        print("1 - Acessar Lista de Exercícios 1")
        print("2 - Acessar Lista de Exercícios 2")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                executar_01()  
            case "2":
                executar_02()  
            case "0":
                print("Encerrando o programa principal...")
                break
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()