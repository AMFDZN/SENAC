# Instalação:
# pip install selenium
# pip install requests
# pip install python-dotenv

import os
import time
import urllib.robotparser

import requests

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException,WebDriverException)


load_dotenv()
URL_LOGIN = os.getenv("URL_LOGIN")
URL_API = os.getenv("URL_API")
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

def iniciar_navegador(headless=False): #headless = false | não mostrar - True mostra o nevegador
    """
    Inicia o navegador utilizando o Selenium
    WebDriver.

    Parâmetros:

        headless:
            Define se o navegador será executado
            sem interface gráfica.

            False:
                Executa o navegador normalmente.

            True:
                Executa o navegador em modo Headless.

    Utiliza:

        webdriver.Chrome()
            Cria uma instância do Google Chrome.

        ChromeOptions()
            Permite configurar opções de execução
            do navegador.

        --headless=new
            Executa o navegador sem interface gráfica.

        --window-size
            Define o tamanho da janela do navegador.

    Retorno:

        driver:
            Objeto responsável pelo controle
            do navegador.
    """

    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--window-size=1920,1080")
    if headless:
        opcoes.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opcoes)
    return driver

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

    Retorno:

        None.
    """

    print("\nAcessando:")
    print(url)
    driver.get(url)

def localizar_elemento(driver, tipo, valor):
    """
    Localiza um elemento na página.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

        tipo:
            Tipo de localização utilizado
            pelo Selenium.

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

    Retorno:

        WebElement:
            Elemento localizado na página.
    """

    elemento = driver.find_element(tipo,valor)
    return elemento

def aguardar_elemento(driver, tipo, valor):
    """
    Aguarda até que um elemento esteja visível
    na página.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

        tipo:
            Tipo de localização utilizado
            pelo Selenium.

        valor:
            Valor utilizado para localizar
            o elemento.

    Utiliza:

        WebDriverWait()
            Cria uma espera explícita.

        visibility_of_element_located()
            Aguarda até que o elemento esteja
            presente e visível.

        TimeoutException
            Trata o caso em que o elemento
            não aparece dentro do tempo limite.

    Retorno:

        WebElement:
            Elemento localizado e visível.

        None:
            Caso o elemento não seja encontrado
            dentro do tempo determinado.
    """

    try:
        espera = WebDriverWait(driver,10)
        elemento = espera.until(EC.visibility_of_element_located((tipo,valor)))
        return elemento
    except TimeoutException:
        print("\nErro")
        print("O elemento não ficou disponível " "dentro do tempo limite.")
        return None
def preencher_campo(driver, tipo, valor, texto):
    """
    Localiza um campo e envia dados para ele.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

        tipo:
            Tipo de localização do elemento.

        valor:
            Valor utilizado para localizar
            o campo.

        texto:
            Texto que será enviado ao campo.

    Utiliza:

        aguardar_elemento()
            Aguarda o campo ficar disponível.

        clear()
            Limpa o conteúdo atual.

        send_keys()
            Envia os dados para o elemento.

        WebDriverException
            Trata erros relacionados ao navegador.

    Retorno:

        True:
            Caso o campo seja preenchido.

        False:
            Caso ocorra algum erro.
    """

    try:
        campo = aguardar_elemento(driver,tipo,valor)
        if campo is None:
            return False
        campo.clear()
        campo.send_keys(texto)
        print("\nCampo preenchido:")
        print(valor)
        return True
    except WebDriverException as erro:
        print("\nErro ao preencher o campo")
        print(erro)
        return False
def clicar_elemento(driver, tipo, valor):
    """
    Localiza um elemento e executa um clique.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

        tipo:
            Tipo de localização do elemento.

        valor:
            Valor utilizado para localizar
            o elemento.

    Utiliza:

        WebDriverWait()
            Cria uma espera explícita.

        element_to_be_clickable()
            Aguarda o elemento ficar disponível
            para receber um clique.

        click()
            Executa o clique.

        TimeoutException
            Trata o caso em que o elemento
            não fica disponível.

        WebDriverException
            Trata erros relacionados ao navegador.

    Retorno:

        True:
            Caso o clique seja realizado.

        False:
            Caso ocorra algum erro.
    """

    try:

        espera = WebDriverWait(driver,10)
        elemento = espera.until(EC.element_to_be_clickable((tipo,valor)))
        elemento.click()
        print("\nClique realizado:")
        print(valor)
        return True
    except TimeoutException:
        print("\nERRO")
        print("O elemento não ficou disponível ""para clique.")
        return False
    except WebDriverException as erro:
        print("\n Erro ao clicar no Elemento.")
        print(erro)
        return False
def realizar_login(driver):
    """
    Realiza o processo de autenticação.

    Etapas:

        1 - Aguardar campo de usuário.
        2 - Preencher usuário.
        3 - Preencher senha.
        4 - Localizar botão.
        5 - Clicar no botão.
        6 - Aguardar a mensagem da página.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

    Retorno:

        True:
            Caso o processo de login seja enviado.

        False:
            Caso algum campo ou botão não esteja
            disponível.
    """

    if not preencher_campo(driver,By.ID,"username",USUARIO):return False
    if not preencher_campo(driver,By.ID,"password",SENHA):return False
    if not clicar_elemento(driver,By.CSS_SELECTOR,"button[type='submit']"):return False
    print("\nLogin enviado.")
    elemento = aguardar_elemento(driver,By.ID,"flash")


    if elemento is None:

        return False


    print("\nPágina autenticada carregada.")


    return True
def verificar_login(driver):
    """
    Verifica se a autenticação foi realizada.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

    Utiliza:

        current_url
            Obtém a URL atual.

        page_source
            Obtém o HTML atual da página.

    Retorno:

        True:
            Caso a autenticação seja confirmada.

        False:
            Caso a autenticação não seja confirmada.
    """

    try:
        url_atual = driver.current_url
        html = driver.page_source
        if "secure" in url_atual:
            print("\nAutenticação realizada.")
            print("URL atual:",url_atual)
            return True
        if "You logged into a secure area!" in html:
            print("\nLogin realizado com sucesso.")
            return True
        print(
            "\nNão foi possível confirmar "
            "a autenticação.")
        return False


    except WebDriverException as erro:

        print("\n Erro ao verificar o Login")
        print(erro)
        return False
def ler_mensagem(driver):
    """
    Localiza e mostra uma mensagem exibida
    pelo sistema após o login.

    Parâmetros:

        driver:
            Instância do Selenium WebDriver.

    Utiliza:

        aguardar_elemento()
            Aguarda a mensagem ficar disponível.

        text
            Obtém o conteúdo textual do elemento.

    Retorno:

        None.
    """

    mensagem = aguardar_elemento(driver,By.ID,"flash")
    if mensagem is None:
        print("\nMensagem não encontrada.")
        return
    print("\nMensagem do sistema:")
    print(mensagem.text)
    
def verificar_robots_txt(url):
    """
    Verifica as regras de acesso definidas
    pelo arquivo robots.txt do website.

    Parâmetros:

        url:
            Endereço do website que será
            verificado.

    Utiliza:

        RobotFileParser()
            Cria um analisador para o arquivo
            robots.txt.

        set_url()
            Define o endereço do robots.txt.

        read()
            Realiza a leitura das regras.

        can_fetch()
            Verifica se o acesso ao endereço
            é permitido para um robô.

    Retorno:

        True:
            Caso o acesso seja permitido.

        False:
            Caso o acesso não seja permitido
            ou ocorra algum erro.
    """

    try:
        parser = urllib.robotparser.RobotFileParser()
        endereco_robots = ( url.rstrip("/") + "/robots.txt")
        parser.set_url(endereco_robots)
        parser.read()
        permitido = parser.can_fetch( "*", url)
        if permitido:
            print("\nrobots.txt:")
            print("Acesso permitido.")
        else:
            print("\nrobots.txt:")
            print( "Acesso não permitido." )
        return permitido


    except Exception as erro:

        print("\n Erro ao verificar Robots.txt")
        print(erro)
        return False
def executar_navegacao(headless=False):
    """
    Executa o fluxo completo de automação
    utilizando Selenium.

    Etapas:

        1 - Verificar robots.txt.
        2 - Iniciar navegador.
        3 - Acessar página.
        4 - Aguardar carregamento.
        5 - Realizar login.
        6 - Verificar autenticação.
        7 - Ler mensagem.
        8 - Encerrar navegador.

    Parâmetros:

        headless:
            Define se o navegador será executado
            sem interface gráfica.

    Utiliza:

        verificar_robots_txt()
            Verifica as regras de acesso.

        iniciar_navegador()
            Inicia o navegador.

        time.sleep()
            Adiciona um pequeno intervalo entre
            operações de acesso.

        WebDriverWait
            Aguarda elementos necessários.

        try / except / finally
            Controla erros e garante o encerramento
            do navegador.

    Retorno:

        None.
    """

    if not verificar_robots_txt(URL_LOGIN):
        print("\nAutomação cancelada.")
        return
    driver = iniciar_navegador(headless)


    try:

        acessar_pagina( driver, URL_LOGIN)


        time.sleep(
            1
        )


        if realizar_login(
            driver
        ):

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
                    "\nRobô não conseguiu confirmar "
                    "a autenticação."
                )


        else:

            print(
                "\nRobô não conseguiu realizar "
                "o login."
            )


    except TimeoutException:

        print(
            "\nERRO: tempo limite excedido "
            "durante a automação."
        )


    except WebDriverException as erro:

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

    API REST (Representational State Transfer)
    é uma forma de comunicação entre sistemas
    utilizando o protocolo HTTP.

    Nesta função, o método GET é utilizado
    para solicitar dados de uma API pública.

    Parâmetros:

        Nenhum.

    Utiliza:

        requests.get()
            Realiza a requisição HTTP.

        timeout
            Define o tempo máximo de espera.

        raise_for_status()
            Identifica respostas HTTP de erro.

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

        print(
            "\nConsultando API..."
        )


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


        print(
            "\nJSON recebido com sucesso."
        )


        return dados


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
            "Não foi possível conectar à API."
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


    except ValueError:

        print(
            "\nERRO"
        )


        print(
            "A resposta não contém "
            "um JSON válido."
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
def interpretar_json(dados):
    """
    Interpreta os dados recebidos em JSON.

    O JSON é convertido pelo requests
    em listas e dicionários Python.

    Parâmetros:

        dados:
            Lista contendo os usuários
            retornados pela API.

    Utiliza:

        get()
            Obtém valores dos dicionários.

        for
            Percorre os usuários retornados.

    Mostra:

        - nome;
        - usuário;
        - e-mail;
        - cidade.

    Retorno:

        None.
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

    A pesquisa não diferencia letras
    maiúsculas de minúsculas.

    Parâmetros:

        dados:
            Lista contendo os usuários
            retornados pela API.

    Utiliza:

        input()
            Recebe o termo de pesquisa.

        lower()
            Converte o texto para letras
            minúsculas.

        in
            Verifica se o termo está contido
            no nome do usuário.

        get()
            Obtém os dados do usuário.

    Retorno:

        None.
    """

    if dados is None:

        return
    termo = input("\nDigite o nome do usuário: ")


    encontrado = False


    for usuario in dados:

        nome = usuario.get( "name","")
        if termo.lower() in nome.lower():
            print("\nUsuário encontrado:")
            print("Nome:",usuario.get("name"))
            print("E-mail:",usuario.get("email"))
            print("Telefone:",usuario.get("phone"))
            encontrado = True


    if not encontrado:

        print("\nUsuário não encontrado." )

def executar_robo():
    """
    Executa o projeto completo.

    Etapas:

        1 - Verificação do robots.txt.
        2 - Automação do navegador utilizando
            Selenium.
        3 - Consulta da API REST utilizando
            requests.
        4 - Interpretação dos dados JSON.

    Utiliza:

        executar_navegacao()
            Executa a automação do navegador.

        consultar_api()
            Realiza a consulta à API.

        interpretar_json()
            Interpreta os dados retornados.

    Retorno:

        None.
    """


    print("Automação do navegador.")
    executar_navegacao(headless=True)
    print("Consulta da API.")
    dados = consultar_api()
    if dados is None:
        print(
            "\nNão foi possível obter "
            "os dados da API."
        )


        return
    print("Interpretação do JSON.")
    interpretar_json( dados)
    print("\nRobô finalizado.")

def menu():
    """
    Exibe o menu principal do robô.

    O menu reúne as funcionalidades
    de automação Selenium, API REST,
    interpretação JSON e execução completa.

    Opções:

        1 - Iniciar navegador.
        2 - Acessar página.
        3 - Realizar login.
        4 - Ler mensagem.
        5 - Executar navegação completa.
        6 - Consultar API.
        7 - Interpretar JSON.
        8 - Pesquisar usuário.
        9 - Executar robô completo.
        0 - Sair.

    Retorno:

        None.
    """

    dados_api = None


    while True:

        print(
            """




1  - Iniciar navegador
2  - Acessar página
3  - Realizar login
4  - Ler mensagem da página
5  - Executar navegação completa

API REST E JSON

6  - Consultar API
7  - Interpretar JSON
8  - Pesquisar usuário

ROBÔ COMPLETO

9  - Executar robô completo

0  - Sair

"""
        )


        opcao = input(
            "Escolha uma opção: "
        )


        if opcao == "1":

            driver = iniciar_navegador(
                headless=False
            )


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


        elif opcao == "2":

            driver = iniciar_navegador(
                headless=False
            )


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

            driver = iniciar_navegador(
                headless=False
            )


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

            driver = iniciar_navegador(
                headless=False
            )


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

            executar_navegacao(
                headless=False
            )


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
            interpretar_json(dados_api)
            input("\nPressione Enter para continuar.")
        elif opcao == "8":
            if dados_api is None:
                dados_api = consultar_api()
            pesquisar_usuario(dados_api)
            input("\nPressione Enter para continuar.")
        elif opcao == "9":
            executar_robo()
            input("\nPressione Enter para continuar.")
        elif opcao == "0":
            print("\nRobô encerrado.")
            break

        else:
            print("\nOpção inválida.")
if __name__ == "__main__":

    menu()
