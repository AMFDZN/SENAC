#pip install openpyxl

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import BarChart, Reference
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.comments import Comment
from openpyxl import load_workbook
from tabulate import tabulate
import re #regex para filtrar as entradas usando letras e números 
import os
from pathlib import Path


NOMEDOARQUIVO = "planilha_openpyxl.xlsx"
NOMEDOARQUIVO2="planilha_pd_openPy.xlsx"
DIRETORIOEXERCICIO = Path(__file__).resolve().parent #pasta do exercício [excel]
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
            criaNovamente = input(f"{LINHA}\n{ATENCAO} Atenção: A planilha '{NOMEDOARQUIVO}' já existe!\nEstá na pasta do exercício ({DIRETORIOEXERCICIO})\n{LI} Tem certeza que quer criá-la novamente com os dados iniciais de teste?\n (s/n): ")
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
    
        planilha.save(ARQUIVO) #é preciso salvar as alterações
    
        print(f"\n{OK} Planilha ({NOMEDOARQUIVO}) criada com sucesso!") 
        
        #mostra a planilha e seus valores para o usuário
        mostraPlanilha(mostraValores=True)

 
# Exercício 3 
# Crie uma função que abra uma planilha existente e permita que as demais 
# operações do programa utilizem esse arquivo.

def abrePlanilha(tipo="r"):
    if tipo=="p":
        if not verificaArquivo(avisar=True):
            return None
    else:
        if not verificaArquivo(avisar=False):
            return None
    
    planilha = load_workbook(ARQUIVO) #carrega a planilha e deixa pronta pro jogo
    if tipo == "p":
        print(f"{OK} Planilha ({NOMEDOARQUIVO}) aberta para manipulação")
    elif tipo == "r":
        return planilha
    else:
        return planilha
    
 
# Exercício 4 
# Crie uma função que apresente na tela todas as abas existentes dentro do arquivo 
# Excel. 

# Exercício 5 
# Crie uma função que permita visualizar todos os dados armazenados em uma aba 
# da planilha. 

def mostraPlanilha(mostraValores=False,qualAba=False,top=False):
    planilha = abrePlanilha()
    if planilha is None: return
    
    """USANDO:
    
    1. LISTAR ABAS:
       mostraPlanilha(mostraValores=False)
       ou simplesmente: mostraPlanilha()
       -> mostraValores=False mostra as abas da planilha, em forma de linhas, 
          com índice e título em cada linha.
    
    2. VER A ABA INTEIRA:
       mostraPlanilha(mostraValores=True, qualAba="Produtos")
       OU usando o índice numérico: mostraPlanilha(mostraValores=True, qualAba=0)
       
    3. MOSTRAR ANTES E DEPOIS DE EXECUTAR ALGUM EXERCÍCIO (VISÃO RÁPIDA):
       mostraPlanilha(mostraValores=True, qualAba="Produtos", top=True)
       
    DETALHES DOS PARÂMETROS:
    - O valor default de todos os parâmetros é False, para que quando omitido ou vazio funcione.
    - qualAba aceita: o número do índice (int) ou o "nome da aba" (str).
    - top=True mostra apenas as duas primeiras linhas (Para exibir antes/depois das ações com colunas).
    """
       
    #############################
    # --- qual aba ---
    if qualAba is False or qualAba is None:
        aba = planilha.active
    elif isinstance(qualAba, int):
        aba = planilha.worksheets[qualAba]
    elif str(qualAba).strip().isdigit():
        numeroDaAba = int(str(qualAba).strip())
        aba = planilha.worksheets[numeroDaAba]
    else:
        tituloDaAba = str(qualAba).strip()
        aba = planilha[tituloDaAba]
    #############################     
    
    if mostraValores:
        #print(f"PLANILHA {planilha.title} Aba {aba.title}")
        # trecho abaixo com a biblioteca padrão OpenPyXL
        # printando uma lista por linha
        # i=0
        # for linha in aba.iter_rows(values_only=True):
        #     print(f"{LI} linha Nº{i} - {linha}")
        #     i+=i  
        #
        #########################
        """
        como sou um cara do front-end + UI/UX,
        não suportei ver tuplas e listas desalinhadas
        e usei a biblioteca "tabulate"
        com uma opção que não usa emojis 😂
        usa os caracteres de cálculo ( - + = ) e o "palito" ( | )
        para formar um desenho de tabela,
        e tem funções de tabulação de dados mais "amigas"
        """
        #cria uma lista com os dados da aba selecionada
        listaDados = list(aba.iter_rows(values_only=True))
        if not listaDados:
            print(f"\n{ATENCAO} A aba Nº{qualAba}- '{aba.title}' está vazia.\nNão há nada para mostrar")
            return

        #separa o acabeçalho do resto
        cabecalho = listaDados[0] #a linha índice [0]
        
        #o que mostrar
        if top:
            # Mostra o cabeçalho e apenas a primeira linha de dados (útil para antes/depois de ações)
            linhas = listaDados[1:2] if len(listaDados) > 1 else []
            print(f"--- [Visualização Rápida] Aba: {aba.title} ---")
            print(tabulate(linhas, headers=cabecalho, tablefmt="grid"))
        else:
            # Mostra a tabela inteira
            print(f"\n[{NOMEDOARQUIVO}] Aba: {aba.title}")
            print(tabulate(listaDados[1:], headers=cabecalho, tablefmt="grid"))
    else:
        print(f"\nABAS DA PLANILHA [{NOMEDOARQUIVO}]")
        i=0 #escalando para quando tiver mais abas
        for aba in planilha.sheetnames:
            print(f"{LI} Aba Nª{i}: {aba}")
            i+=1

 

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
            print(f"\n[{NOMEDOARQUIVO}] Aba: {aba.title}")
            print(tabulate(listaDados[1:], headers=cabecalho, tablefmt="grid"))
    else:
        print(f"{LINHAZINHA}\nABAS DA PLANILHA {NOMEDOARQUIVO}")
        for i, tituloAba in enumerate(planilha.sheetnames):
            print(f"{LI} Aba Nº{i}: {tituloAba}")
            
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

