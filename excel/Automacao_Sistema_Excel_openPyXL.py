#pip install openpyxl

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.chart import BarChart, Reference
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.comments import Comment
import os
from pathlib import Path

NOMEDOARQUIVO = "planilha_openpyxl.xlsx"
DIRETORIOEXERCICIO = Path(__file__).resolve().parent #pasta do exercício [excel]
ARQUIVO = DIRETORIOEXERCICIO / NOMEDOARQUIVO

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
# Todos os exercícios devem estar organizados dentro de um único programa. 
# Utilize a biblioteca OpenPyXL para criação, leitura, manipulação e formatação de 
# arquivos Excel. 
# Organize o programa de forma modularizada, utilizando funções separadas para 
# cada operação, controle pelo menu principal, verificação da existência do arquivo, 
# tratamento de erros e opção para encerrar a execução do programa. 
# O programa deverá trabalhar com arquivos no formato .xlsx. 
 

########################
# Exercício 2 
# Crie uma função que verifique se o arquivo Excel criado pelo programa existe. 
# Caso o arquivo não exista, informe ao usuário que a planilha precisa ser criada 
# primeiro. 
def verificaArquivo(avisar=True):
    
    if not ARQUIVO.exists():
        if avisar:
            print(f"{ERRO} A planilha ainda não existe.")
            print(f"{LI} Para criar a planilha selecione a opção 1 no menu.")
            
        return False
    else:
        if avisar:
            print(f"{OK} A planílha {NOMEDOARQUIVO} existe")
    return True

####################
# Exercício 1 
# Crie uma função que gere uma nova planilha Excel contendo uma tabela de 
# produtos. 
# A planilha deverá possuir informações de produto, quantidade e preço. 
# Adicione alguns registros de exemplo e salve o arquivo no formato .xlsx. 
def criaPlanilha():
    #verifica se a planilha já existe e questiona se qquer subscrever
        if verificaArquivo(avisar=False):
            criaNovamente = input(f"{LINHA}\n{ATENCAO} Atenção: A planilha '{ARQUIVO}' já existe na pasta do exercício!\nTem certeza que quer criá-la novamente\ncom os dados iniciais de teste? (s/n): ")
            #se desistir, não recria
            if criaNovamente.lower() != "s":
                print("\nOperação cancelada.\nA planilha original foi mantida.")
                input("Use ENTER para sair desta opção\n")
                return
        planilha = Workbook()
    
        aba = planilha.active
    
        aba.title = "Produtos"
    
    
        aba["A1"] = "Produto"
        aba["B1"] = "Quantidade"
        aba["C1"] = "Preço"
        aba["D1"] = "Estado"
    
    
        aba.append(["Toca-discos Pioneer",1,800,"usado"])    
        aba.append(["3 em Um Philips",1,600,"usado"])
        aba.append(["CD Pink Floyd Animals",15,350,"novo"])
        aba.append(["CD Pink Floyd The Wall",5,750,"novo"])
        aba.append(["CD Black Sabbath 13",25,200,"novo"])
        aba.append(["Blueray AIKA",2,800,"usado"])
    
    
        planilha.save(ARQUIVO)
    
    
        print(f"\n{OK} Planilha {NOMEDOARQUIVO} criada com sucesso!") 

 
# Exercício 3 
# Crie uma função que abra uma planilha existente e permita que as demais 
# operações do programa utilizem esse arquivo.

def abrirPlanilha(tipo="r"):
    if not verificaArquivo():
        return None
    
    planilha = load_workbook(ARQUIVO)
    if tipo == "p":
        print(planilha)
    else:
        return planilha
    
 
# Exercício 4 
# Crie uma função que apresente na tela todas as abas existentes dentro do arquivo 
# Excel. 
 
# Exercício 5 
# Crie uma função que permita visualizar todos os dados armazenados em uma aba 
# da planilha. 
 
# Exercício 6 
# Crie uma função que permita inserir um valor em uma célula específica da 
# planilha. 
# O usuário deverá informar a posição da célula e o valor que será inserido. 
 
# Exercício 7 
# Crie uma função que permita consultar o conteúdo de uma célula informada pelo 
# usuário. 
 
# Exercício 8 
# Crie uma função que permita alterar o valor de uma célula existente na planilha. 
# O usuário deverá informar qual célula será alterada e qual será o novo valor. 
 
# Exercício 9 
# Crie uma função que permita adicionar novos registros de produtos na planilha. 
# O usuário deverá informar os dados do novo produto, quantidade e preço. 
 
# Exercício 10 
# Crie uma função que permita remover uma linha da planilha informando o número 
# correspondente. 
 
