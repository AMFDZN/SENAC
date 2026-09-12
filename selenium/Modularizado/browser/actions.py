from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (TimeoutException,WebDriverException,)


DEFAULT_TIMEOUT = 10


def acessar_pagina(driver, url):
    driver.get(url)


def aguardar_elemento(driver, tipo, valor, timeout=DEFAULT_TIMEOUT):
    try:
        espera = WebDriverWait(driver, timeout)

        return espera.until(EC.visibility_of_element_located((tipo, valor)))

    except TimeoutException:
        return None


def preencher_campo(driver, tipo, valor, texto):
    try:
        campo = aguardar_elemento(driver, tipo, valor)

        if campo is None:
            return False

        campo.clear()
        campo.send_keys(texto)

        return True

    except WebDriverException:
        return False


def clicar_elemento(driver, tipo, valor, timeout=DEFAULT_TIMEOUT):
    try:
        espera = WebDriverWait(driver, timeout)

        elemento = espera.until(EC.element_to_be_clickable((tipo, valor)))

        elemento.click()

        return True

    except (TimeoutException, WebDriverException):
        return False
