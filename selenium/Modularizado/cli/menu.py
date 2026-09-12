def menu():
    """
    Exibe o menu principal do robô.
    """

    while True:

        print(
            """
1 - Iniciar navegador
2 - Acessar página
3 - Realizar login
4 - Ler mensagem da página
5 - Executar navegação completa

API REST E JSON

6 - Consultar API
7 - Interpretar JSON
8 - Pesquisar usuário

ROBÔ COMPLETO

9 - Executar robô completo

0 - Sair

"""
        )

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("\nRobô encerrado.")
            break

        executar_opcao(opcao)


def executar_opcao(opcao):
    """
    Direciona a opção escolhida
    para o respectivo handler.
    """

    from cli.handlers import (
        iniciar_navegador_menu,
        acessar_pagina_menu,
        realizar_login_menu,
        ler_mensagem_menu,
        executar_navegacao_menu,
        consultar_api_menu,
        interpretar_json_menu,
        pesquisar_usuario_menu,
        executar_robo_menu
    )

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
