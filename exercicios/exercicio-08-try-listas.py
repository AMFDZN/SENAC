
# Instrução geral
# Crie um programa em Python que funcione como um menu de opções utilizando
# match-case. O usuário deverá escolher uma opção do menu e cada opção
# executará um dos exercícios abaixo. Todos os exercícios devem estar organizados
# dentro de um único menu.
# Regras do programa
# O programa deve utilizar match-case para o menu principal. Cada opção do menu
# deve executar um exercício diferente. Deve existir uma opção para sair do
# programa. Cada exercício deve funcionar de forma independente dentro do menu.

#viva as funções python!
def Linha():
    print("╍" *30)
    
def Linhazinha():
    print("╌" *30)

#variáveis UI/UX para terminal e log 😎
seta="🠆"
linha =("╍"*30)
linhazinha=("╌"*30)
    
while True:
    
    print("""Menu de Opções try / listas
          Escolha uma opção abaixo para testar:""")
    print("1 - Calcular uma divisão entre dois números")
    print("2 - Verificar sua idade")
    print("3 - Avaliar 5 números digitados")
    print("4 - Criar uma lista de nomes")
    print("5 - Validar a entrada de números positivos")
    print("6 - Um novo menu de opções")
    
    opcao = input("Escolha sua opção: ").strip()
    match opcao:
        case "1":
            # Exercício 1
            # # Faça um programa que peça dois números ao usuário e exiba o resultado da
            # # divisão. Trate divisão por zero e entradas inválidas.
            print("\nInforme dois números para fazer um divisão entre eles")
            while True:
                try:
                    numero1=int(input("Informe o primeiro número: "))
                    numero2=int(input("Informe o segundo número: "))
                    resultado = numero1 / numero2
                except ValueError: #valida se a entrada é numérico inteiro 
                    print("Erro: digite apenas números válidos. Números sem ponto ou vírgula\n    -----------")
                    continue #volta pro início do while
                except ZeroDivisionError:  # método de validação se é divisível por zero
                    print("Erro: não é possível dividir por zero.\n    -----------")
                    continue #volta pro início do while
                else:
                    print(f"Resultado da divisão: {resultado}")
                    break #para o while e volta ao menu
            Linha()
            input("Para voltar ao menu, pressione Enter.")
            
        case "2":