########################
#função para reconhecer se a ação na célula seja na linha 1. para não mudar o cabeçalho
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
            # (o not é mais rápido)
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
                qualCelula = input("Informe a célula que você quer mudar o valor (ex.: A3): ").strip().upper()
                
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
        planilha.save(ARQUIVO)
        
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
            print(f"Célula [{qualCelula}] = [{valorDaCelula}]")
        else:
            print(f"A célula {qualCelula} está vazia")
        
        
# Exercício 9 
# Crie uma função que permita adicionar novos registros de produtos na planilha. 
# O usuário deverá informar os dados do novo produto, quantidade e preço. 
def adicionarLinha():
    planilha = abrePlanilha() #carrega e abre pra jogo
    
    if planilha is None: return
    
    aba = planilha.active
    
    ## aqui só acontece porque eu sei o que tem na planilha
    # neste momento.se retirar uma coluna, inserir couna, ou mudar seu nome ou posição,
    # antes de fazer este exercício,
    # tudo pára
    produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade em estoque: "))
    preco = float(input("Preço unitário: "))
    estado = input("Estado de conservação: (novo/usado)")
    
    aba.append([produto,quantidade,preco,estado])
    

    planilha.save(ARQUIVO)

    print("Linha adicionada com sucesso.")
    
 #####################

""" Escalando para quando não tiver acesso à planilha """ 
def adicionarLinha2(oq="produto"):
    if oq.lower()=="linha":
        oq="nova Linha"
    elif oq.lower()=="produto":
        oq="novo Produto"
    else:
        oq="novo Produto"
    planilha = abrePlanilha()
    if planilha is None: return
    
    aba = planilha.active

    # Extrair os cabeçalhos da primeira linha, para saber o nome da coluna, pra pedir ao usuário dado por dado
    cabecalhos = [cell.value for cell in aba[1] if cell.value is not None]
    
    if not cabecalhos:
        print("A planilha está vazia ou não possui cabeçalhos na primeira linha.")
        return

    # Identifica os tipos de dados baseados na segunda linha (se existir dado prévio)
    tipos = []
    if aba.max_row >= 2: #max_row é top! exatamente para buscas deste tipo, ou buscas binárias, por eliminação, para encontrar um valor aleatório numa tabela imensa
        for cell in aba[2]: #usa a primeira linha com valores, na qual provavelmente foi inserido o tipo correto de valor
            val = cell.value #caminha por cada célula
            #isisntance reconhecendo o tipo. Classe type
            if isinstance(val, bool): #é booleano?
                tipos.append(bool)
            elif isinstance(val, int): #é inteiro
                tipos.append(int)
            elif isinstance(val, float): #é float
                tipos.append(float)
            else:
                tipos.append(str) #sobrou string
    else:
        # Caso a planilha esteja vazia, só com o cabeçalho, define como string para todas as colunas
        tipos = [str] * len(cabecalhos) #string X o comprimento do cabeçalho (número de colunas)

    # Um for para solicitar cada input, de acordo com o que está escrito no cabeçalho
    novaLinha = []
    print(f"\n--- Inserindo {oq} ---")
    
    for col_idx, (nomeDaColuna, tipo) in enumerate(zip(cabecalhos, tipos)):
        while True:
            try:
                # Exibe dica do tipo esperado para o usuário
                qualTipo = f" ({tipo.__name__})" if tipo != str else "" #se o tipo de valor não for especificado, else: é string
                valorCelula = input(f"{nomeDaColuna}{qualTipo}: ")
                
                # Trata a conversão do input de acordo com o tipo detectado
                if tipo == int:
                    valor = int(valorCelula)
                elif tipo == float:
                    valor = float(valorCelula.replace(',', '.')) # Aceita vírgula ou ponto
                elif tipo == bool:
                    valor = valorCelula.strip().lower() in ['sim', 's', 'true', '1', 'novo']
                else:
                    valor = valorCelula
                
                novaLinha.append(valor)
                break
            except ValueError:
                print(f"{ERRO} Entrada inválida! Digite um valor do tipo {tipo.__name__}.")

    # Adiciona a nova linha e salva a planilha
    aba.append(novaLinha)
    planilha.save(ARQUIVO)
    print(f"\n{OK} Adicionamos {oq} com sucesso!")
    
    print(tabulate([novaLinha], headers=cabecalhos, tablefmt="grid"))
    
    maisUmaLinha=input(f"Você quer continuar adicionando {oq} na tabela? (s/n)")
    if maisUmaLinha.lower()=="s":
        adicionarLinha2()
    elif maisUmaLinha.lower()=="n":
        input(f"{LI} Use ENTER para finalizar a adição de {oq}\n")
    else:
        input(f"{LI} Use ENTER para finalizar a adição de {oq}\n")
 
# Exercício 10 
# Crie uma função que permita remover uma linha da planilha informando o número 
# correspondente. 
def removeLinha():
    """
            delete_rows() Remove uma ou mais linhas.
            argumentos: (idx da linha, quantidade após a idx, até o max_row)

        """

    planilha = abrePlanilha()
    if planilha is None: return
    
    aba = planilha.active


    qualLinha = int(input(f"Informe o número da linha que deseja remover (de 2 a {aba.max_row}): "))


    if qualLinha <= 1 or qualLinha > aba.max_row: #a linha é a do cabeçalho? ou é uma linha além do máximo de linhas desta aba
        print(f"{ERRO} A linhainha {qualLinha} não é válida para remoção!")
        return

    aba.delete_rows(qualLinha) # delete_rows(idx da linha) deleta uma linha específica
    planilha.save(ARQUIVO)

    print(f"{OK} Linha {qualLinha} removida com sucesso.")
 
#COLUNAS
# Exercício 11 
# Crie uma função que permita adicionar uma nova coluna na planilha. 
# O usuário deverá informar o nome da nova coluna e os valores que serão 
# inseridos. 

