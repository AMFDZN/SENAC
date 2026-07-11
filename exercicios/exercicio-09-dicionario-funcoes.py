# Instrução geral
# Crie um programa em Python que funcione como um menu de opções utilizando
# match-case. O usuário deverá escolher uma opção do menu e cada opção
# executará um dos exercícios abaixo. Todos os exercícios devem estar organizados
# dentro de um único menu.
# Regras do programa
# O programa deve utilizar match-case para construir o menu principal. Cada opção
# do menu deve executar um exercício diferente. Deve existir uma opção específica
# para sair do programa. Cada exercício deve funcionar de forma independente
# dentro do menu. Todos os exercícios devem utilizar tratamento de erros com try e
# except para validar entradas e evitar interrupções inesperadas durante a
# execução.
# 
# !!!!
# O programa deve utilizar a biblioteca logging para registrar eventos
# importantes, como início e encerramento do programa, erros encontrados,
# entradas inválidas e operações realizadas com sucesso.
# Os registros do logging devem ser armazenados em um arquivo de log.
# O tratamento de exceções e o registro de eventos devem estar presentes em todos os exercícios do programa.

import logging

logging.basicConfig(                    
    filename="exercico.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"                  
)

logging.info("Programa iniciado.")

#viva as funções python!
def Linha():
    print("╍" *30)
    
def Linhazinha():
    print("╌" *30)

#variáveis UI/UX para terminal 😎
seta="🠆"
linha =("╍"*30)
linhazinha=("╌"*30)
    
#funções para as ações do exercício
def mostraDicionario(qual):
    return list(qual.items())
            
def mostraValor(qual):
    return list(qual.values())
            
def mostraChave(qual):
    return list(qual.keys())
    
def mostraSomaChaves(somaTitulo=None, qual1=None, qual2=None):
    totalQual1 = sum(qual1.values()) if qual1 else 0
    totalQual2 = sum(qual2.values()) if qual2 else 0
    print(f"{somaTitulo}: {totalQual1 + totalQual2}")
    return totalQual1 + totalQual2
            
# def mostraSomaChaves(soma="Soma das Chaves",*qual1, **qual2):
#     # recebe estes dados em *qual1: lista1=list(qual1.values())
#     # recebe estes dados em **qual2: lista2=list(qual2.values())
#     soma=soma
#     return (sum(qual1)+sum(qual2))
        

while True:

    print(""" 
Escolha uma opção para testar:
1 - Inserindo chave-valore
2 - Dicionário Aninhado
3 - Trabalhando com mais de um dicionŕio
4 - Criar uma função de multiplicação com dois parâmetros
5 - Criar função que aceita parâmetros indefinidos
6 - Criar uma lista, usar map(), filter() e reduce()
7 - Eencerrar o programa e finalizar o log
""")

    opcao = input("Digite sua opção: ")

    match opcao:
        case "1":
            
