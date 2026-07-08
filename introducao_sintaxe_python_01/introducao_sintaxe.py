letra = ''  
salariop = 0.0  
idadep = 0  
fez = False 
texto = ""  

letra: str = '' 
texto: str = "" 

idadep: int = 0 
numero_inteiro: int = 10 

salariop: float = 0.0 
preco_produto: float = 99.99  

fez: bool = False  
ativo: bool = True  


print("\n Olá Mundo ")
print("Vamos exibir a mensagem 'Olá Mundo'.")
print("Olá Mundo\n")
print("Agora vamos exibir 'olá' em uma linha e 'Mundo' na próxima.")
print("olá\n Mundo\n")

print("\nOperações Matemáticas")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
print(f"\nA soma dos dois números é: {numero1 + numero2}")
print(f"A subtração dos dois números é: {numero1 - numero2}")
print(f"A multiplicação dos dois números é: {numero1 * numero2}")

print("\nTabela Simples")
print("Nome\tIdade")
print("João\t30")
print("Maria\t25")
print("Pedro\t35")

print("\nTamanho da String")
minha_string = "Olá, mundo!"
numero_de_caracteres = len(minha_string)
print(f"Número de caracteres em '{minha_string}': {numero_de_caracteres}")

print("\nConversões de String")
texto_mundo = "Olá, MUNDO!"
texto_minusculo = texto_mundo.lower()
print(f"'{texto_mundo}' em minúsculo: {texto_minusculo}")
texto_mundo_lower = "olá, mundo!"
texto_maiusculo = texto_mundo_lower.upper()
print(f"'{texto_mundo_lower}' em maiúsculo: {texto_maiusculo}")

print("\nSubstituição em String")
letra_para_substituir = input("Digite a letra que gostaria de substituir: ")
texto_replace = "Olá, mundo! Como você está?"
novo_texto = texto_replace.replace(letra_para_substituir, " ")
print(f"'{texto_replace}' após substituir '{letra_para_substituir}' por '': {novo_texto}")
