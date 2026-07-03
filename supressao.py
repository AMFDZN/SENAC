numero1=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
resposta=numero1 > numero2
if resposta == True:
    resposta="Sim"
else:
    resposta="Não"
print(f"O {numero1} é maior que o número {numero2}? {numero1 > numero2}\n------\ncom if else:\n")
print(f"O {numero1} é maior que o número {numero2}? {resposta}")