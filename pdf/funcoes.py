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

"""CONSTANTES PARA TODAS AS FUNÇÕES """
ARQUIVO_TESTE = "dados.txt"
PDFS = "pdfs"
SAIDA = "saida"
CERTIFICADO = "certificado.pdf"
CONTRATO = "contrato.pdf"

#CRIAR DENTRO DA PASTA DO EXERCÍCIO
DIRETORIOEXERCICIO = Path(__file__).resolve().parent #pasta do exercício [pdf]
# CERIFICADO = DIRETORIOEXERCICIO / CERTIFICADO
# CONTRATO = DIRETORIOEXERCICIO / CONTRATO
PASTA_PDFS = DIRETORIOEXERCICIO / PDFS 
PASTA_SAIDA = DIRETORIOEXERCICIO / SAIDA

#decorativos
LINHA="══════════════════════════"
LINHAZINHA="┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅"
OK="[✔]"
ERRO="[✕]"
ATENCAO="[⚠]"
LI="➤"
MUDOU="[⇄]"

## funções complementares para ajudar o usuário
def listDir(qual=False):
    if qual:
        listarDiretorio=DIRETORIOEXERCICIO / qual
    else:
        listarDiretorio=DIRETORIOEXERCICIO
        
    pastas = [item for item in listarDiretorio.iterdir() if item.is_dir()]
    
    
    if not pastas:
        input(f"{ERRO} Não há pastas neste diretório. Crie as pastas de teste usando a opção: 0 (ZERO):\n")
        return

    #
    print(f"Pastas do diretório: {qual if qual else 'Raiz'}")
    for pasta in pastas:
        print(f"{LI} [{pasta.name}]")

##criando as pastas

def criaPastas(qual=False):
    if qual:
        qual=qual.lower()
        if qual=="pdf":
            os.makedirs(PASTA_PDFS, exist_ok=True)
            print(f"{OK} Pasta {qual} criada!")
        elif qual=="txt":
            os.makedirs(PASTA_SAIDA, exist_ok=True)
            print(f"{OK} Pasta {qual} criada!")
        else:
            #qual=qual.upper()
            #qualPasta = qual
            os.makedirs(DIRETORIOEXERCICIO / qual, exist_ok=True)
            print(f"{OK} Pasta {qual} criada!")
    else:
        os.makedirs(PASTA_PDFS, exist_ok=True)
        os.makedirs(PASTA_SAIDA, exist_ok=True)
        print(f"{OK} Pastas criadas\n{LI}{PASTA_PDFS}\n{LI}{PASTA_SAIDA}\n")
    
    """ 
    CRIA DIRETÓRIOS - os.makedirs
    os.makedirs(NOME_DA_PASTA, exist_ok=True) - exist_ok=True Evita erro caso a pasta já exista.
    """


# Exercício 1  
# Crie uma função que permita ao usuário criar um novo arquivo de texto. 
# O usuário deverá informar o nome do arquivo e o conteúdo que será armazenado. 
# O arquivo deverá ser criado utilizando codificação UTF-8. 
def criarArquivo(nomeDoArquivo=False): #inserir variável para definir extensão
    if not nomeDoArquivo:
        nomeDoArquivo = input("Dê um nome para o arquivo de texto (.txt): ")

    if not nomeDoArquivo.endswith(".txt"): # .endswith() extensão do arquivo 
        nomeDoArquivo += ".txt" #SE NÃO ESTIVER, INSERE A EXTENSÃO
        nomeDoArquivo=DIRETORIOEXERCICIO / nomeDoArquivo 
    
    conteudo = input(f"Escreva algo no arquivo {nomeDoArquivo}: ")


    with open( nomeDoArquivo,"w", encoding="utf-8" ) as arquivo: #abre para escrita w = "write"

        arquivo.write(conteudo) #escreve efetivamente
        #conteudo = arquivo.read() #lê o conteúdo, depois de escrito, para confirmar se escreveu

    print(f"\n{OK} Arquivo criado com sucesso.")
    print(f"Conteúdo do arquivo:\n{conteudo}")
    
  
