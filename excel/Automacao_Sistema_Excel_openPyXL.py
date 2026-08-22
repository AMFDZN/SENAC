#pip install openpyxl

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.chart import BarChart, Reference
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.comments import Comment
from openpyxl import load_workbook
from tabulate import tabulate
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
        
        # a variável (aba) é a aba da planilha
        # em que se está trabalhando
    
        aba = planilha.active # .active é uma propriedade para "ativar" a aba da planilá
    
        aba.title = "Produtos" # define o nome da aba da planilha
    
    
        aba["A1"] = "Nome do Produto"
        aba["B1"] = "Quantidade"
        aba["C1"] = "Preço"
        aba["D1"] = "Estado"
    
    
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

 
# Exercício 3 
# Crie uma função que abra uma planilha existente e permita que as demais 
# operações do programa utilizem esse arquivo.

def abrePlanilha(tipo="r"):
    if not verificaArquivo(avisar=True):
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
    - top=True mostra apenas a primeira linha (ideal para conferir antes/depois de ações em colunas/linhas).
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
    """
    mostraValores : tipo booleano | True : mostra as linhas e valores da tabela, False : mostra as abas
iter_rows() # Percorre todas as linhas da planilha.
usa índices (ipo:int) das linhas e colunas
sem parâmetros declarados retorna todas as linhas e colunas

parâmetros de listagem - ótimo para buscas
min_row e min_column
max_row e max_column

values_only=True #tipo booleano - default: False - True Retorna os valores das células e fórmulas.

    """

     
    
    if mostraValores:
        #print(f" - - - PLANILHA - - - \n{planilha.title} Aba {aba.title}")
        # trecho abaixo com a biblioteca padrão OpenPyXL
        #
        # for linha in aba.iter_rows(values_only=True):
        #     print(linha)
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
        #cria uma lista com os dados da aba
        listaDados = list(aba.iter_rows(values_only=True))
        if not listaDados:
            print(f"{ATENCAO} A aba '{aba.title}' está vazia.")
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
        print(f"\nABAS DA PLANILHA {NOMEDOARQUIVO}\n")
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

