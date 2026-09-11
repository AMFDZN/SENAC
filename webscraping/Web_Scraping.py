# pip install requests
# pip install beautifulsoup4

from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import os

# ==========================================
# CONSTANTES E DIRETÓRIOS DO PROJETO
# ==========================================
DIRETORIO_EXERCICIO = Path(__file__).resolve().parent
PASTA_SAIDA = DIRETORIO_EXERCICIO / "saida"

URL_SITE = "https://books.toscrape.com/"

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
    """Cria a pasta 'saida' caso não exista."""
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
        print("Categoria: 1xx - Informativo")
    elif 200 <= codigo < 300:
        print("Categoria: 2xx - Sucesso")
    elif 300 <= codigo < 400:
        print("Categoria: 3xx - Redirecionamento")
    elif 400 <= codigo < 500:
        print("Categoria: 4xx - Erro do cliente")
    elif 500 <= codigo < 600:
        print("Categoria: 5xx - Erro do servidor")
    else:
        print("Categoria: Código HTTP não identificado.")
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
        print(f"\n{ERRO} Não foi possível estabelecer conexão com o servidor.")
        return None
    except requests.exceptions.HTTPError as erro:
        print(f"\n{ERRO} Erro HTTP: {erro}")
        return None
    except requests.exceptions.RequestException as erro:
        print(f"\n{ERRO} Erro durante a requisição: {erro}")
        return None


# ==========================================
# EXERCÍCIOS 1 A 25
# ==========================================

def exercicio01_requisicaoGet():
    """Exercício 1: Realiza requisição GET e apresenta o resultado."""
    try:
        resposta = requests.get(URL_SITE, timeout=10)
        print(f"\n{OK} Requisição GET realizada com sucesso! Status: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"\n{ERRO} Falha na requisição: {e}")


def exercicio02_informacoesHttp():
    """Exercício 2: Apresenta as principais informações da resposta HTTP."""
    try:
        resposta = requests.get(URL_SITE, timeout=10)
        mostrarRespostaHttp(resposta)
    except requests.exceptions.RequestException as e:
        print(f"\n{ERRO} Erro: {e}")


def exercicio03_tratarErrosHttp():
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


def exercicio04_mostrarHtml():
    """Exercício 4: Apresenta o código HTML retornado pelo website."""
    try:
        resposta = requests.get(URL_SITE, timeout=10)
        resposta.raise_for_status()
        print(f"\n{LINHA}\n             HTML DA PÁGINA\n{LINHA}")
        print(resposta.text[:1000] + "\n... [Conteúdo truncado para exibição] ...")
    except requests.exceptions.RequestException as e:
        print(f"{ERRO} {e}")


def exercicio05_obterSoup():
    """Exercício 5: Transforma o HTML em objeto BeautifulSoup."""
    soup = obterPagina()
    if soup:
        print(f"\n{OK} Objeto BeautifulSoup criado com sucesso!")
    return soup


def exercicio06_mostrarTitulo():
    """Exercício 6: Apresenta o conteúdo da tag title da página."""
    soup = obterPagina()
    if soup and soup.title:
        print(f"\n{LINHA}\n          TÍTULO DA PÁGINA\n{LINHA}")
        print(soup.title.get_text(strip=True))


def exercicio07_contarLinks():
    """Exercício 7: Conta a quantidade de links (tag 'a') na página."""
    soup = obterPagina()
    if soup:
        links = soup.find_all("a")
        print(f"\n{OK} Quantidade de links encontrados: {len(links)}")


def exercicio08_contarImagens():
    """Exercício 8: Conta a quantidade de imagens (tag 'img') na página."""
    soup = obterPagina()
    if soup:
        imagens = soup.find_all("img")
        print(f"\n{OK} Quantidade de imagens encontradas: {len(imagens)}")


def exercicio09_contarParagrafos():
    """Exercício 9: Conta a quantidade de parágrafos (tag 'p') na página."""
    soup = obterPagina()
    if soup:
        paragrafos = soup.find_all("p")
        print(f"\n{OK} Quantidade de parágrafos encontrados: {len(paragrafos)}")


def exercicio10_contarLivros():
    """Exercício 10: Apresenta a quantidade de livros encontrados na página."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{OK} Quantidade de livros na página: {len(livros)}")


def exercicio11_listarTitulos():
    """Exercício 11: Lista todos os títulos dos livros encontrados."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{LINHA}\n           TÍTULOS DOS LIVROS\n{LINHA}")
        for livro in livros:
            titulo = livro.h3.a.get("title")
            print(f"- {titulo}")


