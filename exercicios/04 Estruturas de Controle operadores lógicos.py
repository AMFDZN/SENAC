
# Exercício 1 
# Crie um programa que receba uma nota de 0 a 10 e exiba: 
# Reprovado se a nota for menor que 5 
# Recuperação se a nota estiver entre 5 e 6.9 
# Aprovado se for 7 ou mais 
linha="\n--------------------------------\n"

print(f"{linha}VAMOS VERIFICAR NOTAS DE UM ALUNO, PARA AVALIAÇÃO")
numero1=float(input("INFORME A NOTA (de 1.0 a 10.0) NA MATÉRIA (ESTRUTURAS DE CONTROLE): "))
if numero1 >5:
    if numero1 <7:
        print(f"Com a nota {numero1} o aluno está em RECUPERAÇÃO")
    elif numero1>10:
        print("O aluno fraudou a sua nota, informando uma nota maior que (10)\nPor este motivo está EM RECUPERAÇÃO.")
    else:
        print(f"O aluno está Aprovado")
else:
    print("O aluno está REPROVADO")
# Exercício 2 
# Peça ao usuário para digitar uma letra e informe se é vogal ou consoante. 
# Considere apenas letras do alfabeto e trate maiúsculas e minúsculas. 
print(f"{linha}VAMOS VERIFICAR SE UMA LETRA É VOGAL OU CONSOANTE")
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
print(f"{linha}CLASSIFICANDO UM NUMERAL")
numero1=input("Digite um número inteiro para o classificarmos dentro do conceito numeral: ").strip()

if numero1.lstrip("-").isdigit() and numero1 != "-":
    numero1 = int(numero1)  
    if numero1 > 0:
        if numero1 % 2 == 0:
            print(f"O número {numero1} é um número POSITIVO, e é um número PAR")
        else:
            print(f"O número {numero1} é um número POSITIVO, e também é um número ÍMPAR")
    else:
        if numero1 % 2 == 0:
            print(f"O número {numero1} é um número NEGATIVO, e também é um número PAR")
        else:
            print(f"O número {numero1} é um número NEGATIVO, e também é um número ÍMPAR")    
else:
    if numero1==0:
        print(f"{numero1} é ZERO")
    else:
        print(F"{numero1} não é um número válido\n")
 
# Exercício 4 
# Peça ao usuário para digitar a temperatura em Celsius. Informe se está: 
# Muito frio (abaixo de 10) 
# Frio (entre 10 e 20) 
# Agradável (entre 21 e 25) 
# Quente (entre 26 e 30) 
# Muito quente (acima de 30) 
print(f"{linha}VAMOS CLASSIFICAR COMO A TEMPERATURA ESTÁ")
temperatura=input("Informe uma temperatura em graus Celsius: ").strip()

if temperatura.lstrip("-").isdigit() and temperatura != "-":
    temperatura = int(temperatura)
    if temperatura<10:
        print("Muito frio")
    elif temperatura>=10 and temperatura<=20:
        print("Frio")
    elif temperatura >20 and temperatura<25:
        print("Agradável")
    elif temperatura >25 and temperatura<30:
        print("Quente")
    elif temperatura>30:
        print("Muito quente")
    else:
        print("?")
else:
    print(f"{temperatura} não é um valor válido para temperatura")
    
    
# Exercício 5 
# Faça um programa que pergunte a idade de uma pessoa e informe a sua categoria de 
# acordo com a tabela: 
# 0 a 12 anos: Criança 
# 13 a 17 anos: Adolescente 
# 18 a 59 anos: Adulto 
# 60 anos ou mais: Idoso 
print(f"{linha}VAMOS CLASSIFICAR SUA FAIXA ETÁRIA")
idade=input("Informe sua idade: ").strip()

if idade.isdigit():
    idade=int(idade)
    if idade<12 and idade>0:
        print("Você é Criança")
    elif idade >12 and idade<18:
        print("Você é Adolescente")
    elif idade >17 and idade<60:
        print("Você é Adulto")
    elif idade >59:
        print("Você é Idoso")
    else:
        print("Idade inválida")
