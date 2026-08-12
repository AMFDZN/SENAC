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


ARQUIVO_TEXTO = "dados.txt"

PASTA_PDFS = "pdfs"

PASTA_SAIDA = "saida"

ARQUIVO_CERTIFICADO = "certificado.pdf"

ARQUIVO_CONTRATO = "contrato.pdf"


def criar_pastas():
    """
    Cria as pastas utilizadas pelo programa.

    Utiliza:

        os.makedirs()
            Cria diretórios.

        exist_ok=True
            Evita erro caso a pasta já exista.
    """

    os.makedirs( PASTA_PDFS,
        exist_ok=True
    )

    os.makedirs(
        PASTA_SAIDA,
        exist_ok=True
    )


def criar_arquivo_texto():
    """
    Cria um novo arquivo de texto.

    Utiliza:

        open()
            Abre ou cria um arquivo.

        mode="w"
            Permite escrever no arquivo.

        encoding="utf-8"
            Permite trabalhar com acentos.

    """

    nome = input(
        "Nome do arquivo: "
    )


    if not nome.endswith(".txt"):

        nome += ".txt"


    conteudo = input(
        "Digite o conteúdo: "
    )


    with open(
        nome,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            conteudo
        )


    print(
        "\nArquivo criado com sucesso."
    )


def ler_arquivo_texto():
    """
    Lê o conteúdo de um arquivo de texto.

    Utiliza:

        open()
            Abre o arquivo.

        read()
            Lê todo o conteúdo.

    """

    nome = input(
        "Nome do arquivo: "
    )


    if not os.path.exists(nome):

        print(
            "Arquivo não encontrado."
        )

        return


    with open(
        nome,
        "r",
        encoding="utf-8"
    ) as arquivo:

        conteudo = arquivo.read()


    print(
        "\nCONTEÚDO DO ARQUIVO\n"
    )

    print(conteudo)


def adicionar_texto():
    """
    Adiciona conteúdo ao final de um arquivo de texto.

    Utiliza:

        mode="a"
            Abre o arquivo para adicionar conteúdo
            sem apagar o conteúdo existente.

    """

    nome = input(
        "Nome do arquivo: "
    )


    if not os.path.exists(nome):

        print(
            "Arquivo não encontrado."
        )

        return


    texto = input(
        "Texto que deseja adicionar: "
    )


    with open(
        nome,
        "a",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "\n" + texto
        )


    print(
        "Texto adicionado com sucesso."
    )


def procurar_texto():
    """
    Procura uma informação específica
    dentro de um arquivo de texto.

    Utiliza:

        in
            Verifica se um texto existe dentro de outro.

    """

    nome = input(
        "Nome do arquivo: "
    )


    if not os.path.exists(nome):

        print(
            "Arquivo não encontrado."
        )

        return


    termo = input(
        "Digite o termo que deseja procurar: "
    )


    with open(
        nome,
        "r",
        encoding="utf-8"
    ) as arquivo:

        linhas = arquivo.readlines()


    encontrado = False


    print(
        "\nRESULTADOS\n"
    )


    for numero, linha in enumerate(
        linhas,
        start=1
    ):

        if termo.lower() in linha.lower():

            print(
                f"Linha {numero}: {linha.strip()}"
            )

            encontrado = True


    if not encontrado:

        print(
            "Nenhuma ocorrência encontrada."
        )


def listar_pdfs():
    """
    Lista os arquivos PDF existentes na pasta.

    Utiliza:

        os.listdir()
            Lista os arquivos de um diretório.

        endswith()
            Verifica a extensão do arquivo.

    """

    criar_pastas()


    arquivos = os.listdir(
        PASTA_PDFS
    )


    print(
        "\nARQUIVOS PDF\n"
    )


    encontrou = False


    for arquivo in arquivos:

        if arquivo.lower().endswith(".pdf"):

            print(
                "-",
                arquivo
            )

            encontrou = True


    if not encontrou:

        print(
            "Nenhum PDF encontrado."
        )


def verificar_pdf():
    """
    Verifica se um arquivo PDF existe.

    Retorno:

        True:
            Arquivo encontrado.

        False:
            Arquivo inexistente.
    """

    arquivo = input(
        "Informe o caminho do PDF: "
    )


    if not os.path.exists(arquivo):

        print(
            "PDF não encontrado."
        )

        return None


    return arquivo


def mostrar_informacoes_pdf():
    """
    Mostra informações básicas de um PDF.

    Utiliza:

        PdfReader()
            Abre um arquivo PDF.

        len()
            Retorna a quantidade de páginas.

    """

    arquivo = verificar_pdf()


    if arquivo is None:

        return


    leitor = PdfReader( arquivo )


    print(
        "\nINFORMAÇÕES DO PDF\n"
    )


    print(
        "Arquivo:",
        arquivo
    )


    print(
        "Quantidade de páginas:",
        len(leitor.pages)
    )


