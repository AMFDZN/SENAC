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

def escreverNoArquivo(caminho):
    arquivo_criado = "arquivo_criado.txt"
    if not caminho:
        caminho= os.path.join(os.getcwd(), arquivo_criado)
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

    texto = input(f"Digite o texto que deseja adicionar no arquivo ({arquivo_criado}): ")

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")

    print(f"Texto adicionado com sucesso no arquivo ({arquivo_criado})!")