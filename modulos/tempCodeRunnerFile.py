import os
from pathlib import Path
from modulos.decorativos import *
        
def conferirCaminho():
    info=""
    caminho = input("Digite um caminho para verificr se ele existe: ")
    if not caminho:
        caminho = input("o caminho não pode ser vazio\nDigite um caminho: ")
    """
    Parâmetros:
        caminho (str): Caminho que será verificado.

    Utiliza:
        Path.exists()  Verifica se o caminho existe.
        Path.is_file()  Verifica se é um arquivo.
        Path.is_dir()  Verifica se é um diretório.
    """

    arquivo = Path(caminho)

    print("\nVerificação")

    if arquivo.exists():

        print("O caminho existe.")
        info="O caminho existe"
        Linhazinha()
        #try
        if arquivo.is_file():
            print("É um arquivo.")
            info=info+"\nÉ um arquivo"

        elif arquivo.is_dir():
            print("É um diretório.")
            info=info+"\nÉ um diretório"

    else:
        print("O caminho não existe.")
        Linha()
    return info