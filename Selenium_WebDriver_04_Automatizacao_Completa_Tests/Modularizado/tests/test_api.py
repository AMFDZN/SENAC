from api.client import consultar_api


def test_consultar_api_retorna_dados():
    """
    Verifica se a função consultar_api()
    consegue obter dados da API.

    consultar_api():
        É uma função criada no projeto para fazer
        uma requisição HTTP para a API.

    dados:
        É uma variável que recebe o resultado
        retornado pela função consultar_api().

    None:
        Representa a ausência de um valor.

    assert:
        É uma verificação feita pelo pytest.
        Se a condição for verdadeira, o teste passa.
        Se for falsa, o teste falha.

    is not None:
        Verifica se a variável recebeu algum valor.

    Neste teste:
         A função consulta a API.
         O resultado é armazenado em dados.
         O teste verifica se dados não é None.
    """

    dados = consultar_api()

    assert dados is not None


def test_consultar_api_retorna_lista():
    """
    Verifica se a API retorna os dados no formato
    de uma lista Python.


    list:
        É uma estrutura do Python utilizada para
        armazenar vários valores em sequência.

      

        ["Ana", "João", "Maria"]

    isinstance():
        Verifica se um objeto pertence a determinado
        tipo de dado.

   

        isinstance(dados, list)

        significa:

        "dados é uma lista?"

    Neste teste:
         A API é consultada.
         O resultado é armazenado em dados.
         isinstance() verifica se dados é uma list.
    """

    dados = consultar_api()

    assert isinstance(dados,list)


def test_consultar_api_retorna_usuarios():
    """
    Verifica se a API retornou pelo menos um usuário.

    len():
        Retorna a quantidade de elementos existentes
        dentro de uma estrutura.

        

        len([1, 2, 3])

        retorna:

        3

    >:
        Significa "maior que".

    Neste teste:

        len(dados) > 0

        significa:

        "A quantidade de usuários é maior que zero?"

    O teste passa se existir pelo menos um usuário
    na resposta da API.
    """

    dados = consultar_api()

    assert len(dados) > 0


def test_usuario_possui_nome():
    """
    Verifica se o primeiro usuário retornado pela API
    possui a informação de nome.

    dados[0]:
        A posição 0 representa o primeiro elemento
        de uma lista Python.

        Exemplo:

        dados = ["Ana", "João"]

        dados[0]

        retorna:

        "Ana"

    usuario:
        Recebe o primeiro usuário da lista.

    dicionário:
        Os usuários retornados pela API são representados
        como dicionários Python.

        Exemplo:

        {
            "name": "Leanne Graham",
            "email": "email@example.com"
        }

    "name" in usuario:
        Verifica se existe uma chave chamada "name"
        dentro do dicionário.

    usuario["name"]:
        Acessa o valor armazenado na chave "name".

    Neste teste:
         A API é consultada.
         O primeiro usuário é selecionado.
         Verificamos se existe a chave "name".
         Verificamos se ela possui algum valor.
    """

    dados = consultar_api()

    usuario = dados[0]

    assert "name" in usuario
    assert usuario["name"]


def test_usuario_possui_email():
    """
    Verifica se o primeiro usuário retornado pela API
    possui um endereço de e-mail.


    "email" in usuario:
        Verifica se existe uma chave chamada "email"
        dentro do dicionário do usuário.

    usuario["email"]:
        Acessa o valor armazenado na chave "email".

    assert:
        Primeiro verifica se a chave existe.
        Depois verifica se o valor da chave não está vazio.

    Neste teste:
        A API é consultada.
        O primeiro usuário é selecionado.
        Procuramos a chave "email".
        Verificamos se existe um valor nessa chave.
    """

    dados = consultar_api()

    usuario = dados[0]

    assert "email" in usuario
    assert usuario["email"]


def test_usuario_possui_endereco():
    """
    Verifica se o primeiro usuário possui um endereço
    e se esse endereço está representado como um
    dicionário Python.

    "address" in usuario:
        Verifica se o usuário possui uma chave chamada
        "address".

    usuario["address"]:
        Acessa o endereço armazenado dentro do usuário.

    dict:
        É o tipo de dado utilizado pelo Python para
        armazenar informações no formato chave e valor.

        Exemplo:

        {
            "city": "Gwenborough",
            "zipcode": "92998-387"
        }

    isinstance():
        Verifica se o valor recebido é realmente
        um dicionário.

        Exemplo:

        isinstance(usuario["address"], dict)

        significa:

        "O endereço é um dicionário?"

    Neste teste:
         A API é consultada.
         O primeiro usuário é selecionado.
         Verificamos se existe a chave "address".
         Verificamos se o endereço é um dict.
    """

    dados = consultar_api()

    usuario = dados[0]

    assert "address" in usuario

    assert isinstance(usuario["address"],dict)
