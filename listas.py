

print("Estrutura de Dados: Listas")
print("=" * 50)

while True:
    print("""
Menu de tópicos:
1 - Introdução a Listas
2 - Entrada de Dados e Manipulação
3 - Classificação e Menu de Opções
4 - Manipulação de Listas
5 - Tratamento de Erros com Listas
6 - Sair
""")
    escolha = input("Escolha uma opção: ").strip()

    match escolha:
        case "1":
            print("\n Introdução a Listas ")
            frutas = ["maçã", "banana", "laranja"]
            print("Lista inicial:", frutas)
            print("Primeira fruta:", frutas[0])
            print("Última fruta:", frutas[-1])
            frutas[1] = "morango"
            print("Lista após alteração:", frutas)
            frutas.append("abacaxi")
            print("Lista após append:", frutas)
            frutas.remove("laranja")
            print("Lista após remove:", frutas)
            removido = frutas.pop(0)
            print(f"Removido com pop: {removido}")
            print("Lista final:", frutas)

            print("Percorrendo com for índice:")
            for i in range(len(frutas)):
                print(f"{i} = {frutas[i]}")

            input("\nPressione Enter para voltar ao menu...")

        case "2":
            print("\n Entrada de Dados e Manipulação ")
            quantidade = int(input("Quantos nomes deseja adicionar? "))
            nomes = []
            for i in range(quantidade):
                nome = input(f"Digite o nome {i+1}: ").strip()
                nomes.append(nome)
            print("Lista criada:", nomes)
            print("Iterando com while:")
            i = 0
            while i < len(nomes):
                print(f"Nome[{i}]: {nomes[i]}")
                i += 1
            input("\nPressione Enter para voltar ao menu...")

        case "3":
            print("\n Classificação e Menu de Opções ")
            nomes = ["Ana", "Beatriz", "Carlos", "Eduardo"]
            print("Classificação por tamanho com match case:")
            for nome in nomes:
                tamanho_nome = len(nome)
                match tamanho_nome:
                    case tamanho_nome if tamanho_nome <= 3:
                        print(f"{nome}: Curto")
                    case tamanho_nome if 4 <= tamanho_nome <= 6:
                        print(f"{nome}: Médio")
                    case _:
                        print(f"{nome}: Longo")
            input("\nPressione Enter para voltar ao menu...")

        case "4":
            print("\n Manipulação  de Listas ")
       

            nomes = []
            for i in range(3):
                nome = input(f"Digite o nome {i+1}: ").strip()
                nomes.append(nome)

            print(f"\nLista original: {nomes}")

            
            print(f"Tamanho da lista: {len(nomes)}")

           
            nome_busca = input("Digite um nome para verificar se está na lista: ").strip()
            if nome_busca in nomes:
                print(f"{nome_busca} está na lista!")
            else:
                print(f"{nome_busca} não está na lista.")

           
            nomes_ordenados = sorted(nomes)
            print(f"Lista ordenada (sorted): {nomes_ordenados}")

            
            nomes.reverse()
            print(f"Lista invertida (reverse): {nomes}")

       
            nome_conta = input("Digite um nome para contar quantas vezes aparece na lista: ").strip()
            ocorrencias = nomes.count(nome_conta)
            print(f"{nome_conta} aparece {ocorrencias} vez(es) na lista.")

            if nome_conta in nomes:
                posicao = nomes.index(nome_conta)
                print(f"A primeira ocorrência de {nome_conta} está na posição {posicao}.")
            else:
                print(f"{nome_conta} não está na lista, então não há índice.")

   
            copia_lista = nomes.copy()
            print(f"Cópia da lista: {copia_lista}")

            
            
            print("\nFatiamento da lista:")
            print(f"Lista original: {nomes}")

           
            print(f"[1:] - Do índice 1 até o final: {nomes[1:]}")
            print(f"[:-1] - Do início até o penúltimo: {nomes[:-1]}")
            print(f"[1:3] - Do índice 1 até o 2 (exclui o 3): {nomes[1:3]}")
            print(f"[:] - Lista completa (cópia superficial): {nomes[:]}")

            
            print(f"[::1] - Todos os elementos, passo 1: {nomes[::1]}")
            print(f"[::2] - Todos os elementos, pulando de 2 em 2: {nomes[::2]}")
            print(f"[1::2] - A partir do índice 1, pulando de 2 em 2: {nomes[1::2]}")

            
            print(f"[::-1] - Lista invertida: {nomes[::-1]}")
            print(f"[::-2] - Lista invertida, pulando de 2 em 2: {nomes[::-2]}")
            print(f"[2::-1] - Do índice 2 até o início, invertido: {nomes[2::-1]}")

           
            print(f"[0:2] - Do índice 0 ao 1: {nomes[0:2]}")
            print(f"[1:len(nomes)] - Do índice 1 até o final: {nomes[1:len(nomes)]}")

            input("\nPressione Enter para voltar ao menu...")
        case "5":
            print("\n Tratamento de Erros com Listas ")
          
            numeros = []

            try:
                quantidade = int(input("Quantos números deseja inserir? "))

                if quantidade <= 0:
                    raise ValueError("A quantidade deve ser maior que zero.")

                for i in range(quantidade):
                    try:
                        valor = int(input(f"Digite o número {i+1}: "))
                        if valor < 0:
                            raise ValueError("Não são permitidos números negativos.")
                        numeros.append(valor)
                    except ValueError as ve:
                        print(f"Entrada inválida: {ve}")
                        continue

                print(f"\nLista final criada com sucesso: {numeros}")
                print(f"Quantidade de números válidos inseridos: {len(numeros)}")

            except ValueError as e:
                print("Erro ao definir a quantidade de números:", e)

            finally:
                print("Finalizando a operação de inserção de dados na lista.")

            input("\nPressione Enter para voltar ao menu...")
        case "6":
            print("Saindo")
            break
        case _:
            print("Opção inválida, tente novamente.")