def extrair_texto_pdf():
    """
    Extrai texto de um arquivo PDF.

    Utiliza:

        pdfplumber.open()
            Abre o PDF.

        extract_text()
            Extrai o texto de uma página.

    """

    arquivo = verificar_pdf()


    if arquivo is None:

        return


    with pdfplumber.open(arquivo) as pdf:

        print(
            "\nTEXTO EXTRAÍDO\n"
        )


        for numero, pagina in enumerate(pdf.pages,start=1):

            texto = pagina.extract_text()


            print(
                f"\n--- PÁGINA {numero} ---\n"
            )


            if texto:

                print(texto)

            else:

                print(
                    "Nenhum texto encontrado."
                )


def extrair_informacao_pdf():
    """
    Procura uma informação específica
    dentro de um PDF.

    Utiliza:

        extract_text()
            Obtém o texto de cada página.

        lower()
            Facilita a comparação sem diferenciar
            letras maiúsculas e minúsculas.

    """

    arquivo = verificar_pdf()


    if arquivo is None:

        return


    termo = input(
        "Informação que deseja procurar: "
    )


    encontrado = False


    with pdfplumber.open(
        arquivo
    ) as pdf:

        for numero, pagina in enumerate(
            pdf.pages,
            start=1
        ):

            texto = pagina.extract_text()


            if not texto:

                continue


            if termo.lower() in texto.lower():

                print(
                    f"\nEncontrado na página {numero}."
                )


                encontrado = True


    if not encontrado:

        print(
            "Informação não encontrada."
        )


def extrair_pagina_pdf():
    """
    Extrai uma página específica de um PDF.

    Utiliza:

        PdfWriter()
            Cria um novo documento PDF.

        add_page()
            Adiciona uma página ao novo documento.

    """

    arquivo = verificar_pdf()


    if arquivo is None:

        return


    leitor = PdfReader(
        arquivo
    )


    pagina = int(
        input(
            "Número da página: "
        )
    )


    if pagina < 1 or pagina > len(leitor.pages):

        print(
            "Página inexistente."
        )

        return


    escritor = PdfWriter()


    escritor.add_page(
        leitor.pages[pagina - 1]
    )


    nome_saida = input(
        "Nome do novo PDF: "
    )


    if not nome_saida.endswith(".pdf"):

        nome_saida += ".pdf"


    with open(
        nome_saida,
        "wb"
    ) as arquivo_saida:

        escritor.write(
            arquivo_saida
        )


    print(
        "Página extraída com sucesso."
    )


def mesclar_pdfs():
    """
    Mescla vários arquivos PDF em um único documento.

    Utiliza:

        PdfWriter()
            Cria o documento final.

        append_pages_from_reader()
            Adiciona as páginas de outro PDF.

    """

    criar_pastas()


    arquivos = []


    print(
        "\nDigite os caminhos dos PDFs."
    )

    print(
        "Digite ENTER vazio para finalizar."
    )


    while True:

        caminho = input(
            "PDF: "
        )


        if caminho == "":

            break


        if not os.path.exists(caminho):

            print(
                "Arquivo não encontrado."
            )

            continue


        if not caminho.lower().endswith(".pdf"):

            print(
                "Informe um arquivo PDF."
            )

            continue


        arquivos.append(
            caminho
        )


    if len(arquivos) < 2:

        print(
            "É necessário informar pelo menos dois PDFs."
        )

        return


    escritor = PdfWriter()


    for caminho in arquivos:

        leitor = PdfReader(
            caminho
        )


        for pagina in leitor.pages:

            escritor.add_page(
                pagina
            )


    nome_saida = input(
        "Nome do PDF final: "
    )


    if not nome_saida.endswith(".pdf"):

        nome_saida += ".pdf"


    with open(
        nome_saida,
        "wb"
    ) as arquivo_saida:

        escritor.write(
            arquivo_saida
        )


    print(
        "PDFs mesclados com sucesso."
    )


