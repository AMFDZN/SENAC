print("Menu de Opções if,elif e else")
print("1 - Verificar se número é positivo, negativo ou zero")
print("2 - Verificar se letra é vogal ou consoante")
print("3 - Verificar se número é par ou ímpar")
print("4 - verificar se uma pessoa pode dirigir")
print("5 - verificar se pode entrar na festa")
print("6 - Sair")


opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Você escolheu verificar se número é positivo, negativo ou zero")
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Número positivo.")
    elif numero < 0:
        print("Número negativo.")
    else:
        print("Número é zero.")
elif opcao == "2":
    print("Você escolheu verificar se letra é vogal ou consoante.\n")
    letra = input("Digite uma letra: ")
    if letra.isalpha() and len(letra) == 1:
        if letra.lower() in "aeiou":
            print("É uma vogal.")
        else:
            print("É uma consoante.")
    else:
        print("Não é uma letra válida.")
elif opcao == "3":
    print("Você escolheu verificar se número é par ou ímpar.\n")
    numero = int(input("Digite um número: "))
    if numero %2==0:
        print(f"O {numero} é par.")
    else:
        print(f"O {numero} é impar.")
elif opcao == "4":
    print("Você escolheu verificar se uma pessoa pode dirigir.\n")
    idade = int(input("Digite sua idade: "))
    carteira = input("Você tem carteira de motorista? (s/n): ").lower()

    if idade >= 18 and carteira == "s":
        print("Você pode dirigir.")
    else:
        print("Você NÃO pode dirigir.")

elif opcao == "5":
    print("Você escolheu verificar se pode entrar na festa.\n")

    idade = int(input("Digite sua idade: "))
    tem_convite = input("Você tem convite? (s/n): ").lower()
    esta_na_lista_vip = input("Você está na lista VIP? (s/n): ").lower()
    roupa = input("Você está usando roupa formal? (s/n): ").lower()

    if (idade >= 18 and (tem_convite == "s" or esta_na_lista_vip == "s")) and not roupa == "n":
        print("Entrada permitida. Bem-vindo(a) à festa!")
    else:
        print("Entrada negada.")
elif opcao =="6":
    print("Saindo do programa. Até mais!")
else:
    print("Opção inválida.")
print("-" * 30)



print("Menu de Opções match case")
print("1 - Verificar se número é positivo, negativo ou zero")
print("2 - Verificar se letra é vogal ou consoante")
print("3 - Verificar se número é par ou ímpar")
print("4 - verificar se uma pessoa pode dirigir")
print("5 - verificar se pode entrar na festa")
print("6 - Sair")

opcao_match_case = input("Escolha uma opção: ").strip()

match opcao_match_case:
    case "1":
        print("Você escolheu verificar se número é positivo, negativo ou zero")
        numero = int(input("Digite um número: "))
        if numero > 0:
            print("Número positivo.")
        elif numero < 0:
            print("Número negativo.")
        else:
            print("Número é zero.")
    case "2":
        print("Você escolheu verificar se letra é vogal ou consoante.\n")
        letra = input("Digite uma letra: ")
        if letra.isalpha() and len(letra) == 1:
            if letra.lower() in "aeiou":
                    print("É uma vogal.")
            else:
                    print("É uma consoante.")
        else:
            print("Não é uma letra válida.")
    case "3":
        print("Você escolheu verificar se número é par ou ímpar.\n")
        numero = int(input("Digite um número: "))
        if numero %2==0:
            print(f"O {numero} é par.")
        else:
            print(f"O {numero} é impar.")
    case "4":
        print("Você escolheu verificar se uma pessoa pode dirigir.\n")
        idade = int(input("Digite sua idade: "))
        carteira = input("Você tem carteira de motorista? (s/n): ").lower()

        if idade >= 18 and carteira == "s":
            print("Você pode dirigir.")
        else:
            print("Você NÃO pode dirigir.")
    case "5":
        print("Você escolheu verificar se pode entrar na festa.\n")
        idade = int(input("Digite sua idade: "))
        tem_convite = input("Você tem convite? (s/n): ").lower()
        esta_na_lista_vip = input("Você está na lista VIP? (s/n): ").lower()
        roupa = input("Você está usando roupa formal? (s/n): ").lower()

        if (idade >= 18 and (tem_convite == "s" or esta_na_lista_vip == "s")) and not roupa == "n":
            print("Entrada permitida. Bem-vindo(a) à festa!")
        else:
            print("Entrada negada.")
    case "6":
        print("Saindo do programa. Até mais!")
    
    case _:
        print("Opção inválida")
print("-" * 30)