# Exercício 12 
# Crie uma função que permita remover uma coluna existente na planilha. 


def acaoNaColuna(oq=None):
    
    """
    parâmetro oq - define a ação
        insert_cols(i) e delete_cols(i) - parâmetros | (idx:numero[i] da coluna, amount:quantas colunas)
            Insere: coluna vazia logo depois da última.
            Delete: a coluna referente ao índice informado
    """
    if oq:
        oq = oq.strip().lower()

    # Loop para validar a ação (evita a execução múltipla da recursão)
    while not oq or oq.isdigit() or (oq != "del" and oq != "add" and oq!="nome"):
        oq = input(f"""\n{ATENCAO} Informe uma das duas ações que será feita em uma das colunas:
            {LI}  add = Adicionar uma coluna
            {LI}  del = Deletar uma coluna
            {LI}  nome = Muda nome de uma coluna
            {LI} """
        ).strip().lower()

    planilha = abrePlanilha()
    if planilha is None: return
    
    aba = planilha.active
    
    if oq=="add":
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
        qualColuna = int(input(f"Informe a posição da coluna (após a coluna Nº{aba.max_column}): "))
        if qualColuna >= aba.max_column:
            aba.insert_cols(qualColuna)
        else:
            print(f"A coluna Nº:{qualColuna} está sendo usada")
            return


        titulo = input("Digite o título da nova coluna: ")

        #.cell(reow=em qual linha,índice da célula na linha).value = valor da célula
        aba.cell(row=1,column=qualColuna).value = titulo

        planilha.save(ARQUIVO)

        print(f"A coluna {titulo} foi adicionada com sucesso.")
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
    
    if oq=="del":
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
        qualColuna = int(input(f"Informe o número da coluna a deletar (entre 1 e {aba.max_column}): "))
        
        if qualColuna < 1 or qualColuna > aba.max_column:
            print(f"A coluna {qualColuna} não está em uso.")
        
            return
        
        else:
            if aba.max_row >= 2:
                val_celula = aba.cell(row=2, column=qualColuna).value
                # Se o valor na primeira linha de dados for numérico, protege a coluna
            if isinstance(val_celula, (int, float)):
                    titulo_coluna = aba.cell(row=1, column=qualColuna).value or f"Coluna {qualColuna}"
                    print(f"{ERRO} Ação bloqueada! A coluna '{titulo_coluna}' contém dados numéricos essenciais para cálculos e não pode ser removida.")
                    return
        
        aba.delete_cols(qualColuna)
        planilha.save(ARQUIVO)        
        
        print(f"Coluna {qualColuna} removida com sucesso.")
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
        
    #mostra para o usuário a tabela com a coluna nova. O cabeçalho e a primeira linha
        mostraPlanilha(mostraValores=True,qualAba=0,top=True)

#ABAS
# Exercício 13 
# Crie uma função que permita criar uma nova aba dentro do arquivo Excel. 
# A nova aba deverá possuir um nome informado pelo usuário. 

# Exercício 14 
# Crie uma função que permita alterar o nome de uma aba existente. 
 
# Exercício 15 
# Crie uma função que permita excluir uma aba existente no arquivo Excel. 

def acaoNaAba(oq="ver"):
    if oq:
        oq = oq.strip().lower()
    
    while not oq or oq.isdigit() or (oq not in ["ver", "list", "add", "del","nome"]):
        oq = input(f"""
            \n{ATENCAO} Informe uma das ações disponíveis para as abas:
            {LI} ver = Visualizar uma aba
            {LI} list = Listar todas as abas
            {LI} add = Adicionar uma aba
            {LI} del = Deletar uma aba
            {LI} nome = Mudar o nome de uma aba
            {LI} """
        ).strip().lower()
    
    planilha = abrePlanilha()
    if planilha is None: return

    # ADICIONAR UMA ABA (ABA)
    if oq == "add":
        nomeDaAba = input(f"Escolha um Título para a nova aba na planilha \"{NOMEDOARQUIVO}\":\n").strip()

        if nomeDaAba in planilha.sheetnames:
            print(f"\n{ATENCAO} A aba '{nomeDaAba}' já existe na planilha.")
            return
        
        planilha.create_sheet(nomeDaAba)
        planilha.save(ARQUIVO)
        print(f"\n{OK} Aba '{nomeDaAba}' criada com sucesso.")
        mostraPlanilha()

    # DELETAR ABA
    elif oq == "del":
        mostraPlanilha(mostraValores=False)
        
        try:
            if len(planilha.worksheets)<=1:
                print(f"{ATENCAO} Como a quantidade de abas é {len(planilha.worksheets)},\nnão é possível apagar a única aba.")
                criarAgora=input(f"{LI} Quer criar uma nova Aba agora?\n{LI} (s/n): ").strip()
                if criarAgora.lower()=="s":
                    acaoNaAba("add")
                else:
                    return
                
            qualAba = int(input(f"{LI} Qual o Nº(número) da aba, exceto a de Nº0, que deseja remover? "))
            #indice_python = qualAba - 1

            # Valida o índice de acordo com a lista de abas=worksheets
            if qualAba <= 0 or qualAba >= len(planilha.worksheets):
                print(f"\n{ATENCAO} A aba com Nº:{qualAba} não pode ser removida!")
                return

            # Seleciona a aba pelo índice do objeto
            aba = planilha.worksheets[qualAba]
            
            planilha.remove(aba)
            planilha.save(ARQUIVO)
            print(f"\n{OK} A aba Nº{qualAba} - '{aba.title}'foi removida!")
            mostraPlanilha(mostraValores=False)

        except ValueError:
            print(f"\n{ERRO} Digite um NÚMERO INTEIRO válido para o Nº da aba.")
            return
    
    #MUDAR O NOME DE UMA ABA
    
    elif oq=="nome":
        mostraPlanilha()
        
        qualAba = input(f"{LINHAZINHA}\nEscolha o Nº da aba a ser renomeada.\n{LI} ")
        
        if qualAba < 0 or qualAba >= len(planilha.worksheets):
            print(f"\n{ATENCAO} A aba com ID:{qualAba} não existe!")
            return
        
            # if qualAba not in planilha.sheetnames:
            #     print("Aba inexistente.")
            #     return
        
        aba = planilha.worksheets[qualAba]
        
        nomeNovo = input(f"Informe o novo nome para a aba Nº{qualAba} | Nome: {aba.title}: ")
        
        planilha[qualAba].title = nomeNovo
        planilha.save(ARQUIVO)
        
        print(f"{OK} A aba Nº{qualAba}:{aba.title} foi renomeada para {nomeNovo} com sucesso.")
    
    # LISTAR OU VISUALIZAR
    elif oq in ["ver", "list"]:
        mostraPlanilha(mostraValores=(oq == "ver")) 

 
