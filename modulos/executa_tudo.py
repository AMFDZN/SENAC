import os
from pathlib import Path
from import_main import *
import logging

logging.basicConfig(                    
    filename="manipulacao-arquivos-e-dados.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"                  
)

seta="🠆"
linha =("╍"*30)
linhazinha=("╌"*30)

def executaTudo():
    """
    Executa todas as operações em sequência,
    realizando a criação,
    verificação,
    leitura e
    alteração de um arquivo.
    """
    logging.info("Executando todas as operações em sequência.")
    logging.info(f"executando: criaCaminhoParaArquivo()\n{linhazinha}")
    caminho = criarCaminho()
    logging.info(f"\nexecutando conferirCaminho()\n{linhazinha}")
    conferirCaminho(caminho)
    logging.info(f"\nCaminho conferido: {caminho}")
    print(f"\nCaminho absoluto do diretório: {caminho}")
    logging.info(f"Executando criarArquivo()\n{linhazinha}")
    print(f"\nCriarArquivo()\n{linhazinha}")
    criarArquivo(caminho)
    logging.info(f"\nExecutando escreverNoArquivo()\n{linhazinha}")
    print(f"\nEscreverNoArquivo()\n{linhazinha}")
    escreverNoArquivo(caminho)
    logging.info(f"\nExecutando lerArquivo()\n{linhazinha}")
    print(f"\nLerArquivo()\n{linhazinha}")
    lerArquivo(caminho)