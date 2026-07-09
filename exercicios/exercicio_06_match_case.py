# Instrução geral
# Crie um programa em Python que funcione como um menu de opções utilizando 
# match-case. O usuário deverá escolher uma opção do menu e cada opção 
# executará um dos exercícios abaixo. Todos os exercícios devem estar organizados 
# dentro de um único menu.
linha = ("--" * 20)
print("Menu de Opções if,elif e else")
print("1 - Verificar se  se qualifica para uma vaga de emprego")
print("2 - Digitar 3 números inteiros")
print("3 - Verificar se número é par ou ímpar")
print("4 - verificar se uma pessoa pode dirigir")
print("5 - verificar se pode entrar na festa")
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
        idade = int(input("Qual sua idade? "))
        salarioAtual = float(input("Informe o seu salário atual: R$"))
        experiencia = int(input("Quantos anos de experiência você tem? "))
        if idade >=30 and salarioAtual >=4000 and experiencia >10:
            print("Voce é qualificado para a vaga.\nAguarde que ligaremos pra você")
        else:
            print("Voce não é qualificado para a vaga.\nProcure outro ramo de atividade.")
        print(linha)
    case "2":
# Exercício 2
# Peça para o usuário digitar três números inteiros.
# Informe qual é o maior número e se ele é positivo ou se ele é múltiplo de 5, mas 
# não múltiplo de 3.
        print("digitar três números inteiros")
        numero1=int(input("digite o primeiro número"))
        numero2=int(input("digite o segundo número"))
        numero3=int(input("digite o terceiro número"))
        qualNumeroMaior = max(numero1, numero2, numero3)
        print(f"O número maior entre os números {numero1}, {numero2} e {numero3}, é o número: ({qualNumeroMaior})")

        if numero1 > 0:
            print("Número positivo.")
        elif numero1 < 0:
            print("Número negativo.")
        else:
            print("Número é zero.")
        print(linha)
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
        elif notaDaProva<5 and numeroDeFaltas>5
            print("Você está reprovado")
        elif 
        print(linha)
    case "4":
# Exercício 4
# Peça ao usuário para digitar duas palavras e uma opção de E ou OU.
# Se a opção for E, verifique se ambas as palavras têm mais de 5 caracteres e não 
# são iguais.
# Se a opção for OU, verifique se pelo menos uma das palavras tem mais de 5 
# caracteres ou se são iguais.

        print(linha)
    case "5":
        print(linha)



    case _:
        print("opçao inexistente")



# Exercício 4
# Peça ao usuário para digitar duas palavras e uma opção de E ou OU.
# Se a opção for E, verifique se ambas as palavras têm mais de 5 caracteres e não 
# são iguais.
# Se a opção for OU, verifique se pelo menos uma das palavras tem mais de 5 
# caracteres ou se são iguais.
# Exercício 5
# Peça para o usuário digitar o valor de uma compra e o tipo de pagamento à vista ou 
# parcelado.
# Se a compra for superior a R$500,00 e o pagamento for parcelado, aplique um 
# desconto de 10%.
# Caso contrário, aplique um desconto de 5% se o pagamento for à vista.
# Informe o valor final após o desconto.