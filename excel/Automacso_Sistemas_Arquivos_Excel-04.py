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

ARQUIVO = "planilha_pandas_criada.xlsx"

DIRETORIORAIZ = os.path.join(os.getcwd(), ARQUIVO) #Opção de usar a pasta raiz - SENAC
CAMINHOARQUIVO= Path(DIRETORIORAIZ) #caminho até o arquivo para a mopção de usar o diretório raiz

DIRETORIOEXERCICIO = Path(__file__).resolve().parent #pasta do exercício [excel]
CAMINHOCOMPLETO = DIRETORIOEXERCICIO / ARQUIVO
print(f"printando caminho2\n{CAMINHOCOMPLETO}")
print(f"printando caminho1\n{CAMINHOARQUIVO}")

#decorativos
LINHA="\n══════════════════════════\n" 
SUCESSO="✔"
ATENCAO="⚠"


#VERIFICA SE O CAMINHO EXISTE
def verificaArquivo(avisar=True):
    
    if not CAMINHOCOMPLETO.exists():
        if avisar:
            print(f"{LINHA}{ATENCAO} A planilha ainda não existe.")
            print(f"\nPara criar a planilha selecione a opção 1 no menu.{LINHA}")
            
        return False
    return True

# Exercício 1
# Crie uma função que gere uma planilha do Excel contendo uma tabela de
# produtos, quantidades e preços, salvando-a em um arquivo .xlsx
def criaPlanilha():
    #verifica se a planilha já existe e questiona se qquer subscrever
    if verificaArquivo(avisar=False):
        criaNovamente = input(f"{LINHA}{ATENCAO} Atenção: A planilha '{ARQUIVO}' já existe na pasta do exercício!\nTem certeza que quer criá-la novamente com os dados iniciais de teste? (s/n): ")
        #se desistir, não recria
        if criaNovamente.lower() != "s":
            print("\nOperação cancelada. A planilha original foi mantida.")
            input("Use ENTER para sair desta opção")
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
    print(f"\nPlanilha {ARQUIVO} criada com sucesso!{LINHA}")


def lerPlanilha(tipo="P"): #tipos de saída: p=print | r=return
    if not verificaArquivo(avisar=True): #ver DIRETORIOEXERCICIO / ARQUIVO existe
        return None
            
    df=pd.read_excel(CAMINHOCOMPLETO)
    if tipo == "p":
        print(f"\n Planilha ({ARQUIVO}):\n")
        print(f"{df.to_string()}{LINHA}")
    elif tipo == "r":
        return df
    
def mostraLinha1(tipo="p"):
    df=lerPlanilha("r")#opção return
    listalinha1=list(df.columns)#linha 0 em forma de lista
    if tipo.lower()=="r":
        return listalinha1
    elif tipo.lower()=="p":
        print(listalinha1)
    else:
        print(listalinha1)
# Exercício 3
# Crie uma função que permita ao usuário informar o nome de uma coluna existente
# e alterar todos os seus valores por um novo valor informado.
def mudaColuna():
        if not verificaArquivo():
            return

        df=lerPlanilha("r")#opção return
        linha1=mostraLinha1("r")#pega a linha 1 "r" = return

        qualColuna = input(f"{LINHA}COLUNAS DA PLANILHA:\n{linha1}\nInforme o nome da coluna que queres alterar: ")
                              

        if qualColuna not in df.columns:
            print(f"\n{ATENCAO}Coluna \"{qualColuna}\" não existe na tabela \"{ARQUIVO}\".")
            return

        valor = input(f"\nDefina o novo valor para a coluna {qualColuna}: ")

        df[qualColuna] = valor

        df.to_excel(CAMINHOCOMPLETO, index=False)

        print(f"\nColuna ({qualColuna}) alterada com sucesso, para o valor {valor}.{LINHA}")

# Exercício 4
# Crie uma função que permita alterar apenas uma célula específica da planilha,
# solicitando a LINHA, a coluna e o novo valor.
def alteraCelula():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        linhaIDx = int(input(f"\nDigite o índice da linha (de 1 a {len(df)-1}): "))
        print("\n")
        mostraLinha1() #informa o nome das colunas     
        colunaNome = input("Digite o nome da coluna: ")
        if colunaNome not in df.columns:
            print(f"{ATENCAO} Coluna não encontrada.")
            return
        novoValor = input(f"\nDigite o novo valor para a coluna \"{colunaNome}\", linha {linhaIDx}: ")
        
        # Converte o tipo de dado se a coluna for numérica
        if np.issubdtype(df[colunaNome].dtype, np.number):
            novoValor = float(novoValor) if '.' in novoValor else int(novoValor)

        df.at[linhaIDx, colunaNome] = novoValor
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print(f"\n{SUCESSO} Célula alterada com sucesso!")
    except Exception as e:
        print(f"{ATENCAO} Erro ao alterar célula: {e}")