# Exercício 16 
# Crie uma função que calcule automaticamente o valor total de cada produto. 
# O valor total deverá ser calculado utilizando a quantidade multiplicada pelo preço. 
# O resultado deverá ser armazenado em uma nova coluna chamada Total. 
def calcularTotalProduto():
    planilha = abrePlanilha()
    if planilha is None: return
    
    aba = planilha.active
    
    # Localizar os (idx) das colunas pelo cabeçalho (Linha 1)
    cabecalhos = [cell.value for cell in aba[1] if cell.value is not None]
    
    # Procura pelas colunas necessárias (ignorando maiúsculas/minúsculas)
    idx_produto = -1
    idx_qtd = -1
    idx_preco = -1
    idx_total = -1
    
    for i, h in enumerate(cabecalhos):
        h_lower = str(h).lower()
        if "produto" in h_lower:
            idx_produto = i
        elif "quantidade" in h_lower or "qtd" in h_lower:
            idx_qtd = i
        elif "preço" in h_lower or "preco" in h_lower:
            idx_preco = i
        elif "total" in h_lower:
            idx_total = i
            
    if idx_produto == -1 or idx_qtd == -1 or idx_preco == -1:
        print(f"{ERRO} Não foi possível encontrar as colunas obrigatórias (Produto, Quantidade, Preço).")
        return

    # se a coluna "Total" não existir, adiciona ela na última posição
    if idx_total == -1:
        nova_coluna_idx = aba.max_column + 1 # vasculha e encontra a última coluna, para criar a coluna [Total]
        aba.cell(row=1, column=nova_coluna_idx).value = "Total"
        idx_total = nova_coluna_idx - 1 # Índice baseado em 0 para a lista
        # Atualiza os cabeçalhos
        cabecalhos = [cell.value for cell in aba[1] if cell.value is not None]

    # for nas linhas depois d o cabeçalho, pra calcular e atualizar
    for row_idx in range(2, aba.max_row + 1):
        cel_qtd = aba.cell(row=row_idx, column=idx_qtd + 1).value
        cel_preco = aba.cell(row=row_idx, column=idx_preco + 1).value
        
        # Filtro de segurança: se quantidade ou preço não forem numéricos, assume 0 para evitar quebrar
        try:
            qtd = float(str(cel_qtd).replace(',', '.')) if cel_qtd is not None else 0.0
        except ValueError:
            qtd = 0.0
            
        try:
            preco = float(str(cel_preco).replace(',', '.')) if cel_preco is not None else 0.0
        except ValueError:
            preco = 0.0
            
        total_linha = qtd * preco
        
        # Insere o resultado na coluna Total da respectiva linha
        aba.cell(row=row_idx, column=idx_total + 1).value = total_linha

    planilha.save(ARQUIVO)
    print(f"{OK} Cálculo dos valores totais realizados e salvos com sucesso!")

    # 4. Renderização personalizada: Filtrar apenas as colunas desejadas ("Produto", "Quantidade", "Total")
    listaDados = list(aba.iter_rows(values_only=True))
    if len(listaDados) <= 1:
        print(f"{ATENCAO} A tabela não possui dados de produtos.")
        return

    # pega os (i) idx - das colunas a mostrar
    colunasDesejadas = []
    titulosDesejados = []
    
    for idx, titulo in enumerate(listaDados[0]):
        if titulo in [cabecalhos[idx_produto], cabecalhos[idx_preco],cabecalhos[idx_qtd], cabecalhos[idx_total]]:
            colunasDesejadas.append(idx)
            titulosDesejados.append(titulo)

    # Monta apenas as linhas filtradas com as 3 colunas escolhidas
    linhasFiltradas = []
    for linha in listaDados[1:]:
        # Pega apenas os valores das colunas mapeadas
        linhaFiltrada = [linha[i] if i < len(linha) else "" for i in colunasDesejadas]
        linhasFiltradas.append(linhaFiltrada)

    # Exibe no terminal com o tabulate limpo
    print(f"\n--- [Relatório Filtrado] Aba: {aba.title} ---")
    print(tabulate(linhasFiltradas, headers=titulosDesejados, tablefmt="grid")) 

#FORMATAÇÃO
# Exercício 17 
# Crie uma função que aplique formatação ao cabeçalho da planilha. 
# O cabeçalho deverá possuir destaque visual para facilitar a leitura do relatório. 

# Exercício 22 
# Crie uma função que permita aplicar filtros nos dados da planilha. 