# Exercício 2  
# Crie uma função que permita abrir um arquivo de texto existente e apresentar seu 
# conteúdo na tela. 
# Antes de realizar a leitura, o programa deverá verificar se o arquivo existe. 
def lerArquivo(): 
    """
        open() - Abre o arquivo.
        read() - Lê todo o conteúdo.
    """

    nome = input("Informe o nome do arquivo de texto: ")
    if not nome.endswith(".txt"): # .endswith() extensão do arquivo 
            nome += ".txt"
    arquivo = DIRETORIOEXERCICIO / nome

    if not arquivo.exists():
        print(f"\n{ERRO}Arquivo [{nome}] não encontrado.")
        opcao=input("Deseja criar este arquivo? (s/n) ").strip()
        if opcao.lower()=="s":
            print(LINHAZINHA)
            criarArquivo(nomeDoArquivo=nome)
            return
        else:
            
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

        mode="a" = append()
            Abre o arquivo para adicionar conteúdo
            sem apagar o conteúdo existente.

    """

    nome = input("Diga o nome do arquivo no qual vai ser adicionado o conteúdo: ")
    
    if not os.path.exists(DIRETORIOEXERCICIO/nome): #verifica se o caminho e arquivo existem
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
    #listarArquivos(tipo=False,pasta=False)

    nome = input("Informe o nome do arquivo: ")


    if not os.path.exists(DIRETORIOEXERCICIO/nome):
        print(f"{ERRO} Arquivo não encontrado na pasta {DIRETORIOEXERCICIO}")
        return


    termo = input("Digite o trecho que deseja procurar: ")

    with open(nome,"r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    encontrado = False
    print("\nRESULTADOS\n")


    for numero, linha in enumerate(linhas,start=1): #numero é o índice

        if termo.lower() in linha.lower():

            print(f"Linha {numero}: {linha.strip()}")

            encontrado = True

    if not encontrado:

        print(F"O TRECHO {termo} FÃO FOI ENCONTRADO NO ARQUIVO {arquivo}.")

 
# Exercício 5  
# Crie uma função que liste todos os arquivos com extensão .pdf existentes em uma 
# pasta específica. 
# Caso a pasta não exista, ela deverá ser criada automaticamente. 
# Caso não existam arquivos PDF, o programa deverá informar ao usuário. 

def listarArquivos(tipo=False,pasta=False): #extensão (pdf / txt)
    if not pasta:
        pasta=DIRETORIOEXERCICIO
        
    """
    Lista os arquivos existentes na pasta.

    Utiliza:

        os.listdir()
            Lista os arquivos de um diretório.

        endswith()
            Verifica a extensão dos arquivos.

    """
    if tipo:
        tipo = "."+tipo.lower()
    
        if tipo==".pdf":
            pasta=PASTA_PDFS
    
            if not pasta:
                criaPastas(qual="pdfs")

            arquivos = os.listdir(PASTA_PDFS)
        
        if tipo==".txt":
            pasta=PASTA_SAIDA
    
            if not pasta:
                criaPastas(qual="txt")

            arquivos = os.listdir(PASTA_SAIDA)
    else:
        arquivos=os.listdir(pasta)


    print(f"\nARQUIVOS {tipo}\n")

    encontrou = False

    for arquivo in arquivos:
        i=1

        if arquivo.lower().endswith(tipo): #tipo    
            print(f" Nº {i}",arquivo)
            i+=1
            encontrou = True

    if not encontrou:
        print(f"Nenhum arquivo [{tipo.lower()}] encontrado NA PASTA [{pasta}].")


# Exercício 6  
# Crie uma função que permita verificar se determinado arquivo PDF existe. 
# Caso o arquivo não exista, o programa deverá informar o usuário e impedir que as 
# demais operações sejam executadas sobre esse arquivo. 

def procuraArquivo(tipo=False):
    listDir()
    
    qualPasta=input("Informe a pasta em que queres procurar o arquivo PDF:\n")
    qualPasta = DIRETORIOEXERCICIO / qualPasta
    if not qualPasta.exists() or not qualPasta.is_dir():
        print(f"A pasta {qualPasta} não foi encontrada")
        return
    
    qualArquivo=input("Informe o nome do arquivo PDF: ")
    if not qualArquivo.lower().endswith(".pdf"):
        qualArquivo += ".pdf"
        
    arquivo = qualPasta / qualArquivo

    if not arquivo.exists():
        print("Arquivo não encontrado.")
        return
    else:
        print(f"Arquivo {qualArquivo} encontrado")
        return arquivo
        
        
            
    
 
# Exercício 7  
# Crie uma função que abra um arquivo PDF existente e apresente informações 
# básicas sobre ele. 
# O programa deverá apresentar pelo menos: 
# nome ou caminho do arquivo;  
# quantidade de páginas.  
def verPdf(oq=False):
    """
    Mostra informações básicas de um PDF.

    Utiliza:

        PdfReader()
            Abre um arquivo PDF.

        len()
            Retorna a quantidade de páginas.

    """

    arquivo = procuraArquivo(tipo="pdf")
    #listDir(qual="pdfs")
    
    listarArquivos(tipo="pdf",pasta="pdfs")


    if arquivo is None: return


    leitor = PdfReader( arquivo )
    metaDados=None
    if not leitor.is_encrypted:
        metaDados = leitor.metadata
    else:
        input(f"{ATENCAO} ARQUIVO PROTEGIDO COM SENHA.\nNão é possível extrair informações dele\nUtilize a opção 16 para tentar quebrar a senha e ver os metadados.")
        return

    print(
        "\nINFORMAÇÕES DO PDF\n"
    )


    print("Arquivo:",arquivo)

    if metaDados:
            print(f"{LI} Título: {metaDados.title if metaDados.title else 'Não informado'}")
            print(f"{LI} Número de páginas: {len(leitor.pages) if leitor.pages else 'Sem páginas'}")
            print(f"{LI} Autor: {metaDados.author if metaDados.author else 'Não informado'}")
            print(f"{LI} Criador: {metaDados.creator if metaDados.creator else 'Não informado'}")
            print(f"{LI} Produtor: {metaDados.producer if metaDados.producer else 'Não informado'}")
    else:
        print(f"{ATENCAO} Nenhum metadado encontrado no arquivo.")
 
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
def criaCertificado():
    """
            reportlab
            Biblioteca para geração de PDF.

        canvas.Canvas()
            Cria um documento PDF a partir de medidas em cm usando
            padrões de iumpressão predefinidos.
            tamanhos de folhas (A4, A3, A2...)
            usa a propriedade Canvas, para delimitar largura, altura e posicionamentos .

        drawString()
            Escreve texto no documento.

    """

    nome = input("Informe o nome do participante: ").upper()

    curso = input("Informe um nome para o curso do certificado: ")

    carga_horaria = input(" Informe uma Carga Horária em horas: ")

    data = input("Data de emissão do certificado (dd/mm/aaaa): ")

    criaPastas()

    caminho = os.path.join(PASTA_PDFS,CERTIFICADO)

    documento = canvas.Canvas(caminho,pagesize=A4)

    largura, altura = A4
    #metadados do Canvas
    documento.setTitle(f"Certificado de {nome}")
    documento.setAuthor("SENAC RS")
    documento.setSubject(f"Certificado de conclusão do curso {curso}")
    documento.setCreator("A.C.M.E. Creator v1.0")

    documento.setFont("Helvetica-Bold", 28)
    documento.drawCentredString(largura / 2, altura - 150, "C E R T I F I C A D O")

    documento.setFont("Helvetica", 16)
    documento.drawCentredString(largura / 2, altura - 230, "Certificamos que")

    documento.setFont("Helvetica-Bold", 20)
    documento.drawCentredString(largura / 2, altura - 280, nome)

    documento.setFont("Helvetica", 16)
    documento.drawCentredString(largura / 2, altura - 340, f"concluiu o curso de {curso}")
    documento.drawCentredString(largura / 2, altura - 380, f"com carga horária de {carga_horaria} horas.")
    documento.drawCentredString(largura / 2, altura - 450, f"Data: {data}")


    documento.save()


    print("\nCertificado criado com sucesso")
    print(f"Arquivo: {CERTIFICADO}\nPasta: {PASTA_PDFS}\n{LINHA}")

 
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
def configuraTesseract(): ####????? muito complicado
    """
    Permite configurar manualmente o caminho
    do executável Tesseract.

    Utiliza:

        pytesseract.pytesseract.tesseract_cmd
            Define o caminho do Tesseract OCR.

    """
    caminho=DIRETORIOEXERCICIO
    caminho = input(
        "Caminho do Tesseract "
        "(ENTER para manter o padrão): "
    )


    if caminho != "":

        pytesseract.pytesseract.tesseract_cmd = caminho


    print(
        "Configuração do Tesseract concluída."
    )
 
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
def verificarSenhaPdf():
    """
    Exercício 16: Verifica se o PDF possui senha e tenta descriptografar
    usando uma variável de ambiente chamada 'PDF_SENHA'.
    """
    print(f"\n{LINHA}\n PROTEÇÃO POR SENHA? . . .\n{LINHA}")
    
    # Reutiliza a sua função de busca para pegar o arquivo
    arquivo = procuraArquivo(tipo="pdf")
    if arquivo is None: 
        return

    leitor = PdfReader(arquivo)

    # 1. Verifica se o PDF está criptografado
    if not leitor.is_encrypted:
        print(f"{OK} O arquivo [{arquivo.name}] NÃO possui proteção por senha.")
        return

    print(f"{ATENCAO} O arquivo [{arquivo.name}] ESTÁ protegido por senha.")
    print(f"{LI} Buscando senha na variável de ambiente...")

    # 2. Busca a senha na variável de ambiente (Não salva a senha direto no código)
    senha_ambiente = os.environ.get("PDF_SENHA")

    if not senha_ambiente:
        print(f"{ERRO} A variável de ambiente 'PDF_SENHA' não está configurada no sistema.")
        print(f"{ATENCAO} Não foi possível testar a descriptografia.")
        return

    # 3. Tenta realizar a descriptografia (decrypt)
    try:
        # O método decrypt retorna 0 se falhar ou um número > 0 (como 1 ou 2) se der certo
        resultado = leitor.decrypt(senha_ambiente)
        
        if resultado:
            print(f"{OK} Senha da variável de ambiente ACEITA com sucesso!")
            print(f"{LI} O arquivo foi descriptografado na memória e está pronto para leitura.")
        else:
            print(f"{ERRO} Senha da variável de ambiente RECUSADA (Senha incorreta).")
            
    except Exception as e:
        print(f"{ERRO} Ocorreu um erro ao tentar descriptografar: {e}")
 
# Exercício 17  
# Crie uma função que apresente as configurações relacionadas à variável de 
# ambiente utilizada pelo programa. 
# Por questões de segurança, a senha nunca deverá ser exibida. 
# O programa deverá informar somente se a variável PDF_SENHA está configurada 
# ou não.
