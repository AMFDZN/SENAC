import os
#from pathlib import Path
from modulos.decorativos import *
import logging
logging.basicConfig(
    filename="manipulacao-arquivos-e-dados.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"
)

# Exercício 2
# Crie uma função que liste todos os arquivos e pastas existentes no diretório atual.
def listarArquivos():

    print(f"\nArquivos e pastas dentro da Pasta do teste: {os.getcwd()}")
    for arquivo in os.listdir():
        print(arquivo)