import os
from pathlib import Path
from modulos.decorativos import *


def lerArquivo(caminho):
    if not caminho:
        caminho = input("Se prefirir, digite o caminho do arquivo que deseja ler,\nou pressione ENTER para usar o diretório padrão do teste: ")
    if not caminho:
        caminho = os.getcwd()
        #caminho = criaCaminhoParaArquivo()
        
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