import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter
import pdfplumber
import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ==========================================
# CONSTANTES E DIRETÓRIOS DO PROJETO
# ==========================================
DIRETORIO_EXERCICIO = Path(__file__).resolve().parent
PASTA_TXTS = DIRETORIO_EXERCICIO / "txts"
PASTA_PDFS = DIRETORIO_EXERCICIO / "pdfs"
PASTA_SAIDA = DIRETORIO_EXERCICIO / "saida"

# Elementos visuais para formatação no console
LINHA = "══════════════════════════"
LINHAZINHA = "┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅"
OK = "[✔]"
ERRO = "[✕]"
ATENCAO = "[⚠]"
LI = "➤"


# ==========================================
# FUNÇÕES AUXILIARES / SUPORTE
# ==========================================

def criarPastas():
    """Cria as pastas 'txts', 'pdfs' e 'saida' caso não existam."""
    try:
        os.makedirs(PASTA_TXTS, exist_ok=True)
        os.makedirs(PASTA_PDFS, exist_ok=True)
        os.makedirs(PASTA_SAIDA, exist_ok=True)
        print(f"{OK} Pastas '{PASTA_TXTS.name}', '{PASTA_PDFS.name}' e '{PASTA_SAIDA.name}' prontas!")
    except Exception as e:
        print(f"{ERRO} Erro ao criar pastas: {e}")


def listarArquivosNaPasta(pasta: Path, extensao: str):
    """Lista todos os arquivos de uma determinada extensão dentro da pasta informada."""
    if not pasta.exists():
        return []
    
    arquivos = []
    for item in os.listdir(pasta):
        if item.lower().endswith(extensao.lower()):
            arquivos.append(item)
    return arquivos


def verificarTxt():
    """Auxilia o usuário a localizar e escolher um arquivo TXT, listando a pasta."""
    criarPastas()
    arquivos = listarArquivosNaPasta(PASTA_TXTS, ".txt")
    
    print(f"\n--- PASTA DE TEXTOS: [{PASTA_TXTS.name}] ---")
    if arquivos:
        print("Arquivos disponíveis:")
        for arq in arquivos:
            print(f"  {LI} {arq}")
    else:
        print(f"{ATENCAO} Nenhum arquivo .txt encontrado nesta pasta.")

    entrada = input("\nDigite o nome do arquivo de texto: ").strip()
    if not entrada:
        return None

    caminho = Path(entrada)
    if not caminho.is_absolute() and not caminho.exists():
        caminho = PASTA_TXTS / entrada

    if not str(caminho).lower().endswith(".txt"):
        caminho = Path(str(caminho) + ".txt")

    if not caminho.exists():
        print(f"{ERRO} O arquivo de texto não foi encontrado em: {caminho}")
        return None

    return str(caminho)


def verificarPdf():
    """Auxilia o usuário a localizar e escolher um arquivo PDF, listando a pasta."""
    criarPastas()
    arquivos = listarArquivosNaPasta(PASTA_PDFS, ".pdf")
    
    print(f"\n--- PASTA DE PDFs: [{PASTA_PDFS.name}] ---")
    if arquivos:
        print("Arquivos disponíveis:")
        for arq in arquivos:
            print(f"  {LI} {arq}")
    else:
        print(f"{ATENCAO} Nenhum arquivo .pdf encontrado nesta pasta.")

    entrada = input("\nDigite o nome ou caminho do arquivo PDF: ").strip()
    if not entrada:
        return None

    caminho = Path(entrada)
    if not caminho.is_absolute() and not caminho.exists():
        caminho = PASTA_PDFS / entrada

    if not str(caminho).lower().endswith(".pdf"):
        caminho = Path(str(caminho) + ".pdf")

    if not caminho.exists():
        print(f"{ERRO} O arquivo PDF não foi encontrado em: {caminho}")
        return None

    return str(caminho)


# ==========================================
# EXERCÍCIOS DE ARQUIVOS DE TEXTO (.txt)
# ==========================================

