import pandas as pd
import openpyxl
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

ARQUIVO = "planilha_criada.xlsx"
DIRETORIOABSOLUTO = Path(__file__).resolve().parent
CAMINHOCOMPLETO = DIRETORIOABSOLUTO / ARQUIVO


LINHA="\n════════════════════\n"

#VERIFICA SE O CAMINHO EXISTE
def verificaArquivo(avisar=True):
    
    if not CAMINHOCOMPLETO.exists():
        if avisar:
            print(f"{LINHA}A planilha ainda não existe.")
            print(f"Para criar a planilha selecione a opção 1 no menu.{LINHA}")
        return False
    return True

# Exercício 1
# Crie uma função que gere uma planilha do Excel contendo uma tabela de
# produtos, quantidades e preços, salvando-a em um arquivo .xlsx
def criaPlanilha():
    if not verificaArquivo():
        return
    df = pd.DataFrame({
                            
                         "Produto": [
                             "Guitarra Tagima Stratocaster",
                              "BaixoFender squire",
                            "Teclado Hammond",
                             "Bateria Perl Export"
                         ],
                            
                         "Quantidade": [2,3,1,2],
                            
                        "Preço": [3500,4500,8300,3200]
                            
                        })
    df.to_excel(CAMINHOCOMPLETO, index=False)
    print(f"Planilha {ARQUIVO} criada com sucesso!")


def lerPlanilha(tipo="P"):
    if not verificaArquivo(): #ver DIRETORIOABSOLUTO / ARQUIVO existe
        return None
            
    df=pd.read_excel(CAMINHOCOMPLETO)
    if tipo == "p":
        print(f"\n Planilha ({ARQUIVO}) \n")
        print(f"{df.to_string()}{LINHA}")
    elif tipo == "r":
        return df
# Exercício 3
# Crie uma função que permita ao usuário informar o nome de uma coluna existente
# e alterar todos os seus valores por um novo valor informado.
def mudaColuna():
                if not verificaArquivo():
                    return

                df=lerPlanilha("r")#opção return
                LINHA1=df.iloc[0]

                qualColuna = input(f"{LINHA1}\nInforme o nome da coluna que queres alterar: ")
                              

                if qualColuna not in df.columns:
                    print("Coluna inexistente.")
                    return

                valor = input(f"Novo valor para a coluna {qualColuna}: ")

                df[qualColuna] = valor

                df.to_excel(CAMINHOCOMPLETO, index=False)

                print("Coluna alterada com sucesso.")

# Exercício 4
# Crie uma função que permita alterar apenas uma célula específica da planilha,
# solicitando a LINHA, a coluna e o novo valor.
def alteraCelula():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        linhaIDx = int(input(f"Digite o índice da linha (0 a {len(df)-1}): "))
        colunaNome = input("Digite o nome da coluna: ")
        if colunaNome not in df.columns:
            print("Coluna não encontrada.")
            return
        novoValor = input("Digite o novo valor: ")
        
        # Converte tipo se a coluna for numérica
        if np.issubdtype(df[colunaNome].dtype, np.number):
            novoValor = float(novoValor) if '.' in novoValor else int(novoValor)

        df.at[linhaIDx, colunaNome] = novoValor
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print("Célula alterada com sucesso!")
    except Exception as e:
        print(f"Erro ao alterar célula: {e}")

# Exercício 5
# Crie uma função que permita alterar um intervalo de células de uma mesma
# coluna, informando a LINHA inicial, a LINHA final e o novo valor.
def alteraIntervalo():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    coluna = input("Digite o nome da coluna: ")
    if coluna not in df.columns:
        print("Coluna não encontrada.")
        return
    try:
        linhaIni = int(input("Linha inicial (índice): "))
        linhaFim = int(input("Linha final (índice): "))
        novoValor = input("Novo valor para o intervalo: ")
        
        if np.issubdtype(df[coluna].dtype, np.number):
            novoValor = float(novoValor) if '.' in novoValor else int(novoValor)

        df.loc[linhaIni:linhaFim, coluna] = novoValor
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print("Intervalo alterado")
    except Exception as e:
        print(f"Erro no intervalo:\n {e}")

# Exercício 6
# Crie uma função que permita adicionar uma nova coluna à planilha, solicitando o
# nome da coluna e um valor padrão para todos os registros.
def adicionaColuna():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    novaColuna = input("Nome da nova coluna: ")
    valorPadrao = input("Valor padrão para os registros: ")
    df[novaColuna] = valorPadrao
    df.to_excel(CAMINHOCOMPLETO, index=False)
    print(f"Coluna '{novaColuna}' adicionada!")

# Exercício 7
# Crie uma função que permita remover uma coluna existente da planilha.
def removeColuna():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    coluna = input("Nome da coluna a remover: ")
    if coluna in df.columns:
        df = df.drop(columns=[coluna])
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print(f"Coluna '{coluna}' removida.")
    else:
        print("Coluna não encontrada.")
