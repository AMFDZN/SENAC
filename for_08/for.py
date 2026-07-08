
print("Exemplo for com range")
for i in range(5):
    print(f"Iteração {i}")
print("-" * 30)


print("Exemplo for com range")
voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
for i in range(voltas):
    print(f"Iteração {i}")
print("-" * 30)


print("Exemplo com range começando do 1 até 5")
for i in range(1, 6):
    print(i)
print("-" * 30)

inicio = int(input("Digite o valor de início das voltas:"))
voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
for i in range(inicio, voltas):
    print(i)
print("-" * 30)



print("Exemplo com passo de 2 no range")
for i in range(0, 10, 2):
    print(i)
print("-" * 30)

print("Exemplo com passo de 2 no range")
inicio = int(input("Digite o valor de início das voltas:"))
voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
intervalo= int(input("Digite o valor de intervalo das voltas: "))
for i in range(inicio, voltas, intervalo):
    print(i)
print("-" * 30)


print("Exemplo com range regressivo")
for i in range(5, 0, -1):
    print(i)
print("-" * 30)

inicio = int(input("Digite o valor de início das voltas:"))
voltas = int(input("Digite quantas voltas o sistema deve percorrer: "))
intervalo_regressivo= int(input("Digite o valor de intervalo das voltas: "))
for i in range(inicio, voltas, intervalo_regressivo):
    print(i)
print("-" * 30)


print("Iterando caracteres de uma string")
texto = input("Digite uma palavra para iterar seus caracteres: ")
for letra in texto:
    print(letra)
print("-" * 30)

print("Usando operadores de comparação dentro do for")
print("Digite 5 números para analisar se são maiores, menores ou iguais a 3:")
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    if num > 3:
        print(f"{num} é maior que 3")
    elif num == 3:
        print(f"{num} é igual a 3")
    else:
        print(f"{num} é menor que 3")
print("-" * 30)

print("Operadores lógicos and, or e not dentro do for")
print("Digite 3 idades para verificar se podem dirigir (idade >=18 e carteira 's'):")
for i in range(3):
    idade = int(input(f"Idade {i+1}: "))
    carteira = input("Tem carteira de motorista? (s/n): ").lower()
    if idade >= 18 and carteira == 's':
        print("Pode dirigir")
    elif idade < 18 or not carteira == 's':
        print("Não pode dirigir")
print("-" * 30)

print("Exemplo match case dentro do for")
print("Digite 4 opções (a, b, c ou outra letra) para mostrar mensagem correspondente:")
for i in range(4):
    opcao = input(f"Opção {i+1}: ").lower()
    match opcao:
        case 'a':
            print("Você escolheu a opção A")
        case 'b':
            print("Você escolheu a opção B")
        case 'c':
            print("Você escolheu a opção C")
        case _:
            print(f"Opção '{opcao}' inválida")
print("-" * 30)

print("Contando letras maiúsculas em uma palavra")
palavra = input("Digite uma palavra: ")
maiusculas = 0
for letra in palavra:
    if letra.isupper():
        maiusculas += 1
print(f"A palavra tem {maiusculas} letras maiúsculas.")
print("-" * 30)

print("Contando vogais em uma frase")
vogais = "aeiouAEIOU"
frase = input("Digite uma frase para contar as vogais: ")
cont_vogais = 0
for letra in frase:
    if letra in vogais:
        cont_vogais += 1
print(f"A frase tem {cont_vogais} vogais.")
print("-" * 30)

print("Verificando número par ou ímpar com for")
print("Digite 4 números para verificar se são pares ou ímpares:")
for i in range(4):
    num = int(input(f"Número {i+1}: "))
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")
print("-" * 30)

texto = input("Digite um texto: ")
letra_substituir = input("Digite a letra que deseja substituir: ")
letra_substituta = input("Digite a letra substituta: ")

novo_texto = ""
for caractere in texto:
    if caractere == letra_substituir:
        novo_texto += letra_substituta
    else:
        novo_texto += caractere

print(f"Texto original: {texto}")
print(f"Texto modificado: {novo_texto}")
print("-" * 30)

print("Soma, máximo e mínimo de 3 números com for e variáveis")
soma = 0.0
maximo = None
minimo = None

for i in range(1, 4):
    num = float(input(f"Digite o número {i}: "))
    soma += num
    if maximo is None or num > maximo:
        maximo = num
    if minimo is None or num < minimo:
        minimo = num

print(f"Soma dos números: {soma}")
print(f"Maior número: {maximo}")
print(f"Menor número: {minimo}")
print("-" * 30)