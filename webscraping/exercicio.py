# pip install requests
# pip install beautifulsoup4

from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import os

DIRETORIO_EXERCICIO = Path(__file__).resolve().parent
PASTA_SAIDA = DIRETORIO_EXERCICIO / "saida"
# ==========================================
# CONSTANTE DO NO ARQUIVO .env
# ==========================================
from dotenv import load_dotenv
load_dotenv()
URL_SITE = os.getenv("URL_SITE")


# Elementos visuais para formatação no console
LINHA = "========================================"
LINHAZINHA = "----------------------------------------"
OK = "[✔]"
ERRO = "[✕]"
ATENCAO = "[⚠]"
LI = "➤"


# ==========================================
# FUNÇÕES AUXILIARES / SUPORTE
# ==========================================

def criarPastas():
    """Cria a pasta para o arquivo texto (exercício 21) caso não exista."""
    try:
        os.makedirs(PASTA_SAIDA, exist_ok=True)
    except Exception as e:
        print(f"{ERRO} Erro ao criar pastas: {e}")



def mostrarRespostaHttp(resposta):
    """
    Mostra informações detalhadas sobre uma resposta HTTP.
    """
    codigo = resposta.status_code

    print(f"\n{LINHA}")
    print("           RESPOSTA HTTP")
    print(LINHA)
    print("Método:", resposta.request.method)
    print("URL:", resposta.url)
    print("Código HTTP:", codigo)
    print("Descrição:", resposta.reason)

    if 100 <= codigo < 200:
        print(f"Categoria: 1xx - Informativo | Código:{codigo}")
    elif 200 <= codigo < 300:
        print(f"Categoria: 2xx - Sucesso | Código:{codigo}")
    elif 300 <= codigo < 400:
        print(f"Categoria: 3xx - Redirecionamento | Código:{codigo}")
    elif 400 <= codigo < 500:
        print(f"Categoria: 4xx - Erro do cliente | Código:{codigo}")
    elif 500 <= codigo < 600:
        print(f"Categoria: 5xx - Erro do servidor | Código:{codigo}")
    else:
        print("Código HTTP não identificado.")
    print(LINHA)


def obterPagina(url=URL_SITE):
    """
    Acessa o website especificado e retorna o objeto BeautifulSoup tratado com exceções.
    """
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return BeautifulSoup(resposta.text, "html.parser")
    except requests.exceptions.Timeout:
        print(f"\n{ERRO} O servidor demorou muito para responder.")
        return None
    except requests.exceptions.ConnectionError:
        print(f"\n{ERRO} Não foi possível estabelecer conexão com o servidor\nVerifique sua conexão com a internet.")
        return None
    except requests.exceptions.HTTPError as erro:
        print(f"\n{ERRO} Erro HTTP: {erro}")
        return None
    except requests.exceptions.RequestException as erro:
        print(f"\n{ERRO} Erro durante a requisição: {erro}")
        return None


# Exercício 1 
# Crie uma função que realize uma requisição GET para o website. 
# A função deverá utilizar a biblioteca Requests e apresentar na tela o resultado da 
# requisição.
########################
def requisicaoGet():
    """Exercício 1: Realiza requisição GET e apresenta o resultado."""
    try:
        resposta = requests.get(URL_SITE, timeout=10)
        print(f"\n{OK} Requisição GET realizada com sucesso! Status: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"\n{ERRO} Falha na requisição: {e}")

# Exercício 2 
# Crie uma função que apresente na tela as principais informações da resposta 
# HTTP. A função deverá apresentar o método utilizado, a URL acessada, o código 
# HTTP, a descrição da resposta e a categoria da resposta. 
def informacoesHttp():
    """Exercício 2: Apresenta as principais informações da resposta HTTP."""
    try:
        resposta = requests.get(URL_SITE, timeout=10)
        mostrarRespostaHttp(resposta)
    except requests.exceptions.RequestException as e:
        print(f"\n{ERRO} Erro: {e}")

# Exercício 3 
# Crie uma função que trate possíveis erros durante a requisição HTTP. 
# O programa deverá tratar situações como tempo limite de conexão, falha de 
# conexão, erro HTTP e outros erros relacionados à requisição. 
# Utilize try, except e as exceções disponibilizadas pela biblioteca Requests. 
def tratarErrosHttp():
    """Exercício 3: Demonstra o tratamento de erros de requisição HTTP."""
    urlInvalida = "https://books.toscrape.com/pagina-que-nao-existe-12345.html"
    try:
        print(f"\nTentando acessar URL inválida para testar tratamento de erro...")
        resposta = requests.get(urlInvalida, timeout=5)
        resposta.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"{ATENCAO} Tempo limite excedido.")
    except requests.exceptions.ConnectionError:
        print(f"{ATENCAO} Falha de conexão.")
    except requests.exceptions.HTTPError as e:
        print(f"{OK} Erro HTTP tratado com sucesso: {e}")
    except requests.exceptions.RequestException as e:
        print(f"{ATENCAO} Erro geral: {e}")