def criarArquivoTexto():
    """Cria um novo arquivo de texto dentro da pasta 'txts'."""
    criarPastas()
    nome = input("Nome do arquivo de texto: ").strip()
    if not nome:
        print(f"{ERRO} Nome inválido.")
        return
        
    if not nome.endswith(".txt"):
        nome += ".txt"
        
    caminho = PASTA_TXTS / nome
    conteudo = input("Digite o conteúdo que será armazenado: ")

    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print(f"\n{OK} Arquivo '{caminho.name}' criado com sucesso na pasta '{PASTA_TXTS.name}'!")
    except Exception as e:
        print(f"{ERRO} Ocorreu um erro ao criar o arquivo: {e}")


def lerArquivoTexto():
    """Lê o conteúdo de um arquivo de texto existente."""
    caminho = verificarTxt()
    if not caminho:
        return

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        print(f"\n--- CONTEÚDO DO ARQUIVO [{Path(caminho).name}] ---\n")
        print(conteudo)
    except Exception as e:
        print(f"{ERRO} Erro ao ler o arquivo: {e}")


def adicionarTexto():
    """Adiciona novas informações ao final do arquivo de texto."""
    caminho = verificarTxt()
    if not caminho:
        return

    textoNovo = input("Texto que deseja adicionar ao final: ")

    try:
        with open(caminho, "a", encoding="utf-8") as arquivo:
            arquivo.write("\n" + textoNovo)
        print(f"{OK} Texto adicionado com sucesso!")
    except Exception as e:
        print(f"{ERRO} Erro ao modificar o arquivo: {e}")


def procurarTexto():
    """Procura um termo no arquivo de texto."""
    caminho = verificarTxt()
    if not caminho:
        return

    termo = input("Digite o termo que deseja procurar: ")

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        print(f"\n--- RESULTADOS DA BUSCA POR '{termo}' ---\n")
        for numero, linha in enumerate(linhas, start=1):
            if termo.lower() in linha.lower():
                print(f"Linha {numero}: {linha.strip()}")
                encontrado = True

        if not encontrado:
            print("Nenhuma ocorrência encontrada para este termo.")
    except Exception as e:
        print(f"{ERRO} Erro durante a busca: {e}")


# ==========================================
# EXERCÍCIOS DE MANIPULAÇÃO E LEITURA DE PDF
# ==========================================

def listarPdfs():
    """Lista todos os arquivos .pdf existentes na pasta 'pdfs'."""
    criarPastas()
    try:
        arquivos = listarArquivosNaPasta(PASTA_PDFS, ".pdf")
        print(f"\n--- ARQUIVOS PDF EM [{PASTA_PDFS.name}] ---\n")
        
        if arquivos:
            for arquivo in arquivos:
                print(f"{LI} {arquivo}")
        else:
            print("Nenhum arquivo PDF encontrado na pasta.")
    except Exception as e:
        print(f"{ERRO} Erro ao listar diretório: {e}")


def procurarArquivoPdf():
    """Verifica se determinado arquivo PDF existe."""
    caminho = verificarPdf()
    if caminho:
        print(f"{OK} O arquivo PDF existe e está acessível: {caminho}")
    return caminho


def mostrarInformacoesPdf():
    """Exibe informações básicas e metadados detalhados de um PDF."""
    caminho = verificarPdf()
    if not caminho:
        return

    try:
        leitor = PdfReader(caminho)
        meta = leitor.metadata
        
        print(f"\n--- INFORMAÇÕES E METADADOS DO PDF ---\n")
        print(f"{LI} Arquivo: {os.path.basename(caminho)}")
        print(f"{LI} Quantidade de páginas: {len(leitor.pages)}")
        
        if meta:
            print(f"{LI} Título: {meta.title if meta.title else 'Não informado'}")
            print(f"{LI} Autor: {meta.author if meta.author else 'Não informado'}")
            print(f"{LI} Assunto: {meta.subject if meta.subject else 'Não informado'}")
            print(f"{LI} Criador: {meta.creator if meta.creator else 'Não informado'}")
            print(f"{LI} Produtor: {meta.producer if meta.producer else 'Não informado'}")
        else:
            print(f"{ATENCAO} Este arquivo não possui metadados embutidos.")
    except Exception as e:
        print(f"{ERRO} Erro ao extrair informações do PDF: {e}")


