import requests

from config import URL_API


def consultar_api():
    """
    Realiza uma requisição GET para uma API REST.

    Retorno:
        list:
            Dados recebidos da API.

        None:
            Caso ocorra algum erro.
    """

    try:
        print("\nConsultando API...")

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

        print("\nJSON recebido com sucesso.")

        return dados

    except requests.exceptions.Timeout:
        print("\nERRO")
        print(
            "O servidor demorou muito "
            "para responder."
        )

        return None

    except requests.exceptions.ConnectionError:
        print("\nERRO")
        print(
            "Não foi possível conectar à API."
        )

        return None

    except requests.exceptions.HTTPError as erro:
        print("\nERRO HTTP")
        print(erro)

        return None

    except ValueError:
        print("\nERRO")
        print(
            "A resposta não contém "
            "um JSON válido."
        )

        return None

    except requests.exceptions.RequestException as erro:
        print("\nERRO DURANTE A REQUISIÇÃO")
        print(erro)

        return None
