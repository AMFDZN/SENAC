linha="\n--------------------------------\n"
# Exercício 1  
# Peça para o usuário digitar dois números. 
# Verifique e informe se ambos os números são positivos. 

print(f"{linha}VERIFICANDO SE OS DOIS NUMERAIS SÃO POSITIVOS")
numero1=input("Digite o primeiro número: ").strip()
if numero1.lstrip("-").isdigit() and numero1 != "-":
    numero1 = int(numero1)
else:
    numero1=input(f"{numero1} não é um número\nDigite o primeiro número: ").strip()
    
numero2=input("Digite o segundo número: ").strip()
if numero2.lstrip("-").isdigit() and numero2 != "-":
    numero2 = int(numero2)
else:
    numero2=input(f"{numero2} não é um número\nDigite o primeiro número: ").strip()
"""comparação"""
if numero1>0 and numero2>0:
    print("os dois números são positivos")
else:
    if numero1<0 and numero2>0:
        print(f"O número {numero1} é negativo")
    elif numero2<0 and numero1>0:
        print(f"O número {numero2} é negativo")
    else:
        print(f"os números {numero1} e {numero2} são negativos")
# Exercício 2  
# Peça para o usuário digitar dois números. 
# Verifique e informe se pelo menos um dos números é negativo. 
print(f"{linha}VERIFICANDO SE OS UM DOS DOIS NUMERAIS É NEGATIVO")
numero1=input("Digite o primeiro número: ").strip()
if numero1.lstrip("-").isdigit() and numero1 != "-":
    numero1 = int(numero1)
else:
    numero1=input(f"{numero1} não é um número\nDigite o primeiro número: ").strip()
    
numero2=input("Digite o segundo número: ").strip()
if numero2.lstrip("-").isdigit() and numero2 != "-":
    numero2 = int(numero2)
else:
    numero2=input(f"{numero2} não é um número\nDigite o primeiro número: ").strip()
"""comparação"""
if numero1<0 and numero2<0:
    print("os dois números são negativos")
else:
    if numero1<0:
        print(f"Os dois não são negativos, por que o número {numero1} é negativo")
    elif numero2<0:
        print(f"Os dois não são negativos, por que o número {numero2} é negativo")
    else:
        print(f"os números {numero1} e{numero2} são negativos") 
# Exercício 3  
# Peça para o usuário digitar um número. 
# Informe se o número não é zero. 

# Exercício 2  
# Peça para o usuário digitar dois números. 
# Verifique e informe se pelo menos um dos números é negativo. 
print(f"{linha}VERIFICANDO SE O NÚMERO É ZERO")
numero1=input("Digite o número: ").strip()
if numero1.lstrip("-").isdigit() and numero1 != "-":
    numero1 = int(numero1)
else:
    numero1=input(f"{numero1} não é um número\nDigite um NÚMERO: ").strip()
if numero1==0:
    print("O número é ZERO")
else:
    print()
# Exercício 4  
# Peça a idade do usuário e se ele tem carteira de motorista s ou n. 
# Informe se a pessoa pode dirigir, verificando se a idade é maior ou igual a 18 e tem 
# carteira. 
print(f"{linha}VAMOS CLASSIFICAR SUA FAIXA ETÁRIA")
idade=input("Informe sua idade: ").strip()
if idade.isdigit():
    idade=int(idade)
else:
    print(f"{idade} não é um valor numério.")
    idade=input("Informe novamente a sua idade usando um número: ").strip()
idade=int(idade)
temCarteira=input("Você tem carteira de motorista: (s/n) ")
if temCarteira.lower()!="s" or temCarteira.lower()!="n":
    temCarteira=input("Responda apenas usndo as letras s= sim e n=não\nVocê tem carteira de motorista: (s/n) ")
    

if idade>0:
    if idade >17 and temCarteira.lower()=="s":
        print("Você pode dirigir")
    elif idade >17 and temCarteira.lower()=="n":
        print("Você não pode dirigir")
else:
    print("Idade inválida")
    
    
  
# Exercício 5  
# Pergunte ao usuário se ele tem dinheiro s ou n e convite s ou n. 
# Informe se ele pode entrar no evento, ou porque tem dinheiro ou tem convite. 
print(f"{linha} - exercício 5")
temDinheiro=input("Você tem dinheiro? (s/n)").lower()
temConvite=input("Você tem convite? (s/n").lower()
if temDinheiro=="s" or temConvite=="s":
    print("Você pode entrar no evento")
    if temDinheiro=="s":
        print=("Você tem dinheiro.")
    else:
        print=("Você tem convite.")
# Exercício 6  
# Pergunte ao usuário se está chovendo s ou n. 
# Informe se ele pode sair sem guarda-chuva, ou se deve levar. 
###
chove=input(f"{linha}Está chovendo agora? (s/n)").strip().lower()
if chove == "s":
    print("leve o guarda-chuva")
else:
    print("Saia tranquilo. N~eo precisa de guarda-chuva")
 
# Exercício 7  
# Peça uma letra ao usuário. 
# Verifique se é uma única letra e se é vogal ou consoante. 
 
# Exercício 8  
# Peça um texto ao usuário. 
# Informe: 
# Você não digitou nada se estiver vazio 
# Texto maior que 10 caracteres 
# Texto com 10 ou menos caracteres 
 
# Exercício 9  
# Usando o texto fixo "Python é incrível!, peça uma letra para o usuário. 
# Informe se a letra está no texto e é uma letra válida alfabeto. 
 
# Exercício 10  
# Peça um número inteiro. 
# Informe se é: 
# Positivo e par 
# Positivo e ímpar 
# Zero 
# Negativo e par 
# Negativo e ímpar 
 
 
 
 
 
# Exercício 11  
# Peça nome de usuário e senha. 
# Informe: 
# Se algum está vazio informe que não pode ser vazio 
# Se usuário for admin e senha 1234, acesso permitido 
# Caso contrário, acesso negado 
 
# Exercício 12 
# Peça a nota 0 a 10 e o número de faltas. 
# Informe: 
# Aprovado se nota ≥ 7 e faltas ≤ 3 
# Recuperação se nota ≥ 5 ou faltas ≤ 5 
# Reprovado caso contrário 
 
# Exercício 13  
# Peça para o usuário digitar dois números. 
# Informe se pelo menos um é positivo e pelo menos um é par. 
 
# Exercício 14  
# Peça uma resposta s ou n para as perguntas: Está chovendo? e Está frio? 
# Informe se não está chovendo ou não está frio.