def formataTabela2(oq="top", fontWeight=800, color="navy", textTransform="uppercase", backgroundColor="#F0F0F0", borderBottom=True):
    planilha = abrePlanilha()
    if planilha is None: return
    
    aba = planilha.active
    
    match oq.lower():
        case "top" | "cabecalho":
            print(f"\nAplicando formatação no cabeçalho...")
            color=int(input(f"Escolha a cor do texto do cabeçalho?\n{LI} 1- CINZA\n{LI} 2- PRETO\n{LI} 3- AZUL\n{LI} 4- LARANJA\n{LI} "))
            # Text Color
            match str(color).lower():
                case "1" | "gray" | "cinza":
                    hexColor = "666666"
                case "2" | "black" | "preto":
                    hexColor = "000000"
                case "3" | "navy" | "azul":
                    hexColor = "5d66fd"
                case "4" | "darkorange" | "laranja":
                    hexColor = "ff8d3a"
                case _:
                    hexColor = "000000" # Padrão preto
            
            input("\nENTER para seguir com a personalização do cabeçalho\n")
            
            # Background Sólido
            backgroundColor=input(f"Escolha a cor do fundo:\n{LI} 1- CINZA\n{LI} 2- PRETO\n{LI} 3- AZUL\n{LI} 4- LARANJA\n{LI} ")
            match str(backgroundColor).lower():
                case "1" | "lightgray" | "cinza":
                    bgHex = "999999"
                case "2" | "black" | "preto":
                    bgHex = "000000"
                case "3" | "lightblue" | "azul":
                    bgHex = "b3b7f2"
                case "4" | "lightorange" | "laranja":
                    bgHex = "fcddc7"
                case _:
                    bgHex = "666666" # Padrão gray
            # Aceita códigos hex diretos (ex: #333333 ou 333333) ou padrões
            bgHex = backgroundColor.replace("#", "")
            input("\nENTER para seguir com a personalização do cabeçalho\n")
            fontFamily=input(f"Escolha a fonte do título:\n{LI} 1- Arial\n{LI} 2- Verdana\n{LI} 3- Calibri")
            
            match str(fontFamily).lower():
                case "1" | "arial":
                    fontFamily = "Arial"
                case "2" | "verdana":
                    fontFamily = "Verdana"
                case "3" | "caibri":
                    fontFamily = "Calibri"
                case _:
                    fontFamily = "Arial" # Padrão arial            
            
            # Estilos do OpenPyxl
            fonteCabecalho = Font(
                name=fontFamily,
                family=2,
                size=14,
                bold=(fontWeight >= 700),
                condense=True,
                color=hexColor
            )
            
            preenchimentoFundo = PatternFill(
                start_color=bgHex,
                end_color=bgHex,
                fill_type="solid"
            )
            
            # Borda inferior opcional na mesma cor do texto
            bordaInferior = None
            if borderBottom:
                ladoBorda = Side(style="medium", color=hexColor)
                bordaInferior = Border(bottom=ladoBorda)

            # 4. Aplicação na Linha 1 (Cabeçalho)
            for cell in aba[1]:
                if cell.value is not None:
                    # Text-transform
                    textoOriginal = str(cell.value)
                    match textTransform.lower():
                        case "uppercase":
                            cell.value = textoOriginal.upper()
                        case "lowercase":
                            cell.value = textoOriginal.lower()
                        case "capitalize":
                            cell.value = textoOriginal.capitalize()
                    
                    # Aplicando estilos
                    cell.font = fonteCabecalho
                    cell.fill = preenchimentoFundo
                    if bordaInferior:
                        cell.border = bordaInferior
            
            planilha.save(ARQUIVO)
            print(f"{OK} Cabeçalho formatado com sucesso!")
        
        case "filtro":
            aba.auto_filter.ref = aba.dimensions
            planilha.save(ARQUIVO)
            print(f"{OK} Filtros aplicados.")
        case _:
            print(f"{ATENCAO} Parâmetro '{oq}' não reconhecido para formatação.") 

def formataTabela(oq="top", fontWeight=800, color="darkOrange", textTransform="uppercase", backgroundColor="#999999", borderBottom=True):
    planilha = abrePlanilha()
    if planilha is None: return
    
    aba = planilha.active
    
    match oq.lower():
        case "top" | "cabecalho":
            print(f"\nAplicando formatação no cabeçalho...")
            
            # 1. Tratamento da Cor da Fonte
            match str(color).lower():
                case "gray" | "cinza":
                    hexColor = "666666"
                case "black" | "preto":
                    hexColor = "000000"
                case "navy" | "azul":
                    hexColor = "000080"
                case "darkorange" | "laranja":
                    hexColor = "FF8C00"
                case _:
                    hexColor = "000080" # Padrão navy
            
            # 2. Tratamento da Cor de Fundo (Background)
            # Aceita códigos hex diretos (ex: #333333 ou 333333) ou padrões
            bgHex = backgroundColor.replace("#", "")
            
            # 3. Construção dos Estilos do OpenPyxl
            fonteCabecalho = Font(
                name="Calibri",
                size=11,
                bold=(fontWeight >= 700),
                color=hexColor
            )
            
            preenchimentoFundo = PatternFill(
                start_color=bgHex,
                end_color=bgHex,
                fill_type="solid"
            )
            
            # Borda inferior opcional na mesma cor do texto
            bordaInferior = None
            if borderBottom:
                ladoBorda = Side(style="medium", color=hexColor)
                bordaInferior = Border(bottom=ladoBorda)

            # 4. Aplicação na Linha 1 (Cabeçalho)
            for cell in aba[1]:
                if cell.value is not None:
                    # Text-transform
                    textoOriginal = str(cell.value)
                    match textTransform.lower():
                        case "uppercase":
                            cell.value = textoOriginal.upper()
                        case "lowercase":
                            cell.value = textoOriginal.lower()
                        case "capitalize":
                            cell.value = textoOriginal.capitalize()
                    
                    # Aplicando estilos
                    cell.font = fonteCabecalho
                    cell.fill = preenchimentoFundo
                    if bordaInferior:
                        cell.border = bordaInferior
            
            planilha.save(ARQUIVO)
            print(f"{OK} Cabeçalho formatado com sucesso!")
            
        case _:
            print(f"{ATENCAO} Parâmetro '{oq}' não reconhecido para formatação.")