# Exercício 4 
# Crie uma função que apresente na tela o código HTML retornado pelo website. 
# Utilize response.text para obter o conteúdo textual da resposta. 
def mostrarHtml():
    """Exercício 4: Apresenta o código HTML retornado pelo website."""
    try:
        resposta = requests.get(URL_SITE, timeout=10)
        resposta.raise_for_status()
        print(f"\n{LINHA}\n             HTML DA PÁGINA\n{LINHA}")
        print(resposta.text[:1000] + "\n... [Conteúdo truncado para exibição] ...")
    except requests.exceptions.RequestException as e:
        print(f"{ERRO} {e}")

# Exercício 5 
# Crie uma função que transforme o HTML recebido em um objeto BeautifulSoup. 
# Utilize a biblioteca BeautifulSoup para analisar o código HTML recebido. 
# A função deverá retornar o objeto criado para que as demais operações do 
# programa possam utilizá-lo. 
def obterSoup():
    """Exercício 5: Transforma o HTML em objeto BeautifulSoup."""
    soup = obterPagina()
    if soup:
        print(f"\n{OK} Objeto BeautifulSoup criado com sucesso!")
    return soup

# Exercício 6 
# Crie uma função que apresente o conteúdo da tag title da página. 
# Utilize o objeto BeautifulSoup para localizar a tag. 
def mostrarTitulo():
    """Exercício 6: Apresenta o conteúdo da tag title da página."""
    soup = obterPagina()
    if soup and soup.title:
        print(f"\n{LINHA}\n          TÍTULO DA PÁGINA\n{LINHA}")
        print(soup.title.get_text(strip=True))

# Exercício 7 
# Crie uma função que conte a quantidade de links existentes na página. 
# Utilize o método find_all() e a tag a. 
# Apresente a quantidade de links encontrados.
def contarLinks():
    """Exercício 7: Conta a quantidade de links (tag 'a') na página."""
    soup = obterPagina()
    if soup:
        links = soup.find_all("a")
        print(f"\n{OK} Quantidade de links encontrados: {len(links)}")

# Exercício 8 
# Crie uma função que conte a quantidade de imagens existentes na página. 
# Utilize o método find_all() e a tag img. 
# Apresente a quantidade de imagens encontradas. 
def contarImagens():
    """Exercício 8: Conta a quantidade de imagens (tag 'img') na página."""
    soup = obterPagina()
    if soup:
        imagens = soup.find_all("img")
        print(f"\n{OK} Quantidade de imagens encontradas: {len(imagens)}")

# Exercício 9 
# Crie uma função que conte a quantidade de parágrafos existentes na página. 
# Utilize o método find_all() e a tag p. 
# Apresente a quantidade de parágrafos encontrados. 
def econtarParagrafos():
    """Exercício 9: Conta a quantidade de parágrafos (tag 'p') na página."""
    soup = obterPagina()
    if soup:
        paragrafos = soup.find_all("p")
        print(f"\n{OK} Quantidade de parágrafos encontrados: {len(paragrafos)}")

# Exercício 10 
# Crie uma função que apresente a quantidade de livros encontrados na página. 
# Utilize um seletor CSS para localizar os elementos correspondentes aos produtos. 
def contarLivros():
    """Exercício 10: Apresenta a quantidade de livros encontrados na página."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{OK} Quantidade de livros na página: {len(livros)}")

# Exercício 11 
# Crie uma função que liste todos os títulos dos livros encontrados na página. 
# Utilize seletores CSS e atributos HTML para localizar o título de cada livro. 
# Apresente os títulos um por linha. 
def listarTitulos():
    """Exercício 11: Lista todos os títulos dos livros encontrados."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{LINHA}\n           TÍTULOS DOS LIVROS\n{LINHA}")
        for livro in livros:
            titulo = livro.h3.a.get("title")
            print(f"- {titulo}")

