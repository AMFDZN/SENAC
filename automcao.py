import pandas as pd
import numpy as np
import os


ARQUIVO = "planilha.xlsx"


def criar_excel():
    """Cria uma planilha de exemplo."""

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

    print("\nPlanilha criada com sucesso!")


def verificar_arquivo():

    if not os.path.exists(ARQUIVO):

        print("\nA planilha não existe.")

        print("Crie a planilha primeiro (Opção 1).")

        return False

    return True


def listar_planilha():
    """Mostra toda a planilha."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    print("\n Planilha \n")

    print(df)


def alterar_coluna():
    """Altera todos os valores de uma coluna."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    coluna = input("Nome da coluna: ")

    if coluna not in df.columns:

        print("Coluna inexistente.")

        return

    valor = input("Novo valor para toda a coluna: ")

    df[coluna] = valor

    df.to_excel(ARQUIVO, index=False)

    print("Coluna alterada com sucesso.")


def alterar_celula():
    """Altera apenas uma célula."""

    if not verificar_arquivo():
        return

    df = pd.read_excel(ARQUIVO)

    linha = int(input("Linha: "))

    coluna = input("Coluna: ")

    if coluna not in df.columns:
        print("Coluna inexistente.")
        return

    if linha < 0 or linha >= len(df):
        print("Linha inválida.")
        return

    valor = input("Novo valor: ")

 
    try:
        tipo_coluna = df[coluna].dtype

        if tipo_coluna == "int64":
            valor = int(valor)

        elif tipo_coluna == "float64":
            valor = float(valor)

        elif tipo_coluna == "bool":
            valor = valor.lower() in ["true", "sim", "s", "1"]

    except ValueError:
        print("Valor inválido para essa coluna.")
        return


    df.loc[linha, coluna] = valor


    df.to_excel(ARQUIVO, index=False)

    print("Célula alterada com sucesso.")


def alterar_intervalo():
    """Altera várias células."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    coluna = input("Coluna: ")

    if coluna not in df.columns:

        print("Coluna inexistente.")

        return

    inicio = int(input("Linha inicial: "))

    fim = int(input("Linha final: "))

    valor = input("Novo valor: ")

    df.loc[inicio:fim, coluna] = valor

    df.to_excel(ARQUIVO, index=False)

    print("Intervalo alterado.")


def adicionar_coluna():
    """Adiciona uma nova coluna."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    coluna = input("Nome da nova coluna: ")

    valor = input("Valor padrão: ")

    df[coluna] = valor

    df.to_excel(ARQUIVO, index=False)

    print("Coluna adicionada.")


def remover_coluna():
    """Remove uma coluna."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    coluna = input("Coluna para remover: ")

    if coluna not in df.columns:

        print("Coluna inexistente.")

        return

    df = df.drop(columns=[coluna])

    df.to_excel(ARQUIVO, index=False)

    print("Coluna removida.")


def aplicar_desconto():
    """Aplica desconto na coluna Preço."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    desconto = float(input("Desconto (%): "))

    df["Preço"] = df["Preço"] * (1 - desconto / 100)

    df.to_excel(ARQUIVO, index=False)

    print("Desconto aplicado.")


def aumentar_estoque():
    """Aumenta a quantidade em estoque."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    quantidade = int(input("Quantidade a adicionar: "))

    df["Quantidade"] += quantidade

    df.to_excel(ARQUIVO, index=False)

    print("Estoque atualizado.")


def calcular_total():
    """Cria a coluna Total."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    df["Total"] = df["Quantidade"] * df["Preço"]

    df.to_excel(ARQUIVO, index=False)

    print(df)


def ordenar_produtos():
    """Ordena a planilha pelo preço."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    df = df.sort_values(by="Preço", ascending=False)

    df.to_excel(ARQUIVO, index=False)

    print(df)


def estatisticas():
    """Mostra estatísticas da planilha."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    print("\n Estatísticas \n")

    print(f"Preço médio: {df['Preço'].mean():.2f}")

    print(f"Maior preço: {df['Preço'].max():.2f}")

    print(f"Menor preço: {df['Preço'].min():.2f}")

    print(f"Total em estoque: {df['Quantidade'].sum()}")

    print(f"Desvio padrão do preço: {df['Preço'].std():.2f}")


def filtrar_produtos():
    """Filtra produtos acima de um valor."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    valor = float(input("Preço mínimo: "))

    resultado = df[df["Preço"] >= valor]

    print(resultado)


def adicionar_linha():
    """Adiciona um novo produto."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    produto = input("Produto: ")

    quantidade = int(input("Quantidade: "))

    preco = float(input("Preço: "))

    nova_linha = pd.DataFrame({

        "Produto": [produto],

        "Quantidade": [quantidade],

        "Preço": [preco]

    })

    df = pd.concat([df, nova_linha], ignore_index=True)

    df.to_excel(ARQUIVO, index=False)

    print("Produto adicionado.")


def remover_linha():
    """Remove uma linha."""

    if not verificar_arquivo():

        return

    df = pd.read_excel(ARQUIVO)

    linha = int(input("Linha para remover: "))

    if linha < 0 or linha >= len(df):

        print("Linha inválida.")

        return

    df = df.drop(linha).reset_index(drop=True)

    df.to_excel(ARQUIVO, index=False)

    print("Linha removida.")


def menu():

    while True:

        print("""


1  - Criar planilha

2  - Listar planilha

3  - Alterar coluna

4  - Alterar célula

5  - Alterar intervalo de células

6  - Adicionar coluna

7  - Remover coluna

8  - Adicionar linha

9  - Remover linha

10 - Aplicar desconto

11 - Aumentar estoque

12 - Calcular coluna Total

13 - Ordenar por preço

14 - Filtrar produtos

15 - Estatísticas

0  - Sair

""")

        opcao = input("Escolha uma opção: ")
        match opcao:

            case "1":

                criar_excel()
                input("Pressione Enter para voltar ao menu.")

            case "2":

                listar_planilha()
                input("Pressione Enter para voltar ao menu.")

            case "3":

                alterar_coluna()
                input("Pressione Enter para voltar ao menu.")

            case "4":

                alterar_celula()
                input("Pressione Enter para voltar ao menu.")

            case "5":
                alterar_intervalo()
                input("Pressione Enter para voltar ao menu.")

            case "6":

                adicionar_coluna()
                input("Pressione Enter para voltar ao menu.")

            case "7":

                remover_coluna()
                input("Pressione Enter para voltar ao menu.")

            case "8":

                adicionar_linha()
                input("Pressione Enter para voltar ao menu.")

            case "9":

                remover_linha()
                input("Pressione Enter para voltar ao menu.")

            case "10":

                aplicar_desconto()
                input("Pressione Enter para voltar ao menu.")

            case "11":

                aumentar_estoque()
                input("Pressione Enter para voltar ao menu.")

            case "12":

                calcular_total()
                input("Pressione Enter para voltar ao menu.")

            case "13":

                ordenar_produtos()
                input("Pressione Enter para voltar ao menu.")

            case "14":

                filtrar_produtos()
                input("Pressione Enter para voltar ao menu.")

            case "15":

                estatisticas()
                input("Pressione Enter para voltar ao menu.")

            case "0":

                print("Programa encerrado.")

                break

            case _:

                print("Opção inválida.")

if __name__=="__main__":

    menu()