def formataTabela3(oq="top", color="darkOrange", corTexto="#333333", backgroundColor="#999999"):
    planilha = abrePlanilha()
    if planilha is None: 
        return
    
    aba = planilha.active
    
    # Tratamento simples de cores caso venham em formato amigável
    coresHex = {
        "darkorange": "FF8C00",
        "navy": "000080",
        "black": "000000",
        "gray": "666666"
    }
    
    # Converte cor do texto do cabeçalho/borda principal se for string nomeada
    corPrincipalHex = coresHex.get(color.lower(), color.replace("#", ""))
    corConteudoHex = corTexto.replace("#", "")
    bgHex = backgroundColor.replace("#", "")
    
    match oq.lower():
        case "top" | "cabecalho":
            # Cabeçalho: uppercase, bold, alinhado ao centro, borda inferior medium na cor principal
            fonteCabecalho = Font(name="Arial", size=12, bold=True, color=corPrincipalHex)
            preenchimentoFundo = PatternFill(fill_type="solid", start_color=bgHex, end_color=bgHex)
            alinhamento = Alignment(horizontal="center", vertical="center")
            bordaCabecalho = Border(bottom=Side(style="medium", color=corPrincipalHex))

            for cell in aba[1]:
                if cell.value is not None:
                    cell.value = str(cell.value).upper()
                    cell.font = fonteCabecalho
                    cell.fill = preenchimentoFundo
                    cell.alignment = alinhamento
                    cell.border = bordaCabecalho
                    
        case "filtros":
            # Ativa os filtros nas colunas preenchidas
            aba.auto_filter.ref = aba.dimensions
            
        case "bordas":
            # Usa backgroundColor para linhas internas (thin) e color principal para bordas de destaque (thick)
            bordaInterna = Side(style="thin", color=bgHex)
            bordaExterna = Side(style="medium", color=corPrincipalHex)
            bordaFinal= Side(style="thick", color=corPrincipalHex)
            alinhamento = Alignment(horizontal="center", vertical="center")
            
            # Aplica formatação de fonte padrão para o conteúdo das células (corTexto)
            
            
            for row in aba[aba.dimensions]:
                # Pula a linha 1 se já foi tratada pelo cabeçalho
                for cell in row:
                    # Borda fina na linha e grossa na coluna
                    cell.border = Border(
                        left=bordaExterna, 
                        right=bordaExterna, 
                        top=bordaInterna, 
                        bottom=bordaInterna
                    )
                    
            linhaFinal = aba.max_row
            colunaFinal = aba.max_column

            for r in range(1, linhaFinal + 1):
                for c in range(1, colunaFinal + 1):
                    celula = aba.cell(row=r, column=c)
                    
                    # Mantém as bordas internas finas como padrão
                    bordaEsquerda = bordaExterna
                    bordaDireita = bordaExterna
                    bordaTop = bordaInterna
                    bordaBottom = bordaInterna

                    # Aplica borda espessa na PRIMEIRA COLUNA (left)
                    if c == 1:
                        bordaEsquerda = bordaExterna

                    # Aplica borda espessa na ÚLTIMA COLUNA (right)
                    if c == colunaFinal:
                        bordaDireita = bordaExterna

                    # Aplica borda espessa na ÚLTIMA LINHA (bottom)
                    if r == linhaFinal:
                        bordaBottom = bordaExterna

                    # Aplica o objeto Border montado na célula
                    celula.border = Border(
                        left=bordaEsquerda,
                        right=bordaDireita,
                        top=bordaTop,
                        bottom=bordaBottom
                    )
                    
                                 
        case "congelar" | "top-sticky":
            # Mantém o cabeçalho visível na rolagem
            aba.freeze_panes = "A2"
            
        case "center" | "colunas":
            alinhamento = Alignment(horizontal="center", vertical="center")
            fonteConteudo = Font(name="Arial", size=11, color=corConteudoHex)
            for row in aba[aba.dimensions]:
                # Pula a linha 1 se já foi tratada pelo cabeçalho
                for cell in row:
                    cell.font = fonteConteudo
                    cell.alignment=alinhamento
            
            
            for coluna in aba.columns:
                   
                    maior = 0
                    letra = coluna[0].column_letter
                    for celula in coluna:
                        if celula.value:
            
                            tamanho = len(str(celula.value))       
            
                            if tamanho > maior:            
                                maior = tamanho
            
                    aba.column_dimensions[letra].width = maior + 4
                    aba.row_dimensions[celula.row].height = 20
            
            
        case _:
            print(f"{ATENCAO} Opção de formatação '{oq}' não reconhecida.")
            return

    # Salvamento centralizado no final
    planilha.save(ARQUIVO)
    print(f"{OK} Missão: {oq} executada com sucesso!")