def criar_certificado():
    """
    Gera um certificado PDF automaticamente.

    Utiliza:

        reportlab
            Biblioteca para geração de PDF.

        canvas.Canvas()
            Cria um documento PDF.

        drawString()
            Escreve texto no documento.

    """

    nome = input(
        "Nome do participante: "
    )


    curso = input(
        "Nome do curso: "
    )


    carga_horaria = input(
        "Carga horária: "
    )


    data = input(
        "Data: "
    )


    criar_pastas()


    caminho = os.path.join(
        PASTA_SAIDA,
        ARQUIVO_CERTIFICADO
    )


    documento = canvas.Canvas(
        caminho,
        pagesize=A4
    )


    largura, altura = A4


    documento.setFont(
        "Helvetica-Bold",
        28
    )


    documento.drawCentredString(
        largura / 2,
        altura - 150,
        "CERTIFICADO"
    )


    documento.setFont(
        "Helvetica",
        16
    )


    documento.drawCentredString(
        largura / 2,
        altura - 230,
        "Certificamos que"
    )


    documento.setFont(
        "Helvetica-Bold",
        20
    )


    documento.drawCentredString(
        largura / 2,
        altura - 280,
        nome
    )


    documento.setFont(
        "Helvetica",
        16
    )


    documento.drawCentredString(
        largura / 2,
        altura - 340,
        f"concluiu o curso de {curso}"
    )


    documento.drawCentredString(
        largura / 2,
        altura - 380,
        f"com carga horária de {carga_horaria} horas."
    )


    documento.drawCentredString(
        largura / 2,
        altura - 450,
        f"Data: {data}"
    )


    documento.save()


    print(
        "\nCertificado criado com sucesso."
    )


    print(
        "Arquivo:",
        caminho
    )


def criar_contrato():
    """
    Gera um contrato PDF padronizado.

    Utiliza:

        reportlab
            Cria documentos PDF.

        textobject
            Permite escrever várias linhas.

    """

    contratante = input(
        "Nome do contratante: "
    )


    contratado = input(
        "Nome do contratado: "
    )


    servico = input(
        "Descrição do serviço: "
    )


    valor = input(
        "Valor do contrato: "
    )


    data = input(
        "Data: "
    )


    criar_pastas()


    caminho = os.path.join(
        PASTA_SAIDA,
        ARQUIVO_CONTRATO
    )


    documento = canvas.Canvas(
        caminho,
        pagesize=A4
    )


    largura, altura = A4


    documento.setFont(
        "Helvetica-Bold",
        18
    )


    documento.drawCentredString(
        largura / 2,
        altura - 80,
        "CONTRATO DE PRESTAÇÃO DE SERVIÇOS"
    )


    texto = documento.beginText(
        60,
        altura - 130
    )


    texto.setFont(
        "Helvetica",
        11
    )


    linhas = [

        f"CONTRATANTE: {contratante}",

        f"CONTRATADO: {contratado}",

        "",

        "1. DO OBJETO",

        f"O presente contrato tem como objeto: {servico}.",

        "",

        "2. DO VALOR",

        f"O valor acordado para o serviço é de R$ {valor}.",

        "",

        "3. DAS OBRIGAÇÕES",

        "As partes comprometem-se a cumprir as condições",

        "estabelecidas neste contrato.",

        "",

        "4. DA DATA",

        f"Este documento foi elaborado em {data}.",

        "",

        "________________________________________",

        f"{contratante}",

        "",

        "________________________________________",

        f"{contratado}"

    ]


    for linha in linhas:

        texto.textLine(
            linha
        )


    documento.drawText(
        texto
    )


    documento.save()


    print(
        "\nContrato criado com sucesso."
    )


    print(
        "Arquivo:",
        caminho
    )


def configurar_tesseract():
    """
    Permite configurar manualmente o caminho
    do executável Tesseract.

    Utiliza:

        pytesseract.pytesseract.tesseract_cmd
            Define o caminho do Tesseract OCR.

    """

    caminho = input(
        "Caminho do Tesseract "
        "(ENTER para manter o padrão): "
    )


    if caminho != "":

        pytesseract.pytesseract.tesseract_cmd = caminho


    print(
        "Configuração do Tesseract concluída."
    )


def realizar_ocr():
    """
    Realiza OCR em uma imagem.

    OCR significa:

        Optical Character Recognition
        Reconhecimento Óptico de Caracteres.

    Utiliza:

        PIL.Image.open()
            Abre a imagem.

        pytesseract.image_to_string()
            Reconhece o texto da imagem.

    """

    arquivo = input(
        "Caminho da imagem: "
    )


    if not os.path.exists(arquivo):

        print(
            "Imagem não encontrada."
        )

        return


    try:

        imagem = Image.open(
            arquivo
        )


        texto = pytesseract.image_to_string(
            imagem,
            lang="por"
        )


        print(
            "\nTEXTO RECONHECIDO\n"
        )


        print(texto)


    except Exception as erro:

        print(
            "Erro durante o OCR:"
        )

        print(erro)


