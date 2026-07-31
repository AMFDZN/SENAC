
# Instrução geral
# Crie um programa em Python que funcione como um menu de opções utilizando
# match-case. O usuário deverá escolher uma opção do menu e cada opção
# executará um dos exercícios abaixo. Todos os exercícios devem estar organizados
# dentro de um único menu.
# Regras do programa
# O programa deve utilizar match-case para o menu principal. Cada opção do menu
# deve executar um exercício diferente. Deve existir uma opção para sair do
# programa. Cada exercício deve funcionar de forma independente dentro do menu.
def Linha():
    print("-" *30)
def Linhazinha():
    print("\/" *12)
    
while True:

    print("Menu de Opções match / case")
    print("1 - Calcular uma divisão entre dois números")
    print("2 - Verificar sua idade")
    print("3 - Avaliar 5 números digitados")
    print("4 - Criar uma lista de nomes")
    print("5 - Validar a entrada de números positivos")
    print("6 - Um novo menu de opções")
    
    opcao = input("Escolha sua opção: ").strip()
    match opcao:
        case "1":
        # Exercício 1
# Faça um programa que peça dois números ao usuário e exiba o resultado da
# divisão. Trate divisão por zero e entradas inválidas.
            
            Linha()
            
        case "2":
            Linha()
        
        case "3":
            Linha()
        case "4":
            Linha()
        case "5":
            Linha()
        case "6":
            Linha()

    
# Exercício 2
# Peça a idade do usuário. Se a idade for negativa, levante um erro manualmente
# com a mensagem Idade inválida. Caso contrário, mostre a idade.
# Exercício 3
# Peça ao usuário que digite 5 números. Para cada um, valide a entrada, acumule a
# soma, conte quantas entradas foram válidas e mostre no final a média dos
# números digitados.
# Exercício 4
# Peça ao usuário para informar quantos nomes deseja inserir e crie a lista. Verifique
# se um nome digitado pelo usuário está presente na lista. Mostre a lista ordenada.
# Inverta a ordem da lista e mostre o resultado.
# Exercício 5
# Peça ao usuário para informar quantos números inteiros positivos deseja inserir.
# Para cada valor: Permita apenas números inteiros e positivos. Caso contrário,
# exiba uma mensagem de erro e peça novamente. Exiba a lista final e a quantidade
# de números válidos inseridos.
# Exercício 6
# Crie um programa com o seguinte menu:
# 1 - Adicionar item à lista
# 2 - Remover item pelo índice
# 3 - Verificar se um item está na lista
# 4 - Mostrar todos os itens
# 5 - Ordenar lista
# 6 - Sair 
# O programa deve:
# Começar com uma lista vazia. Permitir que o usuário insira a quantidade de itens
# sempre que necessário. Utilizar um controle de menu. Capturar entradas
# inválidas.