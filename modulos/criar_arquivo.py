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

# Exercício 5
# Crie uma função que receba um caminho e crie um arquivo de texto com uma
# mensagem
# inicial.
            
#def criarArquivo(caminho):
def criarArquivo(qualArquivo):
    if not qualArquivo:
        qualArquivo="arquivo_criado.txt"
    diretorio = os.getcwd()
    caminho = os.path.join(diretorio, qualArquivo)
    
    print(f"\nCriando o arquivo de texto\n{qualArquivo}\n")
    texto = input("Digite o texto que deseja adicionar: ")

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)
        arquivo.write("\n")

    print("\nArquivo criado com sucesso!")
    print(f"texto adicionado ao arquivo: {caminho}\n -> {texto}")