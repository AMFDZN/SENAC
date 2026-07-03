# Exercício 1
# Crie um programa que imprima o seu nome completo, sua idade e sua cidade em linhas 
# separadas.
print("\n---------------------\nexercício 1 - listar os dados coletados")
nomeUsuario=input("Qual é o seu nome?") #pede nome
idadeUsuario=int(input("Quantos anos você tem? ")) #pede idade
cidadeUsuario=input("Informe o nome da cidade onde você está agora: ")
print(f"Nome: {nomeUsuario}\nIdade: {idadeUsuario}\nCidade: {cidadeUsuario}")
# Exercício 2
# Crie um programa como o programa anterior, porém mostre todas as informações em uma 
# única linha, separadas por vírgulas.
print("\n---------------------\nexercício 2 - listando os dados coletados em uma só linha")
print(f"nome: {nomeUsuario}, idade: {idadeUsuario}, cidade: {cidadeUsuario}")
# Exercício 3
# Crie um programa que imprima uma tabela simples, com duas colunas: Nome e Idade. 
# Preencha a tabela com os dados de 3 pessoas.
print("\n---------------------\nexercício 3 - Tabela simples com 2 colunas e 3 linhas")
print("Tabela simples\nNome\tIdade\nAcelio\t57\nJorge\t18\nJosé\t25\n") 
# Exercício 4
# Crie um programa que peça ao usuário para digitar seu nome e, em seguida, imprima uma 
# mensagem de boas-vindas personalizada, utilizando o nome digitado.
print("\n---------------------\nexercício 4 - coleta nome e retorna mensagem de saudação")
nomeDaPessoa=input("Qual o seu Nome: ")
print(f"\n{nomeDaPessoa}, Seja bem-vindo à linguagem Python\n")
# Exercício 5
# Crie um programa que peça ao usuário que digite dois números decimais. Calcule e exiba a 
# soma dos dois números.
print("\n---------------------\nexercício 5 - somar dois números inteiros de dois dígitos") 
numero=int(input("Informe um número de dois dígitos: "))
numero2=int(input("informe o outro número, também com 2 dígitos: "))
print(f"A soma de {numero} + {numero2} é: {numero+numero2}")
# Exercício 6
# Crie um programa que peça ao usuário que digite dois números decimais. Calcule e exiba a 
# multiplicação dos dois números.
print("\n---------------------\nexercício 6 - multiplicar os dois números") 
numero3=int(input("Informe um número (dois dígitos): "))
numero4=int(input("informe o outro número (dois dígitos): "))
print(f"{numero3} X {numero4} é: {numero3*numero4}") 
# Exercício 7
# Crie um programa que calcule a área de um retângulo. Peça ao usuário para digitar a base e a 
# altura, e imprima o resultado.
print("\n---------------------\nexercício 7") 
print("Vamos calcular a área de um retângulo\n Informe as medidas.") 
base=float(input("Quantos centímetros tem a largura? "))
altura=float(input("Quantos centímetros tem a altura? "))
print(f"A área do quadrado é de {round(base*altura,2)}cm²") # testes resultando em "dízima periódica"
#pesquisei: "como limitar as casas decimais de um número float" = round(número,casas decimais)
# Exercício 8
# Crie um programa que peça ao usuário que digite 4 notas de uma disciplina. Calcule e exiba a 
# média das notas.
print("\n---------------------\nexercício 8") 
print("Vamos calcular a média das suas notas em Lógica de Programação nos 4 meses de curso.") 
nota1=float(input("Qual sua nota em Março? "))
nota2=float(input("Qual sua nota em Abril? "))
nota3=float(input("Qual sua nota em Maio? "))
nota4=float(input("Qual sua nota em Junho? "))
print(f"A sua média é {round((nota1+nota2+nota3+nota4)/4,1)}") #arredondando e limitndo em uma casa decimal - padrão de notas escolares 
# Exercício 9
# Crie um programa que peça ao usuário que digite use uma frase e imprima o número de 
# caracteres dessa string.
print("\n---------------------\nexercício 9") 
frase=input("Escreva uma frase, para contarmos quantoscaracteres ela tem: ")
quantos_caracteres = len(frase)
print(f"A frase tem {quantos_caracteres} caracteres com os espaços\n-------------")
frase = frase.replace(" ","")
quantos_caracteres = len(frase)
print(f" Sem os espaços a frase tem {quantos_caracteres} caracteres") 

# Exercício 10
# Crie um programa que peça ao usuário para digitar uma frase contendo uma palavra 
# maiúscula, converta essa palavra para minúsculas e exiba o resultado.
print("\n---------------------\nexercício 10") 
frase=input("Escreva UMA FRASE com ALGUMAS palavras em letras MAIÚSCULAS, que será convertida em \"minúsculas\": ")
print(f"{frase.lower()}") 
# Exercício 11
# Crie um programa que peça ao usuário para digitar uma frase contendo uma palavra 
# minúscula, converta essa palavra para maiúscula e exiba o resultado
print("\n---------------------\nexercício 11") 
frase=input("ESCREVA uma frase COM algumas PALAVRAS em letras minúsculas, que será convertida em \"MAIÚSCULAS\": ")
print(f"{frase.upper()}") 
