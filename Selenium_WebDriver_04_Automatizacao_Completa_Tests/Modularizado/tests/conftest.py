import pytest
from browser.driver import iniciar_navegador


@pytest.fixture
def driver():
    """
    Cria e disponibiliza um navegador para os testes
    que precisam utilizar o Selenium.

    @pytest.fixture:
        É um recurso do pytest utilizado para preparar
        algo que será usado pelos testes.

        Neste projeto, a fixture cria um navegador
        antes de cada teste que receber o parâmetro
        'driver'.

    driver:
        É o objeto do Selenium WebDriver.

        Ele representa o navegador que será controlado
        automaticamente pelo Selenium.

        Através dele podemos:
             abrir páginas;
             localizar elementos;
             preencher campos;
             clicar em botões;
             consultar a URL atual;
             acessar informações da página.

    iniciar_navegador():
        É uma função criada no projeto que configura
        e inicia o Google Chrome através do Selenium.

    headless=True:
        Informa que o navegador deve ser executado
        sem abrir uma janela visível na tela.

        O navegador continua funcionando normalmente,
        mas sua interface gráfica não é exibida.

    yield:
        Entrega o navegador para o teste.

        Tudo que estiver antes do yield funciona como
        preparação do teste.

        O código depois do yield será executado quando
        o teste terminar.

    try:
        Permite executar o teste com segurança e
        garantir que o código de encerramento seja
        executado mesmo se ocorrer algum erro.

    finally:
        O bloco finally sempre é executado depois
        do teste, mesmo quando o teste falha.

    navegador.quit():
        Encerra completamente o navegador e a sessão
        criada pelo Selenium.

        Isso é importante para não deixar processos
        do Chrome abertos depois dos testes.

    Fluxo:

         O pytest encontra um teste que precisa de driver.
         A fixture é executada.
         Um navegador Chrome é criado.
         O navegador é executado em modo headless.
         O yield entrega o navegador ao teste.
         O teste utiliza o driver.
         O teste termina.
         O bloco finally é executado.
         navegador.quit() encerra o navegador.


    """

    navegador = iniciar_navegador(
        headless=True
    )

    try:
        yield navegador

    finally:
        navegador.quit()