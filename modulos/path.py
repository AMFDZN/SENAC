import os
from pathlib import Path
from modulos.decorativos import *

### CRUD r w a

def ler_arquivo(caminho):
    """
    Realiza a leitura do conteúdo de um arquivo de texto.

    Parâmetros:
        caminho (str): Caminho do arquivo que será lido.

    Modo utilizado:
        "r" (read):
            Abre o arquivo somente para leitura.
            O arquivo precisa existir para funcionar.

    Utiliza:
        read() -> Lê todo o conteúdo do arquivo.
    """

    if Path(caminho).exists():

        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        print("\nCONTEÚDO DO ARQUIVO:")
        print(conteudo)

    else:
        print("Arquivo não encontrado.")



def adicionar_texto(caminho):
    """
    Adiciona novas informações no final de um arquivo.

    Parâmetros:
        caminho (str): Caminho do arquivo que receberá o texto.

    Modo utilizado:
        "a" (append):
            Abre o arquivo para adicionar conteúdo.
            O texto novo é colocado no final sem apagar informações antigas.
            Caso o arquivo não exista, ele será criado.

    Utiliza:
        write() -> Escreve informações dentro do arquivo.
    """

    texto = input("Digite o texto que deseja adicionar: ")

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")

    print("Texto adicionado com sucesso!")

