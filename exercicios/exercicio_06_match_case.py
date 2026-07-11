# Instrução geral
# Crie um programa em Python que funcione como um menu de opções utilizando 
# match-case. O usuário deverá escolher uma opção do menu e cada opção 
# executará um dos exercícios abaixo. Todos os exercícios devem estar organizados 
# dentro de um único menu.
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
    print("Menu de Opções match / case")
    print("1 - Verificar se  se qualifica para uma vaga de emprego")
    print("2 - Digitar 3 números inteiros, e verificar qual é maior")
    print("3 - Verificar se o aluno está aprovado, reprovado ou em recuperação")
    print("4 - digitar duas palavras e uma opção de E ou OU")
    print("5 - valor de uma compra, tipo de pagamento e desconto")
    print("6 - Sair")

    opcao = input("Escolha sua opção: ").strip()
    # Regras do programa
    # O programa deve utilizar match-case para o menu principal. Cada opção do menu 
    # deve executar um exercício diferente. Deve existir uma opção para sair do 
    # programa. Cada exercício deve funcionar de forma independente dentro do menu.

    match opcao:
        case "1":
    # Exercício 1
    # Peça para o usuário digitar sua idade, seu salário e o número de anos de 
    # experiência.
    # Verifique e informe se ele se qualifica para uma vaga de emprego que exige:
    # Idade maior ou igual a 30 e salário maior ou igual a 4000.
    # Ou se ele tem mais de 10 anos de experiência, independentemente da idade e 
    # salário.
            print("Informe seus dados para ser avaliado a uma vaga de emprego aqui:")
            idade = int(input("Quantos anos de idade você tem? "))
            salarioAtual = float(input("Qual o seu salário atual? R$"))
            experiencia = int(input("Quantos anos de experiência você tem? "))
            if idade >=30 and salarioAtual >=4000 and experiencia >10:
                print("\nVoce é qualificado para a vaga.\nAguarde que ligaremos pra você")
            elif experiencia >10:
                print("\nVoce é qualificado para a vaga.\nAguarde que ligaremos pra você")
            else:
                print("\nVoce não é qualificado para a vaga.\nProcure outro ramo de atividade.")
            print(linha)
            print("Clique ENTER para voltar ao menu")
        case "2":
            # Exercício 2
            # Peça para o usuário digitar três números inteiros.
            # Informe qual é o maior número e se ele é positivo ou se ele é múltiplo de 5, mas 
            # não múltiplo de 3.
            print("digitar três números inteiros")
            numero1=int(input("digite o primeiro número: "))
            numero2=int(input("digite o segundo número: "))
            numero3=int(input("digite o terceiro número: "))
            numeroMaior = max(numero1, numero2, numero3) #usando max da aula de quarta
            print(f"\nO número maior entre os números {numero1}, {numero2} e {numero3}, é o número: ({numeroMaior})")
            print(linha)
            if numeroMaior > 0:
                print(f"o {numeroMaior} é positivo.")
            elif numeroMaior < 0:
                print(f"o {numeroMaior} é negativo.")
            else:
                print(f"o {numeroMaior} é zero.")
            print(linhazinha)
            if numeroMaior % 5==0 and numeroMaior % 3!=0:
               print(f"O número {numeroMaior} é múltiplo de 5, mas NÃO é múltiplo de 3.")
    
            elif numeroMaior % 5 == 0 and numeroMaior % 3 == 0:
                print(f"O número {numeroMaior} é múltiplo de 5 e de 3.")
                    
            else:
                print(f"O número {numeroMaior} não é múltiplo de 5, portanto não veifiquei se é múltiplo de 3.") 
            print(linha)
            print("Clique ENTER para voltar ao menu")
        case "3":
    # Exercício 3
    # Peça para o usuário digitar a nota de uma prova de 0 a 10 e o número de faltas.
    # Informe se o aluno está aprovado, reprovado ou em recuperação, considerando:
    # Aprovado se a nota for maior ou igual a 7 e faltas menores ou iguais a 3.
    # Em recuperação se a nota for maior ou igual a 5, mas menor que 7, ou se a 
    # quantidade de faltas for maior que 3, mas menor ou igual a 5.
    # Reprovado se a nota for menor que 5 e as faltas forem maiores que 5.
            notaDaProva = float(input("Qual a sua nota na prova? "))
            numeroDeFaltas= int(input("Quantas faltas você teve? "))
            if notaDaProva >=7 and numeroDeFaltas <=5:
                print("Você está Aprovado")
            elif (notaDaProva >= 5 and notaDaProva < 7) or (numeroDeFaltas>3 and numeroDeFaltas<=5) :
                print("Você está em recuperação")
            elif notaDaProva<5 and numeroDeFaltas>5:
                print("Você está reprovado")            
            print(linha)
            print("Clique ENTER para voltar ao menu")
        case "4":
    # Exercício 4
    # Peça ao usuário para digitar duas palavras e uma opção de E ou OU.
    # Se a opção for E, verifique se ambas as palavras têm mais de 5 caracteres e não 
    # são iguais.
    # Se a opção for OU, verifique se pelo menos uma das palavras tem mais de 5 
    # caracteres ou se são iguais.
            print("Digite duas palavras para fazermos comparaçõesde comprimento")
            palavra1=input("Digite a primeira palavra: ")
            palavra2=input("Digite a segunda palavra: ")
            fatorComparador=input("Digite um dos dois fatores de comparação: E / OU ").lower()
            if fatorComparador=="e":
                if len(palavra1)> 5 and len(palavra2)>5 and palavra1!=palavra2:
                    print("são maiores que 5, e não são iguais")
            if fatorComparador=="ou":
                if len(palavra1)> 5 or len(palavra2)>5 or palavra1==palavra2:
                    print("alguma das palavras tem mais de 5 letras, e podem são iguais")

            print(linha)
            print("Clique ENTER para voltar ao menu")
        case "5":
    # Exercício 5
    # Peça para o usuário digitar o valor de uma compra e o tipo de pagamento à vista ou 
    # parcelado.
    # Se a compra for superior a R$500,00 e o pagamento for parcelado, aplique um 
    # desconto de 10%.
    # Caso contrário, aplique um desconto de 5% se o pagamento for à vista.
    # Informe o valor final após o desconto.
            # Exercício 5
            print("\nExercício 5: Cálculo de desconto em uma compra")
            
            valorCompra = input("Digite o valor da compra (somente números): R$").strip().replace(".", "").replace(",", ".")
            formaDePagamento = input("Digite a forma de pagamento (à vista ou parcelado): ").lower()
            valorCompra = float(valorCompra)
            
            if valorCompra > 500.00 and formaDePagamento == "parcelado":
                valorCompra = valorCompra * 0.90  # Aplica 10% de desconto (paga 90% do valor)
            
            elif formaDePagamento == "à vista" or formaDePagamento == "a vista" or formaDePagamento == "vista":
                valorCompra = valorCompra * 0.95  # Aplica 5% de desconto (paga 95% do valor)

            valorFinal = f"{valorCompra:.2f}".replace(".", ",") #:.2f pesquisa de como printar um float como string, na versão currency Real
            
            print(f"Valor final após o desconto: R${valorFinal}")
            print(linha)
            print("FIM!\n")
            print("Clique ENTER para voltar ao menu, se quiser repetir algum teste.")


        case _:
            print("opçao inexistente")



