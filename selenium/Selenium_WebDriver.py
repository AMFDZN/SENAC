
# Instalação:
# pip install selenium
# pip install requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#para o Chrome no linux
import re
import subprocess
import pytest
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

import requests

URL_LOGIN = "https://the-internet.herokuapp.com/login"
URL_API = "https://jsonplaceholder.typicode.com/users"
USUARIO = "tomsmith"
SENHA = "SuperSecretPassword!"

def iniciar_navegador():
    # 1. Configura as opções do Chrome
        options = webdriver.ChromeOptions()
    
        # Caminho padrão onde o Flatpak expõe o executável do Chrome no sistema host
        #options.binary_location = "~/.local/share/flatpak/app/com.google.Chrome/current/active/export/bin/com.google.Chrome"
        #options.binary_location = "~/.local/share/flatpak/exports/bin/com.google.Chrome"
        # Nota: Se foi instalado apenas para o seu usuário (--user), o caminho será:
        # "~/.local/share/flatpak/exports/bin/com.google.Chrome"
        #na minha máquina
        ###/home/acelio/.local/share/flatpak/app/com.google.Chrome/current/active/files/bin/chrome
        # ~/.local/share/flatpak/app/com.google.Chrome/current/active/files/bin/chrome
    
        # Argumentos recomendados para evitar problemas de permissões com a Sandbox do Flatpak
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
        # 2. Inicializa o WebDriver
        # O Selenium Manager baixará o ChromeDriver compatível automaticamente se você estiver usando o Selenium 4+
        
        #service = webdriver.ChromeService()
        #driver = webdriver.Chrome(service=service)
        driver = webdriver.Chrome(options=options)
        
        #driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    

# def iniciar_navegador():
#     """
#     Inicia o navegador utilizando o Selenium WebDriver.

#     Utiliza:

#         webdriver.Chrome()
#             Cria uma instância do Google Chrome.

#         maximize_window()
#             Maximiza a janela do navegador.

#     Retorno:

#         driver:
#             Objeto responsável pelo controle
#             do navegador.
#     """
    
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver




def acessar_pagina(driver, url):
    """
    Acessa uma página utilizando o WebDriver.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

        url:
            Endereço da página.

    Utiliza:

        get()
            Abre uma URL no navegador.
    """

    print(
        "\nAcessando:"
    )

    print(
        url
    )

    driver.get(
        url
    )




def localizar_elemento(driver, tipo, valor):
    """
    Localiza um elemento na página.

    Parâmetros:

        driver:
            WebDriver.

        tipo:
            Tipo de localização.

        valor:
            Valor utilizado para localizar
            o elemento.

    Exemplos:

        By.ID
        By.NAME
        By.CLASS_NAME
        By.TAG_NAME
        By.CSS_SELECTOR
        By.XPATH
    """

    elemento = driver.find_element(tipo,valor)

    return elemento



def aguardar_elemento(driver, tipo, valor):
    """
    Aguarda até que um elemento esteja disponível
    na página.

    Utiliza:

        WebDriverWait
            Cria uma espera explícita.

        presence_of_element_located()
            Aguarda a presença do elemento.
    """

    espera = WebDriverWait(driver,10)
    elemento = espera.until(EC.presence_of_element_located((tipo,valor)))
    return elemento




def preencher_campo(driver, tipo, valor, texto):
    """
    Localiza um campo e envia dados para ele.

    Utiliza:

        find_element()
            Localiza o campo.

        clear()
            Limpa o campo.

        send_keys()
            Envia os dados para o elemento.
    """

    campo = localizar_elemento(driver,tipo,valor)
    campo.clear()
    campo.send_keys(texto)
    print("\nCampo preenchido:")
    print(valor)



def clicar_elemento(driver, tipo, valor):
    """
    Localiza um elemento e executa um clique.

    Utiliza:

        find_element()
            Localiza o elemento.

        click()
            Executa o clique.
    """
    elemento = localizar_elemento(driver,tipo,valor)
    elemento.click()
    print("\nClique realizado:")
    print(valor)




