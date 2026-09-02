# Instalação:
# pip install selenium requests tabulate

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from tabulate import tabulate

# CONSTANTES E DIRETÓRIOS DO PROJETO
URL_LOGIN = "https://the-internet.herokuapp.com/login"
URL_API = "https://jsonplaceholder.typicode.com/users"
USUARIO = "tomsmith"
SENHA = "SuperSecretPassword!"


def iniciar_navegador(headless=False):
    """Exercício 1: Inicia o navegador utilizando o Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def acessar_pagina(driver, url=URL_LOGIN):
    """Exercício 2: Acessa uma página e localiza elementos."""
    print(f"\nAcessando URL: {url}")
    driver.get(url)


def localizar_elemento_por_id(driver, valor_id="username"):
    """Exercício 2: Localiza elemento utilizando By.ID."""
    return driver.find_element(By.ID, valor_id)


def localizar_elemento_por_css(driver, seletor_css="button[type='submit']"):
    """Exercício 2: Localiza elemento utilizando By.CSS_SELECTOR."""
    return driver.find_element(By.CSS_SELECTOR, seletor_css)


def interagir_com_elemento(driver, tipo=By.ID, valor="username", texto=""):
    """Exercício 3: Limpa conteúdo, preenche o campo ou clica."""
    try:
        elemento = driver.find_element(tipo, valor)
        if texto:
            elemento.clear()
            elemento.send_keys(texto)
            print(f"\nCampo '{valor}' preenchido com sucesso.")
        else:
            elemento.click()
            print(f"\nElemento '{valor}' clicado com sucesso.")
    except Exception as erro:
        print(f"\nErro ao interagir com o elemento {valor}: {erro}")


def realizar_login(driver=None):
    """Exercício 4: Realiza o login no website de treinamento."""
    fechar_local = False
    if driver is None:
        driver = iniciar_navegador()
        fechar_local = True

    try:
        acessar_pagina(driver, URL_LOGIN)
        
        # Preencher usuário
        interagir_com_elemento(driver, By.ID, "username", USUARIO)
        # Preencher senha
        interagir_com_elemento(driver, By.ID, "password", SENHA)
        # Clicar no botão de login
        interagir_com_elemento(driver, By.CSS_SELECTOR, "button[type='submit']", "")
        
        print("\nLogin enviado.")
        return driver
    except Exception as erro:
        print(f"\nErro no processo de login: {erro}")
        if fechar_local:
            driver.quit()
        return None


def verificar_resultado_automacao(driver):
    """Exercício 5: Controla e verifica o resultado da automação com WebDriverWait."""
    try:
        espera = WebDriverWait(driver, 10)
        mensagem_elem = espera.until(EC.presence_of_element_located((By.ID, "flash")))
        
        url_atual = driver.current_url
        html = mensagem_elem.text
        
        print(f"\nURL Atual: {url_atual}")
        print(f"Mensagem do Sistema: {html.strip()}")
        
        if "secure" in url_atual or "You logged into a secure area!" in html:
            print("\nAutenticação realizada com sucesso!")
            return True
        else:
            print("\nA autenticação falhou.")
            return False
    except Exception as erro:
        print(f"\nErro ao verificar resultado: {erro}")
        return False


def executar_automacao_com_tratamento(driver=None):
    """Exercício 6: Adiciona tratamento de erros completo (try, except, finally)."""
    driver_criado = False
    if driver is None:
        driver = iniciar_navegador()
        driver_criado = True

    try:
        acessar_pagina(driver, URL_LOGIN)
        realizar_login(driver)
        verificar_resultado_automacao(driver)
    except Exception as erro:
        print(f"\nERRO DURANTE A AUTOMAÇÃO: {erro}")
    finally:
        print("\nFinalizando ciclo de automação...")
        if driver_criado:
            driver.quit()


def consultar_api_get(url=URL_API):
    """Exercícios 7 e 8: Realiza requisição GET para a API com tratamento robusto de erros."""
    print(f"\nAcessando API: {url}")
    try:
        resposta = requests.get(url, timeout=10)
        print(f"Método HTTP: {resposta.request.method}")
        print(f"URL Acessada: {resposta.url}")
        print(f"Código HTTP: {resposta.status_code}")
        
        resposta.raise_for_status()
        return resposta.json()

    except requests.exceptions.Timeout:
        print("\nErro: Tempo limite excedido (Timeout).")
    except requests.exceptions.ConnectionError:
        print("\nErro: Falha na conexão com o servidor.")
    except requests.exceptions.HTTPError as erro:
        print(f"\nErro HTTP retornado: {erro}")
    except ValueError:
        print("\nErro: A resposta não contém um JSON válido.")
    except requests.exceptions.RequestException as erro:
        print(f"\nErro geral na requisição: {erro}")
    
    return None


def listar_usuarios_api(dados=False):
    """Exercício 9: Lista os usuários da API usando a biblioteca tabulate."""
    if not dados:
        dados = consultar_api_get()
    
    if not dados:
        print("\nNenhum dado disponível para listagem.")
        return

    tabela_dados = []
    for usuario in dados:
        nome = usuario.get("name")
        username = usuario.get("username")
        email = usuario.get("email")
        cidade = usuario.get("address", {}).get("city")
        tabela_dados.append([nome, username, email, cidade])

    cabecalho = ["Nome", "Usuário", "E-mail", "Cidade"]
    print("\n" + tabulate(tabela_dados, headers=cabecalho, tablefmt="grid"))


def pesquisar_usuario_api(dados=False):
    """Exercício 9: Pesquisa usuário por parte do nome (ignorando maiúsculas/minúsculas) com tabulate."""
    if not dados:
        dados = consultar_api_get()

    if not dados:
        print("\nNenhum dado disponível para pesquisa.")
        return

    termo = input("\nDigite o nome ou parte do nome para pesquisar: ").strip().lower()
    
    tabela_resultados = []
    for usuario in dados:
        nome = usuario.get("name", "")
        if termo in nome.lower():
            email = usuario.get("email")
            telefone = usuario.get("phone")
            tabela_resultados.append([nome, email, telefone])

    if tabela_resultados:
        cabecalho = ["Nome Encontrado", "E-mail", "Telefone"]
        print("\n" + tabulate(tabela_resultados, headers=cabecalho, tablefmt="grid"))
    else:
        print("\nNenhum usuário encontrado com o termo informado.")


def executar_robo_completo(fluxo_completo=True):
    """Exercício 10: Executa o fluxo completo integrando Selenium e API."""
    if fluxo_completo:
        print("\n--- INICIANDO FLUXO COMPLETO DO ROBÔ ---")
        driver = iniciar_navegador()
        try:
            acessar_pagina(driver, URL_LOGIN)
            realizar_login(driver)
            verificar_resultado_automacao(driver)
        finally:
            print("\nEncerrando navegador da automação...")
            driver.quit()

        print("\n--- INICIANDO CONSULTA À API ---")
        dados = consultar_api_get()
        if dados:
            listar_usuarios_api(dados=dados)
        print("\n--- FLUXO COMPLETO CONCLUÍDO ---")


def menu(opcao_menu=False):
    """Exercício 10: Menu principal interativo."""
    dados_api = None

    while True:
        print("""
