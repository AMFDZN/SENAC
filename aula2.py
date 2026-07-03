# Exercício 0:
# Crie um programa que remova todas as ocorrências de um caractere específico da string 
# digitada pelo usuário. Solicite ao usuário para digitar o caractere a ser removido
print("--------------------\nExercício 1\n FRASE: Esta frase é a frase que vai ser eduitada pelo script")
removeCaracter = input("Digite um caractere para ser retirado da sentença acima: ")
frase="Esta frase é a frase que vai ser editada pelo script"
nova_frase = frase.replace(removeCaracter, '')
print(f"A frase original: ''{frase}''\nApós retirar a letra '{removeCaracter}' ficou assim:\n{nova_frase}")
#print(f"")
# Exercício 1:
# Solicite ao usuário para digitar dois valores e use o operador condicional > para mostrar 
# qual é o maior valor.
numero1=int(input("Digite um número: "))
numero2=int(input("Digite outro número: "))

if numero1 > numero2:
    print(f"o número {numero1} é maior que o número {numero2}")
else:
    print(f"o número {numero2} é maior que o número {numero1}")
 
# Exercício 2:
# Solicite ao usuário para digitar dois valores e use o operador condicional < para mostrar 
# qual é o menor valor.
print("--------------------\nExercício 2:\nVamos verificar qual número é maior que o outro")
numeroMenor1=int(input("Digite o primeiro número: "))
numeroMenor2=int(input("Digite o segundo número: "))

if numeroMenor1 > numeroMenor2:
    print(f"Entre os números {numeroMenor1} e {numeroMenor2}, o maior é o número {numeroMenor1}")
else:
    print(f"Entre os números {numeroMenor1} e {numeroMenor2}, o maior é o número {numeroMenor2}")

# Exercício 3:
# Solicite ao usuário para digitar dois valores e use o operador condicional >= para verificar 
# se o primeiro número é maior ou igual ao segundo. Caso afirmativo, imprima uma 
# mensagem indicando isso.
print("--------------------\nExercício 3:\nVamos verificar se o primeiro número é maior ou igual ao segundo")
numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))

if numero1 >= numero2:
    print(f"Entre os números {numero1} e {numero2}, o {numero1} é maior ou iugual ao {numero2}")
else:
    print(f"Entre os números {numero1} e {numero2}, o número {numero1} não é maior ou igual ao {numero2}")
# Exercício 4:
# Solicite ao usuário para digitar dois valores e use o operador condicional <= para verificar 
# se o primeiro número é menor ou igual ao segundo. Caso afirmativo, imprima uma 
# mensagem indicando isso.
print("--------------------\nExercício 4:\nVamos verificar se o primeiro número é menor ou igual ao segundo")
numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))

if numero1 <= numero2:
    print(f"Entre os números {numero1} e {numero2}, o {numero1} é mmenor ou iugual ao {numero2}")
else:
    print(f"Entre os números {numero1} e {numero2}, o número {numero1} não é maior ou igual ao {numero2}")
# Exercício 5:
# Solicite ao usuário para digitar dois valores e use o operador condicional == para verificar 
# se os dois números são iguais.
print("--------------------\nExercício 5:\nVamos verificar se o primeiro número é igual ao segundo")
numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))

if numero1 == numero2:
    print(f"Os números {numero1} e {numero2} são iuguais")
else:
    print(f"Os números {numero1} e {numero2} são diferentes")
# Exercício 6:
# Solicite ao usuário para digitar dois valores e use o operador condicional != para verificar 
# se os dois números são diferentes
print("--------------------\nExercício 6:\nVamos verificar se o primeiro número é diferente do segundo")
numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))

if numero1 != numero2:
    print(f"Os números {numero1} e {numero2} são diferentes")
else:
    print(f"Os números {numero1} e {numero2} são iguais")