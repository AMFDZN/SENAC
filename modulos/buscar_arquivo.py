import os
from pathlib import Path
from modulos.decorativos import *
import logging

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

def buscarArquivo(qualArquivo):
    
    #diretorio = os.getcwd()
    caminho = os.path.join(os.getcwd(), qualArquivo)
    qualArquivo= Path(caminho)

    print("\nVerificação")
    logging.info(f"Verificação de caminho: {qualArquivo}")

    if qualArquivo.exists():

        if qualArquivo.is_file():
            print("É um arquivo.")
            logging.info(f"\nÉ um arquivo")
        else:
            print(f"O arquivo {qualArquivo} não existe no diretório\n{caminho}")
            logging.info(f"\nO arquivo \"{qualArquivo}\" não existe no diretório: \"{caminho}\"")
   
