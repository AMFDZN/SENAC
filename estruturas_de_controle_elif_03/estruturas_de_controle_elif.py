
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
elif numero1 == numero2:
    print(f"{numero1} é igual a {numero2}")
else:
    print(f"{numero1} é menor que {numero2}")
print("-" * 30)



palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if palavra1 > palavra2:
    print(f"{palavra1} é maior que {palavra2}")
elif palavra1 == palavra2:
    print(f"{palavra1} é igual a {palavra2}")
else:
    print(f"{palavra1} é menor que {palavra2}")
print("-" * 30)




numero3 = float(input("Digite um número para comparar com uma palavra: "))

if palavra1 == str(numero3):
    print(f"{palavra1} é igual a {numero3}")
else:
    print(f"{palavra1} é diferente de {numero3}")
print("-" * 30)




palavra3 = "python"
palavra4 = "java"

if palavra3 > palavra4:
    print(f"{palavra3} é maior que {palavra4}")
elif palavra3 == palavra4:
    print(f"{palavra3} é igual a {palavra4}")
else:
    print(f"{palavra3} é menor que {palavra4}")
print("-" * 30)




entrada = input("Digite algo para verificar se é um número inteiro: ")

if entrada.isdigit():
    print(f"A entrada '{entrada}' contém apenas dígitos.")
else:
    print(f"A entrada '{entrada}' NÃO contém apenas dígitos.")
print("-" * 30)




texto_com_espacos = input("Digite um texto com espaços antes e depois: ")
texto_limpo = texto_com_espacos.strip()

if texto_limpo == "":
    print("Você digitou apenas espaços.")
else:
    print(f"Antes do strip(): '{texto_com_espacos}'")
    print(f"Depois do strip(): '{texto_limpo}'")
print("-" * 30)




texto_replace = "Olá, mundo! Como você está?"
letra_para_substituir = input("Digite a letra que deseja substituir no texto: ")

if letra_para_substituir in texto_replace:
    novo_texto = texto_replace.replace(letra_para_substituir, 'r')
    print(f"'{texto_replace}' após substituir '{letra_para_substituir}' por 'r': {novo_texto}")
else:
    print("Letra não encontrada no texto.")
print("-" * 30)




entrada_tipo = input("Digite algo: ")

if type(entrada_tipo) == str:
    print("A entrada é uma string.")
elif type(entrada_tipo) == int:
    print("A entrada é um inteiro.")
elif type(entrada_tipo) == float:
    print("A entrada é um número decimal.")
else:
    print(f"A entrada é do tipo {type(entrada_tipo)}")
print("-" * 30)




texto = "Python é incrível!"
letra = input("Digite uma letra para verificar se está no texto: ")

if letra in texto:
    print(f"A letra '{letra}' está no texto.")
else:
    print(f"A letra '{letra}' NÃO está no texto.")
print("-" * 30)



entrada_num = input("Digite um número decimal (use vírgula ou ponto): ").strip()
entrada_num = entrada_num.replace(",", ".") #substitui , pr

if entrada_num.replace(".", "", 1).isdigit():
    numero_convertido = float(entrada_num)
    if numero_convertido >= 0:
        print(f"Número positivo: {numero_convertido}")
    elif numero_convertido < 0:
        print(f"Número negativo: {numero_convertido}")
    else:
        print("Número é zero.")
else:
    print("Valor inválido.")
print("-" * 30)




valor = float(input("Digite um número decimal (positivo ou negativo): "))

if valor > 0:
    print(f"Valor arredondado: {round(valor)}")
elif valor < 0:
    print(f"Valor absoluto: {abs(valor)}")
else:
    print("Você digitou zero.")
print("-" * 30)




valor1 = float(input("Digite o 1º número: "))
valor2 = float(input("Digite o 2º número: "))
valor3 = float(input("Digite o 3º número: "))

soma = sum((valor1, valor2, valor3))
maior = max(valor1, valor2, valor3)
menor = min(valor1, valor2, valor3)

if soma > 100:
    print(f"A soma dos números é {soma}, que é maior que 100.")
elif soma == 100:
    print("A soma dos números é exatamente 100.")
else:
    print(f"A soma dos números é {soma}, que é menor que 100.")

if maior == menor:
    print("Todos os números digitados são iguais.")
else:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
print("-" * 30)