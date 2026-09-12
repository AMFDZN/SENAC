def interpretar_json(dados):
    """
    Interpreta os dados recebidos em JSON.
    """

    if dados is None:
        return

    for usuario in dados:

        nome = usuario.get("name")
        username = usuario.get("username")
        email = usuario.get("email")

        endereco = usuario.get(
            "address",
            {}
        )

        cidade = endereco.get("city")

        print("\nNome:", nome)
        print("Usuário:", username)
        print("E-mail:", email)
        print("Cidade:", cidade)
        print("-" * 40)


def pesquisar_usuario(dados):
    """
    Pesquisa um usuário dentro dos dados
    retornados pela API.
    """

    if dados is None:
        return

    termo = input(
        "\nDigite o nome do usuário: "
    )

    encontrado = False

    for usuario in dados:

        nome = usuario.get("name", "")

        if termo.lower() in nome.lower():

            print("\nUsuário encontrado:")
            print(
                "Nome:",
                usuario.get("name")
            )

            print(
                "E-mail:",
                usuario.get("email")
            )

            print(
                "Telefone:",
                usuario.get("phone")
            )

            encontrado = True

    if not encontrado:
        print("\nUsuário não encontrado.")
