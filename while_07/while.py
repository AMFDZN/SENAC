import random

while True:
    print("\n Menu de Exemplos com while ")
    print("1  - While com contador simples")
    print("2  - While com número definido pelo usuário")
    print("3  - While com incremento personalizado")
    print("4  - While com decremento")
    print("5  - Iterando string com while")
    print("6  - Comparação de números")
    print("7  - Operadores lógicos")
    print("8  - Match case dentro do while")
    print("9  - Contar letras maiúsculas")
    print("10 - Contar vogais")
    print("11 - Verificar número par ou ímpar")
    print("12 - Substituir letras em um texto")
    print("13 - Soma, máximo e mínimo")
    print("14 - While com break")
    print("15 - While com continue")
    print("16 - While com else")
    print("17 - Jogo de adivinhação")
    print("18 - Menu interativo")
    print("0  - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:

        case "1":
            print("While com contador simples")
            i = 0
            while i < 5:
                print(f"Iteração {i}")
                i += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "2":
            print("While com número definido pelo usuário")
            voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))

            contador = 0
            while contador < voltas:
                print(f"Iteração {contador}")
                contador += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "3":
            print("While com incremento personalizado")

            inicio = int(input("Digite o valor de início: "))
            fim = int(input("Digite o valor final (exclusivo): "))
            passo = int(input("Digite o valor do incremento: "))

            i = inicio

            while i < fim:
                print(i)
                i += passo

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "4":
            print("While com decremento")

            inicio = int(input("Digite o valor inicial: "))
            fim = int(input("Digite o valor final (parada): "))
            passo = int(input("Digite o valor do decremento (ex: -1): "))

            i = inicio

            while i > fim:
                print(i)
                i += passo

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "5":
            print("Iterando string com while")

            texto = input("Digite uma palavra: ")

            i = 0

            while i < len(texto):
                print(texto[i])
                i += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "6":
            print("Comparação de números")
            print("Digite 5 números para analisar se são maiores, iguais ou menores que 3:")

            contador = 0

            while contador < 5:
                num = int(input(f"Número {contador + 1}: "))

                if num > 3:
                    print(f"{num} é maior que 3")
                elif num == 3:
                    print(f"{num} é igual a 3")
                else:
                    print(f"{num} é menor que 3")

                contador += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "7":
            print("Operadores lógicos")
            print("Digite 3 idades e se possuem carteira de motorista para verificar se podem dirigir:")

            contador = 0
            while contador < 3:
                idade = int(input(f"Idade {contador + 1}: "))
                carteira = input("Tem carteira de motorista? (s/n): ").lower()

                if idade >= 18 and carteira == "s":
                    print("Pode dirigir")
                else:
                    print("Não pode dirigir")

                contador += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "8":
            print("Match case dentro do while")
            print("Digite 4 letras para ver uma mensagem personalizada:")

            contador = 0
            while contador < 4:
                letra = input(f"Letra {contador + 1}: ").lower()

                match letra:
                    case "a":
                        print("Você escolheu A")
                    case "b":
                        print("Você escolheu B")
                    case "c":
                        print("Você escolheu C")
                    case _:
                        print(f"Opção '{letra}' inválida")

                contador += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "9":
            print("Contando letras maiúsculas em uma palavra")

            palavra = input("Digite uma palavra: ")

            i = 0
            maiusculas = 0

            while i < len(palavra):
                if palavra[i].isupper():
                    maiusculas += 1
                i += 1

            print(f"A palavra tem {maiusculas} letras maiúsculas.")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "10":
            print("Contando vogais em uma frase")

            vogais = "aeiouAEIOU"
            frase = input("Digite uma frase: ")

            i = 0
            contador_vogais = 0

            while i < len(frase):
                if frase[i] in vogais:
                    contador_vogais += 1
                i += 1

            print(f"A frase tem {contador_vogais} vogais.")
            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "11":
            print("Verificando números pares ou ímpares")

            contador = 0

            while contador < 4:
                num = int(input(f"Número {contador + 1}: "))

                if num % 2 == 0:
                    print(f"{num} é par")
                else:
                    print(f"{num} é ímpar")

                contador += 1

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "12":
            print("Substituir letras em um texto")

            texto = input("Digite um texto: ")
            letra_antiga = input("Letra a ser substituída: ")
            letra_nova = input("Letra substituta: ")

            i = 0
            novo_texto = ""

            while i < len(texto):
                if texto[i] == letra_antiga:
                    novo_texto += letra_nova
                else:
                    novo_texto += texto[i]

                i += 1

            print(f"Texto original: {texto}")
            print(f"Texto modificado: {novo_texto}")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "13":
            print("Soma, máximo e mínimo de 3 números")

            soma = 0
            maximo = None
            minimo = None

            contador = 0

            while contador < 3:
                num = float(input(f"Digite o número {contador + 1}: "))

                soma += num

                if maximo is None or num > maximo:
                    maximo = num

                if minimo is None or num < minimo:
                    minimo = num

                contador += 1

            print(f"Soma total: {soma}")
            print(f"Maior número: {maximo}")
            print(f"Menor número: {minimo}")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "14":
            print("While com break")

            while True:
                comando = input("Digite 'sair' para encerrar: ").lower()

                if comando == "sair":
                    print("Saindo do loop...")
                    break

                print(f"Você digitou: {comando}")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "15":
            print("While com continue")

            contador = 0

            while contador < 6:
                contador += 1

                if contador == 3:
                    print("Pulei o número 3")
                    continue

                print(f"Número: {contador}")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "16":
            print("While com else")

            tentativas = 0

            while tentativas < 3:
                senha = input("Digite a senha: ")

                if senha == "1234":
                    print("Acesso concedido.")
                    break

                print("Senha incorreta.")
                tentativas += 1

            else:
                print("Número máximo de tentativas alcançado. Acesso bloqueado.")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "17":
            print("Jogo de adivinhação")
            print("Você tem 5 tentativas para adivinhar um número entre 1 e 20.")

            numero_secreto = random.randint(1, 20)
            tentativas = 0

            while tentativas < 5:
                palpite = int(input(f"Tentativa {tentativas + 1}: "))

                if palpite == numero_secreto:
                    print("Parabéns! Você acertou o número!")
                    break
                elif palpite < numero_secreto:
                    print("Muito baixo.")
                else:
                    print("Muito alto.")

                tentativas += 1

            else:
                print(f"Você perdeu! O número era {numero_secreto}")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")

        case "18":
            print("Menu interativo")

            while True:
                print("""
Escolha uma opção:
1 - Contar até um número
2 - Verificar par ou ímpar
3 - Iterar letras de uma palavra
4 - Voltar ao menu principal
                """)

                escolha = input("Digite sua opção: ")

                match escolha:
                    case "1":
                        limite = int(input("Digite até que número contar: "))
                        i = 1

                        while i <= limite:
                            print(i)
                            i += 1

                    case "2":
                        num = int(input("Digite um número: "))

                        if num % 2 == 0:
                            print(f"{num} é par")
                        else:
                            print(f"{num} é ímpar")

                    case "3":
                        palavra = input("Digite uma palavra: ")

                        i = 0
                        while i < len(palavra):
                            print(palavra[i])
                            i += 1

                    case "4":
                        break

                    case _:
                        print("Opção inválida.")

            print("-" * 30)
            input("Pressione Enter para voltar ao menu.")