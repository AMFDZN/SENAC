idade = int(input("Digite sua idade: "))
tem_convite = input("Você tem convite? (s/n): ").strip().lower()

if (idade > 18 and idade <= 25) or (idade > 25 and tem_convite == 's'):
    print("Você pode entrar na festa.")
else:
    print("Você não pode entrar na festa.")
print("-" * 30)



renda = float(input("Digite sua renda mensal: R$ "))
historico_credito = input("Digite seu histórico de crédito (bom/excelente): ").strip().lower()

if (renda > 5000 and historico_credito == 'bom') or (renda <= 5000 and historico_credito == 'excelente'):
    print("Você pode solicitar o empréstimo.")
else:
    print("Você não pode solicitar o empréstimo.")
print("-" * 30)


idade = int(input("Digite sua idade: "))
tem_passaporte = input("Você tem passaporte válido? (s/n): ").strip().lower()
tem_autorizacao_pais = input("Você tem autorização dos pais? (s/n): ").strip().lower()

if (idade > 18 and tem_passaporte == 's') or (idade < 18 and tem_autorizacao_pais == 's'):
    print("Você pode viajar.")
else:
    print("Você não pode viajar.")
print("-" * 30)


renda = float(input("Digite sua renda mensal: R$ "))
idade = int(input("Digite sua idade: "))
aprovacao_analise = input("Você foi aprovado na análise de crédito? (s/n): ").strip().lower()

if (renda > 3000 and idade > 25) or (renda > 2000 and aprovacao_analise == 's'):
    print("Você foi aprovado para o crédito!")
else:
    print("Você não foi aprovado para o crédito.")
print("-" * 30)


idade = int(input("Digite sua idade: "))
eh_associado = input("Você é associado ao clube? (s/n): ").strip().lower()
acompanhado_adulto = input("Você está acompanhado de um adulto? (s/n): ").strip().lower()

if (idade > 21 and eh_associado == 's') or (idade < 21 and acompanhado_adulto == 's'):
    print("Você pode entrar no clube.")
else:
    print("Você não pode entrar no clube.")