# Exercício 12 
# Crie uma função que liste todos os preços dos livros encontrados na página. 
# O programa deverá localizar os elementos que possuem o preço e apresentar os 
# valores na tela. 
def listarPrecos():
    """Exercício 12: Lista todos os preços dos livros encontrados."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{LINHA}\n             PREÇOS\n{LINHA}")
        for livro in livros:
            preco = livro.select_one(".price_color")
            if preco:
                print(f"- {preco.get_text(strip=True)}")

# Exercício 13 
# Crie uma função que apresente os títulos e preços dos livros. 
# O resultado deverá apresentar o título do livro e seu respectivo preço. 
def elistarLivrosEPrecos():
    """Exercício 13: Apresenta títulos e preços alinhados dos livros."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{LINHA}\n          LIVROS E PREÇOS\n{LINHA}")
        for livro in livros:
            titulo = livro.h3.a.get("title")
            preco = livro.select_one(".price_color").get_text(strip=True)
            print(f"{titulo} | {preco}")

# Exercício 14 
# Crie uma função que procure um livro pelo nome. 
# O usuário deverá informar o nome completo ou parte do nome. 
# A pesquisa deverá ignorar diferenças entre letras maiúsculas e minúsculas, 
# localizar o livro e apresentar seu título e preço. 
def procurarLivro():
    """Exercício 14: Procura um livro pelo nome (parcial ou completo)."""
    termo = input("Digite o nome ou parte do nome do livro: ").strip()
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    encontrado = False
    print(f"\n{LINHA}\n          RESULTADO DA PESQUISA\n{LINHA}")
    for livro in livros:
        titulo = livro.h3.a.get("title")
        if termo.lower() in titulo.lower():
            preco = livro.select_one(".price_color").get_text(strip=True)
            print(f"Título: {titulo}")
            print(f"Preço: {preco}")
            print(LINHAZINHA)
            encontrado = True
    if not encontrado:
        print("Nenhum livro encontrado com esse termo.")

# Exercício 15 
# Crie uma função que permita filtrar livros pelo preço máximo. 
# O usuário deverá informar um valor máximo. 
# O programa deverá apresentar somente os livros cujo preço seja menor ou igual ao 
# valor informado. 
def filtrarPorPreco():
    """Exercício 15: Filtra livros por preço máximo informado."""
    entrada = input("Preço máximo em libras (£): ")
    try:
        precoMaximo = float(entrada)
    except ValueError:
        print(f"{ERRO} Informe um valor numérico válido.")
        return

    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    encontrou = False
    print(f"\n{LINHA}\n          LIVROS DENTRO DO LIMITE\n{LINHA}")
    for livro in livros:
        titulo = livro.h3.a.get("title")
        precoTexto = livro.select_one(".price_color").get_text(strip=True)
        preco = float(precoTexto.replace("£", ""))
        if preco <= precoMaximo:
            print(f"{titulo} - £{preco:.2f}")
            encontrou = True
    if not encontrou:
        print("Nenhum livro encontrado abaixo deste valor.")

# Exercício 16 
# Crie uma função que converta o preço obtido no HTML para um valor numérico. 
# O programa deverá remover o símbolo da moeda e converter o valor para um 
# número. 
def converterPrecoNumerico():
    """Exercício 16: Converte o preço obtido no HTML para valor numérico float."""
    soup = obterPagina()
    if soup:
        livro = soup.select_one("article.product_pod")
        precoTexto = livro.select_one(".price_color").get_text(strip=True)
        precoNumerico = float(precoTexto.replace("£", ""))
        print(f"\n{OK} Exemplo de conversão: Texto '{precoTexto}' convertido para float -> {precoNumerico} (Tipo: {type(precoNumerico)})")

# Exercício 17 
# Crie uma função que identifique o livro mais barato encontrado na página. 
# O programa deverá coletar os livros, converter os preços para números, comparar 
# os valores e apresentar o livro com menor preço. 
def livroMaisBarato():
    """Exercício 17: Identifica o livro mais barato da página."""
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    livroBarato = None
    menorPreco = float("inf")

    for livro in livros:
        titulo = livro.h3.a.get("title")
        precoTexto = livro.select_one(".price_color").get_text(strip=True)
        preco = float(precoTexto.replace("£", ""))
        if preco < menorPreco:
            menorPreco = preco
            livroBarato = titulo

    print(f"\n{LINHA}\n          LIVRO MAIS BARATO\n{LINHA}")
    print(f"Título: {livroBarato}")
    print(f"Preço: £{menorPreco:.2f}")

