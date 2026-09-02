
# pip install pdfplumber
# pip install pytesseract
# pip install reportlab
# pip install PyMuPDF
import os
from pathlib import Path
from pypdf import (
    PdfReader,
    PdfWriter
)
import pdfplumber
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# Instrução Geral 
# Crie um programa em Python que funcione como um menu de opções. 
# O usuário deverá escolher uma opção do menu e cada opção deverá executar um 
# dos exercícios abaixo. Todos os exercícios devem estar organizados dentro de um 
# único programa. 
# Utilize bibliotecas apropriadas para manipulação de arquivos de texto, arquivos 
# PDF, geração de documentos PDF e reconhecimento óptico de caracteres (OCR). 
# O programa deverá ser organizado de forma modularizada, utilizando funções 
# separadas para cada operação, controle pelo menu principal, verificação da 
# existência dos arquivos, tratamento de erros e opção para encerrar a execução do 
# programa. 
# O programa deverá trabalhar com arquivos .txt, .pdf e imagens utilizadas no 
# processo de OCR. 
ARQUIVO_TESTE = "dados.txt"
PDFS = "pdfs"
SAIDA = "saida"
CERTIFICADO = "certificado.pdf"
CONTRATO = "contrato.pdf"

#CRIAR DENTRO DA PASTA DO EXERCÍCIO
DIRETORIOEXERCICIO = Path(__file__).resolve().parent #pasta do exercício [pdf]
CERIFICADO = DIRETORIOEXERCICIO / CERTIFICADO
CONTRATO = DIRETORIOEXERCICIO / CONTRATO
PASTA_PDFS = DIRETORIOEXERCICIO / PDFS 
PASTA_SAIDA = DIRETORIOEXERCICIO / SAIDA

#funções
import sys
sys.path.append(str(Path(__file__).parent))
from funcoes import *

#decorativos
LINHA="══════════════════════════"
LINHAZINHA="┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅"
OK="[✔]"
ERRO="[✕]"
ATENCAO="[⚠]"
LI="➤"
MUDOU="[⇄]"


while True:
    opcao=input("""
MENU DE OPÇÕES:
ººººººººººººººººººººººº
0-  CRIAR AS PASTAS PARA OS EXERCÍCIOS
1-  CRIAR UM ARQUIVO DE TEXTO                
2-  LER O CONTEÚDO DE UM ARQUIVO
3-  ESCREVER NO ARQUIVO
4-  PROCURAR UMA PARAVRA EM UM ARQUIVO
5-  LISTAR ARQUIVOS EM UMA PASTA
6-  PROCURAR UM ARQUIVO EM UMA PASTA
7-  PDF - INFORMAÇÕES SOBRE UM ARQUIVO
8-  PDF - EXTARAIR UMA OCORRÊNCIA E INGFORMAR ONDE
9-  PDF - PROCURAR UMA OCORRÊNCIA   
10- PDF - SELECIONAR UMA PÁGINA E CRIAR OUTRO ARQUIVO COM ELA
11- PDF - SELECIONAR VÁRIOS ARQUIVOS , E JUNTÁ-LOS EM UM SÓ ARQUIVO
12- PDF - GERAR UM CERTIFICADO
13- PDF - GRRAR UM CONTRATO           

\n-> DIGITE SUA OPÇÃO: """)
    match opcao:
        case "0":
            print("VAMOS CRIAR AS PASTAS PARA OS EXERCÍCIOS")
            criaPastas()
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "1":
            print("VAMOS CRIAR UM ARQUIVO DE TEXTO")
            criarArquivo(nomeDoArquivo=False)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "2":
            print("VAMOS LER UM ARQUIVO DE TEXTO")
            lerArquivo()
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "3":
            print("escrever em um arquivo")
            adicionarConteudo()
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "4":
            print("PROCURAR UMA SENTENÇA EM UM TEXTO")
            procuraConteudo()
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "5":
            print("VAMOS LISTAR OS ARQUIVOS [pdfs]")
            listarArquivos(tipo="pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "6":
            print("PROCURAR UM ARQUIVO NA PASTA [pdfs]")
            procuraArquivo(tipo="pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "7":
            print("VAMOS LISTAR INFORMAÇÕES DE UM ARQUIVO [pdf]")
            verPdf()
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "8":
            print("VAMOS LISTAR OS ARQUIVOS [pdfs]")
            listarArquivos("pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "9":
            print("VAMOS LISTAR OS ARQUIVOS [pdfs]")
            listarArquivos("pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "10":
            print("VAMOS LISTAR OS ARQUIVOS [pdfs]")
            listarArquivos("pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "11":
            print("VAMOS LISTAR OS ARQUIVOS [pdfs]")
            listarArquivos("pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "12":
            print("VAMOS CRIR UM CERTIFICADO NA PASTA [pdfs]")
            criaCertificado()
            
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "13":
            print("VAMOS LISTAR OS ARQUIVOS [pdfs]")
            listarArquivos("pdf")
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")

        case "14":
            print("CONFIGURAR O EXE")
            configuraTesseract()
            input(f"{LINHA}Use ENTER para voltar ao menu")