def extrair_ocr_pdf():
    """
    Realiza OCR nas páginas de um PDF
    transformando cada página em imagem.

    Observação:

        Essa abordagem é útil para PDFs digitalizados,
        nos quais não existe texto selecionável.

    """

    arquivo = verificar_pdf()


    if arquivo is None:

        return


    try:

        import fitz

    except ImportError:

        print(
            "Instale PyMuPDF para utilizar esta função."
        )

        print(
            "Comando: pip install pymupdf"
        )

        return


    documento = fitz.open(
        arquivo
    )


    print(
        "\nTEXTO OCR DO PDF\n"
    )


    for numero, pagina in enumerate(
        documento,
        start=1
    ):

        imagem = pagina.get_pixmap()


        imagem_pil = Image.frombytes(
            "RGB",
            [
                imagem.width,
                imagem.height
            ],
            imagem.samples
        )


        texto = pytesseract.image_to_string(
            imagem_pil,
            lang="por"
        )


        print(
            f"\n--- PÁGINA {numero} ---\n"
        )


        print(texto)


def ler_senha_ambiente():
    """
    Obtém uma senha armazenada em variável de ambiente.

    Utiliza:

        os.getenv()
            Obtém valores das variáveis de ambiente.

    Segurança:

        A senha não fica escrita diretamente no código.

    Exemplo de variável:

        PDF_SENHA

    """

    senha = os.getenv(
        "PDF_SENHA"
    )


    if senha is None:

        print(
            "A variável PDF_SENHA não foi configurada."
        )

        return None


    print(
        "Senha encontrada na variável de ambiente."
    )


    return senha


def verificar_senha_pdf():
    """
    Verifica se um PDF possui senha
    utilizando uma variável de ambiente.

    Utiliza:

        PdfReader()
            Abre o PDF.

        is_encrypted
            Verifica se o documento está protegido.

        decrypt()
            Tenta desbloquear o documento.

    """

    arquivo = verificar_pdf()


    if arquivo is None:

        return


    leitor = PdfReader(
        arquivo
    )


    if not leitor.is_encrypted:

        print(
            "Este PDF não possui senha."
        )

        return


    senha = ler_senha_ambiente()


    if senha is None:

        return


    resultado = leitor.decrypt(
        senha
    )


    if resultado:

        print(
            "Senha aceita. PDF desbloqueado."
        )

    else:

        print(
            "Senha incorreta."
        )


def mostrar_variaveis_ambiente():
    """
    Mostra informações sobre variáveis de ambiente
    utilizadas pelo programa.

    Importante:

        O valor da senha nunca é exibido.

    """

    senha = os.getenv(
        "PDF_SENHA"
    )


    print(
        "\nCONFIGURAÇÕES\n"
    )


    if senha:

        print(
            "PDF_SENHA: configurada"
        )

    else:

        print(
            "PDF_SENHA: não configurada"
        )


def menu():
    """
    Exibe o menu principal do programa.

    O menu reúne todas as funcionalidades
    de manipulação de arquivos, PDFs, OCR
    e segurança.
    """

    while True:

        print(
            """
            


Arquivos de texto

1  - Criar arquivo de texto
2  - Ler arquivo de texto
3  - Adicionar texto
4  - Procurar informação no texto

PDF

5  - Listar PDFs
6  - Informações do PDF
7  - Extrair texto do PDF
8  - Procurar informação no PDF
9  - Extrair página do PDF
10 - Mesclar PDFs

Documentos automáticos

11 - Gerar certificado
12 - Gerar contrato

OCR

13 - Configurar Tesseract
14 - Realizar OCR em imagem
15 - Realizar OCR em PDF

Segurança

16 - Verificar senha do PDF
17 - Mostrar configurações

0  - Sair

"""
        )


        opcao = input(
            "Escolha uma opção: "
        )


        match opcao:

            case "1":

                criar_arquivo_texto()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "2":

                ler_arquivo_texto()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "3":

                adicionar_texto()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "4":

                procurar_texto()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "5":

                listar_pdfs()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "6":

                mostrar_informacoes_pdf()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "7":

                extrair_texto_pdf()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "8":

                extrair_informacao_pdf()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "9":

                extrair_pagina_pdf()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "10":

                mesclar_pdfs()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "11":

                criar_certificado()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "12":

                criar_contrato()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "13":

                configurar_tesseract()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "14":

                realizar_ocr()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "15":

                extrair_ocr_pdf()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "16":

                verificar_senha_pdf()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "17":

                mostrar_variaveis_ambiente()

                input(
                    "Pressione Enter para voltar ao menu."
                )


            case "0":

                print(
                    "Programa encerrado."
                )

                break


            case _:

                print(
                    "Opção inválida."
                )

                input(
                    "Pressione Enter para voltar ao menu."
                )


if __name__ == "__main__":

    menu()