else:
    print(f"{idade} não é um valor numério.")    
# Exercício 6 
# Crie um programa que peça ao usuário para digitar três números e informe qual deles é o 
# maior. 
print(f"{linha}INFORME 3 NÚMEROS INTEIROS, A PARTIR DE ZERO, PARA VERIFICAR QUAL DELES É MAIOR")
numero1 = input("Digite o primeiro número: ").strip()

if not numero1.isdigit():
    numero1 = input(f"{numero1} não é um valor válido\nDigite novamente o primeiro número: ").strip()
elif int(numero1)<=0:
    numero1 = input(f"{numero1} não é um valor válido\nDigite novamente o primeiro número: ").strip()
else:
    numero1=int(numero1)
      
numero2 = input("Digite o segundo número: ").strip()
if not numero2.isdigit():
    numero2 = input(f"{numero2} não é um valor válido\nDigite novamente o segundo número: ").strip()
elif int(numero2)<=0:
    numero2 = input(f"{numero2} não é um valor válido\nDigite novamente o segundo número: ").strip()
else:
    numero2=int(numero2)
numero2=int(numero2)
    
numero3 = input("Digite o primeiro número: ").strip()
if not numero3.isdigit():
    numero3 = input(f"{numero3} não é um valor válido\nDigite novamente o terceiro número: ").strip()
elif int(numero3)<=0:
    numero3 = input(f"{numero3} não é um valor válido\nDigite novamente o terceiro número: ").strip()
else:
    numero3=int(numero3)
numero3=int(numero3) #não consegui validar

#comparação
numeroMaior=numero1

if numero2 > numeroMaior:
    numeroMaior=numero2   

if numero3 > numeroMaior:
    numeroMaior=numero3
    
print(f"{numeroMaior} é o maior número entre os três")    
 
# Exercício 7 
# Crie um programa que peça um número inteiro e diga se ele é múltiplo de 3, de 5, de 
# ambos, ou de nenhum.
print(f"{linha}VAMOS FAZER UMA ANÁLISE DE UM NÚMERO\nEM RELAÇÃO À SUA \"MULTIPLICIDADE\" POR 3 E POR 5:") 
numero1=input("Informe o número para o teste: ").strip()
if not numero1.isdigit():
    numero1=input("Informe o NÚMERO para o teste: ").strip()
else:
    numero1=int(numero1)
    if numero1 % 3 == 0 and numero1 % 5 == 0:
        print(f"O número {numero1} é múltiplo de ambos (3 e 5).")
    elif numero1 % 3 == 0:
        print(f"O número {numero1} é múltiplo apenas de 3.")
    elif numero1 % 5 == 0:
        print(f"O número {numero1} é múltiplo apenas de 5.")
    else:
        print(f"O número {numero1} não é múltiplo de nenhum deles.")
    
# Exercício 8 
# Faça um programa que leia uma senha e valide: 
# A senha deve ter pelo menos 8 caracteres 
# Deve conter pelo menos uma letra minúscula 
# Se a senha for válida, imprima Senha válida, senão imprima qual regra ela não passou. 
print(f"{linha}VAMOS FAZER UM TESTE DE VALIDAÇÃO, SIMULANDO A FORMATAÇÃO ACEITA EM UMA SENHA")
senha=input("DIGITE A SENHA\nDeve ter pelo menos 8 caracteres.\nDeve conter pelo menos uma letra minúscula\n")

#if senha >8 and senha.
""" ideia
validar se a senha em uppercase -e igual a em lower case, se não for é cero que tem ao menosuma maiúscula
"""
senhaUpper = senha.upper()
if senhaUpper == senha or len(senha) >= 8:
    if senhaUpper==senha:
        print("Senha inválida\nNão há uma letra minúscula na senha")
    else:
        print("Senha inválida\nA senha precisa ter 8 ou mais catacteres")
else:
    print("Senha válida")
    
