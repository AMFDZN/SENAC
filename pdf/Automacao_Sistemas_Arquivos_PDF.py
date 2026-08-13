
# pip install pdfplumber
# pip install pytesseract
# pip install reportlab
# pip install PyMuPDF
import os
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
ARQUIVO_TEXTO = "dados.txt"
PASTA_PDFS = "pdfs"
PASTA_SAIDA = "saida"
ARQUIVO_CERTIFICADO = "certificado.pdf"
ARQUIVO_CONTRATO = "contrato.pdf" 

##criando as pastas

def criaPastas():
    """ 
    CRIA DIRETÓRIOS - os.makedirs
    os.makedirs(NOME_DA_PASTA, exist_ok=True) - exist_ok=True Evita erro caso a pasta já exista.
    """

    os.makedirs(PASTA_PDFS, exist_ok=True)

    os.makedirs(PASTA_SAIDA, exist_ok=True)


# Exercício 1  
# Crie uma função que permita ao usuário criar um novo arquivo de texto. 
# O usuário deverá informar o nome do arquivo e o conteúdo que será armazenado. 
# O arquivo deverá ser criado utilizando codificação UTF-8. 
def criarArquivo(): #inserir variável para definir extensão
    nomeDoArquivo = input("Dê um nome para o arquivo: ")

    if not nomeDoArquivo.endswith(".txt"): # .endswith() extensão do arquivo 
        nomeDoArquivo += ".txt"
    
    conteudo = input(f"Escreva algo no arquivo {nomeDoArquivo}: ")


    with open( nomeDoArquivo,"w", encoding="utf-8" ) as arquivo:

        arquivo.write(conteudo)

    print("\nArquivo criado com sucesso.")
    
  
# Exercício 2  
# Crie uma função que permita abrir um arquivo de texto existente e apresentar seu 
# conteúdo na tela. 
# Antes de realizar a leitura, o programa deverá verificar se o arquivo existe. 
def lerArquivo(): 
    """
        open() - Abre o arquivo.
        read() - Lê todo o conteúdo.
    """

    nome = input("Informe o nome do arquivo: ")

    if not os.path.exists(nome):
        print("Arquivo não encontrado.")
        return

    with open(nome,"r",encoding="utf-8") as arquivo:

        conteudo = arquivo.read()

    print("\nCONTEÚDO DO ARQUIVO\n")
    print(conteudo)
  
# Exercício 3  
# Crie uma função que permita adicionar novas informações ao final de um arquivo 
# de texto existente. 
# O conteúdo existente não deverá ser apagado. 
 
def adicionarConteudo():
    """
    Adiciona conteúdo ao final de um arquivo de texto.

    Utiliza:

        mode="a"
            Abre o arquivo para adicionar conteúdo
            sem apagar o conteúdo existente.

    """

    nome = input("Diga o nome do arquivo que vai ser adicionado o conteúdo: ")

    if not os.path.exists(nome): #verifica se o caminho e arquivo existem
        print("Arquivo não encontrado.")
        return

    texto = input("Texto que deseja adicionar: ")

    with open(nome,"a", encoding="utf-8") as arquivo:

        arquivo.write("\n" + texto)

    print("Texto adicionado com sucesso.")
 
