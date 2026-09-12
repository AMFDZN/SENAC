from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from config import USUARIO, SENHA

from browser.actions import (
    aguardar_elemento,
    preencher_campo,
    clicar_elemento
)


def realizar_login(driver):
    """
    Realiza o login no sistema.
    """

    print("\nRealizando login...")

 
    if not preencher_campo(
        driver,
        By.ID,
        "username",
        USUARIO
    ):
        print("\nNão foi possível preencher o usuário.")
        return False


    if not preencher_campo(
        driver,
        By.ID,
        "password",
        SENHA
    ):
        print("\nNão foi possível preencher a senha.")
        return False

   
    if not clicar_elemento(
        driver,
        By.CSS_SELECTOR,
        "button[type='submit']"
    ):
        print("\nNão foi possível clicar no botão de login.")
        return False

    print("\nLogin enviado.")

  
    mensagem = aguardar_elemento(
        driver,
        By.ID,
        "flash",
        timeout=10
    )

    if mensagem is None:
        print("\nA mensagem de login não apareceu.")
        return False

    print("\nPágina autenticada carregada.")

    return True


def verificar_login(driver):
    """
    Verifica se o login foi realizado com sucesso.
    """

    try:

        url_atual = driver.current_url
        html = driver.page_source

        print("\nVerificando autenticação...")
        print("URL atual:", url_atual)

        if "/secure" in url_atual:

            print(
                "\nAutenticação realizada com sucesso."
            )

            return True

        if "You logged into a secure area!" in html:

            print(
                "\nLogin realizado com sucesso."
            )

            return True

        print(
            "\nNão foi possível confirmar "
            "a autenticação."
        )

        return False

    except WebDriverException as erro:

        print(
            "\nErro ao verificar o login."
        )

        print(erro)

        return False


def ler_mensagem(driver):
    """
    Aguarda e mostra a mensagem exibida
    pelo sistema após o login.
    """

    print("\nAguardando mensagem da página...")

    mensagem = aguardar_elemento(
        driver,
        By.ID,
        "flash",
        timeout=10
    )

    if mensagem is None:

        print(
            "\nMensagem não encontrada."
        )

        return False

    texto = mensagem.text.strip()

    if texto:

        print("\nMensagem do sistema:")
        print("-" * 40)
        print(texto)
        print("-" * 40)

        return True

    print(
        "\nO elemento da mensagem foi encontrado, "
        "mas está vazio."
    )

    return False