def personalizarCabecalho():
    """Menu interativo para coletar preferências de estilo do cabeçalho antes de aplicar."""
    print(f"\n{LINHA}\n--- PERSONALIZAÇÃO DO CABEÇALHO ---")
    
    # 1. Escolha da Fonte
    while True:
        print(f"\n{LI} Escolha a família da fonte:")
        print("  1 - Calibri (Padrão)")
        print("  2 - Arial")
        print("  3 - Verdana")
        print("  4 - Open Sans")
        escolhaFonte = input(f"{LI} Opção (1-4): ").strip()
        
        match escolhaFonte:
            case "1" | "":
                fontFamily = "Calibri"
                break
            case "2":
                fontFamily = "Arial"
                break
            case "3":
                fontFamily = "Verdana"
                break
            case "4":
                fontFamily = "Open Sans"
                break
            case _:
                print(f"{ERRO} Opção inválida! Escolha de 1 a 4.")

    # 2. Peso da Fonte (Negrito)
    while True:
        escolhaBold = input(f"\n{LI} Deseja o texto em negrito? (s/n): ").strip().lower()
        if escolhaBold in ["s", "sim"]:
            fontWeight = 800
            break
        elif escolhaBold in ["n", "nao", "não"]:
            fontWeight = 400
            break
        print(f"{ERRO} Digite 's' para sim ou 'n' para não.")

    # 3. Cor do Texto
    while True:
        print(f"\n{LI} Escolha a cor do texto:")
        print("  1 - Azul Navy")
        print("  2 - Preto")
        print("  3 - Cinza")
        print("  4 - Laranja Escuro")
        escolhaCor = input("Opção (1-4): ").strip()
        
        match escolhaCor:
            case "1" | "":
                color = "navy"
                break
            case "2":
                color = "black"
                break
            case "3":
                color = "gray"
                break
            case "4":
                color = "darkorange"
                break
            case _:
                print(f"{ERRO} Opção inválida!")

    # 4. Cor de Fundo (Background)
    while True:
        print(f"\n{LI} Escolha a cor de fundo (Background):")
        print("  1 - Cinza Claro (#F0F0F0)")
        print("  2 - Cinza Médio (#999999)")
        print("  3 - Cinza Escuro (#333333)")
        escolhaBg = input("Opção (1-3): ").strip()
        
        match escolhaBg:
            case "1" | "":
                backgroundColor = "#F0F0F0"
                break
            case "2":
                backgroundColor = "#999999"
                break
            case "3":
                backgroundColor = "#333333"
                break
            case _:
                print(f"{ERRO} Opção inválida!")

    # 5. Borda Inferior
    while True:
        escolhaBorda = input(f"\n{LI} Deseja aplicar borda inferior reforçada? (s/n): ").strip().lower()
        if escolhaBorda in ["s", "sim"]:
            borderBottom = True
            break
        elif escolhaBorda in ["n", "nao", "não"]:
            borderBottom = False
            break
        print(f"{ERRO} Digite 's' ou 'n'.")

    # Executa a função definitiva com os parâmetros acumulados
    print(f"\nAplicando formatação personalizada...")
    formataTabela(
        oq="top",
        fontFamily=fontFamily,
        fontWeight=fontWeight,
        color=color,
        textTransform="uppercase",
        backgroundColor=backgroundColor,
        borderBottom=borderBottom
    )

# Exercício 18 
# Crie uma função que aplique bordas nas células utilizadas pela tabela de 
# produtos. 
 
# Exercício 19 
# Crie uma função que ajuste automaticamente o tamanho das colunas conforme o 
# conteúdo existente. 
 
# Exercício 20 
# Crie uma função que permita mesclar células para criar um título de relatório. 
def mesclarTitulo():
    planilha = abrePlanilha()
    if planilha is None: return
    aba = planilha.active

    aba.insert_rows(1)
    max_col = max(aba.max_column, 1)
    letra_fim = get_column_letter(max_col)
    
    range_mescla = f"A1:{letra_fim}1"
    aba.merge_cells(range_mescla)

    celula_titulo = aba["A1"]
    celula_titulo.value = "RELATÓRIO DE ESTOQUE E PRODUTOS"
    celula_titulo.font = Font(name="Arial", size=14, bold=True, color="1F4E79")
    celula_titulo.alignment = Alignment(horizontal="center", vertical="center")
    celula_titulo.fill = PatternFill(fill_type="solid", start_color="D9E1F2", end_color="D9E1F2")

    planilha.save(ARQUIVO)
    print(f"{OK} Título inserido e células mescladas na faixa {range_mescla}.") 
# Exercício 21 
# Crie uma função que mantenha o cabeçalho da planilha visível durante a 
# navegação em grandes relatórios. 
 

 
# Exercício 23 
# Crie uma função que transforme os dados existentes em uma tabela formatada do 
# Excel. 
def criaPlanilhaPd():
    import pandas as pd
    from openpyxl.utils.dataframe import dataframe_to_rows
    df = pd.DataFrame(
        {

        "Produto": [
            "Notebook",
            "Mouse",
            "Teclado",
            "Monitor"
        ],

        "Quantidade": [
            10,
            35,
            20,
            8
        ],

        "Preço": [
            3500,
            80,
            150,
            1200
        ]

    }
    )
    
    planilha = Workbook()
    aba = planilha.active

    for r in dataframe_to_rows(df, index=True, header=True):
        aba.append(r)

    for cell in aba['A'] + aba[1]:
        cell.style = 'Pandas'

    planilha.save(ARQUIVO2)
    
    
            
def converterParaTabelaExcel():
    planilha = abrePlanilha()
    if planilha is None: return
    aba = planilha.active

    ref = aba.dimensions
    tabela = Table(displayName="TabelaProdutos", ref=ref)
    estilo = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                            showLastColumn=False, showRowStripes=True, showColumnStripes=True)
    tabela.tableStyleInfo = estilo

    if "TabelaProdutos" in aba.tables:
        del aba.tables["TabelaProdutos"]

    aba.add_table(tabela)

    planilha.save(ARQUIVO2)
    print(f"{OK} Intervalo convertido em Tabela nativa do Excel estilo TabelaProdutos.")
 
# Exercício 24 
# Crie uma função que gere um gráfico utilizando os dados da planilha. 
# O gráfico deverá representar informações dos produtos cadastrados. 
def gerarGrafico():
    planilha = abrePlanilha()
    if planilha is None: return
    aba = planilha.active

    cabecalhos = [cell.value for cell in aba[1] if cell.value is not None]
    col_prod = col_total = -1

    for i, h in enumerate(cabecalhos):
        h_str = str(h).lower()
        if "produto" in h_str:
            col_prod = i + 1
        elif "total" in h_str or "quantidade" in h_str:
            if col_total == -1:
                col_total = i + 1

    if col_prod == -1 or col_total == -1:
        print(f"{ERRO} Certifique-se de ter colunas válidas e executar o 'Cálculo de Totais' antes.")
        return

    chart = BarChart()
    chart.type = "col"
    chart.style = 10
    chart.title = "Totais por Produto"
    chart.y_axis.title = "Valores"
    chart.x_axis.title = "Produtos"

    dados = Reference(aba, min_col=col_total, min_row=1, max_row=aba.max_row)
    categorias = Reference(aba, min_col=col_prod, min_row=2, max_row=aba.max_row)

    chart.add_data(dados, titles_from_data=True)
    chart.set_categories(categorias)

    aba.add_chart(chart, "F2")

    planilha.save(ARQUIVO)
    print(f"{OK} Gráfico de colunas adicionado à célula F2 com sucesso!") 
