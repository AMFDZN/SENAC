import logging

logging.basicConfig(                    
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"                  
)

logging.info("Programa iniciado.")

while True:
#doc string tres aspas 
    print(""" 
Escolha o exemplo para executar:
1 - Validação de número float
2 - Divisão com tratamento de erros
3 - Tratando erro de número inteiro inválido
4 - Tratando erro de divisão por zero e valor inválido
5 - Capturando qualquer erro e mostrando mensagem
6 - Uso de finally para mensagem que sempre aparece
7 - Levantando erro manualmente com raise
8 - Uso de else para seguir somente se não houver erro
9 - Contador: contar tentativas até acerto
10 - Acumulador: somar números
11 - Registro de eventos com logging
12 - Sair
""")

    opcao = input("Digite sua opção: ")

    match opcao:

        case "1":
            print("\nValidação de número float.")
            while True:
                entrada = input("Digite um número decimal: ")
                try: #tenta
                    numero = float(entrada) #transforma pra float, se não for numérico
                except ValueError: #excessão - não é um caractere numérico
                    print("Erro: valor inválido! Digite um número decimal.")
                    continue
                else:
                    print(f"Você digitou o número {numero}")
                    break
            input("Para voltar ao menu, pressione Enter.")

        case "2":
            print("\nDivisão com tratamento de erros.")
            while True:
                try:
                    numerador = float(input("Digite o numerador: "))
                    denominador = float(input("Digite o denominador: "))
                    resultado = numerador / denominador
                except ValueError: #ValueError valida se a entrada é numérico 
                    print("Erro: digite apenas números válidos.")
                    continue #volta pro início do while
                except ZeroDivisionError:  # método de validação se é divisível por zero
                    print("Erro: não é possível dividir por zero.")
                    continue
                else:
                    print(f"Resultado da divisão: {resultado}")
                    break #para o while e volta ao menu
            input("Para voltar ao menu, pressione Enter.")

        case "3":
            print("\nTratando erro de número inteiro inválido.")
            while True:
                try:
                    numero_inteiro = int(input("Digite um número inteiro: "))
                except ValueError:
                    print("Erro: digite um número inteiro válido!")
                else:
                    print(f"Você digitou: {numero_inteiro}")
                    break
            input("Para voltar ao menu, pressione Enter.")

        case "4":
            print("\nTratando erro de divisão por zero e valor inválido.")
            while True:
                try:
                    numerador_int = int(input("Digite o numerador: "))
                    denominador_int = int(input("Digite o denominador: "))
                    resultado_divisao = numerador_int / denominador_int
                except ValueError:
                    print("Erro: digite números válidos!")
                except ZeroDivisionError:
                    print("Erro: divisão por zero não é permitida!")
                else:
                    print(f"Resultado da divisão: {resultado_divisao}")
                    break
            input("Para voltar ao menu, pressione Enter.")

        case "5":
            print("\nCapturando qualquer erro e mostrando mensagem.")
            while True:
                try: #tenta. Faz uma verificação
                    valor_texto = input("Digite um número para converter em inteiro: ")
                    numero_convertido = int(valor_texto)
                except Exception as erro_capturado: #se não validou, salva o erro como Exception as nome_do_erro
                    print(f"Erro: {erro_capturado}")
                else:
                    print(f"Número convertido: {numero_convertido}")
                    break
            input("Para voltar ao menu, pressione Enter.")

        case "6":
            print("\nUso de finally para mensagem que sempre aparece.")
            while True:
                try:
                    divisor = int(input("Digite um número para dividir 100 por ele: "))
                    resultado_divisao_100 = 100 / divisor
                except ZeroDivisionError:
                    print("Erro: divisão por zero não é permitida!")
                except ValueError:
                    print("Erro: digite um número válido!")
                else:
                    print(f"Resultado da divisão: {resultado_divisao_100}")
                    break
                finally: #para este case
                    print("Tentativa finalizada.")
            input("Para voltar ao menu, pressione Enter.")

        case "7":
            print("\nLevantando erro manualmente com raise.")
            while True:
                try:
                    idade_usuario = int(input("Digite sua idade: "))
                    if idade_usuario < 0:
                        raise ValueError("Idade não pode ser negativa!")
                except ValueError as erro_entrada:
                    print(f"Erro: {erro_entrada}")
                else:
                    print(f"Idade registrada: {idade_usuario}")
                    break
            input("Para voltar ao menu, pressione Enter.")

        case "8":
            print("\nUso de else para seguir somente se não houver erro.")
            while True:
                try:
                    numero_positivo = int(input("Digite um número positivo: "))
                    if numero_positivo <= 0:
                        print("Erro: número não é positivo.")
                        continue
                except ValueError:
                    print("Erro: digite um número válido!")
                else:
                    print(f"Número positivo: {numero_positivo}")
                    break
            input("Para voltar ao menu, pressione Enter.")

        case "9":
            print("\nContar tentativas até digitar um número válido.")
            tentativas = 0

            while True:
                entrada = input("Digite um número inteiro: ")
                tentativas += 1

                try:
                    numero = int(entrada)
                except ValueError:
                    print("Erro: valor inválido.")
                else:
                    print(f"Você acertou após {tentativas} tentativa(s). Número: {numero}")
                    break

            input("Para voltar ao menu, pressione Enter.")

        case "10":
            print("\nSomar vários números.")
            soma = 0

            while True:
                entrada = input("Digite um número para somar ou 'sair' para finalizar: ")

                if entrada.lower() == "sair":
                    break

                try:
                    numero = float(entrada)
                    soma += numero
                except ValueError:
                    print("Erro: digite um número válido ou 'sair'.")

            print(f"Soma total dos números digitados: {soma}")
            input("Para voltar ao menu, pressione Enter.")

        case "11":
            print("\nRegistro de eventos com a biblioteca logging.")

            while True:
                try:
                    numerador = float(input("Digite o numerador: "))
                    denominador = float(input("Digite o denominador: "))

                    logging.info(
                        f"Valores informados: numerador={numerador}, denominador={denominador}"
                    )

                    resultado = numerador / denominador

                except ValueError:
                    print("Erro: digite apenas números válidos.")

                    logging.warning(
                        "Usuário informou um valor inválido."
                    )

                except ZeroDivisionError:
                    print("Erro: não é possível dividir por zero.")

                    logging.error(
                        "Tentativa de divisão por zero."
                    )

                except Exception:
                    print("Ocorreu um erro inesperado.")

                    logging.exception(
                        "Erro inesperado durante a execução."
                    )

                else:
                    print(f"Resultado: {resultado}")

                    logging.info(
                        f"Divisão realizada com sucesso. Resultado={resultado}"
                    )

                    break

                finally:
                    logging.info("Execução da opção Logging finalizada.")

            input("Para voltar ao menu, pressione Enter.")

        case "12":
            logging.info("Programa encerrado pelo usuário.")
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida.")
            logging.warning("Usuário selecionou uma opção inválida.")
            input("Para voltar ao menu, pressione Enter.")

logging.info("Programa finalizado.")
print("Programa finalizado.")