# Exercício 4  
# Crie uma função que permita procurar uma palavra ou expressão dentro de um 
# arquivo de texto. 
# O programa deverá informar em quais linhas o termo pesquisado foi encontrado. 
# A pesquisa deverá ignorar diferenças entre letras maiúsculas e minúsculas. 
def procuraConteudo():
    """
    Procura um trecho de texto  dentro do arquivo.

    Utiliza:
        in
        Verifica se um texto existe dentro de outro.

    """

    nome = input("Informe o nome do arquivo: ")


    if not os.path.exists(nome):
        print("Arquivo não encontrado.")
        return


    termo = input("Digite o termo que deseja procurar: ")


    with open(nome,"r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    encontrado = False
    print("\nRESULTADOS\n")


    for numero, linha in enumerate(linhas,start=1): #numero é o índice

        if termo.lower() in linha.lower():

            print(f"Linha {numero}: {linha.strip()}")

            encontrado = True

    if not encontrado:

        print("Nenhuma ocorrência encontrada.")

 
# Exercício 5  
# Crie uma função que liste todos os arquivos com extensão .pdf existentes em uma 
# pasta específica. 
# Caso a pasta não exista, ela deverá ser criada automaticamente. 
# Caso não existam arquivos PDF, o programa deverá informar ao usuário. 

def listarArquivos(tipo): #extensão (pdf / txt)
    """
    Lista os arquivos existentes na pasta.

    Utiliza:

        os.listdir()
            Lista os arquivos de um diretório.

        endswith()
            Verifica a extensão dos arquivos.

    """
    tipo = "."+tipo

    criaPastas()


    arquivos = os.listdir(
        PASTA_PDFS
    )


    print("\nARQUIVOS PDF\n")


    encontrou = False


    for arquivo in arquivos:

        if arquivo.lower().endswith(tipo): #tipo

            print(
                "-",
                arquivo
            )

            encontrou = True


    if not encontrou:

        print(
            "Nenhum PDF encontrado."
        )


# Exercício 6  
# Crie uma função que permita verificar se determinado arquivo PDF existe. 
# Caso o arquivo não exista, o programa deverá informar o usuário e impedir que as 
# demais operações sejam executadas sobre esse arquivo. 
 
# Exercício 7  
# Crie uma função que abra um arquivo PDF existente e apresente informações 
# básicas sobre ele. 
# O programa deverá apresentar pelo menos: 
# nome ou caminho do arquivo;  
# quantidade de páginas.  
 
# Exercício 8  
# Crie uma função que permita extrair o texto existente em um arquivo PDF. 
# O programa deverá percorrer todas as páginas e apresentar o conteúdo 
# encontrado, identificando o número de cada página. 
 
 
# Exercício 9  
# Crie uma função que permita procurar uma palavra ou expressão dentro de um 
# arquivo PDF. 
# O programa deverá informar em quais páginas o termo pesquisado foi encontrado. 
# A pesquisa deverá ignorar diferenças entre letras maiúsculas e minúsculas. 
 
# Exercício 10  
# Crie uma função que permita selecionar uma página específica de um arquivo 
# PDF e gerar um novo arquivo contendo somente essa página. 
# O usuário deverá informar: o arquivo PDF;  o número da página; o nome do novo 
# arquivo.  
 
# Exercício 11  
# Crie uma função que permita selecionar dois ou mais arquivos PDF e juntar todas 
# as páginas em um único arquivo PDF. 
# O usuário deverá informar os arquivos que deseja mesclar. 
# O programa deverá verificar se os arquivos existem e se possuem extensão .pdf. 
 
# Exercício 12  
# Crie uma função que gere automaticamente um certificado em PDF. 
# O usuário deverá informar: nome do participante; nome do curso;  carga horária; 
# data. O certificado deverá possuir uma apresentação visual organizada e ser salvo 
# na pasta de saída.  
 
# Exercício 13  
# Crie uma função que gere automaticamente um contrato de prestação de serviços 
# em PDF.O usuário deverá informar: nome do contratante;  nome do contratado; 
# descrição do serviço;  valor do contrato;  data.  
# O documento deverá apresentar as informações de maneira organizada e possuir 
# espaço para assinatura das partes. 
 
# Exercício 14  
# Crie uma função que permita configurar o caminho do executável do Tesseract. 
# Em seguida, crie uma função que permita selecionar uma imagem e realizar o 
# reconhecimento óptico dos caracteres presentes nela. 
# O texto reconhecido deverá ser apresentado na tela. 
 
# Exercício 15  
# Crie uma função que permita realizar OCR em um arquivo PDF. 
# O programa deverá transformar cada página do PDF em uma imagem e utilizar o 
# Tesseract para reconhecer o texto existente. 
# O resultado deverá ser apresentado na tela, identificando cada página. 
 
# Exercício 16  
# Crie uma função que verifique se um arquivo PDF possui proteção por senha. 
# A senha deverá ser obtida por meio de uma variável de ambiente  
# O programa não deverá armazenar a senha diretamente no código. 
# Caso o PDF esteja protegido, o programa deverá tentar realizar a descriptografia 
# utilizando a senha armazenada na variável de ambiente e informar se a senha foi 
# aceita ou recusada. 
 
# Exercício 17  
# Crie uma função que apresente as configurações relacionadas à variável de 
# ambiente utilizada pelo programa. 
# Por questões de segurança, a senha nunca deverá ser exibida. 
# O programa deverá informar somente se a variável PDF_SENHA está configurada 
# ou não.

while True:
    opcao=input("""
MENU DE OPÇÕES:
ººººººººººººººººººººººº
1- CRIAR AS PASTAS PARA OS EXERCÍCIOS
2- CRIAR UM ARQUIVO DE TEXTO                
3- LER O CONTEÚDO DE UM ARQUIVO
4-                 

\n-> DIGITE SUA OPÇÃO: """)
    match opcao:
        case "1":
            print("VAMOS CRIAR AS PASTAS PARA OS EXERCÍCIOS")
            criaPastas()
        case "5":
            listarArquivos("pdf")
        case "6":
            print("fim")