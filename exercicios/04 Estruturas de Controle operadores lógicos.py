
# Exercício 1 
# Crie um programa que receba uma nota de 0 a 10 e exiba: 
# Reprovado se a nota for menor que 5 
# Recuperação se a nota estiver entre 5 e 6.9 
# Aprovado se for 7 ou mais 
print("VAMOS VERIFICAR NOTAS DE UM ALUNO, PARA SUA APROVAÇÃO")
numero1=float(input("INFORME A NOTA (de 1.0 a 10.0) NA MATÉRIA (ESTRUTURAS DE CONTROLE): "))
if numero1 >5:
    if numero1 <6.9:
        print(f"Com a nota {numero1} o aluno está em RECUPERAÇÃO")
    elif numero1>10:
        print("O aluno fraudou a sua nota, informando uma nota maior que (10)")
    else:
        print(f"O aluno está Aprovado")
else:
    print("O aluno está REPROVADO")
# Exercício 2 
# Peça ao usuário para digitar uma letra e informe se é vogal ou consoante. 
# Considere apenas letras do alfabeto e trate maiúsculas e minúsculas. 
print("VAMOS VERIFICAR SE UMA LETRA É VOGAL OU CONSOANTE")
letraEnviada = input("Digite uma letra: ")
#tratando avariaável
letra = letraEnviada.strip().lower()

if len(letra) == 1 and letra.isalpha(): #se é alpha ou numérico
    if letra in "aeiouáàâãéêíóôõú": #com acento gráfico também se mantém como vogal ????
        print(f"A letra '{letraEnviada}' é uma VOGAL.")
    else:
        print(f"A letra '{letraEnviada}' é uma CONSOANTE.")
else:
    print("Entrada inválida.")
 
# Exercício 3 
# Faça um programa que peça ao usuário para digitar um número inteiro e informe se ele é: 
# Positivo par 
# Positivo ímpar 
# Negativo par 
# Negativo ímpar 
# Zero 
 
# Exercício 4 
# Peça ao usuário para digitar a temperatura em Celsius. Informe se está: 
# Muito frio (abaixo de 10) 
# Frio (entre 10 e 20) 
# Agradável (entre 21 e 25) 
# Quente (entre 26 e 30) 
# Muito quente (acima de 30) 
 
# Exercício 5 
# Faça um programa que pergunte a idade de uma pessoa e informe a sua categoria de 
# acordo com a tabela: 
# 0 a 12 anos: Criança 
# 13 a 17 anos: Adolescente 
# 18 a 59 anos: Adulto 
# 60 anos ou mais: Idoso 
 
# Exercício 6 
# Crie um programa que peça ao usuário para digitar três números e informe qual deles é o 
# maior. 
 
# Exercício 7 
# Crie um programa que peça um número inteiro e diga se ele é múltiplo de 3, de 5, de 
# ambos, ou de nenhum. 
 
# Exercício 8 
# Faça um programa que leia uma senha e valide: 
# A senha deve ter pelo menos 8 caracteres 
# Deve conter pelo menos uma letra minúscula 
# Se a senha for válida, imprima Senha válida, senão imprima qual regra ela não passou. 
 