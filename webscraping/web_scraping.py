# pip install requests
# pip install beautifulsoup4

import requests

from bs4 import BeautifulSoup



URL_SITE = "https://books.toscrape.com/"



def mostrar_resposta_http(resposta):
    """
    Mostra informações sobre uma resposta HTTP.

    Parâmetro:

        resposta:
            Objeto Response retornado pelo requests.

    Utiliza:

        status_code
            Código numérico da resposta HTTP.

        reason
            Descrição do código HTTP.

        url
            URL utilizada na requisição.

        request.method
            Método HTTP utilizado.

    Categorias HTTP:

        1xx - Informativo
        2xx - Sucesso
        3xx - Redirecionamento
        4xx - Erro do cliente
        5xx - Erro do servidor

    """

    codigo = resposta.status_code


    print(
        "\n========================================"
    )


    print(
        "           RESPOSTA HTTP"
    )


    print(
        "========================================"
    )


    print(
        "Método:",
        resposta.request.method
    )


    print(
        "URL:",
        resposta.url
    )


    print(
        "Código HTTP:",
        codigo
    )


    print(
        "Descrição:",
        resposta.reason
    )


    if 100 <= codigo < 200:

        print(
            "Categoria: 1xx - Informativo"
        )


        print(
            "Resultado: resposta informativa."
        )


    elif 200 <= codigo < 300:

        print(
            "Categoria: 2xx - Sucesso"
        )


        print(
            "Resultado: requisição processada "
            "com sucesso."
        )


    elif 300 <= codigo < 400:

        print(
            "Categoria: 3xx - Redirecionamento"
        )


        print(
            "Resultado: a resposta indica "
            "um redirecionamento."
        )


    elif 400 <= codigo < 500:

        print(
            "Categoria: 4xx - Erro do cliente"
        )


        print(
            "Resultado: houve um problema "
            "na requisição ou no acesso."
        )


    elif 500 <= codigo < 600:

        print(
            "Categoria: 5xx - Erro do servidor"
        )


        print(
            "Resultado: o servidor apresentou "
            "um problema."
        )


    else:

        print(
            "Categoria: Código HTTP não identificado."
        )


    print(
        "========================================"
    )



def obter_pagina():
    """
    Acessa o website e retorna o objeto BeautifulSoup.

    Utiliza:

        requests.get()
            Realiza uma requisição HTTP GET.

        timeout
            Define o tempo máximo de espera.

        raise_for_status()
            Identifica respostas HTTP de erro.

        BeautifulSoup()
            Analisa o código HTML recebido.

    Retorno:

        BeautifulSoup:
            Página HTML analisada.

        None:
            Caso ocorra algum erro.
    """

    try:

        resposta = requests.get(
            URL_SITE,
            timeout=10
        )


        mostrar_resposta_http(
            resposta
        )


        resposta.raise_for_status()


        soup = BeautifulSoup(
            resposta.text,
            "html.parser"
        )


        return soup


    except requests.exceptions.Timeout:

        print(
            "\nERRO"
        )


        print(
            "O servidor demorou muito "
            "para responder."
        )


        return None


    except requests.exceptions.ConnectionError:

        print(
            "\nERRO"
        )


        print(
            "Não foi possível estabelecer "
            "conexão com o servidor."
        )


        return None


    except requests.exceptions.HTTPError as erro:

        print(
            "\nERRO HTTP"
        )


        print(
            erro
        )


        return None


    except requests.exceptions.RequestException as erro:

        print(
            "\nERRO DURANTE A REQUISIÇÃO"
        )


        print(
            erro
        )


        return None




def testar_conexao():
    """
    Realiza uma requisição GET para testar
    o acesso ao website.

    A função mostra:

        - URL;
        - método HTTP;
        - código HTTP;
        - descrição;
        - categoria da resposta.
    """

    try:

        resposta = requests.get(
            URL_SITE,
            timeout=10
        )


        mostrar_resposta_http(
            resposta
        )


    except requests.exceptions.Timeout:

        print(
            "\nErro: tempo limite excedido."
        )


    except requests.exceptions.ConnectionError:

        print(
            "\nErro: não foi possível "
            "conectar ao servidor."
        )


    except requests.exceptions.RequestException as erro:

        print(
            "\nErro durante a requisição:"
        )


        print(
            erro
        )





def mostrar_html():
    """
    Mostra o código HTML recebido do website.

    Utiliza:

        response.text
            Obtém o conteúdo textual da resposta.
    """

    try:

        resposta = requests.get(
            URL_SITE,
            timeout=10
        )


        mostrar_resposta_http(
            resposta
        )


        resposta.raise_for_status()


        print(
            "\n========================================"
        )


        print(
            "             HTML DA PÁGINA"
        )


        print(
            "========================================"
        )


        print(
            resposta.text
        )


    except requests.exceptions.Timeout:

        print(
            "Erro: tempo limite excedido."
        )


    except requests.exceptions.ConnectionError:

        print(
            "Erro: não foi possível "
            "conectar ao servidor."
        )


    except requests.exceptions.HTTPError as erro:

        print(
            "Erro HTTP:"
        )


        print(
            erro
        )


    except requests.exceptions.RequestException as erro:

        print(
            "Erro durante a requisição:"
        )


        print(
            erro
        )





