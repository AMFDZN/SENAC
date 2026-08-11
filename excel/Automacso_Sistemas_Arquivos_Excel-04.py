import pandas as pd
import numpy as np
import os
from pathlib import Path

# Instrução Geral
# Crie um programa em Python que funcione como um menu de opções. O usuário
# deverá escolher uma opção do menu e cada opção deverá executar um dos
# exercícios abaixo. Todos os exercícios devem estar organizados dentro de um
# único programa.
# Utilize as bibliotecas Pandas, NumPy e OpenPyXL para manipulação de planilhas
# do Excel. Organize o programa de forma modularizada, utilizando funções
# separadas para cada operação, controle pelo menu principal, verificação da
# existência do arquivo, tratamento de erros e opção para encerrar a execução do
# programa.

ARQUIVO="planilha_criada.xlsx"
DIRETORIOABSOLUTO = Path(__file__).resolve().parent


linha="\n- - - - - - - - - - - - -\n"
def verificaArquivo():
    caminhoCompleto = DIRETORIOABSOLUTO / ARQUIVO #Path
    
    if not caminhoCompleto.exists():
        print(f"{linha}A planilha ainda não existe.")
        print(f"Para criar a planilha selecione a opção 1 no menu.{linha}")
        return False
    return True
def criaPlanilha():
                if not verificaArquivo():
                    return
                df = pd.DataFrame(
                                    {
                            
                                    "Produto": [
                                        "Notebook",
                                        "Mouse",
                                        "Teclado",
                                        "Monitor"
                                    ],
                            
                                    "Quantidade": [
                                        10,
                                        35,
                                        20,
                                        8
                                    ],
                            
                                    "Preço": [
                                        3500,
                                        80,
                                        150,
                                        1200
                                    ]
                            
                                }
                                )
                df.to_excel(ARQUIVO, index=False)


def lerPlanilha(tipo):
                if not verificaArquivo(): #ver DIRETORIOABSOLUTO / ARQUIVO existe
                    return
            
                df=pd.read_excel(ARQUIVO)
                if tipo == "p":

                    print(f"\n Planilha ({ARQUIVO}) \n")
                    print(df)
                elif tipo == "r":
                    return df
                

while True:
    
    opcao=input(
"""ESCOLHA SUA OPÇÃO:
1 - GERAR PLANILHA
2- LER PLANILHA
3- ALTERAR PLANILHA
""")

    match opcao:
# Exercício 1
# Crie uma função que gere uma planilha do Excel contendo uma tabela de
# produtos, quantidades e preços, salvando-a em um arquivo .xlsx

        case "1":
            
            
            #chama a função
            criaPlanilha()
            print(f"Planilha {ARQUIVO} criada com sucesso")
            
# Exercício 2
# Crie uma função que leia a planilha criada e exiba todos os seus registros na tela.
        case "2":
            
            #chama a função
            lerPlanilha("p") 
# Exercício 3
# Crie uma função que permita ao usuário informar o nome de uma coluna existente
# e alterar todos os seus valores por um novo valor informado.
        case "3":
            def mudaColuna():
                if not verificaArquivo():
                    return
                
                lerPlanilha("p")#opção print

                qualColuna = input("Informe o nome da coluna que queres alterar: ")
                
                df=lerPlanilha("r")#opção return

                if qualColuna not in df.columns:
                    print("Coluna inexistente.")
                    return

                valor = input(f"Novo valor para a coluna {qualColuna}: ")

                df[qualColuna] = valor

                df.to_excel(ARQUIVO, index=False)

            print("Coluna alterada com sucesso.")
# Exercício 4
# Crie uma função que permita alterar apenas uma célula específica da planilha,
# solicitando a linha, a coluna e o novo valor.
# Exercício 5
# Crie uma função que permita alterar um intervalo de células de uma mesma
# coluna, informando a linha inicial, a linha final e o novo valor.
# Exercício 6
# Crie uma função que permita adicionar uma nova coluna à planilha, solicitando o
# nome da coluna e um valor padrão para todos os registros.
# Exercício 7
# Crie uma função que permita remover uma coluna existente da planilha.
# Exercício 8
# Crie uma função que permita adicionar uma nova linha contendo um novo
# produto, sua quantidade e seu preço.
# Exercício 9
# Crie uma função que permita remover uma linha da planilha, informando seu
# índice.
# Exercício 10
# Crie uma função que solicite um percentual de desconto e aplique esse desconto
# a todos os valores da coluna Preço.
# Exercício 11
# Crie uma função que solicite uma quantidade e aumente o estoque de todos os
# produtos da planilha.
# Exercício 12
# Crie uma função que calcule o valor total de cada produto, multiplicando a
# quantidade pelo preço, armazenando o resultado em uma nova coluna chamada
# Total.
# Exercício 13
# Crie uma função que ordene os produtos pelo preço em ordem decrescente e
# salve a alteração na planilha.
# Exercício 14
# Crie uma função que solicite um valor mínimo e exiba apenas os produtos cujo
# preço seja maior ou igual ao valor informado.
# Exercício 15
# Crie uma função que apresente estatísticas da planilha, incluindo:
# preço médio dos produtos;
# maior preço;
# menor preço;
# quantidade total de itens em estoque;
# desvio padrão dos preços.
        case "16":
            input("CLique ENTER para encerrar")
        
        case _:
            print("Opão errada")