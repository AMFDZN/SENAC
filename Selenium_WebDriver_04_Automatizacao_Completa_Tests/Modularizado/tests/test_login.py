import pytest
from selenium.webdriver.common.by import By
from config import URL_LOGIN
from config import (URL_LOGIN,)
from browser.actions import acessar_pagina
from browser.login import (realizar_login,verificar_login,ler_mensagem)


def test_pagina_login(driver):
    """
    Verifica se o navegador está na página de login.
    
    driver:
        É o objeto do Selenium responsável por controlar
        o navegador. Através dele podemos abrir páginas,
        localizar elementos, clicar, preencher campos
        e consultar informações da página.

    acessar_pagina():
        É uma função do nosso projeto que recebe o driver
        e utiliza driver.get() para abrir uma URL.

    driver.current_url:
        Retorna a URL da página que está aberta atualmente
        no navegador.

    assert:
        É uma verificação do pytest.
        Se a condição for verdadeira, o teste continua.
        Se for falsa, o teste falha.

    Neste teste:
        O driver abre a URL de login.
        O Selenium informa a URL atual.
        O assert verifica se '/login' está na URL.
    """
    acessar_pagina(driver,URL_LOGIN)
    assert "/login" in driver.current_url


def test_campos_login(driver):
    """
    Verifica se os elementos necessários para o login
    existem e estão visíveis.

    driver.find_element():
        É utilizado para procurar um elemento dentro
        da página aberta no navegador.

    By.ID:
        Diz ao Selenium que queremos localizar o elemento
        utilizando o atributo HTML id.

     

        <input id="username">

        Nesse caso usamos:

        By.ID, username

    By.CSS_SELECTOR:
        Permite localizar um elemento utilizando
        um seletor CSS.

   
        button[type='submit']

        significa procurar um elemento <button> que
        possua o atributo type=submit.

    is_displayed():
        Verifica se o elemento está visível na página.

    Neste teste:
        O driver abre a página.
        O Selenium procura o campo de usuário.
        Procura o campo de senha.
        Procura o botão de login.
        Verifica se os três elementos estão visíveis.
    """


    acessar_pagina(driver,URL_LOGIN)
    usuario = driver.find_element(By.ID,"username")
    senha = driver.find_element(By.ID,"password")
    botao = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
    assert usuario.is_displayed()
    assert senha.is_displayed()
    assert botao.is_displayed()


def test_login_sucesso(driver):
    """
    Verifica se o login é realizado com sucesso.

    realizar_login():
        Ela utiliza o driver para:
        localizar o campo de usuário.
        preencher o usuário.
        localizar o campo de senha.
        preencher a senha.
        localizar o botão.
        clicar no botão.

    return True:
        A função realizar_login() retorna True quando
        consegue executar o processo de login.

    verificar_login():
        É uma função criada para verificar se o sistema
        realmente reconheceu a autenticação.

    Neste teste:
        O driver abre a página de login.
        realizar_login() executa o login.
        O primeiro assert verifica se o processo de login retornou True.
        verificar_login() confirma a autenticação.
    """

    acessar_pagina(driver,URL_LOGIN)

    resultado = realizar_login(driver)

    assert resultado is True

    assert verificar_login(driver) is True


def test_mensagem_login(driver):
    """
    Verifica se o sistema apresenta uma mensagem
    depois do login.

    ler_mensagem():
        É uma função criada no nosso projeto para
        localizar o elemento que contém a mensagem
        exibida pelo sistema.

    variável:
        'mensagem' recebe o resultado retornado pela
        função ler_mensagem().

    is not None:
        Verifica se a variável possui algum objeto.
        None significa que nenhum valor foi encontrado.

    len():
        Retorna a quantidade de caracteres de um texto.

    Neste teste:
        O driver abre a página.
        O login é realizado.
        A mensagem é localizada.
        Verificamos se a mensagem existe.
        Verificamos se ela possui algum texto.
    """


    acessar_pagina(
        driver,
        URL_LOGIN
    )

    realizar_login(
        driver
    )

    mensagem = ler_mensagem(
        driver
    )

    assert mensagem is not None
    assert len(mensagem) > 0


def test_mensagem_login_sucesso(driver):
    """
    Verifica se a mensagem apresentada pelo sistema
    contém o texto que confirma o login.
    in:
        O operador in verifica se um texto está
        contido dentro de outro texto.

        Exemplo:

        login in login realizado com sucesso"

        O resultado será True.

    Neste teste:
        O driver abre a página.
        O login é realizado.
        A mensagem do sistema é obtida.
        O assert procura o texto esperado dentroda mensagem.

    O teste falha se o texto esperado não estiver
    presente na mensagem.
    """
    acessar_pagina(driver,URL_LOGIN)
    realizar_login(driver)
    mensagem = ler_mensagem(driver)
    assert "You logged into a secure area!" in mensagem


def test_login_invalido(driver):
    """
        Representa o teste que deverá verificar um login
        utilizando credenciais inválidas.

        Atualmente este teste não é executado porque a função
        realizar_login() utiliza diretamente as credenciais
        configuradas no .env.

        pytest.skip():
            Informa ao pytest que este teste deve ser ignorado
            temporariamente.
        """

    pytest.skip(
        "O login inválido ainda não pode ser testado "
        "com a implementação atual."
    )
