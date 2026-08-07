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
        print(f"Onúmero {numero1} é negativo")
    elif numero2<0:
        print(f"O número {numero2} é negativo")
    else:
        print(f"os números {numero1} e {numero2} são positivos") 
# Exercício 3  
# Peça para o usuário digitar um número. 
# Informe se o número não é zero. 

print(f"{linha}VERIFICANDO SE O NÚMERO É ZERO")
numero1=input("Digite o número: ").strip()
if numero1.lstrip("-").isdigit() and numero1 != "-":
    numero1 = int(numero1)
else:
    numero1=input(f"{numero1} não é um número\nDigite um NÚMERO: ").strip()
        
if numero1==0:
    print("O número é ZERO")
else:
    print("O número não é ZERO")

# Exercício 4  
# Peça a idade do usuário e se ele tem carteira de motorista s ou n. 
# Informe se a pessoa pode dirigir, verificando se a idade é maior ou igual a 18 e tem 
# carteira. 
print(f"{linha}VAMOS CONFERIR SEU DIREITO DE DIRIGIR")
idade=input("Informe sua idade: ").strip()
if idade.isdigit():
    idade=int(idade)
else:
    print(f"{idade} não é um valor numério.")
    idade=input("Informe novamente a sua idade usando um número: ").strip()
idade=int(idade)
temCarteira=input("Você tem carteira de motorista: (s/n) ").lower()

#if temCarteira!="s" or temCarteira!="n":
#    temCarteira=input("Responda apenas usndo as letras s= sim e n=não\nVocê tem carteira de motorista: (s/n) ")
    

if idade>0:
    if idade >17 and temCarteira.lower()=="s":
        print("Você pode dirigir")
    elif idade >17 or temCarteira.lower()=="n":
        print("Você não pode dirigir")
else:
    print("Você não pode dirigir")
    
    
  
# Exercício 5  
# Pergunte ao usuário se ele tem dinheiro s ou n e convite s ou n. 
# Informe se ele pode entrar no evento, ou porque tem dinheiro ou tem convite. 
print(f"{linha} - exercício 5")
temDinheiro=input("Você tem dinheiro? (s/n) ").lower()
temConvite=input("Você tem convite? (s/n) ").lower()

if temDinheiro=="s" or temConvite=="s":
    print("Você pode entrar no evento")
    if temDinheiro=="s":
        print=("Você tem dinheiro.")
    else:
        print=("Você tem convite.")
else:
    print("Você não pode entrar no evento")
# Exercício 6  
# Pergunte ao usuário se está chovendo s ou n. 
# Informe se ele pode sair sem guarda-chuva, ou se deve levar. 
###
print(f"{linha}VERIRICANDO A OPÇÃO DE LEVAR GUARDA-CHUVA OU NÃO")
chove=input("Está chovendo agora? (s/n) ").strip()
if chove.lower() == "s":
    print("leve o guarda-chuva")
else:
    print("Saia tranquilo. não precisa de guarda-chuva")
 
# Exercício 7  
# Peça uma letra ao usuário. 
# Verifique se é uma única letra e se é vogal ou consoante. 
print(f"{linha}VAMOS COMPARAR UMA LETRA PARA SABER SE ELA É VOGAL OU CONSOANTE")
letra1=input("Digite a letra para a comparação: ").lower()
letra1=letra1.strip()
vogais="aeiou"
if letra1.isalpha() and len(letra1) == 1: #verifica se não é um input numérico e se é somente uma letra
    if letra1 in vogais:
        print(f" a letra ({letra1}) é uma vogal.")
    else:
        print(f"a letra ({letra1}) é uma consoante.")
else:
    print(f"você informou {letra1}. Isto não é uma letra válida.")
 
# Exercício 8  
# Peça um texto ao usuário. 
# Informe: 
# Você não digitou nada se estiver vazio 
# Texto maior que 10 caracteres 
# Texto com 10 ou menos caracteres 
print(f"{linha}VAMOS VERIFICAR SUA ENTRADA, SE É VÁLIDA") 
texto1=input("Escreva uma frase para contarmos quantas letras ela tem: ")
if not texto1 or texto1==" " or len(texto1)<1:
    texto1=input("Você não digitou nada!\nTente outra vez, ou use ENTER para desistir.\nEscreva UMA FRASE para contarmos quantas letras ela tem: ")
