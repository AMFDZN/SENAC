# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
# == igual a
# != diferente de 

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


print(f"Operador maior que (>). Ele verifica se o valor à esquerda é maior que o valor à direita.")
if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
else:
    print(f"{numero1} não é maior que {numero2}")
print("-" * 30)

print(f"Operador menor que (<). Ele verifica se o valor à esquerda é menor que o valor à direita.")
if numero1 < numero2:
    print(f"{numero1} é menor que {numero2}")
else:
    print(f"{numero1} não é menor que {numero2}")
print("-" * 30)

print(f"Operador maior ou igual a (>=). Ele verifica se o valor à esquerda é maior ou igual ao valor à direita.")
if numero1 >= numero2:
    print(f"{numero1} é maior ou igual a {numero2}")
else:
    print(f"{numero1} não é maior ou igual a {numero2}")
print("-" * 30)

print(f"Operador menor ou igual a (<=). Ele verifica se o valor à esquerda é menor ou igual ao valor à direita.")
if numero1 <= numero2:
    print(f"{numero1} é menor ou igual a {numero2}")
else:
    print(f"{numero1} não é menor ou igual a {numero2}")
print("-" * 30)

print(f"Operador igual a (==). Ele verifica se o valor à esquerda é igual ao valor à direita.")
if numero1 == numero2:
    print(f"{numero1} é igual a {numero2}")
else:
    print(f"{numero1} não é igual a {numero2}")
print("-" * 30)

print(f"Operador diferente de (!=). Ele verifica se o valor à esquerda é diferente do valor à direita.")
if numero1 != numero2:
    print(f"{numero1} é diferente de {numero2}")
else:
    print(f"{numero1} não é diferente de {numero2}")
print("-" * 30)


print("Substituição em String")
letra_para_substituir = input("Digite a letra que gostaria de substituir: ")
texto_replace = "Olá, mundo! Como você está?"
novo_texto = texto_replace.replace(letra_para_substituir, 'r')
print(f"'{texto_replace}' após substituir '{letra_para_substituir}' por 'r': {novo_texto}")



palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print(f"Operador maior que (>) entre strings.")
if palavra1 > palavra2:
    print(f"{palavra1} é maior que {palavra2}")
else:
    print(f"{palavra1} não é maior que {palavra2}")

print("-" * 30)

print(f"Operador menor que (<) entre strings.")
if palavra1 < palavra2:
    print(f"{palavra1} é menor que {palavra2}")
else:
    print(f"{palavra1} não é menor que {palavra2}")

print("-" * 30)

print(f"Operador igual a (==) entre strings.")
if palavra1 == palavra2:
    print(f"{palavra1} é igual a {palavra2}")
else:
    print(f"{palavra1} não é igual a {palavra2}")

print("-" * 30)

print(f"Operador diferente de (!=) entre strings.")
if palavra1 != palavra2:
    print(f"{palavra1} é diferente de {palavra2}")
else:
    print(f"{palavra1} não é diferente de {palavra2}")
print("-" * 30)



numero3 = float(input("Digite um número para comparar com uma palavra: "))

print(f"Operador igual a (==) entre string e número.")
if palavra1 == str(numero3):
    print(f"{palavra1} é igual a {numero3}")
else:
    print(f"{palavra1} não é igual a {numero3}")

print("-" * 30)


print(f"Operador 'diferente de' (!=) entre string e número.")
if palavra1 != str(numero3):
    print(f"{palavra1} é diferente de {numero3}")
else:
    print(f"{palavra1} não é diferente de {numero3}")
print("-" * 30)



palavra3 = "python"
palavra4 = "java"


print(f"{palavra3} é maior que {palavra4}? {palavra3 > palavra4}")
print(f"{palavra3} é menor que {palavra4}? {palavra3 < palavra4}")
print(f"{palavra3} é igual a {palavra4}? {palavra3 == palavra4}")
print(f"{palavra3} é diferente de {palavra4}? {palavra3 != palavra4}")

print("-" * 30)


palavra5 = "10"
numero4 = 10


print(f"\nComparando string {palavra5} com número {numero4}:")
print(f"{palavra5} é igual a {numero4}? {palavra5 == str(numero4)}")
print(f"{palavra5} é diferente de {numero4}? {palavra5 != str(numero4)}")
print("-" * 30)




entrada = input("Digite algo para verificar se é um número inteiro: ")

print("Verificando se a entrada é um número usando isdigit().")
if entrada.isdigit():
    print(f"A entrada '{entrada}' contém apenas dígitos.")
else:
    print(f"A entrada '{entrada}' NÃO contém apenas dígitos.")
print("-" * 30)



texto_com_espacos = input("Digite um texto com espaços antes e depois: ")

print("Removendo espaços usando strip().")
texto_limpo = texto_com_espacos.strip()
print(f"Antes do strip(): '{texto_com_espacos}'")
print(f"Depois do strip(): '{texto_limpo}'")
print("-" * 30)


print("\nExemplos de round() e abs()")
valor = float(input("Digite um número decimal: "))
print(f"O valor arredondado de {valor} é {round(valor)}")
print(f"O valor absoluto de {valor} é {abs(valor)}")
print("-" * 30)


entrada = input("Digite algo: ")
print(f"O valor digitado é do tipo: {type(entrada)}")
print("-" * 30)


texto = "Python é incrível!"
letra = input("Digite uma letra para verificar se está no texto: ")

if letra in texto:
    print(f"A letra '{letra}' está no texto.")
else:
    print(f"A letra '{letra}' NÃO está no texto.")
print("-" * 30)



entrada = input("Digite um número decimal: ").strip()
entrada = entrada.replace(",", ".")

if entrada.replace(".", "", 1).isdigit():
    numero = float(entrada)
    print(f"Você digitou o número: {numero}")
else:
    print("Valor inválido.")
print("-" * 30)



a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

resultado = sum((a, b, c))
print(f"A soma dos números é: {resultado}")
print("-" * 30)


maior = max(a, b, c)
menor = min(a, b, c)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print("-" * 30)


numero_decimal = float(input("Digite um número decimal: "))
print(f"Número arredondado: {round(numero_decimal)}")
print(f"Valor absoluto: {abs(numero_decimal)}")
print("-" * 30)


texto = input("Digite um texto: ")

if len(texto) > 10:
    print(f"O texto tem {len(texto)} caracteres, que é maior que 10.")
else:
    print(f"O texto tem {len(texto)} caracteres, que é 10 ou menos.")



letra = input("Digite uma letra:")

if letra.isalpha():
        if letra.lower() in "aeiou":
            print("É uma vogal")
        else:
            print("É uma consoante")



char = input("Digite um caractere: ")

if char.isalpha():
        if char.isupper(): 
            print("Letra maiúscula")
        elif char.islower():
            print("Letra minúscula")




num = int(input("Digite um número inteiro: "))


if num % 2 == 0:
            print("Positivo par")
else:
            print("Positivo ímpar")