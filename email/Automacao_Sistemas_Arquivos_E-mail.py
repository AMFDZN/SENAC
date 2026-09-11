# pip install openpyxl
# pip install secure-smtplib
import os
from pathlib import Path

# Instrução Geral
# Crie um sistema de gerenciamento e envio de e-mails personalizados.
# O usuário deverá escolher uma opção no menu principal e cada opção deverá
# executar uma das funcionalidades propostas abaixo

ARQUIVO_EXCEL = "destinatarios.xlsx"
HISTORICO_ENVIO = "historico.txt"
CONFIG_SMTP = "config.txt"


DIRETORIO_EXERCICIO = Path(__file__).resolve().parent
CAMINHO_EXCEL = DIRETORIO_EXERCICIO / ARQUIVO_EXCEL
CAMINHO_HISTORICO = DIRETORIO_EXERCICIO / HISTORICO_ENVIO

#Funções - importando as funções
import sys
sys.path.append(str(Path(__file__).parent))
from funcoes import *

#elementos decorativos usados para UI / UX
LINHA = "══════════════════════════"
LINHAZINHA = "┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅ ┅"
OK = "[✔]"
ERRO = "[✕]"
ATENCAO = "[⚠]"
LI = "➤"
MUDOU = "[⇄]"


while True:
    opcao = input(f"""
    MENU DE GERENCIAMENTO DE E-MAILS:
    ººººººººººººººººººººººº
    00-  CONFIGURAR REMETENTE
    0-  CRIAR PLANILHA DE DESTINATÁRIOS
    1-  VERIFICAR EXISTÊNCIA DA PLANILHA
    2-  ABRIR PLANILHA EXISTENTE
    3-  LISTAR ABAS DA PLANILHA
    4-  VISUALIZAR TODOS OS DESTINATÁRIOS
    5-  CADASTRAR NOVO DESTINATÁRIO
    6-  CONSULTAR DESTINATÁRIO POR E-MAIL
    7-  ALTERAR INFORMAÇÕES DE DESTINATÁRIO
    8-  REMOVER DESTINATÁRIO DA BASE
    9-  ENVIAR E-MAIL INDIVIDUAL
    10- ENVIAR E-MAILS PARA TODOS
    11- REGISTRAR HISTÓRICO DE ENVIOS
    {LINHA}
    \n-> DIGITE SUA OPÇÃO: """)
    
    match opcao:
        case "00":
            configuraRemetente()
        case "0":
            print("VAMOS CRIAR A PLANILHA DE DESTINATÁRIOS")
            criarPlanilhaDestinatarios(CAMINHO_EXCEL)  # Chama a função correspondente
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "1":
            print("VERIFICANDO EXISTÊNCIA DO ARQUIVO EXCEL")
            verificarArquivoExcel(CAMINHO_EXCEL)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "2":
            print("ABRINDO PLANILHA EXISTENTE")
            abrirPlanilhaExcel(CAMINHO_EXCEL)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "3":
            print("LISTANDO ABAS DA PLANILHA")
            listarAbasPlanilha(CAMINHO_EXCEL)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "4":
            print("VISUALIZANDO TODOS OS DESTINATÁRIOS")
            visualizarDestinatarios(CAMINHO_EXCEL)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "5":
            print("CADASTRANDO NOVO DESTINATÁRIO")
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            empresa = input("Digite a empresa: ")
            mensagem = input("Digite a mensagem personalizada: ")
            cadastrarDestinatario(CAMINHO_EXCEL, nome, email, empresa, mensagem)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "6":
            print("CONSULTANDO DESTINATÁRIO POR E-MAIL")
            emailConsulta = input("Digite o e-mail que deseja procurar: ")
            consultarDestinatarioPorEmail(CAMINHO_EXCEL, emailConsulta)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "7":
            print("ALTERANDO INFORMAÇÕES DE DESTINATÁRIO")
            emailAlvo = input("Digite o e-mail do destinatário a ser alterado: ")
            alterarDestinatario(CAMINHO_EXCEL, emailAlvo)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "8":
            print("REMOVENDO DESTINATÁRIO DA BASE")
            linhaAlvo = int(input("Digite o número da linha correspondente a ser removida: "))
            removerDestinatario(CAMINHO_EXCEL, linhaAlvo)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "9":
            print("ENVIANDO E-MAIL INDIVIDUAL")
            destinatarioEmail = input("Digite o e-mail do destinatário: ")
            assunto = input("Digite o assunto do e-mail: ")
            corpo = input("Digite a mensagem do e-mail: ")
            enviarEmailIndividual(destinatarioEmail, assunto, corpo)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "10":
            print("ENVIANDO E-MAILS PARA TODOS OS DESTINATÁRIOS")
            enviarEmailsEmMassa(CAMINHO_EXCEL)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case "11":
            print("REGISTRANDO HISTÓRICO DE ENVIOS")
            registrarHistorico(CAMINHO_HISTORICO)
            input(f"{LINHAZINHA}\n{LI} Use ENTER para voltar ao menu")
        case _:
            print(f"{ERRO} Opção inválida. Tente novamente.")
