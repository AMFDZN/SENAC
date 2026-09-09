#pip install openpyxl

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.comments import Comment
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from openpyxl import load_workbook
from tabulate import tabulate
import re #regex para filtrar as entradas usando letras e números 
import os
from pathlib import Path


NOMEDOARQUIVO = "teste.pdf"
NOMEDOARQUIVO2="planilha_openPy.xlsx"
PASTADOEXERCICIO="raíz do exercício"
DIRETORIOEXERCICIO = Path(__file__).resolve().parent
PDFS = "pdfs"
PASTA_PDFS = DIRETORIOEXERCICIO / PDFS

ARQUIVO = DIRETORIOEXERCICIO / NOMEDOARQUIVO
ARQUIVO2 = DIRETORIOEXERCICIO / NOMEDOARQUIVO2


#decorativos
LINHA="══════════════════════════"
LINHAZINHA="┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅"
OK="[✔]"
ERRO="[✕]"
ATENCAO="[⚠]"
LI="➤"
MUDOU="[⇄]"



# Instrução Geral 
# Crie um programa em Python que funcione como um menu de opções. 
# O usuário deverá escolher uma opção do menu e cada opção deverá executar um  
# dos exercícios abaixo. 
# Todos os exercícios devem estar organizados dentro de um único programa 
##############
#CRIA A PASTA DO pdf
def criaPastaPDF():
    os.makedirs(PASTA_PDFS, exist_ok=True)
    print(f"{OK} Pasta {PDFS} criada!")

def criaPDF():
    criaPastaPDF()

    caminho = os.path.join(PASTA_PDFS,NOMEDOARQUIVO)
    documento = canvas.Canvas(caminho,pagesize=A4)

    largura, altura = A4
    #metadados do Canvas
    documento.setTitle(f"ARQUIVO PDF")
    documento.setAuthor("ACELIO FILHO")
    documento.setSubject(f"EXERCÍCIO DE RECUPERAÇÃO")
    documento.setCreator("A.C.M.E. Creator v1.0")

    documento.setFont("Helvetica-Bold", 28)
    documento.drawCentredString(largura / 2, altura - 150, "CABEÇALHO DO PDF")

    documento.setFont("Helvetica", 16)
    documento.drawCentredString(largura / 2, altura - 230, "TEXTOS DE EXEMPLO PARA O ARQUIVO PDF")

    documento.setFont("Helvetica", 16)
    documento.drawCentredString(largura / 2, altura - 340, f"LINHA 2 DO PDF")
    documento.drawCentredString(largura / 2, altura - 380, f"LINHA 3 DO PDF.")
    documento.drawCentredString(largura / 2, altura - 450, f"RODAPÉ")


    documento.save()


    print("\nPDF criado com sucesso")
    print(f"Arquivo: {NOMEDOARQUIVO}\nPasta: {PDFS}\n{LINHA}")

 
def listarArquivosNaPasta(pasta=PASTA_PDFS, extensao=False):
    if extensao:
        if extensao==".txt":
            pasta=DIRETORIOEXERCICIO
            
        
    """Lista todos os arquivos de uma extensão dentro da pasta informada."""
    if not pasta.exists():
        print(f"{ATENCAO} A pasta [{PASTA_PDFS.name}] não existe. Criando a pasta...")
        criaPastaPDF()
        listarArquivosNaPasta(pasta=PASTA_PDFS, extensao=".pdf")
    encontrado=False
    arquivos = []
    for item in os.listdir(pasta):
        if item.lower().endswith(extensao.lower()):
            arquivos.append(item)
            encontrado=True
            
    if encontrado==False:
        print(f"Não existem arquivos {extensao} nesta pasta")
        criar=input("quer criar um arquivo nesta nova pasta? (s /n)").lower()
        if criar=="s":
            if extensao==".txt":
                criarArquivo()
                listarArquivosNaPasta(pasta=DIRETORIOEXERCICIO, extensao=".txt")
            else:
                criaPDF()
                listarArquivosNaPasta(pasta=PASTA_PDFS, extensao=".pdf")
    else:
        print(f"\n{OK} Arquivos {extensao} encontrados na pasta:")
        for arquivo in arquivos:
            print(f"{LI} {arquivo}")
    #return arquivos
    
#VERIFICA SE A PLANILHA EXISTE
def verificaArquivo(avisar=True):
    
    if not ARQUIVO2.exists():
        print(f"{LI} Para criar a planilha selecione a opção 5 no menu.")
            
        return False
    else:
        if avisar:
            print(f"{OK} A planílha {NOMEDOARQUIVO2} existe")
    return True