# Exercício 5
# Crie uma função que permita alterar um intervalo de células de uma mesma
# coluna, informando a LINHA inicial, a LINHA final e o novo valor.
def alteraIntervalo():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    print("Colunas da tabela:")
    mostraLinha1()
    coluna = input("\nInforme o nome da coluna que vamos usar: ")
    if coluna not in df.columns:
        print(f"{ATENCAO} Coluna '{coluna}'não encontrada.")
        return
    try:
        linhaIni = int(input(f"Linha inicial (índice de 0 a {len(df)-1}): "))
        linhaFim = int(input(f"Linha final (índice de 0 a {len(df)-1}): "))
        novoValor = input(f"Informe o novo valor para o intervalo entre as linhas {linhaIni} e {linhaFim} : ")
        
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
    print("Colunas da tabela:")
    mostraLinha1()
    coluna = input("\nInforme onome da coluna a remover: ")
    if coluna in df.columns:
        df = df.drop(columns=[coluna])
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print(f"{SUCESSO} A coluna '{coluna}' foi removida.")
    else:
        print(f"{ATENCAO} Coluna não encontrada.")
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
        print(f"\n{SUCESSO} Produto adicionado com sucesso!")
    except ValueError:
        print(f"\n{ATENCAO} Erro: Quantidade deve ser um número inteiro!\nPreço deve ser um número.")
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
        print(f"{SUCESSO} Linha removida com sucesso.")
    except Exception as e:
        print(f"{ATENCAO}Erro ao remover linha: {e}")
# Exercício 10
# Crie uma função que solicite um percentual de desconto e aplique esse desconto
# a todos os valores da coluna Preço.
def aplicaDesconto():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        desc = float(input("\nDigite o percentual de desconto (ex: 10 para 10%): "))
        df["Preço"] = df["Preço"] * (1 - desc / 100)
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print(f"{SUCESSO} Desconto de {desc}% aplicado com sucesso!")
    except ValueError:
        print("Por favor, insira um número válido.")

# Exercício 11
# Crie uma função que solicite uma quantidade e aumente o estoque de todos os
# produtos da planilha.
def aumentaEstoque():
    if not verificaArquivo(): return
    df = lerPlanilha("r")
    try:
        qtd = int(input("\nQuantidade a somar ao estoque atual de cada produto: "))
        df["Quantidade"] = df["Quantidade"] + qtd
        df.to_excel(CAMINHOCOMPLETO, index=False)
        print(f"\n{SUCESSO} Estoque atualizado!")
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
    print(f"\n{SUCESSO} Coluna 'Total' criada.\nValores totais de cada produto calculada e salva!")
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
    # tive que procurar o que significava "desvio de preço"
    # O Desvio Padrão dos Preços é uma medida estatística
    # que indica o quanto os preços de um produto,
    # serviço ou ativo financeiro
    # variam em relação ao preço médio
    
    #não entendi, igualmente. O cálculo tive que pesquisar (NumPy.std())
    print(f"Desvio Padrão dos Preços: R$ {np.std(df['Preço']):.2f}")
    print(f"{LINHA}")

while True:
    
    opcao=input(
"""----------------
 ESCOLHA SUA OPÇÃO:
1-  CRIAR PLANILHA PANDAS
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
16- ENCERRAR
---------------------
Opção nº: """)

    match opcao:
        case "1":
            print("CRIANDO UMA PLANILHA")
            criaPlanilha()
            input("use ENTER para retornar ao menu")
            
        case "2":
            
            print("LENDO A PLANILHA DO EXERCÍCIO")
            lerPlanilha("p")
            input("use ENTER para retornar ao menu") 

        case "3":

            print("ALTERANDO OS VALORES DAS CÉLULAS DE UMA COLUNA INTEIRA")
            mudaColuna()
            input("use ENTER para retornar ao menu")
            
        case "4":

            print("ALTERANDO O VALOR DE UMA CÉLULA ESPECÍFICA")
            alteraCelula()
            input("use ENTER para retornar ao menu")
            
        case "5":

            print("ALTERANDO VALORES DE UMA COLUNA, INFORMANDO O INTERVALO ENTRE ELAS")
            alteraIntervalo()
            input("use ENTER para retornar ao menu")
            
        case "6":

            print("ADICIONANDO UMA NOVA COLUNA À NOSSA PLANILHA")
            adicionaColuna()
            input("use ENTER para retornar ao menu")
            
        case "7":

            print("REMOVENDO UMA COLUNA DA NOSSA PLANILHA")
            removeColuna()
            input("use ENTER para retornar ao menu")
            
        case "8":

            print("ADICIONANDO UMA LINHA À NOSSA PLANILHA")
            adicionaLinha()
            input("use ENTER para retornar ao menu")
            
        case "9":

            print("REMOVERNDO UMA LINHA DA NOSSA PLANILHA")
            removeLinha()
            input("use ENTER para retornar ao menu")
            
        case "10":
            
            print("APLICANDO UM PERCENTUAL DE DESCONTO NOS VALORES DOS PRODUTOS DA PLANILHA")
            aplicaDesconto()
            input("use ENTER para retornar ao menu")
            

        case "11":
            
            print("MANIPULANDO A COLUNA \"ESTOQUE\" DA NOSSA PLANILHA DE PRODUTOS")
            aumentaEstoque()
            input("use ENTER para retornar ao menu")
            
        case "12":
            
            print("SOMANDO OS VALORES DOS PRODUTOS NA PLANILHA")
            calculaTotal()
            input("use ENTER para retornar ao menu")

        case "13":
            
            print("ORDENANDO OS PRODUTOS PELO PREÇO")
            ordenaPorPreco()
            input("use ENTER para retornar ao menu")

        case "14":
            
            print("FILTRANDO OS PRODUTOS A PARTIR DE UM PREÇO MÍNIMO")
            filtraValorMinimo()
            input("use ENTER para retornar ao menu")

        case "15":
            
            print("EXIBINDO ESTATÍSTICAS SOBRE A PLANILHA")
            exibeEstatisticas()
            input("use ENTER para retornar ao menu")

        case "16":
            
            print("Encerrando o programa... Até logo!")
            break
        
        case _:
            print("Opção errada")


