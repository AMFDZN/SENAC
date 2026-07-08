num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


if num1 > 0 and num2 > 0:
    print(f"Ambos os números {num1} e {num2} são positivos.")
else:
    print(f"Pelo menos um dos números {num1} ou {num2} não é positivo.")
print("-" * 30)




num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


if num1 < 0 or num2 < 0:
    print(f"Pelo menos um dos números {num1} ou {num2} é negativo.")
else:
    print(f"Nem {num1} nem {num2} são negativos.")
print("-" * 30)




num = float(input("Digite um número: "))


if not num == 0:
    print(f"O número {num} NÃO é zero.")
else:
    print("O número digitado é zero.")
print("-" * 30)




idade = int(input("Digite sua idade: "))
tem_carteira = input("Você tem carteira de motorista? (s/n): ").lower()

if idade >= 18 and tem_carteira == 's':
    print("Você pode dirigir.")
else:
    print("Você NÃO pode dirigir.")
print("-" * 30)



tem_dinheiro = input("Você tem dinheiro? (s/n): ").lower()
tem_convite = input("Você tem convite? (s/n): ").lower()

if tem_dinheiro == 's' or tem_convite == 's':
    print("Você pode entrar no evento.")
else:
    print("Você NÃO pode entrar.")
print("-" * 30)



resposta = input("Está chovendo? (s/n): ").lower()

if not resposta == 's':
    print("Pode sair sem guarda-chuva.")
else:
    print("Leve o guarda-chuva!")
print("-" * 30)




entrada = input("Digite um número inteiro: ").strip()

if not entrada.isdigit():
    print("Entrada inválida. Não é um número inteiro.")
else:
    numero = int(entrada)
    print(f"Você digitou o número {numero}.")
print("-" * 30)



letra = input("Digite uma letra: ")

if letra.isalpha() and len(letra) == 1:
    if letra.lower() in "aeiou":
        print("É uma vogal.")
    else:
        print("É uma consoante.")
else:
    print("Não é uma letra válida.")
print("-" * 30)



char = input("Digite um caractere: ")

if char.isalpha():
    if char.isupper():
        print("Letra maiúscula.")
    elif char.islower():
        print("Letra minúscula.")
else:
    print("Não é uma letra.")
print("-" * 30)



texto = input("Digite um texto: ")

if len(texto.strip()) == 0:
    print("Você não digitou nada.")
elif len(texto) > 10:
    print(f"O texto tem {len(texto)} caracteres, que é maior que 10.")
else:
    print(f"O texto tem {len(texto)} caracteres, que é 10 ou menos.")
print("-" * 30)



texto_fixo = "Python é incrível!"
letra = input("Digite uma letra para verificar se está no texto: ")

if letra in texto_fixo and letra.isalpha():
    print(f"A letra '{letra}' está no texto.")
else:
    print(f"A letra '{letra}' NÃO está no texto.")
print("-" * 30)



entrada = input("Digite um número inteiro: ")

if entrada.isdigit():
    num = int(entrada)
    if num > 0 and num % 2 == 0:
        print("Número positivo e par.")
    elif num > 0 and num % 2 != 0:
        print("Número positivo e ímpar.")
    elif num == 0:
        print("Número é zero.")
    else:
        print("Número negativo.")
else:
    print("Valor inválido.")
print("-" * 30)



usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if not usuario or not senha:
    print("Usuário e senha não podem estar vazios.")
elif usuario == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")
print("-" * 30)



nota = float(input("Digite a nota do aluno (0 a 10): "))
faltas = int(input("Digite o número de faltas: "))

if nota >= 7 and faltas <= 3:
    print("Aprovado com bom desempenho.")
elif nota >= 5 or faltas <= 5:
    print("Recuperação.")
else:
    print("Reprovado.")
print("-" * 30)