# Exercício 25 
# Crie uma função que gere um relatório final automatizado. 
# O relatório deverá: criar uma área de apresentação, organizar os dados dos 
# produtos, aplicar formatação, calcular informações automaticamente, ajustar a 
# visualização da planilha e gerar um arquivo pronto para apresentação.  
def gerarRelatorio():
    print(f"\n--- INICIANDO AUTOMAÇÃO COMPLETA DO RELATÓRIO ---")
    criaPlanilha()
    calcularTotalProduto()
    mesclarTitulo()
    formataTabela3(oq="top")
    formataTabela3(oq="bordas")
    formataTabela3(oq="colunas")
    formataTabela3(oq="congelar")
    formataTabela3(oq="filtros")
    gerarGrafico()
    print(f"\n{OK} RELATÓRIO COMPLETO E AUTOMATIZADO GERADO COM SUCESSO!") 
 
 
 
 
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
9  - ADICIONAR NOVO PRODUTO
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
22 - FAZER O CABEÇALHO FICAR FIXO
23 - APLICAR FILTROS
24 - TRANSFORMAR DADOS EM UMA PLANILHA FORMATADA
25 - GERAR UM GRÁFICO
26 - GERAR UM RELATÓRIO
     E UMA PILHA DE COISAS
27 - FINALIZAR
{LINHAZINHA}
{LI} ESCOLHA UMA OPÇÃO: """)
    match opcao:
        case "1":
            
            print(f"{LINHA}\nCRIANDO O ARQUIVO {NOMEDOARQUIVO}")
            criaPlanilha()
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "2":
            
            print(F"{LINHA}\nVERIFICANDO SE O ARQUIVO {NOMEDOARQUIVO} EXISTE")
            verificaArquivo(avisar=True) 
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "3":
            
            print(f"{LINHA}\nABRINDO A PLANILHA PARA INICIAR OS TESTES:")
            abrePlanilha("p")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        
        case "4":
            
            print(f"{LINHA}\nLISTANDO AS ABAS DA PLANILHA\n{NOMEDOARQUIVO}")
            mostraPlanilha()
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "5":
            
            print(f"{LINHA}\nLISTANDO UMA ABA DA PLANILHA")
            mostraPlanilha()
            qualAba=input(f"Qual o Nº da aba que queres visualizar?\n{LI} ")
            mostraPlanilha(mostraValores=True,qualAba=qualAba,top=False)
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "6":
            
            print(f"{LINHA}\nINSERIR UM VALOR EM UMA CÉLULA:")
            acaoNaCelula(oq="mudar")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "7":
                    
            print(f"{LINHA}\nVER O CONTEÚDO DE UMA CÉLULA:")
            acaoNaCelula(oq="ler")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        
        case "8":
                            
            print(f"{LINHA}\nMUDAR O CONTEÚDO DE UMA CÉLULA:")
            acaoNaCelula(oq="mudar")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
                
        case "9":
            
            print(f"{LINHA}\n'INSERIR UM PRODUTO NA PLANILHA")
            adicionarLinha2("produto")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "10":
            
            print(f"{LINHA}\nVAMOS REMOVER UMA LINHA DA TABELA")
            removeLinha()
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "11":
            
            print(f"{LINHA}\nVAMOS INSERIR UMA LINHA NA TABELA")
            adicionarLinha2("linha")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "12":
            print(f"{LINHA}\nVAMOS REMOVER UMA COLUNA DA TABELA")
            acaoNaColuna(oq="del")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "13":
            print(f"{LINHA}\nVAMOS ADICIONAR UMA NOVA COLUNA NA TABELA")
            acaoNaColuna(oq="add")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
        
        case "14":
            
            print(f"{LINHA}\nINSERIR NOVA ABA NA PLANILHA")
            acaoNaAba(oq="add")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "15":
            
            print(f"{LINHA}\nMUDAR DE NOME UMA ABA DA PLANILHA")
            acaoNaAba(oq="nome")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "16":
            
            print(f"{LINHA}\nEXCLUIR UMA ABA DA PLANILHA")
            acaoNaAba(oq="del")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "17":
            
            print(f"{LINHA}\nCALCULAR O VALOR TOTAL DE CADA PRODUTO")
            calcularTotalProduto()
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "18":
            
            print(f"{LINHA}\nFORMATAnDO O CABEÇALHO DA TABELA\n")
            formataTabela3(oq="top", color="#FF6A00", backgroundColor="#f4ddcb", corTexto="#606060")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "19":
            
            print("APLICAR BORDAS À TABELA\n")
            formataTabela3(oq="bordas", color="#FF6A00", backgroundColor="#f4ddcb", corTexto="#606060")
            #https://share.google/OM9kQM1kyLwcsWW1v
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
                    
        case "20":
            
            print("AJUSTAR O TAMANHO DAS COLUNAS NA TABELA\n")
            formataTabela3(oq="colunas")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
                                                
        case "21":
            
                print("MESCLAR CÉLULAS DA TABELA\n")
                mesclarTitulo()
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "22":
            
                print("OCULTAR O CABEÇALHO DA TABELA\n")
                formataTabela3(oq="congelar")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "23":                                    
            
                print("APLICAR FILTROS NA TABELA\n")
                formataTabela3(oq="filtros")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "24":
            
                print("TRANSFORMAR DADOS EM UMA PLANILHA\n")
                #converterParaTabelaExcel()
                criaPlanilhaPd()
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "25":                        
            
                print("VAMOS GERAR UM GRÁFICO DA TABELA\n")
                gerarGrafico(aba="0",tipo="barras")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "26":
            
                print("VAMOS GERAR UM RELATÓRIO(DASHBOARD) DA TABELA\n")
                gerarRelatorio()
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "27":
            #finalizar o while
            break
        
        case _:
            #se deu mal. ficou preso no while
            input(F"NÃO EXISTE ESTA OPÇÃO\n{LI} Use ENTER PARA RETOMAR")                        