# Exercício 1  
# Crie um programa que peça ao usuário para digitar dois números e compare-os utilizando 
# os operadores >, <, >=, <=, ==, !=. Imprima o resultado de cada comparação de forma clara 
# e explicativa. 
#linha divisória
linha= "-" *30
#-------------------
print("-"*30)
print("digita dois números para fazermos algumas comparações entre os dois")
numero1=input("digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
#comparando o número 1 com o número 2
maior= numero1 > numero2
menor= numero1 < numero2
maior_ou_igual = numero1 >= numero2
menor_ou_igual = numero1 <= numero2
igual = numero1 == numero2
diferente = numero1 != numero2
print(f"COMPARAÇÕES\n{linha}")
if maior==True:
    print(f"o número {numero1} é maior que o número {numero2}\n{linha}")
if menor==True:
    print(f"o número {numero1} é menor que o número {numero2}\n{linha}")
if maior_ou_igual==True:
    print(f"o número {numero1} é maior ou igual ao número {numero2}\n{linha}")
if menor_ou_igual==True:
    print(f"o número {numero1} é menor ou igual ao número {numero2}\n{linha}")
if igual==True:
    print(f"o número {numero1} é igual ao número {numero2}\n{linha}")
if diferente==True:
    print(f"o número {numero1} é diferente do número {numero2}\n{linha}")

# Exercício 2  
# Crie um programa que peça ao usuário para digitar duas palavras (strings) e compare-as 
# utilizando os operadores >, <, ==, e !=. Exiba o resultado de cada comparação de maneira 
# clara.
print("\n")
print("Digite duas palavras para fazermos algumas comparações entre elas")
palavra1=input("Digite a primeira palavra: ") 
palavra2=input("Digite a segunda palavra: ") 
maior= len(palavra1) > len(palavra2)
menor= len(palavra1) < len(palavra2)
igual = len(palavra1) == len(palavra2)
diferente = len(palavra1) !=len(palavra2)
print("COMPARAÇÕES ENTRE PALAVRAS\n--------")
if maior==True:
    print(f"a palavra {palavra1} é maior que a palavra {palavra2}\n{linha}")
if menor==True:
    print(f"a palavra {palavra1} é menor que a palavra {palavra2}\n{linha}")
if igual==True:
    print(f"a palavra {palavra1} tem o mesmo tamanho da palavra {palavra2}\n{linha}")
if diferente==True:
    print(f"a palavra {palavra1} tem tamanho diferente da palavra {palavra2}\n{linha}")
# Exercício 3  
# Crie um programa que peça ao usuário para digitar um número e uma palavra (string). 
# Compare o número com a string utilizando os operadores == e !=. Converta o número para 
# uma string antes da comparação.
print("\n")
print("Digite um número e uma palavra para fazermos algumas comparações entre os dois")
palavra1=input("Digite a primeira palavra: ") 
numero1=input("Digite um número: ")
if palavra1 == str(numero1):
    print(f"a palavra e o número são iguais") 
else:
    print(f"a palavra e o número são diferentes")
print(f"{linha}\n")
# Exercício 4  
# Crie um programa que peça ao usuário para digitar duas palavras. O programa deve 
# comparar o comprimento das duas palavras e dizer qual delas tem mais caracteres ou se 
# elas têm o mesmo número de caracteres. 
print("digite duas palavras para compararação sobre o comprimento delas")
palavra1=input("Digite a primeira palavra: ") 
palavra2=input("Digite a segunda palavra: ") 
if len(palavra1) > len(palavra2):
    print(f"{palavra1} é maior que {palavra2}")
elif len(palavra1) == len(palavra2):
    print(f"as palavras {palavra1} e {palavra2} tem o mesmo tamanho")
else:
    print(f"{palavra1} é menor que {palavra2}")
# Exercício 5  
# Crie um programa que peça ao usuário para digitar duas palavras (strings) e compare-as 
# em ordem alfabética. Exiba qual palavra vem primeiro na ordem alfabética. 
print("digitar duas palavras para compararmos as suas ordens na ordenação alfabética")
palavra1=input("Digite a primeira palavra: ").lower() 
palavra2=input("Digite a segunda palavra: ").lower()
if palavra1 < palavra2:
    print(f"A palavra '{palavra1}' vem antes de '{palavra2}' na ordem alfabética.")
elif palavra2 < palavra1:
    print(f"A palavra '{palavra2}' vem antes de '{palavra1}' na ordem alfabética.")
else:
    print("As duas palavras são iguais!")
print(f"{linha}\n")
# Exercício 6  
# Crie um programa que peça ao usuário para digitar três palavras. O programa deve exibir 
# as palavras ordenadas em ordem alfabética crescente.
print("Digite três palavras para colocarmos elas em ordem alfabética")
palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()
palavra3 = input("Digite a terceira palavra: ").lower()

print("\nlistando as plavras em ordem alfabética:")

# ver se a palavra1 é a menor de todas
if palavra1 <= palavra2 and palavra1 <= palavra3:
    if palavra2 <= palavra3:
        print(palavra1, palavra2, palavra3)
    else:
        print(palavra1, palavra3, palavra2)

elif palavra2 <= palavra1 and palavra2 <= palavra3: 
    if palavra1 <= palavra3:
        print(palavra2, palavra1, palavra3)
    else:
        print(palavra2, palavra3, palavra1)

# Sobrou a palavra3 como sendo a menor
else:
    if palavra1 <= palavra2:
        print(palavra3, palavra1, palavra2)
    else:
        print(palavra3, palavra2, palavra1)
print(f"{linha}\n")
# Exercício 7  
# Crie um programa que compare duas palavras em relação à sua ordem lexicográfica e 
# informe se a primeira palavra é maior ou menor que a segunda.
print("Digite duas palavras para vermos qual vem primeiro na ordem alfabética, e é maior ou menos na ordem lexográfica") 
palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

if palavra1 < palavra2:
    print(f"A palavra {palavra1} (maior) vem depois de {palavra2} na ordem alfabética.")
elif palavra1 > palavra2:
    print(f"A palavra {palavra1} (menor) vem antes de {palavra2} na ordem alfabética.")
else:
    print("As duas palavras são iguais.")
# Exercício 8  
# Crie um programa que peça ao usuário para digitar uma palavra e um número. O programa 
# deve verificar se o número é maior que 10 e, caso seja, imprimir "O número é maior que 
# 10". Caso contrário, deve verificar se a palavra digitada é "Python" e imprimir "Você 
# digitou Python". 
print("exercício 8")
print("digite uma palavra e um número.\nPara testar, use a palavra Python, e um númeo maior ou menor que 10")
palavra1 = input("Digite uma palavra: ").lower()
numero1 = int(input("Digite um número: "))


if numero1 > 10:
    print("O número é maior que 10")
elif palavra1 == "python":
    print("Você digitou Python")
print(f"\n{linha}")
# Exercício 9  
# Crie um programa que peça ao usuário para digitar um número e uma palavra. O programa 
# deve verificar se a palavra é "Python" e, caso seja, imprimir "Você digitou Python". Caso 
# contrário, verifique se o número digitado é maior que 5 e imprima "O número é maior que 
# 5".
print("exercício 9")
print("digite uma palavra e um número.\nPara testar, use a palavra Python, e um númeo maior ou menor que 10")
palavra1 = input("Digite uma palavra: ").lower()
numero1 = int(input("Digite um número: "))

# Verifica as condições pedidas
if palavra1 == "python":
    print("Você digitou Python")
elif numero1 > 5:
    print("O número é maior que 5")
print(f"\n{linha}")
# Exercício 10  
# Crie um programa que compare duas strings de diferentes tamanhos e imprima se a 
# primeira string é maior ou menor que a segunda, levando em consideração a comparação 
# lexicográfica.
print("Exercício 10\nDigite duas palavras para fazermos uma comparação entre elas:")
palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

if palavra1 < palavra2:
    print(f"\nA palavra {palavra1} é menor que a palavra {palavra2}.")
elif palavra1 > palavra2:
    print(f"\nA palavra {palavra1} é maior que a palavra {palavra2}.")
else:
    print("\nAs duas palavras são iguais.")
print(f"\n{linha}")
# Exercício 11  
# Crie um programa que peça ao usuário para digitar uma palavra e verifique se ela é um 
# número. Se for, imprima "Você digitou um número". Caso contrário, imprima "Você digitou 
# uma palavra"
print("Digite uma palavra ou um número, para ser avaliado se é string ou number")
palavra1 = input("Digite uma palavra: ")

if palavra1.isdigit():
    print("Você digitou um número")
else:
    print("Você digitou uma palavra")
print(f"\n{linha}")
# Exercício 12  
# Crie um programa que peça ao usuário para digitar duas strings e compare-as. Se as 
# palavras forem iguais, imprima "As palavras são iguais". Caso contrário, imprima "As 
# palavras são diferentes".
print("Digite duas palavras para fazermos umeacomparação entre elas")
palavra1=input("Digite a palavra 1: ")
palavra2=input("Digite a palavra 1: ")
if palavra1==palavra2:
    print(f" as palavras {palavra1} e {palavra2} são iguais")
else:
    print(f"as palavras {palavra1} e {palavra2} são diferentes")
print(f"\n{linha}")
# Exercício 13  
# Crie um programa que peça ao usuário para digitar um número e uma palavra. O programa 
# deve verificar se o número digitado é maior que 10 e se a palavra é "Python". Se ambos 
# forem verdadeiros, imprima "Você acertou os dois!". Caso contrário, imprima "Tente 
# novamente".
print("Exercício 13\n Digite um número e uma palavra, tente adivinhar as duas opções.\nDica: já estiveram em ouros exercícios")
numero = int(input("Digite um número: "))
palavra1 = input("Digite uma palavra: ").lower()

# Verifica se ambas as condições são verdadeiras ao mesmo tempo
if numero > 10 and palavra1 == "python":
    print("Você acertou as duas!")
else:
    print("Tente novamente")
print(f"\n{linha}")
# Exercício 14  
# Crie um programa que peça ao usuário para digitar duas palavras, uma em maiúsculas e a 
# outra em minúsculas. O programa deve comparar essas palavras e exibir se elas são iguais 
# ou diferentes, levando em conta a diferença entre letras maiúsculas e minúsculas.
print("Exercício 14\n Digite duas palavras, uma em maiúscula, outra em minúscula:")
palavra1 = input("Digite a primeira palavra (em maiúsculas): ")
palavra2 = input("Digite a segunda palavra (em minúsculas): ")

if palavra1.isupper() and palavra2.isupper():
    print("As palavras estão em maiúsculas.")
else:
    print("As palavras tem valores semânticos diferentes.")

print(f"\n{linha}")
# Exercício 15  
# Crie um programa que peça ao usuário para digitar uma palavra e um número. O programa 
# deve comparar o número com a string digitada, convertendo o número para string, e 
# verificar se são iguais ou diferentes.
print("Exercício 15\nDigite uma palavra e um número para compararmos se são iguais")
palavra1 = input("Digite uma palavra: ")
numero1 = int(input("Digite um número: "))
if palavra1 == str(numero1):
    print("São iguais!")
else:
    print("São diferentes!")
print(f"\n{linha}")