# Exercício 1
# Peça ao usuário que informe quantos pares chave-valor deseja adicionar em um
# dicionário. Solicite as chaves e os valores um por um e armazene-os. Depois,
# mostre o dicionário criado. Em seguida, exiba apenas as chaves, apenas os
# valores e todos os pares.

            print("\nExercício 1:\nCriar um dicionário com base em informações do usuário")
            logging.info("\n\rExercício 1:\n")
            try:
                    quantidadePares = int(input("Quantos pares chave-valor você deseja adicionar? "))
                    if quantidadePares <= 0:
                        print("⚠ Erro: A quantidade deve ser maior que zero.")
                        Linhazinha()
                        logging.warning("⚠ Usuário tentou inserir uma quantidade menor ou igual a zero.")
                        continue
                        break # Sai do loop da quantidade se não for um número válido
            except ValueError:
                    print("⚠ Erro: Digite um número inteiro válido para a quantidade.")
                    Linhazinha()
                    logging.warning("⚠ Usuário digitou um valor não inteiro para a quantidade de chaves.")

            # declara a variável como dicionário
            dicionarioUsuario = {}

            # usa range para controlar os loopings, partindo da variável infoermanda no iinput 
            for i in range(quantidadePares):
                while True:
                    chave = input(f"Digite o nome da chave {i+1}: ").strip()
                    if chave == "":
                        print("⚠ Erro: O nome da chave não pode ser vazio.")
                        logging.warning("⚠ Erro: Usuário digitou chave com valor vazio.")
                        continue
                    break
                
                valor = input(f"Digite o valor para a chave '{chave}': ").strip()
                #cria a chave com o valor informado
                dicionarioUsuario[chave] = valor

            
            print("\nDicionário:")
            print(f"1. Dicionário Completo:\n {dicionarioUsuario}")
            logging.info(f"1. Dicionário printado ao usuário:\n {dicionarioUsuario}\n{linhazinha}")
            Linhazinha()
            
            # usando .keys() para printar só as chaves list() para formato tupla
            print(f"2. Chaves do dicionário:\n {list(dicionarioUsuario.keys())}")
            logging.info(f"2. Printadas as Chaves:\n {list(dicionarioUsuario.keys())}\n{linhazinha}")
            Linhazinha()
            
            # usando .values() para printar só os valores list() para formato tupla
            print(f"3. Valores do dicionário:\n {list(dicionarioUsuario.values())}")
            logging.info(f"3. Printados os valores:\n {list(dicionarioUsuario.values())}\n{linhazinha}")
            Linhazinha()
            
            # usando .items() para printar as chaves/valores, list() formato  tupla
            print(f"4. Pares (Chave , Valor):\n {list(dicionarioUsuario.items())}")
            logging.info(f"4. Printandos os pares (chave,valor):\n {list(dicionarioUsuario.items())}\n{linhazinha}")
            Linhazinha()

            # Registra o final deste case no log
            Linha()
            logging.info(f"{linha}\nEx. 1 finalizado\n")
            input("\nPara voltar ao menu, pressione ENTER.")
            
        case "2":
            # Exercício 2
            # Crie um dicionário aninhado representando alunos e suas notas.
            # Mostre o nome e a nota de cada aluno separadamente, além da média das notas.
            logging.info("\nExercício 2\n")
            print("\nExercício 3: Dicionário: Alunos e suas notas\n")
            
            alunos = {
                "aluno1": {"nome": "Eu", "nota": [7.4,8,5.2]},
                "aluno2": {"nome": "Tu", "nota": [8.0, 5.3, 6.7]},
                "aluno3": {"nome": "Ele", "nota": [6.4,8,5.2]},
                "aluno4": {"nome": "Ela", "nota": [7.4,6.7,6.2]},
            }
            #print("Dicionário de alunos:", alunos)
            
            notasDaTurma=0
            quantasNotasDaTurma=0
            
            mediaAlunos=0
            quantosAlunos=0
            print("\nLista de alunos e suas notas:")
            logging.info("\nLista de alunos e suas notas:")
            for aluno, dados in alunos.items():
                nome = dados["nome"]
                notasAluno = dados["nota"] #é uma lista
                #média do aluno atual
                mediaNotasAluno = round(sum(notasAluno) / len(notasAluno),1)
                
                notasDaTurma += sum(notasAluno)
                quantasNotasDaTurma +=len(notasAluno)
            
                
                ## descobri a classe capitalize(), que "enfeita" a string com capitalização
                print(f"{seta}{aluno.capitalize()}\n\rNome: {dados['nome']}\n Notas: {dados['nota']}\n Média: {mediaNotasAluno}\n{Linhazinha()}\n")
                logging.info(f"{seta}aluno{aluno.capitalize()}\nNome: {dados['nome']}\n Notas: {dados['nota']}\n Média: {mediaNotasAluno}\n{linhazinha}\n")
            Linha()
            mediaGeralAlunos=round(notasDaTurma/quantasNotasDaTurma,2)
            
            print(f"Média geral dos alunos da turma: ({mediaGeralAlunos})\n")
            logging.info(f"Média geral dos alunos da turma: ({mediaGeralAlunos})\n{linha}")
            
            Linha()
            
            logging.info(f"Ex. 2 finalizado\n{linha}")
            input("\nPara voltar ao menu, pressione Enter.")
            Linha()
            
        
        case "3":
            # Exercício 3
            # Crie dois dicionários representando estoques de duas lojas. Mostre os produtos
            # que as duas lojas vendem, os produtos exclusivos de cada loja e o estoque total.
            logging.info("\n\rExercício 3:")
            print("\nExercício 3:\n Manipular dicionários \"estoque de vprodutos de 2 lojas\"")
            # Dicionários
            produtosLoja1 = {
                "caderno": 15,
                "caneta": 50,
                "borracha": 22
            }
            produtosLoja2 = {
                "caderno": 45,
                "lápis": 10,
                "borracha": 22,
                "pincel atômico":40
            }
            
            logging.info(f"Dicionários iniciais:\n produtos loja 1:\n{mostraDicionario(produtosLoja1)}\n Produtos loja 2:\n{mostraDicionario(produtosLoja2)}")
            #mostra o nome dos produtos das duas lojas
            Linhazinha()
            print(f"Produtos da loja 1:\n > {mostraChave(produtosLoja1)}")
            print(f"Produtos da loja 2:\n > {mostraChave(produtosLoja2)}")
            #log
            logging.info(f"Produtos da loja 1:\n {mostraChave(produtosLoja1)}")
            logging.info(f"Produtos da loja 2:\n {mostraChave(produtosLoja2)}")
            Linhazinha()
            print(f"soma dos produtos das lojas:\n {mostraSomaChaves("Total das duas lojas", produtosLoja1, produtosLoja2)}")
            logging.info(f"soma dos produtos das lojas:\n {mostraSomaChaves("Total das duas lojas", produtosLoja1, produtosLoja2)}")

            Linha()
            logging.info("Ex. 3 finalizado\n")
            input("\nPara voltar ao menu, pressione ENTER.")
        case "4":
            # Exercícios 4
            # Crie uma função multiplicar (valor1, valor2) que recebe dois números e retorna o
            # produto. Pergunte ao usuário dois números e mostre o resultado usando a função
            # multiplicar.
            
            Linha()
        case "5 ":
            # Exercício 5
            # Crie uma função soma_numeros que receba qualquer quantidade de números e
            # retorne a soma.
            Linha()
        case "6":
            # Exercício 6
            # Crie uma lista de números com valores fornecidos pelo usuário, use map para
            # dobrar os valores da lista, use filter para selecionar apenas os números maiores
            # que 3 e use reduce para calcular o produto de todos os números.
            Linha()
        case "7":
            logging.info("Programa encerrado pelo usuário.")
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida.")
            logging.warning("Usuário selecionou a opção inválida(_).")
            input("Para voltar ao menu, pressione Enter.")

logging.info("Programa finalizado.")
print("Programa finalizado.")