def extrairTextoPdf():
    """Extrai e exibe o texto de todas as páginas de um PDF."""
    caminho = verificarPdf()
    if not caminho:
        return

    try:
        with pdfplumber.open(caminho) as pdf:
            print(f"\n--- TEXTO EXTRAÍDO DO PDF ---\n")
            for numero, pagina in enumerate(pdf.pages, start=1):
                texto = pagina.extract_text()
                print(f"\n[ PÁGINA {numero} ]\n")
                if texto:
                    print(texto)
                else:
                    print("(Página sem texto reconhecível)")
    except Exception as e:
        print(f"{ERRO} Erro ao extrair texto do PDF: {e}")


def procurarEmPdf():
    """Procura uma palavra ou expressão dentro de um PDF."""
    caminho = verificarPdf()
    if not caminho:
        return

    termo = input("Digite a palavra ou expressão que deseja procurar no PDF: ")
    encontrado = False

    try:
        with pdfplumber.open(caminho) as pdf:
            print(f"\n--- RESULTADO DA BUSCA POR '{termo}' ---\n")
            for numero, pagina in enumerate(pdf.pages, start=1):
                texto = pagina.extract_text()
                if texto and termo.lower() in texto.lower():
                    print(f"{OK} O termo foi encontrado na página {numero}.")
                    encontrado = True

        if not encontrado:
            print("O termo pesquisado não foi encontrado em nenhuma página deste PDF.")
    except Exception as e:
        print(f"{ERRO} Erro ao realizar a busca no PDF: {e}")


def extrairPaginaPdf():
    """Extrai uma página específica de um PDF e salva na pasta de saída."""
    caminho = verificarPdf()
    if not caminho:
        return

    try:
        leitor = PdfReader(caminho)
        totalPaginas = len(leitor.pages)
        
        paginaNum = int(input(f"Informe o número da página que deseja extrair (1 a {totalPaginas}): "))
        
        if paginaNum < 1 or paginaNum > totalPaginas:
            print(f"{ERRO} Número de página inválido.")
            return

        escritor = PdfWriter()
        escritor.add_page(leitor.pages[paginaNum - 1])

        nomeSaida = input("Informe o nome do novo arquivo PDF gerado: ").strip()
        if not nomeSaida.endswith(".pdf"):
            nomeSaida += ".pdf"
            
        caminhoSaida = PASTA_SAIDA / nomeSaida
        criarPastas()

        with open(caminhoSaida, "wb") as arquivoSaida:
            escritor.write(arquivoSaida)

        print(f"\n{OK} Página extraída com sucesso em: {caminhoSaida}")
    except ValueError:
        print(f"{ERRO} Digite um número inteiro válido.")
    except Exception as e:
        print(f"{ERRO} Erro ao extrair a página: {e}")


def mesclarPdfs():
    """Mescla múltiplos PDFs da pasta de PDFs."""
    criarPastas()
    arquivos = []
    
    print("\nInforme os nomes dos PDFs que deseja mesclar.")
    print("Pressione ENTER sem digitar nada para finalizar a lista.")
    
    while True:
        caminho = verificarPdf() if False else input("PDF (ou ENTER para encerrar): ").strip()
        if caminho == "":
            break
            
        caminhoObj = Path(caminho)
        if not caminhoObj.exists() and (PASTA_PDFS / caminho).exists():
            caminhoObj = PASTA_PDFS / caminho
        elif not str(caminhoObj).lower().endswith(".pdf"):
            caminhoObj = Path(str(caminhoObj) + ".pdf")

        if caminhoObj.exists():
            arquivos.append(str(caminhoObj))
            print(f"  {OK} Adicionado à lista.")
        else:
            print(f"  {ERRO} Arquivo não encontrado.")

    if len(arquivos) < 2:
        print(f"{ATENCAO} É necessário informar pelo menos dois PDFs válidos para mesclar.")
        return

    try:
        escritor = PdfWriter()
        for arq in arquivos:
            leitor = PdfReader(arq)
            for pagina in leitor.pages:
                escritor.add_page(pagina)

        nomeSaida = input("Nome do arquivo PDF mesclado final: ").strip()
        if not nomeSaida.endswith(".pdf"):
            nomeSaida += ".pdf"
            
        caminhoFinal = PASTA_SAIDA / nomeSaida

        with open(caminhoFinal, "wb") as saida:
            escritor.write(saida)

        print(f"\n{OK} PDFs mesclados com sucesso em: {caminhoFinal}")
    except Exception as e:
        print(f"{ERRO} Erro ao mesclar os arquivos: {e}")


