# Instrução geral
# Crie um programa em Python que funcione como um menu de opções utilizando
# match-case. O usuário deverá escolher uma opção do menu e cada opção
# executará um dos exercícios abaixo. Todos os exercícios devem estar organizados
# dentro de um único menu.
#Regras do programa
# O programa deve utilizar match-case para o menu principal. Cada opção do menu
# deve executar um exercício diferente. Deve existir uma opção para sair do
# programa. Cada exercício deve funcionar de forma independente dentro do menu.
#viva as funções python!
def Linha():
    print("╍" *30)
    
def Linhazinha():
    print("╌" *30)

#variáveis UI/UX para terminal 😎
seta="🠆"
linha =("╍"*30)
linhazinha=("╌"*30)
    
while True:
    print("Menu de opções. Selecione um dos exercícios")
    print("1- Avalia se pode fazer CNH, pela idade.")
    print("2- Confirmar letra digitada.")
    print("3- Veja a quantidade de números pares em uma sequência.")
    print("4- Veja se o número digitado é maior, menor ou igual a 10.")
    print("5- Veja quantas vogais têm na sua frase digitada.")
    print("6- Trocar letras de uma frase.")
    print("7- surpresa ")

    opcao = input("\nEscolha uma opção: ")
    Linha()
    match opcao:
        case "1":
# Exercício 1
# Faça um while que peça para o usuário digitar 4 idades e, para cada uma, informe
# se a pessoa pode dirigir.
            print("Informe 4 idades para verificar se 4 pessoas têm a idade necesária para ter uma CNH")
            contador = 1  #iniciando com 1, pra ficar mais "bonito" na hora de pedir para informar a idade
            
            # O laço vai rodar enquanto o contador for menor ou igual a 4
            while contador <= 4: #4 voltas
                idade=1
                idade = int(input(f"Digite a idade nº{contador}: "))
                #verifica se a udade é compatível, e dá o resultado
                if idade >= 18:
                    print(f"Com {idade} anos, a pessoa nº{contador} PODE dirigir! 🚗")
                else:
                    print(f"Com {idade} anos, a pessoa nº{contador} NÃO pode dirigir. 🛑")
                
                print(".~." * 20) # Linha separadora simples entre as idades
                
                contador += 1
                # final dos testes
            Linha()
            input("Pressione Enter para voltar ao menu.")
        case "2":
            # Exercício 2
            # Peça para o usuário digitar 3 opções a, b, c ou outra letra usando while e match case.
            # mostre uma mensagem para cada opção, conforme:
            # a = Você escolheu a opção A
            # b = Você escolheu a opção B
            # c = Você escolheu a opção C
            # outra = Opção inválida
            print("\nExercício 2: match / case. Informe 3 letras: a, b ou c.")
            
            contador = 1 
            
            while contador <= 3:
                opcaoLetra = input(f"Tentativa {contador}/3 - Escolha uma letra (a, b ou c): ").strip().lower() #strip e lower para para tratar a variável
                
                match opcaoLetra:
                    case "a":
                        print("Você escolheu a opção A")
                    case "b":
                        print("Você escolheu a opção B")
                    case "c":
                        print("Você escolheu a opção C")
                    case _: # O underline representa "qualquer outra coisa" (padrão/default)
                        print("Opção inválida")
                
                print("~" * 20) # Linha separadora entre as tentativas
                contador += 1
                
            Linha()
            input("Pressione Enter para voltar ao menu.")
    
    # Exercício 3
    # Peça para o usuário digitar um número n. Com um while e usando o operador %,
    # imprima todos os números pares de 0 até n.
        case "3":  
            limiteContador = int(input("exercício 3:\n Digite um número para ser o contador de voltas de um laço while, e saber quantos números pares existem: "))
            contador = 1
            print(f"Os números pares de 1 a {limiteContador} são: ")
            while contador <= limiteContador:
                if contador % 2 == 0:
                    print(contador, end=", ")
                contador += 1
            Linha()
            input("Pressione Enter para voltar ao menu.")
    # Exercício 4
    # Peça para o usuário digitar 5 números. Use um for para imprimir se cada número é
    # maior, menor ou igual a 10.
        case "4":
            print("Digite 5 números para fazermos uma comparação em relação ao número \"10\"")
            for i in range(1, 6): #faz uma pergunta a cada volta, e já reebe a resposta
                
                numeroDigitado = float(input(f"Digite o {i}º número: "))
                #comparação com 10
                if numeroDigitado > 10:
                    print(f"O número {numeroDigitado} é MAIOR que 10.")
                elif numeroDigitado < 10:
                    print(f"O número {numeroDigitado} é MENOR que 10.")
                else:
                    print(f"O número {numeroDigitado} é IGUAL a 10.")
                
                print("~." * 20)
            Linha()
            input("Pressione Enter para voltar ao menu.")
        case "5":
# Exercício 5
# Peça para o usuário digitar uma frase e, usando um for, conte quantas vogais ela
# possui.   
            print("Exercício 5:\n Contando vogais de uma frase")
            fraseOriginal = input("Digite uma frase: ")
            frase = fraseOriginal.lower()
            
            totalVogais = 0
            
            for letra in frase: # percorre a frse a procura de vogais
                if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
                    totalVogais += 1  # Soma 1 ao total de vogais encontradas
            
            print(f"A frase:\n{fraseOriginal}\npossui {totalVogais} vogais.")
            # Exercício 6
            # Faça um programa que recebe um texto e duas letras. Usando for, substitua todas
            # as ocorrências da primeira letra pela segunda e mostre o texto resultante.
            Linha()
            input("Pressione Enter para voltar ao menu.")
        case "6":
            
            print("\nExercício 6:\nSubstituir uma letra em uma frase")
            
            fraseOriginal = input("Digite uma frase: ")
            letraTrocar = input("Digite a letra que deseja trocar: ")
            letraNova = input("Digite a nova letra que vai entrar no lugar: ")
            
            novaFrase = ""
            
            # percorre os caracteres da string original comparando com a letra a mudar
            for letra in fraseOriginal:
                if letra == letraTrocar:
                    novaFrase += letraNova #incrementa à nova frase a letra a trocar
                else:
                    novaFrase += letra #(ou) mantém a mesma letra

            print(f"A frase original\n{fraseOriginal}")
            print(f"Texto resultante\n{novaFrase}")
            Linha()
            
        case "7":
            
            Linha()
        case _:
            print("opçao inexistente")