#ABRE PLANILHA    
def abrePlanilha(tipo="r"):
    if tipo=="p":
        if not verificaArquivo(avisar=True):
            return None
    else:
        if not verificaArquivo(avisar=False):
            return None
    
    planilha = load_workbook(ARQUIVO2) #carrega a planilha e deixa pronta pro jogo
    if tipo == "p":
        print(f"{OK} Planilha ({NOMEDOARQUIVO2}) aberta para manipulação")
    elif tipo == "r":
        return planilha
    else:
        return planilha    
 
# Exercício 1  
# Crie uma função que permita ao usuário criar um novo arquivo de texto. 
# O usuário deverá informar o nome do arquivo e o conteúdo que será armazenado. 
# O arquivo deverá ser criado utilizando codificação UTF-8. 

def criarArquivo(nomeDoArquivo=False): #
    if not nomeDoArquivo:
        nomeDoArquivo = input("Dê um nome para o arquivo de texto (.txt): ")

    if not nomeDoArquivo.endswith(".txt"): # .endswith() extensão do arquivo 
        nomeDoArquivo += ".txt" #SE NÃO ESTIVER, INSERE A EXTENSÃO
        caminhoDoArquivo=DIRETORIOEXERCICIO / nomeDoArquivo 
    
    conteudo = input(f"Escreva algo no arquivo {nomeDoArquivo}: ")


    with open( caminhoDoArquivo,"w", encoding="utf-8" ) as arquivo: #abre para escrita w = "write"

        arquivo.write(conteudo) #escreve efetivamente
        #conteudo = arquivo.read() #lê o conteúdo, depois de escrito, para confirmar se escreveu

    print(f"\n{OK} Arquivo {nomeDoArquivo} criado com sucesso.")
    print(f"Conteúdo do arquivo:\n{conteudo}")
    
  
 