def acaoNaCelula(oq="ler"):
    
    planilha = abrePlanilha()
         
    if planilha is None: return
    
    aba = planilha.active
    
    if oq.lower()=="mudar":
    
        qualCelula = input("Informe a célula que você quer mudar o valor (ex.: A3): ")
        valorAtual=aba[qualCelula].value
        print(f"{LINHAZINHA}\nValor atual da Célula [{qualCelula}] = [{valorAtual}]")
        valorDaCelula = input(f"Novo valor para a célula {qualCelula}: ")
        aba[qualCelula] = valorDaCelula #declara novo valor à célula selecionada
        planilha.save(ARQUIVO) #salva
        
        print(f"{OK} Célula alterada com sucesso.")
        print(f"Novo valor da Célula [{qualCelula}] = [{valorDaCelula}]")
    
    elif oq.lower()=="ler":
        qualCelula = input("Informe a célula (ex.: A1, B3...): ")
        valorDaCelula = aba[qualCelula].value
        
        print("\nCélula encontrada.")
        print(f"Célula [{qualCelula}] = [{valorDaCelula}]")
     
    elif oq.lower()=="escrever":
        
            qualCelula = input("Informe uma célula aleatória (ex.: A15, D10...): ")
            valorDaCelula = input(f"Qual o valor para a célula {qualCelula}: ")
            
            aba[qualCelula] = valorDaCelula #declara novo valor à célula selecionada
            planilha.save(ARQUIVO) #salva
        
            print(f"{OK} Valor inserido na célula com sucesso.")
            print(f"O valor da Célula [{qualCelula}] é [{valorDaCelula}]")
 

 
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
            elif isinstance(val, int): #é inteirp
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


    linha = int(input(f"Informe o número da linha que deseja remover (de 2 a {aba.max_row}): "))


    if linha <= 1 or linha > aba.max_row: #a linha é a do cabeçalho? ou é uma linha além do máximo de linhas desta aba
        print(f"{ERRO} A linha {linha} não é válida para remoção!")
        return

    aba.delete_rows(linha) # delete_rows(idx da linha) deleta uma linha específica
    planilha.save(ARQUIVO)

    print(f"{OK} Linha {linha} removida com sucesso.")
 
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
            print(f"A coluna ID:{qualColuna} está sendo usada")
            return


        titulo = input("Digite o título da nova coluna: ")

        #.cell(em qual linha,índice da célula na linha).value = valor da célula
        aba.cell(row=1,column=qualColuna).value = titulo

        planilha.save(ARQUIVO)

        print(f"A coluna {titulo} foi adicionada com sucesso.")
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
    
    if oq=="del":
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
        qualColuna = int(input(f"Informe o número da coluna a deletar (entre 1 e {planilha.max_column}): "))
        
        if qualColuna < 1 or qualColuna > aba.max_column:
            print(f"A coluna {qualColuna} não está em uso.")
        
            return
        
        
        
        aba.delete_cols(qualColuna)
        planilha.save(ARQUIVO)        
        
        print(f"Coluna {qualColuna} removida com sucesso.")
        mostraPlanilha(mostraValores=True,qualAba=False,top=True)
        
    #mostra para o usuário a tabela com a coluna nova. O cabeçalho e a primeira linha
    # cabecalhos = [cell.value for cell in aba[1] if cell.value is not None]
    # linha1 = [cell.value for cell in aba[2] if cell.value is not None]
    # print(tabulate([linha1], headers=cabecalhos, tablefmt="grid"))
        mostraPlanilha(mostraValores=True,qualAba=0,top=True)

 
 
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
22 - FAZER O CABEÇALHO FICAR INVISÍVEL
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
            
            print(f"{LINHA}\nLISTANDO A PLANILHA {NOMEDOARQUIVO}")
            mostraPlanilha(mostraValores=True)
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
            acaoNaColuna("del")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")
            
        case "13":
            print(f"{LINHA}\nVAMOS ADICIONAR UMA NOVA COLUNA NA TABELA")
            acaoNaColuna("add")
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
            
            print("{LINHA}\nCALCULAR O VALOR TOTAL DE CADA PRODUTO")
            #valorTotalProduto(quant="1")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "18":
            
            print(f"{LINHA}\nFORMATAR O CABEÇALHO DA TABELA\n")
            #formatarTabela(oq="top")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "19":
            
            print("APLICAR BORDAS À TABELA\n")
            #formatarTabela(oq="bordas")
            input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
                    
        case "20":
            
                print("AJUSTAR O TAMANHO DAS COLUNAS NA TABELA\n")
                #formatarTabela(oq="colunas")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
                                                
        case "21":
            
                print("MESCLAR CÉLULAS DA TABELA\n")
                #formatarTabela(oq="top", case="2")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "22":
            
                print("OCULTAR O CABEÇALHO DA TABELA\n")
                #formatarTabela(oq="top", case="2")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "23":                                    
            
                print("APLICAR FILTROS NA TABELA\n")
                #formatarTabela(oq="filtros")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "24":
            
                print("TRANSFORMAR DADOS EM UMA PLANILHA\n")
                criaPlanilha(oq="nova")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "25":                        
            
                print("VAMOS GERAR UM GRÁFICO DA TABELA\n")
                #geraGrafico(aba="0",tipo="barras")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "26":
            
                print("VAMOS GERAR UM RELATÓRIO(DASHBOARD) DA TABELA\n")
                #geraDashboard(aba=0,tipo="1")
                input(f"{LINHAZINHA}\n{LI} Clique ENTER para voltar ao menu\n")            
            
        case "27":
            #finalizar o while
            break
        
        case _:
            #se deu mal. ficou preso no while
            input(F"NÃO EXISTE ESTA OPÇÃO\n{LI} Use ENTER PARA RETOMAR")                        