def Linha():
    print("-.-" * 20)

# Exercício 0:
# Crie um programa que remova todas as ocorrências de um caractere específico da string 
# digitada pelo usuário. Solicite ao usuário para digitar o caractere a ser removido
print("--------------------\nExercício 0\nVAMOS REMOVER UMA LETRA DE UMA FRASE\nFRASE: \"Esta frase é a frase que vai ser eduitada pelo script\"\n")
removeChar = input("Digite um caractere para ser retirado da frase acima: ")
frase="Esta frase é a frase que vai ser eduitada pelo script"
faseTeste=frase.lower()
fraseNova = ""

for letra in faseTeste:
    if removeChar.lower() != letra:
        fraseNova += letra

print(f"Texto original: {frase}")
print(f"Texto modificado: {fraseNova.capitalize()}")
Linha()
# Exercício 1:
# Solicite ao usuário para digitar dois valores e use o operador condicional > para mostrar 
# qual é o maior valor.
print("\nVAMOS FAZER COMPARAÕES ENTRE DOIS NÚMEROS:")
Linha()
print("QUAL NÚMERO É O MAIOR?")
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
if numero1 > numero2:
    print(f"O número {numero1} é maior que o {numero2}")
else:
    print(f"O número {numero2} é mmaior que o {numero1}")
Linha()
# Exercício 2:
# Solicite ao usuário para digitar dois valores e use o operador condicional < para mostrar 
# qual é o menor valor.
print("QUAL É O MENOR?")
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
if numero1 < numero2:
    print(f"O número {numero1} é menor que o {numero2}")
else:
    print(f"O número {numero2} é mmenor que o {numero1}")
# Exercício 3:
# Solicite ao usuário para digitar dois valores e use o operador condicional >= para verificar 
# se o primeiro número é maior ou igual ao segundo. Caso afirmativo, imprima uma 
# mensagem indicando isso.
print("SÃO MAIORES OU IGUAIS?")
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
if numero1 >= numero2:
    if numero1==numero2:
        print(f"os dois números são IGUAIS {numero1}={numero2}")
    else:
        print(f"O número {numero1} é MAIOR que o {numero2}")
else:
    print(f"O número {numero1} é MENOR que o {numero2}")
# Exercício 4:
# Solicite ao usuário para digitar dois valores e use o operador condicional <= para verificar 
# se o primeiro número é menor ou igual ao segundo. Caso afirmativo, imprima uma 
# mensagem indicando isso.
print("SÃO MENORES OU IGUAIS?")
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
if numero1 <= numero2:
    if numero1==numero2:
        print(f"Os dois números são IGUAIS ({numero1} = {numero2})")
    else:
        print(f"O número {numero1} é MENOR que o {numero2}")
else:
    print(f"O número {numero1} é MAIOR que o {numero2}")
# Exercício 5:
# Solicite ao usuário para digitar dois valores e use o operador condicional == para verificar 
# se os dois números são iguais.
print("SÃO IGUAIS OU DIFERENTES")
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
if numero1==numero2:
    print(f"Os dois números são IGUAIS {numero1}={numero2}")
else:
    print(f"Os números {numero1} e {numero2} são DIFERENTES")
# Exercício 6:
# Solicite ao usuário para digitar dois valores e use o operador condicional != para verificar 
# se os dois números são diferentes
print("SÃO DIFERENTES OU IGUAIS?")
numero1=input("Digite o primeiro número: ")
numero2=input("Digite o segundo número: ")
if numero1!=numero2:
    print(f"Os números {numero1} e {numero2} são DIFERENTES")
else:
    print(f"Os dois números são IGUAIS {numero1}={numero2}")