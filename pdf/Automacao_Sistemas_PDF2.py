import sys
from pathlib import Path

# Configura o diretório base para importar o arquivo de funções com segurança
DIRETORIOEXERCICIO = Path(__file__).resolve().parent
sys.path.append(str(DIRETORIOEXERCICIO))

from funcoes import *

# Elementos visuais
LINHA = "════════════════════════════════════════"
LINHAZINHA = "┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅"
LI = "➤"

# Laço principal do menu utilizando while True e match-case
while True:
    opcao = input(f"""
{LINHA}
           MENU DE OPÇÕES - AUTOMAÇÃO
{LINHA}
 0- CRIAR AS PASTAS DO PROJETO
 
 ARQUIVOS DE TEXTO:
 1- CRIAR UM ARQUIVO DE TEXTO (.txt)
 2- LER O CONTEÚDO DE UM ARQUIVO
 3- ADICIONAR CONTEÚDO AO FINAL DO ARQUIVO
 4- PROCURAR UMA PALAVRA/TERMO NO TEXTO
 
 MANIPULAÇÃO DE PDF:
 5- LISTAR ARQUIVOS PDF
 6- VERIFICAR SE UM PDF EXISTE
 7- INFORMAÇÕES BÁSICAS SOBRE UM PDF
 8- EXTRAIR TEXTO DE UM PDF
 9- PROCURAR UM TERMO DENTRO DE UM PDF
 10- EXTRAIR UMA PÁGINA ESPECÍFICA DE UM PDF
 11- MESCLAR VÁRIOS ARQUIVOS PDF EM UM SÓ
 
 DOCUMENTOS AUTOMÁTICOS:
 12- GERAR CERTIFICADO EM PDF
 13- GERAR CONTRATO EM PDF
 
 OCR (RECONHECIMENTO ÓPTICO):
 14- CONFIGURAR CAMINHO DO TESSERACT
 15- REALIZAR OCR EM IMAGEM
 16- REALIZAR OCR EM PDF (PÁGINA POR PÁGINA)
 
 SEGURANÇA:
 17- VERIFICAR SENHA DE PDF (VARIÁVEL DE AMBIENTE)
 18- MOSTRAR CONFIGURAÇÕES DE AMBIENTE
 
 00- SAIR DO PROGRAMA
{LINHA}
{LI} DIGITE SUA OPÇÃO: """).strip()

    match opcao:
        case "0":
            print("\nVAMOS CRIAR AS PASTAS DO PROJETO")
            criar_pastas()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "1":
            print("\nVAMOS CRIAR UM ARQUIVO DE TEXTO")
            criar_arquivo_texto()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "2":
            print("\nVAMOS LER UM ARQUIVO DE TEXTO")
            ler_arquivo_texto()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "3":
            print("\nADICIONAR CONTEÚDO A UM ARQUIVO")
            adicionar_texto()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "4":
            print("\nPROCURAR UMA SENTENÇA EM UM TEXTO")
            procurar_texto()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "5":
            print("\nLISTANDO ARQUIVOS PDF")
            listar_pdfs()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "6":
            print("\nVERIFICAR EXISTÊNCIA DE PDF")
            procurar_arquivo_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "7":
            print("\nINFORMAÇÕES DE UM ARQUIVO PDF")
            mostrar_informacoes_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "8":
            print("\nEXTRAIR TEXTO DE UM PDF")
            extrair_texto_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "9":
            print("\nPROCURAR TERMO EM UM PDF")
            procurar_em_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "10":
            print("\nEXTRAIR UMA PÁGINA ESPECÍFICA DO PDF")
            extrair_pagina_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "11":
            print("\nMESCLAR MÚLTIPLOS PDFs")
            mesclar_pdfs()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "12":
            print("\nGERAR CERTIFICADO EM PDF")
            criar_certificado()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "13":
            print("\nGERAR CONTRATO EM PDF")
            criar_contrato()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "14":
            print("\nCONFIGURAR TESSERACT OCR")
            configurar_tesseract()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "15":
            print("\nREALIZAR OCR EM IMAGEM")
            realizar_ocr_imagem()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "16":
            print("\nREALIZAR OCR EM PDF")
            extrair_ocr_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "17":
            print("\nVERIFICAR SENHA DE PDF")
            verificar_senha_pdf()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "18":
            print("\nCONFIGURAÇÕES DE AMBIENTE")
            mostrar_variaveis_ambiente()
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para voltar ao menu")
            
        case "00" | "sair":
            print("\nEncerrando o programa de automação. Até logo!")
            break
            
        case _:
            print(f"\n{ERRO} Opção inválida! Escolha um número válido do menu.")
            input(f"\n{LINHAZINHA}\n{LI} Pressione ENTER para tentar novamente")