def mostrar_titulo():
    """
    Mostra o título da página.

    Utiliza:

        soup.title
            Localiza a tag <title>.

        text
            Obtém o conteúdo textual da tag.
    """

    soup = obter_pagina()


    if soup is None:

        return


    if soup.title:

        titulo = soup.title.get_text(
            strip=True
        )


        print(
            "\n========================================"
        )


        print(
            "          TÍTULO DA PÁGINA"
        )


        print(
            "========================================"
        )


        print(
            titulo
        )


    else:

        print(
            "A página não possui uma tag <title>."
        )





def analisar_html():
    """
    Analisa elementos básicos encontrados
    no HTML.

    Utiliza:

        find_all()
            Localiza elementos de determinada tag.
    """

    soup = obter_pagina()


    if soup is None:

        return


    links = soup.find_all(
        "a"
    )


    imagens = soup.find_all(
        "img"
    )


    paragrafos = soup.find_all(
        "p"
    )


    titulos = soup.find_all(
        ["h1", "h2", "h3"]
    )


    print(
        "\n========================================"
    )


    print(
        "             ANÁLISE DO HTML"
    )


    print(
        "========================================"
    )


    print(
        "Links:",
        len(links)
    )


    print(
        "Imagens:",
        len(imagens)
    )


    print(
        "Parágrafos:",
        len(paragrafos)
    )


    print(
        "Títulos:",
        len(titulos)
    )





def listar_titulos():
    """
    Lista os títulos dos livros encontrados.

    Utiliza:

        select()
            Localiza elementos utilizando
            seletores CSS.

        get()
            Obtém o valor de um atributo HTML.
    """

    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    print(
        "\n========================================"
    )


    print(
        "           TÍTULOS DOS LIVROS"
    )


    print(
        "========================================"
    )


    for livro in livros:

        titulo = livro.h3.a.get(
            "title"
        )


        print(
            "-",
            titulo
        )





def listar_precos():
    """
    Lista os preços dos livros.

    Utiliza:

        select_one()
            Localiza o primeiro elemento
            correspondente ao seletor.

        get_text()
            Obtém o texto do elemento.
    """

    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    print(
        "\n========================================"
    )


    print(
        "             PREÇOS"
    )


    print(
        "========================================"
    )


    for livro in livros:

        preco = livro.select_one(
            ".price_color"
        )


        if preco:

            print(
                "-",
                preco.get_text(
                    strip=True
                )
            )





def listar_livros():
    """
    Lista títulos e preços dos livros.

    Utiliza:

        CSS Selectors
            Localiza os elementos desejados.

        get_text()
            Obtém o conteúdo textual.
    """

    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    print(
        "\n========================================"
    )


    print(
        "          LIVROS E PREÇOS"
    )


    print(
        "========================================"
    )


    for livro in livros:

        titulo = livro.h3.a.get(
            "title"
        )


        preco_elemento = livro.select_one(
            ".price_color"
        )


        if preco_elemento:

            preco = preco_elemento.get_text(
                strip=True
            )


        else:

            preco = "Preço não encontrado"


        print(
            f"{titulo} | {preco}"
        )




def contar_livros():
    """
    Conta a quantidade de livros encontrada
    na página.

    Utiliza:

        len()
            Retorna a quantidade de elementos.
    """

    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    quantidade = len(
        livros
    )


    print(
        "\n========================================"
    )


    print(
        "           QUANTIDADE DE LIVROS"
    )


    print(
        "========================================"
    )


    print(
        quantidade
    )




def procurar_livro():
    """
    Procura um livro pelo nome.

    A pesquisa não diferencia letras
    maiúsculas de minúsculas.

    Utiliza:

        lower()
            Converte o texto para letras minúsculas.

        in
            Verifica se um texto está dentro
            de outro.
    """

    termo = input(
        "Digite o nome ou parte do nome: "
    )


    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    encontrado = False


    print(
        "\n========================================"
    )


    print(
        "          RESULTADO DA PESQUISA"
    )


    print(
        "========================================"
    )


    for livro in livros:

        titulo = livro.h3.a.get(
            "title"
        )


        if termo.lower() in titulo.lower():

            preco_elemento = livro.select_one(
                ".price_color"
            )


            if preco_elemento:

                preco = preco_elemento.get_text(
                    strip=True
                )


            else:

                preco = "Preço não encontrado"


            print(
                "Título:",
                titulo
            )


            print(
                "Preço:",
                preco
            )


            print(
                "-" * 40
            )


            encontrado = True


    if not encontrado:

        print(
            "Nenhum livro encontrado."
        )