else:
    textoSplit=texto1.split()
    if len(textoSplit)<=9:
        print=(f"A frase {texto1} tem menos de 10 caracteres")
    else:
        print=(f"A frase {texto1} tem 10 ou mais caracteres.")

# Exercício 9  
# Usando o texto fixo "Python é incrível!, peça uma letra para o usuário. 
# Informe se a letra está no texto e é uma letra válida alfabeto.
frase = "Python é incrível!"
letra1=input(f"{linha}VAMOS VER SE A LETRA ESCOLHIDA POR VOCÊ EXISTE NA FRASE ABAIXO\n - \"{frase}\"\n\nEscolha a letra: ").strip()
if letra1.isalpha() and letra1 in frase:
    print(f" a letra {letra1} é uma letra válida, e ela está na frase.")
# Exercício 10  
# Peça um número inteiro. 
# Informe se é: 
# Positivo e par 
# Positivo e ímpar 
# Zero 
# Negativo e par 
# Negativo e ímpar
numero1=input(f"{linha}DIGITE UM NÚMERO PARA CLASSIFICARMOS ELE NO CONTEXTO NUMÉRICO: ").strip() 
if numero1.isdigit():
    num = int(numero1)
    if num > 0 and num % 2 == 0:
        print(F"o Número {numero1} é um número par, e é positivo")
    elif num > 0 and num % 2 != 0:
        print(F"o Número {numero1} é um número ímpar, e é positivo.")
    elif num < 0 and num % 2 == 0:
            print(F"o Número {numero1} é um número par, e é negativo")
    elif num < 0 and num % 2 != 0:
            print(F"o Número {numero1} é um número ímpar, e é negativo.")
    elif num == 0:
        print(F"O número unformado é zero.")
else:
    print("Você não informou um número.")
 
 
 
 
# Exercício 11  
# Peça nome de usuário e senha. 
# Informe: 
# Se algum está vazio informe que não pode ser vazio 
# Se usuário for admin e senha 1234, acesso permitido 
# Caso contrário, acesso negado
print("VERIFICAÇÃO DE LOGIN?")
nomeUsuario = input("Informe o seu nome de usuário: ")
senhaUsuario = input("Informe sua senha: ")

if not nomeUsuario or not senhaUsuario:
    print("ERRO: O nome de usuário ou a senha não poder ser vazios.")
elif nomeUsuario == "admin" and senhaUsuario == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.") 
# Exercício 12 
# Peça a nota 0 a 10 e o número de faltas. 
# Informe: 
# Aprovado se nota ≥ 7 e faltas ≤ 3 
# Recuperação se nota ≥ 5 ou faltas ≤ 5 
# Reprovado caso contrário 
nota=input(f"{linha}VAMOS VER SE VOCÊ FOI APROVADO.\n - Informe sua nota final:  ")
faltas=input("- Informe o número de faltas que você tem:  ")
aprovado=nota>=7 and faltas <=3
recuperacao=nota >= 5 or faltas <= 5
if aprovado:
    print("aprovado")
elif recuperacao:
    print("recuperação")
else:
    print("reprovado")

# Exercício 13  
# Peça para o usuário digitar dois números. 
# Informe se pelo menos um é positivo e pelo menos um é par. 
numero1=input(f"{linha}DIGITE DOIS NÚMEROS PARA AVALIARMOS\n Informre o primeiro número: ").strip() 
if numero1.isdigit():
    num = int(numero1)
numero2=input("Informe o segundo número: ")
if numero2.isdigit():
    num = int(numero2)


# Exercício 14  
# Peça uma resposta s ou n para as perguntas: Está chovendo? e Está frio? 
# Informe se não está chovendo ou não está frio.
print(f"{linha}RESPONDA ÀS PERGUNTAS ABAIXO USANDO (s) PARA SIM, E (n) PARA NÃO")
chovendo=input("Está chovendo? ").lower()
frio=input("Está frio? ").lower()
if not print or not chovendo or not print.isalpha() or not chovendo.isalpha():
    print("Você não informou um dos dados da forma solicitada")
else:
    if chovendo=="s":
        print("Está chovendo")
    else:
        print("Não está chovendo")

    if frio =="s":
        print("EStá frio")
    else:
        print("Está frio.")