def exercicio12_listarPrecos():
    """Exercício 12: Lista todos os preços dos livros encontrados."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{LINHA}\n             PREÇOS\n{LINHA}")
        for livro in livros:
            preco = livro.select_one(".price_color")
            if preco:
                print(f"- {preco.get_text(strip=True)}")


def exercicio13_listarLivrosEPrecos():
    """Exercício 13: Apresenta títulos e preços alinhados dos livros."""
    soup = obterPagina()
    if soup:
        livros = soup.select("article.product_pod")
        print(f"\n{LINHA}\n          LIVROS E PREÇOS\n{LINHA}")
        for livro in livros:
            titulo = livro.h3.a.get("title")
            preco = livro.select_one(".price_color").get_text(strip=True)
            print(f"{titulo} | {preco}")


def exercicio14_procurarLivro():
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


def exercicio15_filtrarPorPreco():
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


def exercicio16_converterPrecoNumerico():
    """Exercício 16: Converte o preço obtido no HTML para valor numérico float."""
    soup = obterPagina()
    if soup:
        livro = soup.select_one("article.product_pod")
        precoTexto = livro.select_one(".price_color").get_text(strip=True)
        precoNumerico = float(precoTexto.replace("£", ""))
        print(f"\n{OK} Exemplo de conversão: Texto '{precoTexto}' convertido para float -> {precoNumerico} (Tipo: {type(precoNumerico)})")


def exercicio17_livroMaisBarato():
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


def exercicio18_livroMaisCaro():
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


def exercicio19_precoMedio():
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


def exercicio20_resumoColeta():
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


def exercicio21_salvarLivrosTxt():
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


def exercicio22_gerarRelatorio():
    """Exercício 22: Gera relatório detalhado em arquivo de texto na pasta saida/."""
    criarPastas()
    soup = obterPagina()
    if not soup:
        return

    livros = soup.select("article.product_pod")
    precos = [float(l.select_one(".price_color").get_text(strip=True).replace("£", "")) for l in livros]
    
    caminhoArquivo = PASTA_SAIDA / "relatorio_livros.txt"
    dataAtual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(caminhoArquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO DE LIVROS - WEB SCRAPING\n")
        arquivo.write(f"Data da coleta: {dataAtual}\n")
        arquivo.write(f"{'='*50}\n\n")
        arquivo.write(f"Quantidade de livros: {len(livros)}\n")
        arquivo.write(f"Menor preço: £{min(precos):.2f}\n")
        arquivo.write(f"Maior preço: £{max(precos):.2f}\n")
        arquivo.write(f"Preço médio: £{sum(precos)/len(precos):.2f}\n\n")
        arquivo.write(f"{'='*50}\n\n")

        for numero, livro in enumerate(livros, start=1):
            titulo = livro.h3.a.get("title")
            preco = livro.select_one(".price_color").get_text(strip=True)
            arquivo.write(f"{numero}. {titulo} - {preco}\n")

    print(f"\n{OK} Relatório criado com sucesso em: {caminhoArquivo}")


def exercicio23_listarLinksLivros():
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


def exercicio24_navegarPaginas():
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


def exercicio25_coletaAutomatizadaMultiplasPaginas():
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
# MENU PRINCIPAL DO PROGRAMA
# ==========================================

def menu():
    """
    Exibe o menu principal de controle de todas as opções e exercícios.
    """
    while True:
        print(
            """


========================================
       MENU PRINCIPAL - WEB SCRAPING
========================================

Requisições HTTP e Tratamento
1  - Realizar requisição GET (Ex 1)
2  - Mostrar informações detalhadas HTTP (Ex 2)
3  - Testar tratamento de erros HTTP (Ex 3)
4  - Mostrar código HTML da página (Ex 4)
5  - Converter em Objeto BeautifulSoup (Ex 5)

