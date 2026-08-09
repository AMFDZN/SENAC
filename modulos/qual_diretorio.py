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

# Exercício 1
# Crie uma função que mostre o diretório atual onde o programa está sendo executado.
def qualDiretorio():
    diretorio = os.getcwd()

    print("\nDiretório default dos testes:")
    print(diretorio)
    return diretorio