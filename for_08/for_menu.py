while True:
    print("\n Menu de Exemplos: ")
    print("1  - For com range")
    print("2  - For com range definido pelo usuário")
    print("3  - Range começando do 1 até 5")
    print("4  - Range com início definido pelo usuário")
    print("5  - Range com passo de 2")
    print("6  - Range com intervalo definido pelo usuário")
    print("7  - Range regressivo")
    print("8  - Range regressivo personalizado")
    print("9  - Iterando caracteres de uma string")
    print("10 - Comparação de números")
    print("11 - Operadores lógicos")
    print("12 - Match case dentro do for")
    print("13 - Contar letras maiúsculas")
    print("14 - Contar vogais")
    print("15 - Verificar número par ou ímpar")
    print("16 - Substituir letras em um texto")
    print("17 - Soma, máximo e mínimo")
    print("0  - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:

        case "1":
            print("Exemplo for com range")
            for i in range(5):
                print(f"Volta {i}")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "2":
            print("Exemplo for com range")
            voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
            for i in range(voltas):
                print(f"Iteração {i}")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "3":
            print("Exemplo com range começando do 1 até 5")
            for i in range(1, 6):
                print(i)
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "4":
            inicio = int(input("Digite o valor de início das voltas: "))
            voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
            for i in range(inicio, voltas):
                print(i)
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "5":
            print("Exemplo com passo de 2 no range")
            for i in range(0, 10, 2):
                print(i)
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "6":
            print("Exemplo com passo personalizado no range")
            inicio = int(input("Digite o valor de início das voltas: "))
            voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
            intervalo = int(input("Digite o valor de intervalo das voltas: "))
            
            for i in range(inicio, voltas, intervalo):
                print(i)
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "7":
            print("Exemplo com range regressivo")
            for i in range(5, 0, -1):
                print(i)
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "8":
            print("Exemplo com range regressivo personalizado")
            inicio = int(input("Digite o valor de início das voltas: "))
            voltas = int(input("Digite o valor final das voltas: "))
            intervalo_regressivo = int(input("Digite o valor do intervalo regressivo: "))

            for i in range(inicio, voltas, intervalo_regressivo):
                print(i)
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "9":
            print("Iterando caracteres de uma string")
            texto = input("Digite uma palavra para iterar seus caracteres: ")

            for letra in texto:
                print(letra)

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "10":
            print("Usando operadores de comparação dentro do for")
            print("Digite 5 números para analisar se são maiores, menores ou iguais a 3:")

            for i in range(5):
                num = int(input(f"Número {i+1}: "))

                if num > 3:
                    print(f"{num} é maior que 3")
                elif num == 3:
                    print(f"{num} é igual a 3")
                else:
                    print(f"{num} é menor que 3")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "11":
            print("Operadores lógicos and, or e not dentro do for")
            print("Digite 3 idades para verificar se podem dirigir:")

            for i in range(3):
                idade = int(input(f"Idade {i+1}: "))
                carteira = input("Tem carteira de motorista? (s/n): ").lower()

                if idade >= 18 and carteira == 's':
                    print("Pode dirigir")
                elif idade < 18 or not carteira == 's':
                    print("Não pode dirigir")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "12":
            print("Exemplo match case dentro do for")
            print("Digite 4 opções (a, b, c ou outra letra):")

            for i in range(4):
                escolha = input(f"Opção {i+1}: ").lower()

                match escolha:
                    case 'a':
                        print("Você escolheu a opção A")
                    case 'b':
                        print("Você escolheu a opção B")
                    case 'c':
                        print("Você escolheu a opção C")
                    case _:
                        print(f"Opção '{escolha}' inválida")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "13":
            print("Contando letras maiúsculas em uma palavra")

            palavra = input("Digite uma palavra: ")
            maiusculas = 0

            for letra in palavra:
                if letra.isupper():
                    maiusculas += 1

            print(f"A palavra tem {maiusculas} letras maiúsculas.")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "14":
            print("Contando vogais em uma frase")

            vogais = "aeiouAEIOU"
            frase = input("Digite uma frase para contar as vogais: ")
            cont_vogais = 0

            for letra in frase:
                if letra in vogais:
                    cont_vogais += 1

            print(f"A frase tem {cont_vogais} vogais.")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "15":
            print("Verificando número par ou ímpar com for")
            print("Digite 4 números:")

            for i in range(4):
                num = int(input(f"Número {i+1}: "))

                if num % 2 == 0:
                    print(f"{num} é par")
                else:
                    print(f"{num} é ímpar")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "16":
            texto = input("Digite um texto: ")
            letra_substituir = input("Digite a letra que deseja substituir: ")
            letra_substituta = input("Digite a letra substituta: ")

            novo_texto = ""

            for caractere in texto:
                if caractere == letra_substituir:
                    novo_texto += letra_substituta
                else:
                    novo_texto += caractere

            print(f"Texto original: {texto}")
            print(f"Texto modificado: {novo_texto}")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "17":
            print("Soma, máximo e mínimo de 3 números")

            soma = 0.0
            maximo = None
            minimo = None

            for i in range(1, 4):
                num = float(input(f"Digite o número {i}: "))

                soma += num

                if maximo is None or num > maximo:
                    maximo = num

                if minimo is None or num < minimo:
                    minimo = num

            print(f"Soma dos números: {soma}")
            print(f"Maior número: {maximo}")
            print(f"Menor número: {minimo}")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "0":
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida!")
            input("Pressione Enter para voltar ao menu.")