# Exercício 8
# Crie uma função que permita adicionar uma nova LINHA contendo um novo
# produto, sua quantidade e seu preço.
def adicionaLinha():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        prod = input("Nome do Produto: ")
        qtd = int(input("Quantidade: "))
        preco = float(input("Preço: "))
        
        novaLinha = pd.DataFrame([{"Produto": prod, "Quantidade": qtd, "Preço": preco}])
        df = pd.concat([df, novaLinha], ignore_index=True) # .concat (join) ignore_index=True - esquece o íncide anterior
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Erro: Quantidade deve ser inteira e Preço deve ser número.")
# Exercício 9
# Crie uma função que permita remover uma LINHA da planilha, informando seu
# índice.
def removeLinha():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        idx = int(input(f"Digite o índice da linha para remover (0 a {len(df)-1}): "))
        df = df.drop(index=idx).reset_index(drop=True)
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print("Linha removida com sucesso.")
    except Exception as e:
        print(f"Erro ao remover linha: {e}")
# Exercício 10
# Crie uma função que solicite um percentual de desconto e aplique esse desconto
# a todos os valores da coluna Preço.
def aplicaDesconto():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        desc = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
        df["Preço"] = df["Preço"] * (1 - desc / 100)
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print(f"Desconto de {desc}% aplicado com sucesso!")
    except ValueError:
        print("Por favor, insira um número válido.")

# Exercício 11
# Crie uma função que solicite uma quantidade e aumente o estoque de todos os
# produtos da planilha.
def aumentaEstoque():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        qtd = int(input("Quantidade a somar ao estoque atual: "))
        df["Quantidade"] = df["Quantidade"] + qtd
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print("Estoque atualizado!")
    except ValueError:
        print("Por favor, insira um número inteiro.")

# Exercício 12
# Crie uma função que calcule o valor total de cada produto, multiplicando a
# quantidade pelo preço, armazenando o resultado em uma nova coluna chamada
# Total.
def calculaTotal():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    df["Total"] = df["Quantidade"] * df["Preço"]
    df.to_excel(CAMINHOCOMPLETO, index=False)
    print("Coluna 'Total' calculada e salva!")
# Exercício 13
# Crie uma função que ordene os produtos pelo preço em ordem decrescente e
# salve a alteração na planilha.
def ordenaPorPreco():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    df = df.sort_values(by="Preço", ascending=False)
    df.to_excel(CAMINHOCOMPLETO, index=False)
    print("Planilha ordenada por preço (Decrescente)!")

# Exercício 14
# Crie uma função que solicite um valor mínimo e exiba apenas os produtos cujo
# preço seja maior ou igual ao valor informado.
def filtraValorMinimo():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        minimo = float(input("Exibir produtos com preço maior ou igual a: "))
        filtro = df[df["Preço"] >= minimo]
        print(f"\n--- Produtos com preço >= {minimo} ---\n")
        print(filtro.to_string())
    except ValueError:
        print("Valor inválido.")
# Exercício 15
# Crie uma função que apresente estatísticas da planilha, incluindo:
# preço médio dos produtos;
# maior preço;
# menor preço;
# quantidade total de itens em estoque;
# desvio padrão dos preços.
def exibeEstatisticas():
    if not verificaArquivo(): return
    df = lerPlanilha("r")

    #NumPy

    print(f"{LINHA}☆ ESTATÍSTICAS DA PLANILHA ☆")
    print(f"Preço Médio: R$ {df['Preço'].mean():.2f}") #DataFrame.Coluna.Média
    print(f"Maior Valor: R$ {df['Preço'].max():.2f}") #DataFrame.Coluna.Máximo
    print(f"Menor Valor: R$ {df['Preço'].min():.2f}") #DataFrame.Coluna.Mínimo
    print(f"Total de Itens no Estoque: {df['Quantidade'].sum()} unidades") #DataFrame.Coluna.soma
    print(f"Desvio Padrão dos Preços: R$ {np.std(df['Preço']):.2f}")
    print(f"{LINHA}")
while True:
    
    opcao=input(
"""∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷ ∷
 ESCOLHA SUA OPÇÃO:

1-  GERAR PLANILHA
2-  LER PLANILHA
3-  ALTERAR PLANILHA
4-  ALTERAR UMA CÉLULA
5-  ALTERA INTERVALO ENTRE CÉLULAS
6-  ADICIONAR NOVA COLUNA
7-  REMOVER COLUNA
8-  ADICIOR LINHA
9-  REMOVER LINHA
10- APLICAR DESCONTO NO PREÇO
11- AUMENTAR ESTOQUE
12- VALOR TOTAL DOS PRODUTOS DO ESTOQUE
13- ORDENAR PRODUTOS PELO PREÇO
14- MOSTRAR PRODUTOS A PARTIR DE UM VALOR MÍNIMO
15- ESTATÍSTICAS
""")

    match opcao:
        case "1":
            criaPlanilha()
            print(f"Planilha {ARQUIVO} criada com sucesso")
            
        case "2":
            
            lerPlanilha("p") 

        case "3":

            mudaColuna()
        case "4":

            alteraCelula()
        case "5":

            alteraIntervalo()
        case "6":

            adicionaColuna()
        case "7":

            removeColuna()
        case "8":

            adicionaLinha()
        case "9":

            removeLinha()
        case "10":
            aplicaDesconto()

        case "11":
            aumentaEstoque()

        case "12":
            calculaTotal()

        case "13":
            ordenaPorPreco()

        case "14":
            filtraValorMinimo()

        case "15":
            exibeEstatisticas()

        case "16":
            input("CLique ENTER para encerrar")
        
        case _:
            print("Opão errada")


