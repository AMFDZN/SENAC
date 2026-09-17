from selenium.webdriver.common.by import By

from config import URL_LOGIN, USUARIO

from browser.actions import (
    acessar_pagina,
    aguardar_elemento,
    preencher_campo,
    clicar_elemento,
)


def test_acessar_pagina(driver):
    """
    Verifica se o Selenium consegue acessar
    a página configurada no .env.

    driver:
        É o objeto do Selenium responsável por
        controlar o navegador.

        Através do driver podemos:
        abrir páginas;
        localizar elementos;
        preencher campos;
        clicar em elementos;
        consultar informações da página.

    URL_LOGIN:
        É a URL de login carregada a partir do
        arquivo .env através do config.py.

    acessar_pagina():
        É uma função criada no projeto que recebe
        o driver e uma URL e utiliza o navegador
        para acessar essa página.

    driver.current_url:
        Retorna a URL da página que está aberta
        atualmente no navegador.

    assert:
        É uma verificação do pytest.
        Se a condição for verdadeira, o teste passa.
        Se for falsa, o teste falha.

    Neste teste:
        O driver abre a URL de login.
        O Selenium informa a URL atual.
        O teste verifica se /login está presente.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    assert "/login" in driver.current_url


def test_aguardar_elemento_encontra_elemento(driver):
    """
    Verifica se a função aguardar_elemento()
    consegue encontrar um elemento visível.

    aguardar_elemento():
        É uma função criada no projeto para esperar
        até que determinado elemento esteja disponível
        e visível na página.

    By.ID:
        Informa ao Selenium que o elemento será
        localizado através do atributo HTML 'id'.

        <input id="username">

        Para localizar esse elemento usamos:

        By.ID, "username"

    elemento:
        Recebe o elemento HTML encontrado pelo Selenium.

        Esse objeto normalmente é um WebElement.

    WebElement:
        É o objeto que representa um elemento HTML
        dentro do navegador.

        Por exemplo:
             campo de texto;
             botão;
             link;
             mensagem.

    is_displayed():
        Verifica se o elemento está visível na página.

    Neste teste:
         O driver abre a página de login.
         O Selenium procura o elemento username.
         aguardar_elemento() espera o elemento aparecer.
         Verificamos se o elemento foi encontrado.
         Verificamos se ele está visível.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    elemento = aguardar_elemento(
        driver,
        By.ID,
        "username"
    )

    assert elemento is not None
    assert elemento.is_displayed()


def test_aguardar_elemento_elemento_inexistente(driver):
    """
    Verifica o comportamento da função
    aguardar_elemento() quando um elemento
    não existe na página.

    elemento_que_nao_existe:
        É um ID propositalmente incorreto.
        Ele é utilizado para simular uma situação
        em que o Selenium não consegue encontrar
        o elemento.

    None:
        Representa que nenhum elemento foi retornado.

    aguardar_elemento():
        A função espera até o tempo configurado.
        Se o elemento não aparecer, retorna None.

    Neste teste:
         O driver abre a página.
         O Selenium procura um elemento inexistente.
         A função aguarda o tempo definido.
         A função retorna None.
         O assert confirma que o retorno é None.

    Esse tipo de teste é importante porque verifica
    como o código se comporta diante de uma situação
    de erro ou elemento ausente.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    elemento = aguardar_elemento(
        driver,
        By.ID,
        "elemento_que_nao_existe"
    )

    assert elemento is None


def test_preencher_campo(driver):
    """
    Verifica se a função preencher_campo()
    consegue preencher um campo de texto.



    preencher_campo():
        É uma função criada no projeto para:
             localizar um campo;
             esperar o campo ficar disponível;
             limpar seu conteúdo;
             inserir um texto.

    USUARIO:
        É o usuário carregado do arquivo .env
        através do config.py.

    send_keys():
        É um método do Selenium utilizado para
        enviar texto para um elemento, como um
        campo de formulário.

    get_attribute():
        Permite consultar o valor de um atributo
        HTML de um elemento.

        Neste caso:

        get_attribute("value")

        retorna o conteúdo digitado no campo.

    Neste teste:
         O driver abre a página.
         preencher_campo() localiza username.
         O usuário é inserido no campo.
         A função retorna True.
         O teste localiza novamente o campo.
         get_attribute("value") verifica o conteúdo.
         O conteúdo deve ser igual a USUARIO.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    resultado = preencher_campo(
        driver,
        By.ID,
        "username",
        USUARIO
    )

    assert resultado is True

    campo = driver.find_element(
        By.ID,
        "username"
    )

    assert campo.get_attribute("value") == USUARIO


def test_preencher_campo_inexistente(driver):
    """
    Verifica o comportamento de preencher_campo()
    quando o campo informado não existe.

    resultado:
        Recebe o valor retornado pela função
        preencher_campo().

    False:
        Representa que a operação não conseguiu
        ser realizada.

    campo_inexistente:
        É um ID propositalmente incorreto usado
        para simular uma falha na localização
        do campo.

    Neste teste:
         O driver abre a página.
         Tentamos localizar um campo inexistente.
         A função não consegue encontrar o campo.
         A função retorna False.
         O assert verifica esse retorno.

    Esse teste verifica se nossa função consegue
    tratar uma situação em que o elemento não existe.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    resultado = preencher_campo(
        driver,
        By.ID,
        "campo_inexistente",
        "teste"
    )

    assert resultado is False


def test_clicar_elemento(driver):
    """
    Verifica se a função clicar_elemento()
    consegue clicar em um botão.


    clicar_elemento():
        É uma função criada no projeto para localizar
        um elemento e executar um clique.

    By.CSS_SELECTOR:
        Permite localizar um elemento utilizando
        um seletor CSS.

        Neste teste:

        button[type='submit']

        significa procurar um elemento <button>
        cujo atributo type seja 'submit'.

    click():
        É o método do Selenium utilizado para
        clicar em um elemento.

    resultado:
        Recebe o retorno da função clicar_elemento().

    True:
        Indica que o clique foi realizado com sucesso.

    Neste teste:
         O driver abre a página.
         O Selenium procura o botão.
         A função aguarda o botão estar disponível.
         O Selenium executa o clique.
         A função retorna True.
         O assert confirma o resultado.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    resultado = clicar_elemento(
        driver,
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    assert resultado is True


def test_clicar_elemento_inexistente(driver):
    """
    Verifica o comportamento de clicar_elemento()
    quando o botão informado não existe.

    botao_inexistente:
        É um ID propositalmente incorreto utilizado
        para simular uma situação em que o Selenium
        não encontra o elemento.

    False:
        Indica que a operação de clique não conseguiu
        ser realizada.

    Tratamento de erro:
        A função clicar_elemento() possui tratamento
        para problemas como TimeoutException e
        WebDriverException.

    Neste teste:
         O driver abre a página.
         Tentamos localizar um botão inexistente.
         O Selenium espera pelo elemento.
         O elemento não é encontrado.
         A função retorna False.
         O assert confirma o resultado.

    Esse teste verifica se o código consegue lidar
    com uma tentativa de clique em um elemento
    que não está disponível.
    """

    acessar_pagina(
        driver,
        URL_LOGIN
    )

    resultado = clicar_elemento(
        driver,
        By.ID,
        "botao_inexistente"
    )

    assert resultado is False