# Exercício 18 
# Crie uma função que identifique o livro mais caro encontrado na página. 
# O programa deverá apresentar o título e o preço do livro mais caro. 
def livroMaisCaro():
    """Exercício 18: Identifica o livro mais caro da página."""
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    livroCaro = None
    maiorPreco = -1.0

    for livro in livros:
        titulo = livro.h3.a.get("title")
        precoTexto = livro.select_one(".price_color").get_text(strip=True)
        preco = float(precoTexto.replace("£", ""))
        if preco > maiorPreco:
            maiorPreco = preco
            livroCaro = titulo

    print(f"\n{LINHA}\n          LIVRO MAIS CARO\n{LINHA}")
    print(f"Título: {livroCaro}")
    print(f"Preço: £{maiorPreco:.2f}")

# Exercício 19 
# Crie uma função que calcule o preço médio dos livros encontrados na página. 
# O programa deverá coletar os preços, converter os valores para números, calcular 
# a média e apresentar o resultado. 
def precoMedio():
    """Exercício 19: Calcula o preço médio dos livros encontrados."""
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    soma = 0.0
    quantidade = len(livros)

    for livro in livros:
        precoTexto = livro.select_one(".price_color").get_text(strip=True)
        soma += float(precoTexto.replace("£", ""))

    media = soma / quantidade if quantidade > 0 else 0
    print(f"\n{LINHA}\n          PREÇO MÉDIO DOS LIVROS\n{LINHA}")
    print(f"Média: £{media:.2f}")

# Exercício 20 
# Crie uma função que apresente um resumo da coleta. 
# O resumo deverá apresentar a quantidade de livros, o menor preço, o maior preço 
# e o preço médio. 
def resumoColeta():
    """Exercício 20: Apresenta um resumo analítico completo da coleta."""
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    if not livros:
        print("Nenhum livro encontrado.")
        return

    precos = [float(l.select_one(".price_color").get_text(strip=True).replace("£", "")) for l in livros]
    
    print(f"\n{LINHA}\n          RESUMO DA COLETA\n{LINHA}")
    print(f"Quantidade de livros: {len(livros)}")
    print(f"Menor preço: £{min(precos):.2f}")
    print(f"Maior preço: £{max(precos):.2f}")
    print(f"Preço médio: £{sum(precos)/len(precos):.2f}")

# Exercício 21 
# Crie uma função que salve os títulos e preços dos livros em um arquivo de texto. 
# O arquivo deverá ser chamado livros.txt. 
# Cada livro deverá ocupar uma linha do arquivo. 
def salvarLivrosTxt():
    """Exercício 21: Salva títulos e preços no arquivo livros.txt dentro de saida/."""
    criarPastas()
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    caminhoArquivo = PASTA_SAIDA / "livros.txt"

    with open(caminhoArquivo, "w", encoding="utf-8") as arquivo:
        for livro in livros:
            titulo = livro.h3.a.get("title")
            preco = livro.select_one(".price_color").get_text(strip=True)
            arquivo.write(f"{titulo} | {preco}\n")

    print(f"\n{OK} Dados salvos com sucesso em: {caminhoArquivo}")