Análise e Contagem HTML
6  - Mostrar título da página (Ex 6)
7  - Contar links (Ex 7)
8  - Contar imagens (Ex 8)
9  - Contar parágrafos (Ex 9)
10 - Contar livros na página (Ex 10)

Extração de Dados dos Livros
11 - Listar títulos dos livros (Ex 11)
12 - Listar preços dos arquivos (Ex 12)
13 - Listar títulos e preços (Ex 13)
14 - Procurar livro por nome (Ex 14)
15 - Filtrar livros por preço máximo (Ex 15)
16 - Converter preço para numérico (Ex 16)

Estatísticas e Análises Avançadas
17 - Identificar livro mais barato (Ex 17)
18 - Identificar livro mais caro (Ex 18)
19 - Calcular preço médio dos livros (Ex 19)
20 - Apresentar resumo completo da coleta (Ex 20)

Armazenamento e Arquivos
21 - Salvar livros em TXT (Ex 21)
22 - Gerar relatório detalhado de livros (Ex 22)

Navegação e Automação Web
23 - Apresentar links dos livros (Ex 23)
24 - Navegar para a próxima página (Ex 24)
25 - Coleta automatizada em múltiplas páginas (Ex 25)

0  - Sair do programa
========================================
"""
        )

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                exercicio01_requisicaoGet()
                input("\nPressione Enter para voltar ao menu.")
            case "2":
                exercicio02_informacoesHttp()
                input("\nPressione Enter para voltar ao menu.")
            case "3":
                exercicio03_tratarErrosHttp()
                input("\nPressione Enter para voltar ao menu.")
            case "4":
                exercicio04_mostrarHtml()
                input("\nPressione Enter para voltar ao menu.")
            case "5":
                exercicio05_obterSoup()
                input("\nPressione Enter para voltar ao menu.")
            case "6":
                exercicio06_mostrarTitulo()
                input("\nPressione Enter para voltar ao menu.")
            case "7":
                exercicio07_contarLinks()
                input("\nPressione Enter para voltar ao menu.")
            case "8":
                exercicio08_contarImagens()
                input("\nPressione Enter para voltar ao menu.")
            case "9":
                exercicio09_contarParagrafos()
                input("\nPressione Enter para voltar ao menu.")
            case "10":
                exercicio10_contarLivros()
                input("\nPressione Enter para voltar ao menu.")
            case "11":
                exercicio11_listarTitulos()
                input("\nPressione Enter para voltar ao menu.")
            case "12":
                exercicio12_listarPrecos()
                input("\nPressione Enter para voltar ao menu.")
            case "13":
                exercicio13_listarLivrosEPrecos()
                input("\nPressione Enter para voltar ao menu.")
            case "14":
                exercicio14_procurarLivro()
                input("\nPressione Enter para voltar ao menu.")
            case "15":
                exercicio15_filtrarPorPreco()
                input("\nPressione Enter para voltar ao menu.")
            case "16":
                exercicio16_converterPrecoNumerico()
                input("\nPressione Enter para voltar ao menu.")
            case "17":
                exercicio17_livroMaisBarato()
                input("\nPressione Enter para voltar ao menu.")
            case "18":
                exercicio18_livroMaisCaro()
                input("\nPressione Enter para voltar ao menu.")
            case "19":
                exercicio19_precoMedio()
                input("\nPressione Enter para voltar ao menu.")
            case "20":
                exercicio20_resumoColeta()
                input("\nPressione Enter para voltar ao menu.")
            case "21":
                exercicio21_salvarLivrosTxt()
                input("\nPressione Enter para voltar ao menu.")
            case "22":
                exercicio22_gerarRelatorio()
                input("\nPressione Enter para voltar ao menu.")
            case "23":
                exercicio23_listarLinksLivros()
                input("\nPressione Enter para voltar ao menu.")
            case "24":
                exercicio24_navegarPaginas()
                input("\nPressione Enter para voltar ao menu.")
            case "25":
                exercicio25_coletaAutomatizadaMultiplasPaginas()
                input("\nPressione Enter para voltar ao menu.")
            case "0":
                print("\nRobô encerrado com sucesso. Até logo!")
                break
            case _:
                print(f"\n{ERRO} Opção inválida. Escolha um número válido do menu.")
                input("\nPressione Enter para tentar novamente.")


if __name__ == "__main__":
    menu()