def filtrar_por_preco():
    """
    Lista livros que possuem preço menor
    ou igual ao valor informado.

    Utiliza:

        float()
            Converte texto para número.

        replace()
            Remove o símbolo da moeda.

        if
            Realiza a comparação.
    """

    entrada = input(
        "Preço máximo em libras: "
    )


    try:

        preco_maximo = float(
            entrada
        )


    except ValueError:

        print(
            "Informe um valor numérico."
        )


        return


    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    encontrou = False


    print(
        "\n========================================"
    )


    print(
        "          LIVROS DENTRO DO LIMITE"
    )


    print(
        "========================================"
    )


    for livro in livros:

        titulo = livro.h3.a.get(
            "title"
        )


        preco_elemento = livro.select_one(
            ".price_color"
        )


        if not preco_elemento:

            continue


        preco_texto = preco_elemento.get_text(
            strip=True
        )


        preco = float(
            preco_texto.replace(
                "£",
                ""
            )
        )


        if preco <= preco_maximo:

            print(
                f"{titulo} - £{preco:.2f}"
            )


            encontrou = True


    if not encontrou:

        print(
            "Nenhum livro encontrado."
        )





def salvar_livros():
    """
    Salva os títulos e preços dos livros
    em um arquivo de texto.

    Utiliza:

        open()
            Abre ou cria um arquivo.

        mode='w'
            Escreve no arquivo.

        encoding='utf-8'
            Permite trabalhar com caracteres especiais.
    """

    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    with open(
        "livros.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        for livro in livros:

            titulo = livro.h3.a.get(
                "title"
            )


            preco_elemento = livro.select_one(
                ".price_color"
            )


            if preco_elemento:

                preco = preco_elemento.get_text(
                    strip=True
                )


            else:

                preco = "Preço não encontrado"


            arquivo.write(
                f"{titulo} | {preco}\n"
            )


    print(
        "\nDados salvos com sucesso."
    )


    print(
        "Arquivo: livros.txt"
    )




def gerar_relatorio():
    """
    Gera um relatório dos livros encontrados.

    O relatório contém:

        - quantidade de livros;
        - títulos;
        - preços.
    """

    soup = obter_pagina()


    if soup is None:

        return


    livros = soup.select(
        "article.product_pod"
    )


    with open(
        "relatorio_livros.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(
            "RELATÓRIO DE LIVROS\n"
        )


        arquivo.write(
            "=" * 50
        )


        arquivo.write(
            "\n\n"
        )


        arquivo.write(
            f"Quantidade de livros: {len(livros)}\n\n"
        )


        for numero, livro in enumerate(
            livros,
            start=1
        ):

            titulo = livro.h3.a.get(
                "title"
            )


            preco_elemento = livro.select_one(
                ".price_color"
            )


            if preco_elemento:

                preco = preco_elemento.get_text(
                    strip=True
                )


            else:

                preco = "Preço não encontrado"


            arquivo.write(
                f"{numero}. {titulo}\n"
            )


            arquivo.write(
                f"   Preço: {preco}\n\n"
            )


    print(
        "\nRelatório criado com sucesso."
    )


    print(
        "Arquivo: relatorio_livros.txt"
    )





def menu():
    """
    Exibe o menu principal do robô.

    O menu reúne as funcionalidades
    de requisição HTTP, análise HTML,
    web scraping e armazenamento.
    """

    while True:

        print(
            """


Requisições http

1  - Realizar requisição GET
2  - Mostrar código HTML
3  - Mostrar título da página

Análuse html

4  - Analisar estrutura HTML

web scraping

5  - Listar títulos dos livros
6  - Listar preços dos livros
7  - Listar títulos e preços
8  - Contar livros
9  - Procurar livro por nome
10 - Filtrar livros por preço

Armazenamento

11 - Salvar livros em arquivo
12 - Gerar relatório

0  - Sair


"""
        )


        opcao = input(
            "Escolha uma opção: "
        )


        match opcao:

            case "1":

                testar_conexao()
                input("Pressione Enter para voltar ao menu.")
                


            case "2":

                mostrar_html()
                input("Pressione Enter para voltar ao menu.")
                


            case "3":

                mostrar_titulo()
                input("Pressione Enter para voltar ao menu.")
                


            case "4":

                analisar_html()
                input("Pressione Enter para voltar ao menu.")


            case "5":

                listar_titulos()
                input("Pressione Enter para voltar ao menu.")


            case "6":

                listar_precos()
                input("Pressione Enter para voltar ao menu.")


            case "7":

                listar_livros()
                input("Pressione Enter para voltar ao menu.")


            case "8":

                contar_livros()
                input("Pressione Enter para voltar ao menu.")


            case "9":

                procurar_livro()
                input("Pressione Enter para voltar ao menu.")


            case "10":

                filtrar_por_preco()
                input("Pressione Enter para voltar ao menu.")

            case "11":

                salvar_livros()
                input("Pressione Enter para voltar ao menu.")


            case "12":

                gerar_relatorio()
                input("Pressione Enter para voltar ao menu.")


            case "0":

                print(
                    "\nRobô encerrado."
                )


                break


            case _:

                print(
                    "\nOpção inválida."
                )




if __name__ == "__main__":

    menu()