# ==========================================
# EXERCÍCIOS DE GERAÇÃO DE DOCUMENTOS (REPORTLAB)
# ==========================================

def criarCertificado():
    """Gera um certificado em PDF com metadados configurados."""
    nome = input("Nome do participante: ").upper()
    curso = input("Nome do curso: ")
    cargaHoraria = input("Carga horária (ex: 40): ")
    data = input("Data de emissão (dd/mm/aaaa): ")

    criarPastas()
    caminho = PASTA_SAIDA / "certificado.pdf"

    try:
        documento = canvas.Canvas(str(caminho), pagesize=A4)
        
        # Adicionando Metadados ao criar o PDF
        documento.setTitle(f"Certificado - {nome}")
        documento.setAuthor("Sistema de Automação de Certificados")
        documento.setSubject(f"Certificado de conclusão do curso {curso}")
        documento.setCreator("Python ReportLab")

        largura, altura = A4

        documento.setFont("Helvetica-Bold", 28)
        documento.drawCentredString(largura / 2, altura - 150, "CERTIFICADO")

        documento.setFont("Helvetica", 16)
        documento.drawCentredString(largura / 2, altura - 230, "Certificamos que")

        documento.setFont("Helvetica-Bold", 20)
        documento.drawCentredString(largura / 2, altura - 280, nome)

        documento.setFont("Helvetica", 16)
        documento.drawCentredString(largura / 2, altura - 340, f"concluiu com êxito o curso de {curso}")
        documento.drawCentredString(largura / 2, altura - 380, f"com carga horária total de {cargaHoraria} horas.")
        documento.drawCentredString(largura / 2, altura - 450, f"Data de emissão: {data}")

        documento.save()
        print(f"\n{OK} Certificado gerado com sucesso na pasta 'saida': {caminho.name}")
    except Exception as e:
        print(f"{ERRO} Erro ao gerar o certificado: {e}")


def criarContrato():
    """Gera um contrato em PDF com metadados configurados."""
    contratante = input("Nome do Contratante: ")
    contratado = input("Nome do Contratado: ")
    servico = input("Descrição resumida do serviço: ")
    valor = input("Valor acordado do contrato (R$): ")
    data = input("Data do contrato: ")

    criarPastas()
    caminho = PASTA_SAIDA / "contrato.pdf"

    try:
        documento = canvas.Canvas(str(caminho), pagesize=A4)
        
        # Adicionando Metadados ao criar o PDF
        documento.setTitle(f"Contrato de Prestação de Serviços - {contratante}")
        documento.setAuthor(contratado)
        documento.setSubject("Contrato comercial padronizado")
        documento.setCreator("Python ReportLab")

        largura, altura = A4

        documento.setFont("Helvetica-Bold", 16)
        documento.drawCentredString(largura / 2, altura - 60, "CONTRATO DE PRESTAÇÃO DE SERVIÇOS")

        texto = documento.beginText(50, altura - 110)
        texto.setFont("Helvetica", 10)

        linhas = [
            f"CONTRATANTE: {contratante}",
            f"CONTRATADO: {contratado}",
            "",
            "1. DO OBJETO DO CONTRATO",
            f"O presente contrato tem por objeto a prestação dos seguintes serviços: {servico}.",
            "",
            "2. DO VALOR E FORMA DE PAGAMENTO",
            f"Pelos serviços prestados, o contratante pagará ao contratado o valor total de R$ {valor}.",
            "",
            "3. DAS DISPOSIÇÕES GERAIS",
            "As partes comprometem-se a cumprir rigorosamente com as obrigações estipuladas.",
            "",
            f"Firmado em: {data}",
            "",
            "",
            "________________________________________      ________________________________________",
            f"          {contratante}                                   {contratado}"
        ]

        for linha in linhas:
            texto.textLine(linha)

        documento.drawText(texto)
        documento.save()
        print(f"\n{OK} Contrato gerado com sucesso na pasta 'saida': {caminho.name}")
    except Exception as e:
        print(f"{ERRO} Erro ao gerar o contrato: {e}")