def realizar_login(driver):
    """
    Realiza o processo de autenticação.

    Etapas:

        1 - Localizar usuário.
        2 - Preencher usuário.
        3 - Localizar senha.
        4 - Preencher senha.
        5 - Localizar botão.
        6 - Clicar no botão.
        7 - Aguardar a página autenticada.
    """

    aguardar_elemento(
        driver,
        By.ID,
        "username"
    )

    preencher_campo(
        driver,
        By.ID,
        "username",
        USUARIO
    )

    preencher_campo(
        driver,
        By.ID,
        "password",
        SENHA
    )

    clicar_elemento(
        driver,
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    print("\nLogin enviado.")

    aguardar_elemento(
        driver,
        By.ID,
        "flash"
    )

    print("\nPágina autenticada carregada.")




def verificar_login(driver):
    """
    Verifica se a autenticação foi realizada.

    Utiliza:

        current_url
            Obtém a URL atual.

        page_source
            Obtém o HTML atual da página.
    """

    url_atual = driver.current_url
    html = driver.page_source
    if "secure" in url_atual:
        print("Autenticação Realizada")
        print("URL atual:",url_atual)
        return True

    if "You logged into a secure area!" in html:
        print("\nLogin realizado com sucesso.")
        return True

    print("\nNão foi possível confirmar a autenticação.")

    return False




def ler_mensagem(driver):
    """
    Localiza e mostra uma mensagem exibida
    pelo sistema após o login.
    """

    try:

        mensagem = aguardar_elemento(
            driver,
            By.ID,
            "flash"
        )

        texto = mensagem.text

        print(
            "\nMensagem do sistema:"
        )

        print(
            texto
        )

    except Exception as erro:

        print(
            "\nMensagem não encontrada."
        )

        print(
            erro
        )




def executar_navegacao():
    """
    Executa o fluxo completo de navegação.

    Fluxo:
        0- inicia lunux

        1 - Iniciar navegador.
        2 - Acessar página.
        3 - Localizar campos.
        4 - Preencher usuário.
        5 - Preencher senha.
        6 - Clicar no botão.
        7 - Verificar autenticação.
        8 - Ler mensagem.
        9 - Encerrar navegador.
    """

    #driver = iniciar_navegador()
    driver= iniciaLinux()

    try:

        acessar_pagina(
            driver,
            URL_LOGIN
        )

        realizar_login(
            driver
        )

        autenticado = verificar_login(
            driver
        )

        if autenticado:

            ler_mensagem(
                driver
            )

            print(
                "\nRobô concluiu a navegação."
            )

        else:

            print(
                "\nRobô não conseguiu concluir "
                "a autenticação."
            )

    except Exception as erro:

        print(
            "\nERRO DURANTE A AUTOMAÇÃO:"
        )

        print(
            erro
        )

    finally:

        print(
            "\nEncerrando navegador..."
        )

        driver.quit()




def consultar_api():
    """
    Realiza uma requisição GET para uma API REST.
    
    API REST (Representational State Transfer) é uma forma
    de comunicação entre sistemas por meio do protocolo HTTP.
    Uma API REST disponibiliza recursos por meio de URLs e
    utiliza métodos HTTP, como GET, POST, PUT e DELETE, para
    realizar diferentes operações sobre esses recursos.

    Nesta função, o método GET é utilizado para solicitar dados
    de uma API. A resposta recebida é convertida de JSON para
    estruturas de dados do Python.

    Utiliza:

        requests.get()
            Realiza a requisição HTTP.

        response.json()
            Converte o JSON recebido
            em estruturas Python.

    Retorno:

        list:
            Dados recebidos da API.

        None:
            Caso ocorra algum erro.
    """



    try:

        resposta = requests.get(
            URL_API,
            timeout=10
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
            resposta.status_code
        )

        resposta.raise_for_status()

        dados = resposta.json()

        return dados

    except requests.exceptions.Timeout:

        print(
            "\nErro: tempo limite excedido."
        )

        return None

    except requests.exceptions.ConnectionError:

        print(
            "\nErro: não foi possível "
            "conectar à API."
        )

        return None

    except requests.exceptions.HTTPError as erro:

        print(
            "\nErro HTTP:"
        )

        print(
            erro
        )

        return None

    except ValueError:

        print(
            "\nErro: resposta não contém "
            "um JSON válido."
        )

        return None

    except requests.exceptions.RequestException as erro:

        print(
            "\nErro durante a requisição:"
        )

        print(
            erro
        )

        return None



def interpretar_json(dados):
    """
    Interpreta os dados recebidos em JSON.

    JSON (JavaScript Object Notation) é um formato de texto
    usado para representar e transportar dados de forma
    estruturada, sendo muito utilizado na comunicação entre
    aplicações e APIs.

    O JSON é convertido pelo requests
    em listas e dicionários Python.

    A função mostra:

        - nome;
        - usuário;
        - e-mail;
        - cidade.
    """

    if dados is None:

        return


    for usuario in dados:

        nome = usuario.get(
            "name"
        )

        username = usuario.get(
            "username"
        )

        email = usuario.get(
            "email"
        )

        endereco = usuario.get(
            "address",
            {}
        )

        cidade = endereco.get(
            "city"
        )

        print(
            "\nNome:",
            nome
        )

        print(
            "Usuário:",
            username
        )

        print(
            "E-mail:",
            email
        )

        print(
            "Cidade:",
            cidade
        )

        print(
            "-" * 40
        )




def pesquisar_usuario(dados):
    """
    Pesquisa um usuário dentro dos dados
    retornados pela API.
    """

    if dados is None:

        return

    termo = input(
        "\nDigite o nome do usuário: "
    )

    encontrado = False

    for usuario in dados:

        nome = usuario.get(
            "name",
            ""
        )

        if termo.lower() in nome.lower():

            print(
                "\nUsuário encontrado:"
            )

            print(
                "Nome:",
                usuario.get("name")
            )

            print(
                "E-mail:",
                usuario.get("email")
            )

            print(
                "Telefone:",
                usuario.get("phone")
            )

            encontrado = True

    if not encontrado:

        print(
            "\nUsuário não encontrado."
        )




def executar_robo():
    """
    Executa o projeto completo.

    Primeira etapa:

        Automação do navegador
        utilizando Selenium.

    Segunda etapa:

        Consumo de API REST
        utilizando requests.

    Terceira etapa:

        Interpretação do JSON.
    """



    print(
        "\nEtapa 1"
    )

    print(
        "Automação do navegador."
    )

    executar_navegacao()

    print(
        "\nEtapa 2"
    )

    print(
        "Consulta da API."
    )

    dados = consultar_api()

    print(
        "\nEtapa 3"
    )

    print(
        "Interpretação do JSON."
    )

    interpretar_json(
        dados
    )

    




def menu():
    """
    Exibe o menu principal do robô.
    """

    dados_api = None

    while True:

        print(
            """



00- linux
1 - Iniciar navegador
2 - Acessar página
3 - Realizar login
4 - Ler mensagem da página
5 - Executar navegação completa

API REST E JSON

6 - Consultar API
7 - Interpretar JSON
8 - Pesquisar usuário

ROBÔ COMPLETO

9 - Executar robô completo

0 - Sair

"""
        )

        opcao = input(
            "Escolha uma opção: "
        )
        
        if opcao=="00":
            driver=iniciaLinux()
            acessar_pagina(driver,URL_LOGIN)
            
            input("\nPressione Enter para fechar.")
            
            driver.quit()



        elif opcao == "1":

            driver = iniciar_navegador()

            acessar_pagina(
                driver,
                URL_LOGIN
            )

            input(
                "\nPressione Enter para fechar."
            )

            driver.quit()

       

        elif opcao == "2":

            driver = iniciar_navegador()

            try:

                acessar_pagina(
                    driver,
                    URL_LOGIN
                )

                input(
                    "\nPressione Enter para fechar."
                )

            finally:

                driver.quit()


        elif opcao == "3":

            driver = iniciar_navegador()

            try:

                acessar_pagina(
                    driver,
                    URL_LOGIN
                )

                realizar_login(
                    driver
                )

                verificar_login(
                    driver
                )

                input(
                    "\nPressione Enter para fechar."
                )

            finally:

                driver.quit()



        elif opcao == "4":

            driver = iniciar_navegador()

            try:

                acessar_pagina(
                    driver,
                    URL_LOGIN
                )

                realizar_login(
                    driver
                )

                ler_mensagem(
                    driver
                )

                input(
                    "\nPressione Enter para fechar."
                )

            finally:

                driver.quit()


        elif opcao == "5":

            executar_navegacao()

            input(
                "\nPressione Enter para continuar."
            )


        elif opcao == "6":

            dados_api = consultar_api()

            if dados_api:

                print(
                    "\nDados recebidos com sucesso."
                )

                print(
                    "Quantidade:",
                    len(dados_api)
                )

            input(
                "\nPressione Enter para continuar."
            )



        elif opcao == "7":

            if dados_api is None:

                dados_api = consultar_api()

            interpretar_json(
                dados_api
            )

            input(
                "\nPressione Enter para continuar."
            )


        elif opcao == "8":

            if dados_api is None:

                dados_api = consultar_api()

            pesquisar_usuario(
                dados_api
            )

            input(
                "\nPressione Enter para continuar."
            )

   

        elif opcao == "9":

            executar_robo()

            input(
                "\nPressione Enter para continuar."
            )


        elif opcao == "0":

            print(
                "\nRobô encerrado."
            )

            break

        else:

            print(
                "\nOpção inválida."
            )


if __name__ == "__main__":

    menu()
