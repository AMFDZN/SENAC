import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()
URL_SITE = os.getenv("URL_SITE")
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
# Utilize as bibliotecas Requests e BeautifulSoup para realizar requisições HTTP, 
# acessar páginas web, analisar estruturas HTML e extrair dados públicos de 
# websites. 
# Utilize como ambiente de treinamento o site Books to Scrape. 
# Organize o programa de forma modularizada, utilizando funções separadas para 
# cada operação, controle pelo menu principal, tratamento de erros, verificação das 
# respostas HTTP e opção para encerrar a execução do programa. 
# O programa deverá realizar requisições utilizando o método GET e trabalhar com 
# os dados públicos disponibilizados pelo website. 
 
# Exercício 1 
# Crie uma função que realize uma requisição GET para o website. 
# A função deverá utilizar a biblioteca Requests e apresentar na tela o resultado da 
# requisição.
def verifica_status_url(resposta):
    if not resposta:
        resposta = requests.get(URL_SITE,timeout=10)
    codigo = resposta.status_code

    print("Método:",resposta.request.method)

    print("URL:",resposta.url)

    print("Código HTTP:",codigo)

    print("Descrição:",resposta.reason)

    if 100 <= codigo < 200:

        print(f"Categoria: 1xx - Informativo | Codigo {codigo}")

        print(f"Resultado: resposta informativa.")


    elif 200 <= codigo < 300:

        print(f"Categoria: 2xx - Sucesso | Código:{codigo}")

        print("Resultado: requisição processada com sucesso.")


    elif 300 <= codigo < 400:

        print(f"Categoria: 3xx - Redirecionamento | Código:{codigo}")

        print("Resultado: a resposta indica um redirecionamento.")


    elif 400 <= codigo < 500:

        print(f"Categoria: 4xx - Erro do cliente | Código:{codigo}" )


        print(
            "Resultado: houve um problema "
            "na requisição ou no acesso."
        )


    elif 500 <= codigo < 600:

        print(f"Categoria: 5xx - Erro do servidor | Código:{codigo}")


        print("Resultado: o servidor apresentou "
            "um problema." )

    else:

        print("Categoria: Código HTTP não identificado.")

    print("========================================")


def request_pagina():
    try:

        resposta = requests.get(URL_SITE,timeout=10)
        verifica_status_url(resposta)
        resposta.raise_for_status()
        soup = BeautifulSoup( resposta.text,"html.parser")
        return soup

    except requests.exceptions.Timeout:

        print("\nERRO")
        print("O servidor demorou muito para responder.")
        return None


    except requests.exceptions.ConnectionError:

        print("\nERRO")
        print("Não foi possível estabelecer a conexão com o servidor\nVerifique sua conexão, Acelio.")
        return None


    except requests.exceptions.HTTPError as erro:

        print("\nERRO HTTP")
        print(erro)
        return None


    except requests.exceptions.RequestException as erro:

        print("\nERRO NA REQUISIÇÃO")
        print(erro)
        return None

def testar_conexao():

    try:

        resposta = requests.get(URL_SITE,timeout=10)


        mostrar_resposta_http(resposta)


    except requests.exceptions.Timeout:

        print("\nErro: tempo limite excedido.")


    except requests.exceptions.ConnectionError:

        print("\nErro: não foi possível conectar ao servidor.")


    except requests.exceptions.RequestException as erro:

        print("\nErro durante a requisição:")


        print(erro)

while True:
    opcao=input("""
                1
                2
                3
                4
                5
                6
                : 
                """)
    
    match opcao:
        case "1":
            request_pagina()
            input=(f"{LI} Use ENTER para voltar ao menu")
        
            
# Exercício 2 
# Crie uma função que apresente na tela as principais informações da resposta 
# HTTP. A função deverá apresentar o método utilizado, a URL acessada, o código 
# HTTP, a descrição da resposta e a categoria da resposta. 
        case "2":
                    request_pagina()
                    verifica_status_url(resposta)
                    input=(f"{LI} Use ENTER para voltar ao menu")
        case _:
            break 
# Exercício 3 
# Crie uma função que trate possíveis erros durante a requisição HTTP. 
# O programa deverá tratar situações como tempo limite de conexão, falha de 
# conexão, erro HTTP e outros erros relacionados à requisição. 
# Utilize try, except e as exceções disponibilizadas pela biblioteca Requests. 
 
# Exercício 4 
# Crie uma função que apresente na tela o código HTML retornado pelo website. 
# Utilize response.text para obter o conteúdo textual da resposta. 
 
# Exercício 5 
# Crie uma função que transforme o HTML recebido em um objeto BeautifulSoup. 
# Utilize a biblioteca BeautifulSoup para analisar o código HTML recebido. 
# A função deverá retornar o objeto criado para que as demais operações do 
# programa possam utilizá-lo. 
 