# Exercício 11 
# Crie uma função que permita adicionar uma nova coluna na planilha. 
# O usuário deverá informar o nome da nova coluna e os valores que serão 
# inseridos. 
 
# Exercício 12 
# Crie uma função que permita remover uma coluna existente na planilha. 
 
# Exercício 13 
# Crie uma função que permita criar uma nova aba dentro do arquivo Excel. 
# A nova aba deverá possuir um nome informado pelo usuário. 
 
# Exercício 14 
# Crie uma função que permita alterar o nome de uma aba existente. 
 
# Exercício 15 
# Crie uma função que permita excluir uma aba existente no arquivo Excel. 
 
# Exercício 16 
# Crie uma função que calcule automaticamente o valor total de cada produto. 
# O valor total deverá ser calculado utilizando a quantidade multiplicada pelo preço. 
# O resultado deverá ser armazenado em uma nova coluna chamada Total. 
 
# Exercício 17 
# Crie uma função que aplique formatação ao cabeçalho da planilha. 
# O cabeçalho deverá possuir destaque visual para facilitar a leitura do relatório. 
 
# Exercício 18 
# Crie uma função que aplique bordas nas células utilizadas pela tabela de 
# produtos. 
 
# Exercício 19 
# Crie uma função que ajuste automaticamente o tamanho das colunas conforme o 
# conteúdo existente. 
 
# Exercício 20 
# Crie uma função que permita mesclar células para criar um título de relatório. 
 
# Exercício 21 
# Crie uma função que mantenha o cabeçalho da planilha visível durante a 
# navegação em grandes relatórios. 
 
# Exercício 22 
# Crie uma função que permita aplicar filtros nos dados da planilha. 
 
# Exercício 23 
# Crie uma função que transforme os dados existentes em uma tabela formatada do 
# Excel. 
 
# Exercício 24 
# Crie uma função que gere um gráfico utilizando os dados da planilha. 
# O gráfico deverá representar informações dos produtos cadastrados. 
 
# Exercício 25 
# Crie uma função que gere um relatório final automatizado. 
# O relatório deverá: criar uma área de apresentação, organizar os dados dos 
# produtos, aplicar formatação, calcular informações automaticamente, ajustar a 
# visualização da planilha e gerar um arquivo pronto para apresentação.  
 
 
 
 
 
# Menu Principal 
# Crie um menu de controle para acessar todas as funções desenvolvidas. 
# O menu deverá permitir; executar cada exercício individualmente, retornar ao 
# menu após cada operação, tratar opções inválidas e encerrar o programa quando 
# solicitado pelo usuário. 
while True:
    
    opcao=input(f"""
---   SELECIONE UMA OPÇÃO    ---
1  - CRIAR PLANILHA
2  - VERIFICA SE A PLANILHA EXISTE
3  - ABRIR A PLANILHA PARA MANIPULAÇÃO
4  - LISTAR AS ABAS DA PLANILHA
5  - VER OS DADOS DE UMA DAS ABAS
6  - INSERIR UM VALOR EM UMA DAS CÉLULAS
7  - VER O CONTEÚDO DE UMA CÉLULA
8  - ALTERAR O CONTEÚDO DE UMA CÉLULA
9  - ADICIONAR NOVOS PRODUTOS
10 - REMOVER UMA LINHA
11 - ADICIONAR NOVA LINHA
12 - REMOVER UMA COLUNA
13 - ADICIONAR UMA COLUNA
14 - CRIAR NOVA [ABA]
15 - MUDAR O NOME DE UMA [ABA]
16 - EXCLUIR UMA [ABA]
17 - CALCULAR O VALOR TOTAL DE CADA PRODUTO
18 - FORMATAR CABEÇALHO
19 - APLICAR BORDAS
20 - AJUSTAR O TAMANHO DAS COLUNAS
21 - MISTURAR CÉLULAS PARA CRIAR UM TÍTULO
22 - FAZER O CABEÇALHO FICAR INVISÍVEL
23 - APLICAR FILTROS
24 - TRANSFORMAR DADOS EM UMA PLANILHA FORMATADA
25 - GERAR UM GRÁFICO
26 - GERAR UM RELATÓRIO
     E UMA PILHA DE COISAS
{LINHAZINHA}
{LI} ESCOLHA UMA OPÇÃO: """)
    match opcao:
        case "1":
            
            print(f"\nCRIANDO O ARQUIVO {NOMEDOARQUIVO}")
            criaPlanilha()
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "2":
            
            print(F"\nVERIFICANDO SE O ARQUIVO {NOMEDOARQUIVO} EXISTE")
            verificaArquivo(avisar=True) 
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "3":
            
            print("\nVAMOS ABRIR A PLANILHA PARA INICIAR AS MANIPULAÇÕES")
            abrirPlanilha("p")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")