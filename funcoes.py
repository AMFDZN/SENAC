

print("Estrutura de Dados: Dicionários")
print("=" * 50)

while True:
    print("""
Menu de tópicos:
1 - Introdução a Dicionários
2 - Entrada de Dados e Manipulação
3 - Operações com Dicionários
4 - Métodos e Iteração
5 - Tratamento de Erros com Dicionários
6 - Dicionários Aninhados
7 - Conversões entre Estruturas (Lista, Tupla e Dicionário)
8 - Diferenças entre Dicionário, Lista, Tupla e Conjunto
9 - Sair
""")
    escolha = input("Escolha uma opção: ").strip()

    match escolha:
        case "1":
            print("\n Introdução a Dicionários ")
            print("Dicionários são coleções de pares chave-valor, usados para armazenar dados de forma associativa.")
            dicionario = {"nome": "Lucas", "idade": 25, "cidade": "São Paulo"}
            print("Dicionário inicial:", dicionario)

            print("\nAcessando valores:")
            print("Nome:", dicionario["nome"])
            print("Idade:", dicionario.get("idade"))

            print("\nAdicionando e removendo elementos:")
            dicionario["profissão"] = "Desenvolvedor"
            print("Após adicionar 'profissão':", dicionario)
            del dicionario["cidade"]
            print("Após remover 'cidade':", dicionario)

            print("\nPercorrendo o dicionário:")
            for chave, valor in dicionario.items():
                print(f"{chave}: {valor}")

            input("\nPressione Enter para voltar ao menu...")

        case "2":
            print("\n Entrada de Dados e Manipulação ")
            try:
                quantidade = int(input("Quantos pares chave-valor deseja adicionar? "))
                dicionario = {}
                for i in range(quantidade):
                    chave = input(f"Digite a chave {i+1}: ").strip()
                    valor = input(f"Digite o valor para '{chave}': ").strip()
                    dicionario[chave] = valor
                print("\nDicionário criado:", dicionario)

                print("\nIterando sobre as chaves:")
                for chave in dicionario:
                    print(f"Chave: {chave}, Valor: {dicionario[chave]}")
            except ValueError:
                print("Erro: Digite apenas números válidos.")
            input("\nPressione Enter para voltar ao menu...")

        case "3":
            print("\n Operações com Dicionários ")
            d1 = {"a": 1, "b": 2, "c": 3}
            d2 = {"b": 4, "d": 5}

            print("Dicionário 1:", d1)
            print("Dicionário 2:", d2)

            print("\nAtualizando dicionário 1 com dicionário 2 (update):")
            d1.update(d2)
            print("Resultado:", d1)

            print("\nRemovendo elementos com pop e popitem:")
            valor_removido = d1.pop("b", "Chave não encontrada")
            print("Valor removido:", valor_removido)
            print("Após pop:", d1)

            chave, valor = d1.popitem()
            print(f"Último item removido -> {chave}: {valor}")
            print("Dicionário final:", d1)

            input("\nPressione Enter para voltar ao menu...")

        case "4":
            print("\n Métodos e Iteração ")
            dicionario = {"nome": "Lucas", "idade": 25, "curso": "Python"}

            print("\nChaves:", list(dicionario.keys()))
            print("Valores:", list(dicionario.values()))
            print("Itens:", list(dicionario.items()))

            print("\nVerificando existência de chaves:")
            chave = "idade"
            if chave in dicionario:
                print(f"A chave '{chave}' existe no dicionário.")
            else:
                print(f"A chave '{chave}' não existe.")

            print("\nUsando dict comprehension:")
            quadrados = {x: x**2 for x in range(1, 6)}
            print("Dicionário de quadrados:", quadrados)

            input("\nPressione Enter para voltar ao menu...")

        case "5":
            print("\n Tratamento de Erros com Dicionários ")
            try:
                dicionario = {"a": 1, "b": 2, "c": 3}
                print("Dicionário atual:", dicionario)
                chave = input("Digite a chave que deseja acessar: ").strip()
                valor = dicionario[chave]
                print(f"O valor da chave '{chave}' é {valor}")
            except KeyError:
                print("Erro: a chave informada não existe no dicionário.")
            finally:
                print("Finalizando a operação de acesso ao dicionário.")
            input("\nPressione Enter para voltar ao menu...")

        case "6":
            print("\n Dicionários Aninhados ")
            alunos = {
                "aluno1": {"nome": "Lucas", "nota": 9.0},
                "aluno2": {"nome": "Maria", "nota": 8.5},
            }
            print("Dicionário de alunos:", alunos)

            print("\nAcessando dados específicos:")
            print("Nome do aluno1:", alunos["aluno1"]["nome"])
            print("Nota do aluno2:", alunos["aluno2"]["nota"])

            print("\nIterando sobre dicionários aninhados:")
            for aluno, dados in alunos.items():
                print(f"{aluno} -> Nome: {dados['nome']}, Nota: {dados['nota']}")

            input("\nPressione Enter para voltar ao menu...")

        case "7":
            print("\n Conversões entre Estruturas (Lista, Tupla e Dicionário) ")
            lista_pares = [("a", 1), ("b", 2), ("c", 3)]
            tupla_pares = (("x", 10), ("y", 20))
            dicionario = {"nome": "Lucas", "idade": 25}

            print("\nLista de pares:", lista_pares)
            print("Tupla de pares:", tupla_pares)
            print("Dicionário original:", dicionario)

            print("\nLista → Dicionário:", dict(lista_pares))
            print("Tupla → Dicionário:", dict(tupla_pares))
            print("Dicionário → Lista de tuplas:", list(dicionario.items()))
            print("Dicionário → Tupla de tuplas:", tuple(dicionario.items()))

            print("\nConvertendo chaves e valores:")
            print("Chaves como lista:", list(dicionario.keys()))
            print("Valores como lista:", list(dicionario.values()))

            input("\nPressione Enter para voltar ao menu...")

        case "8":
            print("\n Diferenças entre Dicionário, Lista, Tupla e Conjunto ")
            print("=" * 60)

            lista = [1, 2, 3, 3]
            tupla = (1, 2, 3, 3)
            conjunto = {1, 2, 3, 3}
            dicionario = {"a": 1, "b": 2, "c": 3}

            print(f"Lista: {lista} → Mutável, permite duplicatas, mantém ordem.")
            print(f"Tupla: {tupla} → Imutável, permite duplicatas, mantém ordem.")
            print(f"Conjunto: {conjunto} → Mutável, não permite duplicatas, sem ordem definida.")
            print(f"Dicionário: {dicionario} → Mutável, usa pares chave-valor, sem duplicatas de chave.")

            print("\nDiferenças práticas:")
            print("- Lista: Ideal para coleções ordenadas e mutáveis.")
            print("- Tupla: Ideal para dados constantes (imutáveis).")
            print("- Conjunto: Ideal para eliminar duplicatas e testar pertencimento.")
            print("- Dicionário: Ideal para armazenar pares nomeados e buscas rápidas por chave.")

            print("\nExemplo comparativo de acesso:")
            print("Lista[0] =", lista[0])
            print("Tupla[0] =", tupla[0])
            print("Dicionário['a'] =", dicionario['a'])
            print("Verificar se 2 está no conjunto:", 2 in conjunto)

            input("\nPressione Enter para voltar ao menu...")

        case "9":
            confirma = input("Deseja realmente sair? (s/n): ").strip().lower()
            if confirma == "s":
                print("Encerrando o programa...")
                break
            else:
                print("Retornando ao menu...")

        case _:
            print("Opção inválida, tente novamente.")