# Exercício 2 
# Crie uma função que permita procurar uma palavra ou expressão dentro de um  
# arquivo de texto. 
# O programa deverá informar em quais linhas o termo pesquisado foi encontrado. 
# A pesquisa deverá ignorar diferenças entre letras maiúsculas e minúsculas. 
def procuraConteudo(nomeDoArquivo=False, extensao=False):

    #listarArquivos(tipo=False,pasta=False)
    listarArquivosNaPasta(pasta=DIRETORIOEXERCICIO, extensao=".txt")
    if not nomeDoArquivo:
        nomeDoArquivo = input("Informe o nome do arquivo que quer procurar o texto: ")
        if not nomeDoArquivo.endswith(".txt"): # .endswith() extensão do arquivo 
            nomeDoArquivo += ".txt"
    arquivo = DIRETORIOEXERCICIO / nomeDoArquivo
        


    if not os.path.exists(arquivo):
        print(f"{ERRO} Arquivo não encontrado na pasta {DIRETORIOEXERCICIO}")
        return


    termo = input("Digite o trecho que deseja procurar: ")

    with open(arquivo,"r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    encontrado = False
    print("\nRESULTADOS\n")


    for numero, linha in enumerate(linhas,start=1): #numero é o índice

        if termo.lower() in linha.lower():

            print(f"Linha {numero}: {linha.strip()}")

            encontrado = True

    if not encontrado:

        print(F"O TRECHO [{termo}] NÃO FOI ENCONTRADO NO ARQUIVO {nomeDoArquivo}.") 
# Exercício 3 
# Crie uma função que liste todos os arquivos com extensão .pdf existentes em uma  
# pasta específica. 
# Caso a pasta não exista, ela deverá ser criada automaticamente. 
# Caso não existam arquivos PDF, o programa deverá informar ao usuário. 
 
# Exercício 4 
# Crie uma função que permita verificar se determinado arquivo PDF existe. 
# Caso o arquivo não exista, o programa deverá informar o usuário e impedir que as  
# demais operações sejam executadas sobre esse arquivo. 
 
# Exercício 5  
# Crie uma função que gere uma nova planilha Excel contendo uma tabela de  
# produtos. 
# A planilha deverá possuir informações de produto, quantidade e preço. 
# Adicione alguns registros de exemplo e salve o arquivo no formato .xlsx. 
def criaPlanilha():        
    #verifica se a planilha já existe e questiona se qquer subscrever
        if verificaArquivo(avisar=False):
            criaNovamente = input(f"{LINHA}\n{ATENCAO} Atenção: A planilha '{NOMEDOARQUIVO2}' já existe!\nEstá na pasta do exercício ({DIRETORIOEXERCICIO})\n{LI} Tem certeza que quer criá-la novamente com os dados iniciais de teste?\n (s/n): ")
            #se desistir, não recria
            if criaNovamente.lower() != "s":
                print("\nOperação cancelada.\nA planilha original foi mantida.")
                input("Use ENTER para sair desta opção\n")
                return
        #se não existe, cria a planilha
        planilha = Workbook()
        
        # a variável (aba) é a aba da planilha
        # em que se está trabalhando. Como foi criada agora, só temos esta aba :-)
        aba = planilha.active # .active é uma propriedade de Workbook()
        #declara-se a variável "aba", onde estamos trabalhando
    
        aba.title = "Produtos" # define o nome da aba da planilha
    
        #criando as colunas, baseando-se no mesmo formato do Excel
        #esta é a linha inicial, [0]
        aba["A1"] = "Nome do Produto"
        aba["B1"] = "Quantidade"
        aba["C1"] = "Preço"
        aba["D1"] = "Estado"
    
        #inserindo dados: aba.append() = uma linha
        aba.append(["Toca-discos Pioneer",1,500,"usado"])    
        aba.append(["3 em Um Philips",1,600,"usado"])
        aba.append(["CD Pink Floyd Animals",15,80,"novo"])
        aba.append(["LP Pink Floyd Pulse",6,100,"usado"])
        aba.append(["CD Pink Floyd The Wall",5,200,"novo"])
        aba.append(["CD Black Sabbath 13",25,80,"novo"])
        aba.append(["BOX Black Sabbath 13",25,300,"novo"])
        aba.append(["Blueray Philips",2,800,"usado"])
    
        planilha.save(ARQUIVO2) #é preciso salvar as alterações
    
        print(f"\n{OK} Planilha ({NOMEDOARQUIVO2}) criada com sucesso!") 
        
        #mostra a planilha e seus valores para o usuário
        mostraPlanilha2(mostraValores=True, qualAba=False, top=False) 
# Exercício 6 
# Crie uma função que permita visualizar todos os dados armazenados em uma aba  
# da planilha. 
def mostraPlanilha2(mostraValores=False, qualAba=False, top=False):
    
    planilha = abrePlanilha()
    
    # Seleção da aba
    if qualAba is False or qualAba is None:
        aba = planilha.active
    elif isinstance(qualAba, int):
        aba = planilha.worksheets[qualAba]
    else:
        aba = planilha[str(qualAba).strip()]

    # Exibição dos dados ou das abas
    if mostraValores:
        listaDados = list(aba.iter_rows(values_only=True))
        if not listaDados:
            print(f"{ATENCAO} A aba '{aba.title}' está vazia.")
            return

        cabecalho = listaDados[0]
        
        if top:
            linhas = listaDados[1:2] if len(listaDados) > 1 else []
            print(f"\n[Visualizar Alteração] Aba: {aba.title}")
            print(tabulate(linhas, headers=cabecalho, tablefmt="grid"))
        else:
            print(f"\n[{NOMEDOARQUIVO2}] Aba: {aba.title}")
            print(tabulate(listaDados[1:], headers=cabecalho, tablefmt="grid"))
    else:
        print(f"{LINHAZINHA}\nABAS DA PLANILHA {NOMEDOARQUIVO}")
        for i, tituloAba in enumerate(planilha.sheetnames):
            print(f"{LI} Aba Nº{i}: {tituloAba}") 
# Exercício 7 
# Crie uma função que permita inserir um valor em uma célula específica da  
# planilha. 
# O usuário deverá informar a posição da célula e o valor que será inserido. 
 
# Exercício 8 
# Crie uma função que permita consultar o conteúdo de uma célula informada pelo  
# usuário. 
########
#função complementar
def isTop(celula):
    """Verifica se a célula pertence à linha 1 (cabeçalho/topo)."""
    match = re.search(r'\d+', celula)
    if match and int(match.group()) == 1:
        print(f"{ERRO} Ação bloqueada!\nA linha 1 (cabeçalho) está protegida contra alterações.")
        return True
    return False
###########################
def acaoNaCelula(oq="ler"):
    
    planilha = abrePlanilha()    
    if planilha is None: return
    aba = planilha.active
    
    if oq.lower() == "mudar" or oq.lower() == "escrever":
        while True:
            legendaMensagem = "mudar o valor" if oq.lower() == "mudar" else "inserir um valor"
            qualCelula = input(f"Informe a célula que você quer {legendaMensagem} (ex.: A3, B6): ").strip().upper()
            
            # Verifica se "qualCelula" não é False
            if not qualCelula:
                print(f"{ERRO} Informe uma célula!")
                continue
                
            # verifica se a célula escolhida para alterar não está no cabecalho
            if isTop(qualCelula):
                continue
            
            if oq.lower() == "escrever":
                valorAtual = aba[qualCelula].value
                if valorAtual is not None and str(valorAtual).strip() != "":
                    print(f"{ATENCAO} A célula [{qualCelula}] já está preenchida com [{valorAtual}].")
                    print(f"{LI} Para alterá-la, utilize a opção (8) ALTERAR O CONTEÚDO DE UMA CÉLULA.")
                    continue # Volta para o início do while para pedir outra célula
                
            break # Passou por tudo, sai do loop
            
        if oq.lower() == "mudar":
            
            while True:
                #qualCelula = input("Informe a célula que você quer mudar o valor (ex.: A3): ").strip().upper()
                
                if not qualCelula:
                    print(f"{ERRO} O campo não pode estar vazio! Informe uma célula.")
                    continue
                    
                if isTop(qualCelula):
                    continue
                    
                break
            
        valorAtual = aba[qualCelula].value
        print(f"{LINHAZINHA}\nValor atual da Célula [{qualCelula}] = [{valorAtual}]")
        
        # --- Verificação de tipo baseada no valor atual ---
        if isinstance(valorAtual, int):
            while True:
                try:
                    valorDaCelula = int(input(f"Novo valor tipo (número inteiro) para a célula {qualCelula}: "))
                    break
                except ValueError:
                    print(f"{ERRO} Entrada inválida! A célula exige um número inteiro.")
        elif isinstance(valorAtual, float):
            while True:
                try:
                    valorDaCelula = float(input(f"Novo valor decimal para a célula {qualCelula}: ").replace(',', '.'))
                    break
                except ValueError:
                    print(f"{ERRO} Entrada inválida! A célula exige um número decimal.")
        else:
            # Se o tipo for str ou vazio, aceita livremente
            valorDaCelula = input(f"Novo valor para a célula {qualCelula}: ")
        
        aba[qualCelula] = valorDaCelula 
        planilha.save(ARQUIVO2)
        
        print(f"{OK} Célula alterada com sucesso.")
        print(f"Novo valor da Célula [{qualCelula}] = [{valorDaCelula}]")
    
    elif oq.lower() == "ler":
        while True:
            qualCelula = input("Informe a célula para leitura (ex.: A1, B3...): ").strip().upper()
            if not qualCelula:
                print(f"{ERRO} Informe uma célula!")
                continue
            break
            
        valorDaCelula = aba[qualCelula].value
        if valorDaCelula:
            print("\nCélula encontrada.")
            print(f"A célula [{qualCelula}] tem o valor: [{valorDaCelula}]")
        else:
            print(f"A célula {qualCelula} está vazia")



while True:
    opcao=input(f"""
{LINHA}\nMENU DE OPÇÕES:
1  - CRIAR UM ARQUIVO DE TEXTO
2  - PROCURAR UMA EXPRESSÃO NO ARQUIVO DE TEXTO
3  - LISTAR OS ARQUIVOS [PDF] NA PASTA {PASTA_PDFS.name}
4  - PROCURAR UM ARQUIVO PDF NA PASTA {PASTA_PDFS.name}
5  - CRIAR A PLANILHA {NOMEDOARQUIVO2}
6  - VER DADOS DA PLANILHA {NOMEDOARQUIVO2}
7  - INSERIR DADO EM UMA CÉLULA DA PLANILHA {NOMEDOARQUIVO2}
8  - CONSULTAR DADOS DE UMA DAS CÉLULAS DA PLANILHA {NOMEDOARQUIVO2}               
                
{LINHAZINHA}
{LI} ESCOLHA UMA OPÇÃO: """)
    match opcao:
        case "1":
            
            print(f"{LINHA}\nCRIANDO UM ARQUIVO DE TEXTO")
            criarArquivo(nomeDoArquivo=False)
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "2":
            print(f"{LINHA}\nPROCURAR UMA EXPRESSÃO EM UM ARQUIVO DE TEXTO")
            
            procuraConteudo(nomeDoArquivo=False)
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "3":
            print(f"{LINHA}\nLISTAR ARQUIVOS PDF NA PASTA {PASTA_PDFS.name}")
            listarArquivosNaPasta(pasta=PASTA_PDFS, extensao=".pdf")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "4":
            print(f"{LINHA}\nPROCURAR UM PDF NA PASTA {PASTA_PDFS.name}")
            listarArquivosNaPasta(pasta=PASTA_PDFS, extensao=".pdf")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "5" :
            print(f"{LINHA}\nCRIAR A PLANILHA {NOMEDOARQUIVO2}")
            criaPlanilha()
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "6":
            print(f"{LINHA}\nVER DADOS DA PLANILHA {NOMEDOARQUIVO2}")
            mostraPlanilha2(mostraValores=True, qualAba=False, top=False)
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "7":
            print(f"{LINHA}\nINSERIR UM VALOR EM UMA CÉLULA DA PLANILHA {NOMEDOARQUIVO2}")
            acaoNaCelula(oq="mudar")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        case "8":
            print(f"{LINHA}\nVER O CONTEÚDO DE UMA CÉLULA DA PLANILHA {NOMEDOARQUIVO2}")
            acaoNaCelula(oq="ler")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")