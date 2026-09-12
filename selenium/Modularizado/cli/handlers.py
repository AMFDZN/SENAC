from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException
)

from config import URL_LOGIN

from browser.driver import iniciar_navegador

from browser.actions import acessar_pagina

from browser.login import (
    realizar_login,
    verificar_login,
    ler_mensagem
)

from api.client import consultar_api

from api.users import (
    interpretar_json,
    pesquisar_usuario
)

from utils.robots import verificar_robots_txt



dados_api = None


def executar_opcao(opcao):
    """
    Executa a função correspondente à opção
    escolhida no menu.
    """

    opcoes = {
        "1": iniciar_navegador_menu,
        "2": acessar_pagina_menu,
        "3": realizar_login_menu,
        "4": ler_mensagem_menu,
        "5": executar_navegacao_menu,
        "6": consultar_api_menu,
        "7": interpretar_json_menu,
        "8": pesquisar_usuario_menu,
        "9": executar_robo_menu,
    }

    funcao = opcoes.get(opcao)

    if funcao:
        funcao()
    else:
        print("\nOpção inválida.")




def iniciar_navegador_menu():
    """
    Inicia o navegador e acessa a página
    definida no arquivo .env.
    """

    driver = iniciar_navegador(headless=False)

    try:

        acessar_pagina(driver,URL_LOGIN )

        input(
            "\nPágina aberta. "
            "Pressione Enter para fechar."
        )

    finally:

        driver.quit()




def acessar_pagina_menu():
    """
    Abre o navegador e acessa a página
    definida no arquivo .env.
    """

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




def realizar_login_menu():
    """
    Abre a página e realiza o login.
    """

    driver = iniciar_navegador(
        headless=False
    )

    try:

        acessar_pagina(
            driver,
            URL_LOGIN
        )

        sucesso = realizar_login(driver)

        if sucesso:

            verificar_login(
                driver
            )

        input(
            "\nPressione Enter para fechar."
        )

    finally:

        driver.quit()




def ler_mensagem_menu():
    """
    Abre a página, realiza o login
    e lê a mensagem do sistema.
    """

    driver = iniciar_navegador(
        headless=False
    )

    try:

        acessar_pagina(
            driver,
            URL_LOGIN
        )

        sucesso = realizar_login(
            driver
        )

        if sucesso:

            if verificar_login(driver):

                ler_mensagem(
                    driver
                )

        input(
            "\nPressione Enter para fechar."
        )

    finally:

        driver.quit()


def executar_navegacao_menu():
    """
    Executa a navegação completa.
    """

    executar_navegacao(
        headless=False
    )

    input(
        "\nPressione Enter para continuar."
    )




def consultar_api_menu():
    """
    Consulta a API definida no arquivo .env.
    """

    global dados_api

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


def interpretar_json_menu():
    """
    Interpreta os dados JSON da API.
    """

    global dados_api

    if dados_api is None:

        dados_api = consultar_api()

    if dados_api is not None:

        interpretar_json(
            dados_api
        )

    input(
        "\nPressione Enter para continuar."
    )



def pesquisar_usuario_menu():
    """
    Pesquisa um usuário nos dados da API.
    """

    global dados_api

    if dados_api is None:

        dados_api = consultar_api()

    if dados_api is not None:

        pesquisar_usuario(
            dados_api
        )

    input(
        "\nPressione Enter para continuar."
    )




def executar_robo_menu():
    """
    Executa o robô completo.
    """

    executar_robo()

    input(
        "\nPressione Enter para continuar."
    )




def executar_navegacao(headless=False):
    """
    Executa o fluxo completo de automação
    utilizando Selenium.

    Etapas:

        1. Verificar robots.txt.
        2. Iniciar navegador.
        3. Acessar página.
        4. Realizar login.
        5. Verificar autenticação.
        6. Ler mensagem.
        7. Encerrar navegador.
    """

    if not verificar_robots_txt(URL_LOGIN):

        print(
            "\nAutomação cancelada."
        )

        return

    driver = iniciar_navegador(
        headless=headless
    )

    try:

        acessar_pagina(
            driver,
            URL_LOGIN
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




def executar_robo():
    """
    Executa o projeto completo.

    Etapas:

        1. Automação do navegador.
        2. Consulta da API.
        3. Interpretação do JSON.
    """

    print(
        "\nAutomação do navegador."
    )

    executar_navegacao(
        headless=True
    )

    print(
        "\nConsulta da API."
    )

    dados = consultar_api()

    if dados is None:

        print(
            "\nNão foi possível obter "
            "os dados da API."
        )

        return

    print(
        "\nInterpretação do JSON."
    )

    interpretar_json(
        dados
    )

    print(
        "\nRobô finalizado."
    )