# ==========================================
# EXERCÍCIOS DE OCR E RECONHECIMENTO DE IMAGEM
# ==========================================

def configurarTesseract():
    """Configura o caminho do executável do Tesseract."""
    caminho = input("Informe o caminho completo do executável do Tesseract (ou ENTER para padrão): ").strip()
    if caminho:
        pytesseract.pytesseract.tesseract_cmd = caminho
        print(f"{OK} Caminho do Tesseract configurado para: {caminho}")
    else:
        print(f"{OK} Mantido o caminho padrão do sistema.")


def realizarOcrImagem():
    """Realiza OCR em uma imagem."""
    caminho = input("Informe o caminho da imagem (ex: imagem.png): ").strip()
    
    if not os.path.exists(caminho):
        print(f"{ERRO} Imagem não encontrada.")
        return

    try:
        imagem = Image.open(caminho)
        textoReconhecido = pytesseract.image_to_string(imagem, lang="por")
        print(f"\n--- TEXTO RECONHECIDO NA IMAGEM ---\n")
        print(textoReconhecido)
    except Exception as e:
        print(f"{ERRO} Erro ao executar o OCR na imagem: {e}")


def extrairOcrPdf():
    """Realiza OCR em páginas de PDFs escaneados."""
    caminho = verificarPdf()
    if not caminho:
        return

    try:
        import fitz
    except ImportError:
        print(f"{ERRO} A biblioteca 'PyMuPDF' (fitz) não está instalada.")
        print("Instale utilizando no terminal: pip install pymupdf")
        return

    try:
        documento = fitz.open(caminho)
        print(f"\n--- EXECUTANDO OCR NAS PÁGINAS DO PDF ---\n")

        for numero, pagina in enumerate(documento, start=1):
            pix = pagina.get_pixmap()
            imagemPil = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            texto = pytesseract.image_to_string(imagemPil, lang="por")
            
            print(f"\n[ OCR - PÁGINA {numero} ]\n")
            print(texto if texto.strip() else "(Nenhum texto detectado por OCR)")
    except Exception as e:
        print(f"{ERRO} Erro ao processar o OCR no PDF: {e}")


# ==========================================
# EXERCÍCIOS DE SEGURANÇA E VARIÁVEIS DE AMBIENTE
# ==========================================

def verificarSenhaPdf():
    """Verifica senha em PDF e usa variável de ambiente."""
    caminho = verificarPdf()
    if not caminho:
        return

    try:
        leitor = PdfReader(caminho)
        if not leitor.is_encrypted:
            print(f"{OK} Este arquivo PDF NÃO possui proteção por senha.")
            return

        print(f"{ATENCAO} O arquivo PDF está protegido por senha.")
        senha = os.getenv("PDF_SENHA")

        if not senha:
            print(f"{ERRO} A variável de ambiente 'PDF_SENHA' não está configurada no sistema.")
            return

        sucesso = leitor.decrypt(senha)
        if sucesso:
            print(f"{OK} Senha aceita! PDF descriptografado com sucesso na memória.")
        else:
            print(f"{ERRO} Senha incorreta ou recusada.")
    except Exception as e:
        print(f"{ERRO} Erro ao processar a segurança do PDF: {e}")


def mostrarVariaveisAmbiente():
    """Mostra o status da variável de ambiente de segurança."""
    senha = os.getenv("PDF_SENHA")
    print(f"\n--- CONFIGURAÇÕES DE SEGURANÇA ---\n")
    if senha:
        print(f"{OK} Variável de ambiente 'PDF_SENHA': Configurada.")
    else:
        print(f"{ATENCAO} Variável de ambiente 'PDF_SENHA': NÃO configurada.")