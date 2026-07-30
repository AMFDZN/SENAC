# Exercício 1  
# Crie um programa que peça ao usuário para digitar dois números e compare-os utilizando 
# os operadores >, <, >=, <=, ==, !=. Imprima o resultado de cada comparação de forma clara 
# e explicativa. 
#linha divisória
linha= "-" *30
#-------------------
print("-"*30)
print("digitae dois números para fazermos algumas comparações entre os dois")
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
print=("\n")
print("Digite duas palavras para fazermos algumas comparações entre elas")
palavra1=input("Digite a primeira palavra: ") 
palavra2=input("Digite a segunda palavra: ") 
maior= palavra1 > palavra2
menor= palavra1 < palavra2
igual = palavra1 == palavra2
diferente = palavra1 != palavra2
print(f"COMPARAÇÕES ENTRE PALAVRAS\n{linha}")
if maior==True:
    print(f"o número {palavra1} é maior que o número {palavra2}\n{linha}")
if menor==True:
    print(f"o número {palavra1} é menor que o número {palavra2}\n{linha}")
if igual==True:
    print(f"o número {palavra1} é igual ao número {palavra2}\n{linha}")
if diferente==True:
    print(f"o número {palavra1} é diferente do número {palavra2}\n{linha}")
# Exercício 3  
# Crie um programa que peça ao usuário para digitar um número e uma palavra (string). 
# Compare o número com a string utilizando os operadores == e !=. Converta o número para 
# uma string antes da comparação.
print=("\n")
print("Digite um número e uma palavra para fazermos algumas comparações entre os dois")
palavra1=input("Digite a primeira palavra: ") 
numero1=input("Digite um número: ") 
 
# Exercício 4  
# Crie um programa que peça ao usuário para digitar duas palavras. O programa deve 
# comparar o comprimento das duas palavras e dizer qual delas tem mais caracteres ou se 
# elas têm o mesmo número de caracteres. 
# Exercício 5  
# Crie um programa que peça ao usuário para digitar duas palavras (strings) e compare-as 
# em ordem alfabética. Exiba qual palavra vem primeiro na ordem alfabética. 
# Exercício 6  
# Crie um programa que peça ao usuário para digitar três palavras. O programa deve exibir 
# as palavras ordenadas em ordem alfabética crescente. 
# Exercício 7  
# Crie um programa que compare duas palavras em relação à sua ordem lexicográfica e 
# informe se a primeira palavra é maior ou menor que a segunda. 
# Exercício 8  
# Crie um programa que peça ao usuário para digitar uma palavra e um número. O programa 
# deve verificar se o número é maior que 10 e, caso seja, imprimir "O número é maior que 
# 10". Caso contrário, deve verificar se a palavra digitada é "Python" e imprimir "Você 
# digitou Python". 
# Exercício 9  
# Crie um programa que peça ao usuário para digitar um número e uma palavra. O programa 
# deve verificar se a palavra é "Python" e, caso seja, imprimir "Você digitou Python". Caso 
# contrário, verifique se o número digitado é maior que 5 e imprima "O número é maior que 
# 5". 
# Exercício 10  
# Crie um programa que compare duas strings de diferentes tamanhos e imprima se a 
# primeira string é maior ou menor que a segunda, levando em consideração a comparação 
# lexicográfica. 
# Exercício 11  
# Crie um programa que peça ao usuário para digitar uma palavra e verifique se ela é um 
# número. Se for, imprima "Você digitou um número". Caso contrário, imprima "Você digitou 
# uma palavra". 
# Exercício 12  
# Crie um programa que peça ao usuário para digitar duas strings e compare-as. Se as 
# palavras forem iguais, imprima "As palavras são iguais". Caso contrário, imprima "As 
# palavras são diferentes". 
# Exercício 13  
# Crie um programa que peça ao usuário para digitar um número e uma palavra. O programa 
# deve verificar se o número digitado é maior que 10 e se a palavra é "Python". Se ambos 
# forem verdadeiros, imprima "Você acertou os dois!". Caso contrário, imprima "Tente 
# novamente". 
# Exercício 14  
# Crie um programa que peça ao usuário para digitar duas palavras, uma em maiúsculas e a 
# outra em minúsculas. O programa deve comparar essas palavras e exibir se elas são iguais 
# ou diferentes, levando em conta a diferença entre letras maiúsculas e minúsculas. 
# Exercício 15  
# Crie um programa que peça ao usuário para digitar uma palavra e um número. O programa 
# deve comparar o número com a string digitada, convertendo o número para string, e 
# verificar se são iguais ou diferentes. 