# Exercício 2
# Peça a idade do usuário. Se a idade for negativa, levante um erro manualmente
# com a mensagem Idade inválida. Caso contrário, mostre a idade.
            print("\n--- Exercício 2: Verificação de Idade ---")
            while True:
                try:
                    idadeUsuario = int(input("Digite a sua idade: "))
                    
                    # Se for negativa, força erro manualmente usando raise
                    if idadeUsuario < 0:
                        raise ValueError("Idade inválida.\nAinda não existem idades negativas!")
                        
                except ValueError as erroIdade:
                    # Captura o erro (seja de texto digitado ou da idade negativa)
                    print(f"Erro: {erroIdade}")
                    continue
                else:
                    print(f"Idade registrada com sucesso: {idadeUsuario} anos.")
                    break # Para o while do exercício e retorna ao menu principal
            Linha()
            input("\nPara voltar ao menu, pressione Enter.")
        
        case "3":
            # type: ignore
            # # Exercício 3
            # # Peça ao usuário que digite 5 números. Para cada um, valide a entrada, acumule a
            # # soma, conte quantas entradas foram válidas e mostre no final a média dos
            # números digitados.
            print("\nExercício 3:\n- Validar 5 números digitados.\n- Somá-los\nContar quantas entradas não validadas\n- Resultar a média dos valores, quando houver")
            #declarando as variáveis vazias
            somaTotal = 0.0 # em float, por que precisamos calcular a média depois
            entradasValidas = 0
            contadorLoop = 1
            quantidadeDeNumeros=5 #cinco tentativas para digitar números validos
            
            # while roda até atingir a quantidadeDeNumeros
            while contadorLoop <= quantidadeDeNumeros:
                try:
                    numeroDigitado = float(input(f"Digite o {contadorLoop}º número: "))
                except ValueError:
                    print("Erro: Entrada inválida! Digite apenas números.")
                    # Como a entrada foi inválida, o contador avança mas não somamos nada
                    contadorLoop += 1 #itera mesmo que não seja válido - são só cinco tentativas
                    continue
                else:
                    somaTotal += numeroDigitado #vai somando a cada volta de números válidos
                    entradasValidas += 1 #acrece +1 entrada válida
                    contadorLoop += 1 #acresce +1 volta no while
            
            # Prints finais depois do final do while
            print("\n- Resultado Final:")
            print(f"1-Quantidade de números válidos: {entradasValidas}")
            Linhazinha()
            print(f"2-Soma total dos números válidos: {somaTotal}")
            Linhazinha()
            # Evitar divisão por zero ao calcular a média se nenhum número foi aceito
            if entradasValidas > 0:
                mediaFinal = somaTotal / entradasValidas
                print(f"3-Média dos números válidos: {mediaFinal}")
            else:
                print("Não foi possível calcular a média\n(nenhum número válido inserido).")
            Linha()   
            input("\nPara voltar ao menu, pressione Enter.")
                        
        case "4":
            # Exercício 4
            # Peça ao usuário para informar quantos nomes deseja inserir e crie a lista. Verifique se um nome digitado pelo usuário está presente na lista. Mostre a lista ordenada.
            # Inverta a ordem da lista e mostre o resultado.

            print("\nExercício 4:\nCriar uma Lista de Nomes")
            listaNomes = [] #declara a variável tipo lista
            
            while True:
                try:
                    #pede no input um número inteiro
                    quantidadeNomes = int(input("Quantos nomes deseja inserir na lista? "))
                    if quantidadeNomes <= 0:
                        print("Erro: Digite uma quantidade maior que zero.")
                        continue #vai pro except
                    break
                except ValueError:
                    print("Erro: Digite um número inteiro válido.")
            i = 0 #dclara o contador como zero, caso queira incluir um só nome na lista
            while i < quantidadeNomes:
                nomeInput = input(f"Digite o {i+1}º nome: ").strip() #{i+1} gambiarra visual, pra formar o ordinal correto ao usuário
                if nomeInput == "":
                    print("Erro: O nome não pode ser vazio.")
                    continue #volta ao while e não itera na lista
                listaNomes.append(nomeInput)
                i += 1
                
            Linha()
            print(f"Lista criada: {listaNomes}")
            
            # Busca de elemento na lista
            nomeBusca = input("\nDigite um nome para buscar na lista: ").strip()
            if nomeBusca in listaNomes:
                print(f"Resultado:\n '{nomeBusca}' ESTÁ presente na lista!")
                Linhazinha()
            else:
                print(f"Resultado:\n '{nomeBusca}' NÃO foi encontrado.")
                Linhazinha()
                
            # Exibir ordenada (sem alterar a lista original permanentemente)
            listaOrdenada = sorted(listaNomes)
            print(f"Lista em ordem alfabética:\n {listaOrdenada}")
            Linhazinha()
            
            # Inverter a ordem da lista
            listaNomes.reverse()
            print(f"Lista invertida (de trás para frente):\n {listaNomes}")
            Linha()
            input("\nPara voltar ao menu, pressione Enter.")
        
        case "5":
            # Exercício 5
            # Peça ao usuário para informar quantos números inteiros positivos deseja inserir.
            # Para cada valor: Permita apenas números inteiros e positivos. Caso contrário,
            # exiba uma mensagem de erro e peça novamente. Exiba a lista final e a quantidade
            # de números válidos inseridos.
            print("""
                  Exercício 5:
                  1-Criar uma lista de números
                  2- Validar Números Positivos
                  3- mostrar lista final e quantidade de números válidos
                  """)
            listaNumeros = [] #declara a variável como uma lista
            
            while True:
                try:
                    quantidadeNumeros = int(input("Quantos números \"inteiros e positivos\" deseja inserir? "))
                    if quantidadeNumeros <= 0: #valida positivos
                        print("Erro: A quantidade de elementos deve ser maior que zero!")
                        continue #retorna ao início e pede novamente um número inteiro
                    break
                except ValueError:
                    print("Erro: Digite um NÚMERO INTEIRO POSITIVO para definir a quantidade de números a lista terá!")
            
            # Loop para receber os números válidos
            while len(listaNumeros) < quantidadeNumeros:
                try:
                    entradaValor = int(input(f"Digite um número inteiro positivo ({len(listaNumeros)+1}/{quantidadeNumeros}): "))
                    
                    if entradaValor <= 0:
                        print("Erro: O número deve ser estritamente positivo (maior que 0).")
                        continue # Pula o append e pede novamente
                        
                    listaNumeros.append(entradaValor) #insere o número válido na lista (no final), a cada volta do while
                    
                except ValueError:
                    print("Erro: Entrada inválida. Digite apenas números inteiros sem letras ou pontos.")
            
            Linhazinha()
            print(f"Lista final criada: {listaNumeros}")
            Linhazinha()
            print(f"Quantidade de números válidos inseridos: {len(listaNumeros)}")
            Linha()
            input("\nPara voltar ao menu, pressione Enter.")
            
        case "6":

            # Exercício 6
            # Crie um programa com o seguinte menu:
            # 1 - Adicionar item à lista
            # 2 - Remover item pelo índice
            # 3 - Verificar se um item está na lista
            # 4 - Mostrar todos os itens
            # 5 - Ordenar lista
            # 6 - Sair 
            # O programa deve:
            # Começar com uma lista vazia. Permitir que o usuário insira a quantidade de itens
            # sempre que necessário. Utilizar um controle de menu. Capturar entradas
            # inválidas.
            print("aqui eu chorei\n Fui pro Gemini me ajudar")
            print("\nExercício 6: Menu Interno de Lista")
            listaItens = [] # declara a variável tipo lista
            
            while True:
                print("\nExercícios com Listas:")
                print("1 - Adicionar item à lista")
                print("2 - Remover item pelo índice")
                print("3 - Verificar se um item está na lista")
                print("4 - Mostrar todos os itens")
                print("5 - Ordenar lista")
                print("6 - Sair do \"Submenu\"")
                
                opcaoListas = input("Escolha uma opção no \"Menu de Listas\": ").strip()
                Linha()
                match opcaoListas:
                    case "1":
                        print("1- Adicionar um item a uma lista")                        
                        #pedi como string pra facilitar minha vida - mesmo que seja digitado um número, passa
                        novoItem = input("Digite o item para adicionar: ").strip()
                        if novoItem != "": #se não esiver vazio, é adicionado á lista
                            listaItens.append(novoItem)
                            print(f"'{novoItem}' adicionado com sucesso.")
                            print(f"{listaItens}\n{linhazinha}")
                        else:
                            print(f"Erro: você não digitou nada.\n{linhazinha}")
                            
                        Linha()    
                    case "2":
                        print("2- Remover um item de uma lista, usando seu índice")
                        if len(listaItens) == 0: 
                            print(f"A lista está vazia. Não há nada para remover.\n{linhazinha}")
                            continue
                        try:
                            print("Itens atuais com seus índices:")
                            for indice, valor in enumerate(listaItens):
                                print(f"Índice {indice}: {valor}")
                                
                            indiceRemover = int(input("Digite o número do índice que queira remover: "))
                            itemRemovido = listaItens.pop(indiceRemover)
                            print(f"Sucesso: O item '{itemRemovido}' foi removido.")
                        except ValueError:
                            print("Erro: Digite um número inteiro para o índice.")
                        except IndexError:
                            print("Erro: Esse índice não existe na lista atual.")
                            
                    case "3":
                        itemVerificar = input("Digite o item que deseja buscar: ").strip()
                        if itemVerificar in listaItens:
                            print(f"O item '{itemVerificar}' ESTÁ na lista na posição {listaItens.index(itemVerificar)}.")
                        else:
                            print(f"O item '{itemVerificar}' NÃO ESTÁ na lista.")
                            
                    case "4":
                        if len(listaItens) == 0:
                            print("A lista está vazia.")
                        else:
                            print(f"Itens na lista: {listaItens}")
                            
                    case "5":
                        if len(listaItens) == 0:
                            print("A lista está vazia, não há o que ordenar.")
                        else:
                            listaItens.sort()
                            print(f"Lista ordenada com sucesso: {listaItens}")
                            
                    case "6":
                        print("Saindo do submenu...")
                        break # Quebra o while deste case e volta para o menu principal
                        
                    case _:
                        print("Opção inválida no exercício de listas.")
            Linha()

        case _:
            print("fim")
            print("Clique ENTER para voltar ao menu principal")
