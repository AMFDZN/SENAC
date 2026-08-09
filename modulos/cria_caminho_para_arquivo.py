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

# Exercício 3
        # Crie uma função que solicite o nome de um arquivo ao usuário e crie o caminho
        # completo desse arquivo.
        
def criaCaminhoParaArquivo(diretorio):
    if not diretorio:
        diretorio = os.getcwd()
    qualArquivo=input(f"\nDigite o nome de um arquivo (nome.ext),\n para criar o caminho até ele no diretório\n{diretorio} ")
    if not qualArquivo:
        qualArquivo="arquivo.txt"
    caminho = os.path.join(diretorio, qualArquivo)
    print("\nCaminho Criado")
    print(caminho)
    return caminho