========================================
       MENU PRINCIPAL - AUTOMAÇÃO       
========================================
1 - Iniciar Navegador e Acessar Página
2 - Realizar Login Automatizado
3 - Verificar Resultado da Automação
4 - Executar Automação Completa com Tratamento de Erros
5 - Consultar API REST (JSON)
6 - Listar Usuários da API (Tabulate)
7 - Pesquisar Usuário na API
8 - Executar Fluxo Completo (Selenium + API)
0 - Sair
========================================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            driver = iniciar_navegador()
            try:
                acessar_pagina(driver, URL_LOGIN)
                input("\nPressione Enter para fechar o navegador...")
            finally:
                driver.quit()

        elif opcao == "2":
            driver = iniciar_navegador()
            try:
                realizar_login(driver)
                input("\nPressione Enter para fechar o navegador...")
            finally:
                driver.quit()

        elif opcao == "3":
            driver = iniciar_navegador()
            try:
                realizar_login(driver)
                verificar_resultado_automacao(driver)
                input("\nPressione Enter para fechar o navegador...")
            finally:
                driver.quit()

        elif opcao == "4":
            executar_automacao_com_tratamento()
            input("\nPressione Enter para continuar...")

        elif opcao == "5":
            dados_api = consultar_api_get()
            if dados_api:
                print(f"\nAPI consultada com sucesso! Total de registros: {len(dados_api)}")
            input("\nPressione Enter para continuar...")

        elif opcao == "6":
            if dados_api is None:
                dados_api = consultar_api_get()
            listar_usuarios_api(dados=dados_api)
            input("\nPressione Enter para continuar...")

        elif opcao == "7":
            if dados_api is None:
                dados_api = consultar_api_get()
            pesquisar_usuario_api(dados=dados_api)
            input("\nPressione Enter para continuar...")

        elif opcao == "8":
            executar_robo_completo(fluxo_completo=True)
            input("\nPressione Enter para continuar...")

        elif opcao == "0":
            print("\nEncerrando programa. Até logo!")
            break
        else:
            print("\nOpção inválida! Escolha um número válido do menu.")


if __name__ == "__main__":
    menu(opcao_menu=False)