# Exercício 22 
# Crie uma função que gere um relatório de livros em um arquivo de texto. 
# O relatório deverá conter título do relatório, data da coleta, quantidade de livros, 
# títulos dos livros, preços, menor preço, maior preço e preço médio. 
def gerarRelatorio():
    """Exercício 22: Gera relatório detalhado em arquivo de texto na pasta saida/."""
    criarPastas()
    soup = obterPagina()
    if not soup: return
    
    livros = soup.select('article.product_pod')

    if not livros:
        print('Nenhum livro encontrado.')
        return

    # Extrai os preços em valores numéricos para o cálculo
    precos = []
    for l in livros:
        texto_preco = l.select_one('.price_color').get_text(strip=True) 
        """ get_text(strip=True) - difícil passar daqui"""
        # Mantém apenas os números e o ponto final
        preco_limpo = ''.join(c for c in texto_preco if c.isdigit() or c == '.')
        precos.append(float(preco_limpo))

    caminhoArquivo = PASTA_SAIDA / 'relatorio_livros.txt'
    dataAtual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Calcula as estatísticas
    qtd_livros = len(livros)
    menor_preco = min(precos)
    maior_preco = max(precos)
    media_preco = sum(precos) / qtd_livros

    # Escreve os dados no arquivo de texto
    with open(caminhoArquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write('=== RELATÓRIO DE LIVROS ===\n')
        arquivo.write(f'Data da coleta: {dataAtual}\n')
        arquivo.write(f'Quantidade de livros: {qtd_livros}\n')
        arquivo.write(f'Menor preço: £{menor_preco:.2f}\n')
        arquivo.write(f'Maior preço: £{maior_preco:.2f}\n')
        arquivo.write(f'Preço médio: £{media_preco:.2f}\n')
        arquivo.write('-' * 40 + '\n\n')

        for numero, livro in enumerate(livros, start=1):
            titulo = livro.h3.a.get('title')
            preco = livro.select_one('.price_color').get_text(strip=True)
            """ get_text(strip=True) - difícil passar daqui
            remove símbolos e caracteres "fantasmas" de codificações diferente """
            arquivo.write(f'{numero}. {titulo} - {preco}\n')

    print(f'\n{OK} Relatório criado com sucesso em: {caminhoArquivo}')

    #print(f"\n{OK} Relatório criado com sucesso em: {caminhoArquivo}")

# Exercício 23 
# Crie uma função que apresente os links dos livros encontrados. 
# O programa deverá utilizar os atributos HTML para obter o endereço associado a 
# cada livro. 
# Apresente o título do livro e sua URL. 
def listarLinksLivros():
    """Exercício 23: Apresenta os links e URLs completas associadas aos livros."""
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    print(f"\n{LINHA}\n          LINKS DOS LIVROS\n{LINHA}")
    for livro in livros:
        titulo = livro.h3.a.get("title")
        linkRelativo = livro.h3.a.get("href")
        urlCompleta = urljoin(URL_SITE, linkRelativo)
        print(f"- {titulo}\n  URL: {urlCompleta}\n")

# Exercício 24 
# Crie uma função que permita navegar pelas páginas do website. 
# O programa deverá acessar a página seguinte utilizando o link disponibilizado pelo 
# próprio website. 
# A função deverá identificar o link da próxima página, realizar uma nova requisição, 
# analisar o HTML e apresentar os livros encontrados. 
def navegarPaginas():
    """Exercício 24: Navega para a próxima página do website utilizando paginação."""
    soup = obterPagina()
    if not soup:
        return

    print(f"\n{OK} Página atual carregada. Analisando link de paginação...")
    botaoProximo = soup.select_one("li.next > a")
    
    if botaoProximo:
        linkProximo = botaoProximo.get("href")
        urlProximaPagina = urljoin(URL_SITE, linkProximo)
        print(f"Próxima página encontrada: {urlProximaPagina}")
        
        soupProxima = obterPagina(urlProximaPagina)
        if soupProxima:
            livrosProxima = soupProxima.select("article.product_pod")
            print(f"{OK} Sucesso ao acessar a próxima página! Quantidade de livros nela: {len(livrosProxima)}")
    else:
        print(f"{ATENCAO} Não há próxima página disponível.")

# Exercício 25 
# Crie uma função que realize uma coleta automatizada de várias páginas. 
# O robô deverá acessar uma página, coletar os livros, identificar a próxima página, 
# acessar a próxima página, repetir o processo, armazenar os dados coletados e 
# apresentar um resumo final. 
# O programa deverá utilizar tratamento de erros e respeitar os limites de acesso ao 
# website. 
def coletaAutomatizadaMultiplasPaginas():
    """Exercício 25: Realiza coleta automatizada em várias páginas em loop controlado."""
    urlAtual = URL_SITE
    pagina = 1
    totalLivrosColetados = 0

    print(f"\n{LINHA}\n      INICIANDO COLETA AUTOMATIZADA\n{LINHA}")
    
    while urlAtual and pagina <= 3:  # Limitando a 3 páginas por segurança de exemplo
        print(f"Acessando página {pagina}: {urlAtual}")
        soup = obterPagina(urlAtual)
        if not soup:
            break

        livros = soup.select("article.product_pod")
        totalLivrosColetados += len(livros)
        print(f"-> {len(livros)} livros coletados nesta página.")

        botaoProximo = soup.select_one("li.next > a")
        if botaoProximo:
            urlAtual = urljoin(urlAtual, botaoProximo.get("href"))
            pagina += 1
        else:
            urlAtual = None

    print(f"\n{OK} Coleta automatizada finalizada! Total acumulado de livros: {totalLivrosColetados}")


# ==========================================
# MENU
# ==========================================

def menu():
    """
    Exibe o menu principal de controle de todas as opções e exercícios.
    """
    while True:
        print(
            f"""
{LINHA}
       MENU PRINCIPAL - WEB SCRAPING
{LINHAZINHA}
1  - Realizar requisição GET
2  - Mostrar informações detalhadas HTTP
3  - Testar tratamento de erros HTTP
4  - Mostrar código HTML da página
5  - Converter em Objeto BeautifulSoup
{LINHAZINHA}
6  - Mostrar título da página
7  - Contar links
8  - Contar imagens
9  - Contar parágrafos
10 - Contar livros na página
{LINHAZINHA}
11 - Listar títulos dos livros
12 - Listar preços dos arquivos
13 - Listar títulos e preços
14 - Procurar livro por nome
15 - Filtrar livros por preço máximo
16 - Converter preço para numérico
{LINHAZINHA}
17 - Identificar livro mais barato
18 - Identificar livro mais caro
19 - Calcular preço médio dos livros
20 - Apresentar resumo completo da coleta
{LINHAZINHA}
21 - Salvar livros em TXT
22 - Gerar relatório detalhado de livros
{LINHAZINHA}
23 - Apresentar links dos livros
24 - Navegar para a próxima página
25 - Coleta automatizada em múltiplas páginas
{LINHAZINHA}
0  - Sair do programa
{LINHA}
""")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                requisicaoGet()
                input("\nPressione Enter para voltar ao menu.")
            case "2":
                informacoesHttp()
                input("\nPressione Enter para voltar ao menu.")
            case "3":
                tratarErrosHttp()
                input("\nPressione Enter para voltar ao menu.")
            case "4":
                mostrarHtml()
                input("\nPressione Enter para voltar ao menu.")
            case "5":
                obterSoup()
                input("\nPressione Enter para voltar ao menu.")
            case "6":
                mostrarTitulo()
                input("\nPressione Enter para voltar ao menu.")
            case "7":
                contarLinks()
                input("\nPressione Enter para voltar ao menu.")
            case "8":
                contarImagens()
                input("\nPressione Enter para voltar ao menu.")
            case "9":
                econtarParagrafos()
                input("\nPressione Enter para voltar ao menu.")
            case "10":
                contarLivros()
                input("\nPressione Enter para voltar ao menu.")
            case "11":
                listarTitulos()
                input("\nPressione Enter para voltar ao menu.")
            case "12":
                listarPrecos()
                input("\nPressione Enter para voltar ao menu.")
            case "13":
                elistarLivrosEPrecos()
                input("\nPressione Enter para voltar ao menu.")
            case "14":
                procurarLivro()
                input("\nPressione Enter para voltar ao menu.")
            case "15":
                filtrarPorPreco()
                input("\nPressione Enter para voltar ao menu.")
            case "16":
                converterPrecoNumerico()
                input("\nPressione Enter para voltar ao menu.")
            case "17":
                livroMaisBarato()
                input("\nPressione Enter para voltar ao menu.")
            case "18":
                livroMaisCaro()
                input("\nPressione Enter para voltar ao menu.")
            case "19":
                precoMedio()
                input("\nPressione Enter para voltar ao menu.")
            case "20":
                resumoColeta()
                input("\nPressione Enter para voltar ao menu.")
            case "21":
                salvarLivrosTxt()
                input("\nPressione Enter para voltar ao menu.")
            case "22":
                gerarRelatorio()
                input("\nPressione Enter para voltar ao menu.")
            case "23":
                listarLinksLivros()
                input("\nPressione Enter para voltar ao menu.")
            case "24":
                navegarPaginas()
                input("\nPressione Enter para voltar ao menu.")
            case "25":
                coletaAutomatizadaMultiplasPaginas()
                input("\nPressione Enter para voltar ao menu.")
            case "0":
                print("\nRobô encerrado com sucesso. Até logo!")
                break
            case _:
                print(f"\n{ERRO} Opção inválida. Escolha um número válido do menu.")
                input("\nPressione Enter para tentar novamente.")


if __name__ == "__main__":
    menu()