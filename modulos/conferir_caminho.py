import os
from pathlib import Path
from modulos.decorativos import *
import logging

logging.basicConfig(
    filename="manipulacao-arquivos-e-dados.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"
)

def conferirCaminho(caminho):
    info=""
    if not caminho:
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
    logging.info(f"\nVerificando o caminho:\n {caminho}")

    if arquivo.exists():

        print("O caminho existe.")
        info="\nO caminho existe"
        Linhazinha()
        #try
        if arquivo.is_file():
            print("É um arquivo.")
            info+="\nÉ um arquivo"

        elif arquivo.is_dir():
            print("É um diretório.")
            info+="\nÉ um diretório"

    else:
        print("O caminho não existe.")
        info="O caminho não existe"
        logging.info(f"{info}")
        Linha()
        return False
    return True