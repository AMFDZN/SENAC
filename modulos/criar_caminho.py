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

def criarCaminho():
   
    diretorio = os.getcwd()
    caminho = os.path.join(diretorio, "arquivo.txt")

    print("\nCaminho Criado")
    print(caminho)
    logging.info(f"Caminho criado: {caminho}")

    return caminho

def qualCaminho():
    diretorio = os.getcwd()
    caminho = os.path.join(diretorio, "arquivo.txt")
    return caminho