# Exercício 6 
# Crie uma função que apresente o conteúdo da tag title da página. 
# Utilize o objeto BeautifulSoup para localizar a tag. 
 
# Exercício 7 
# Crie uma função que conte a quantidade de links existentes na página. 
# Utilize o método find_all() e a tag a. 
# Apresente a quantidade de links encontrados. 
 
# Exercício 8 
# Crie uma função que conte a quantidade de imagens existentes na página. 
# Utilize o método find_all() e a tag img. 
# Apresente a quantidade de imagens encontradas. 
 
 
 
 
 
# Exercício 9 
# Crie uma função que conte a quantidade de parágrafos existentes na página. 
# Utilize o método find_all() e a tag p. 
# Apresente a quantidade de parágrafos encontrados. 
 
# Exercício 10 
# Crie uma função que apresente a quantidade de livros encontrados na página. 
# Utilize um seletor CSS para localizar os elementos correspondentes aos produtos. 
 
# Exercício 11 
# Crie uma função que liste todos os títulos dos livros encontrados na página. 
# Utilize seletores CSS e atributos HTML para localizar o título de cada livro. 
# Apresente os títulos um por linha. 
 
# Exercício 12 
# Crie uma função que liste todos os preços dos livros encontrados na página. 
# O programa deverá localizar os elementos que possuem o preço e apresentar os 
# valores na tela. 
 
# Exercício 13 
# Crie uma função que apresente os títulos e preços dos livros. 
# O resultado deverá apresentar o título do livro e seu respectivo preço. 
 
# Exercício 14 
# Crie uma função que procure um livro pelo nome. 
# O usuário deverá informar o nome completo ou parte do nome. 
# A pesquisa deverá ignorar diferenças entre letras maiúsculas e minúsculas, 
# localizar o livro e apresentar seu título e preço. 
 
# Exercício 15 
# Crie uma função que permita filtrar livros pelo preço máximo. 
# O usuário deverá informar um valor máximo. 
# O programa deverá apresentar somente os livros cujo preço seja menor ou igual ao 
# valor informado. 
 
# Exercício 16 
# Crie uma função que converta o preço obtido no HTML para um valor numérico. 
# O programa deverá remover o símbolo da moeda e converter o valor para um 
# número. 
 
# Exercício 17 
# Crie uma função que identifique o livro mais barato encontrado na página. 
# O programa deverá coletar os livros, converter os preços para números, comparar 
# os valores e apresentar o livro com menor preço. 
 
# Exercício 18 
# Crie uma função que identifique o livro mais caro encontrado na página. 
# O programa deverá apresentar o título e o preço do livro mais caro. 
 
# Exercício 19 
# Crie uma função que calcule o preço médio dos livros encontrados na página. 
# O programa deverá coletar os preços, converter os valores para números, calcular 
# a média e apresentar o resultado. 
 
# Exercício 20 
# Crie uma função que apresente um resumo da coleta. 
# O resumo deverá apresentar a quantidade de livros, o menor preço, o maior preço 
# e o preço médio. 
 
# Exercício 21 
# Crie uma função que salve os títulos e preços dos livros em um arquivo de texto. 
# O arquivo deverá ser chamado livros.txt. 
# Cada livro deverá ocupar uma linha do arquivo. 
 
# Exercício 22 
# Crie uma função que gere um relatório de livros em um arquivo de texto. 
# O relatório deverá conter título do relatório, data da coleta, quantidade de livros, 
# títulos dos livros, preços, menor preço, maior preço e preço médio. 
 
# Exercício 23 
# Crie uma função que apresente os links dos livros encontrados. 
# O programa deverá utilizar os atributos HTML para obter o endereço associado a 
# cada livro. 
# Apresente o título do livro e sua URL. 
 
# Exercício 24 
# Crie uma função que permita navegar pelas páginas do website. 
# O programa deverá acessar a página seguinte utilizando o link disponibilizado pelo 
# próprio website. 
# A função deverá identificar o link da próxima página, realizar uma nova requisição, 
# analisar o HTML e apresentar os livros encontrados. 
 
# Exercício 25 
# Crie uma função que realize uma coleta automatizada de várias páginas. 
# O robô deverá acessar uma página, coletar os livros, identificar a próxima página, 
# acessar a próxima página, repetir o processo, armazenar os dados coletados e 
# apresentar um resumo final. 
# O programa deverá utilizar tratamento de erros e respeitar os limites de acesso ao 
# website. 
 
# Menu Principal 
# Crie um menu de controle para acessar todas as funções desenvolvidas. 
# O menu deverá permitir executar cada exercício individualmente, retornar ao 
# menu após cada operação, tratar opções inválidas, apresentar mensagens de erro 
# e encerrar o programa quando solicitado pelo usuário.