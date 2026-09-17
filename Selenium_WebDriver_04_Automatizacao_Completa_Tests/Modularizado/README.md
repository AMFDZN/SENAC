Selenium WebDriver 03

Projeto de estudos em automação de navegador com Selenium WebDriver, consumo de APIs REST, interpretação de JSON, variáveis de ambiente, robots.txt, tratamento de exceções e execução do navegador em modo Headless.

O projeto evolui o conteúdo desenvolvido na versão Selenium_WebDriver_02, adicionando recursos para tornar a automação mais organizada, segura e resistente a erros.

Objetivo

O objetivo deste projeto é praticar os principais conceitos envolvidos na criação de um robô de automação utilizando Python.

O projeto realiza três atividades principais:

Automação de uma página web utilizando Selenium.
Consulta de uma API REST utilizando Requests.
Interpretação e pesquisa de dados recebidos em formato JSON.

Além disso, foram adicionados recursos de:

Variáveis de ambiente com python-dotenv;
Verificação de robots.txt;
Esperas explícitas;
Tratamento de exceções;
Execução do Chrome em modo Headless;
Controle de fluxo utilizando True e False.
Tecnologias utilizadas
Python
Selenium WebDriver
Google Chrome
Requests
python-dotenv
JSON
HTTP / API REST
Bibliotecas utilizadas

Instale as dependências com:

pip install selenium
pip install requests
pip install python-dotenv


Ou, se utilizar um arquivo requirements.txt:

pip install -r requirements.txt

Estrutura do projeto
Selenium_WebDriver_03/

Selenium_WebDriver_Automatizacao_Completa.py
.env
.gitignore
README.md

Configuração do ambiente

O projeto utiliza o pacote python-dotenv para carregar informações sensíveis e configurações a partir de um arquivo .env.

Crie um arquivo chamado:

.env


Na raiz do projeto.

Exemplo:

URL_LOGIN=https://the-internet.herokuapp.com/login
URL_API=https://jsonplaceholder.typicode.com/users

USUARIO=tomsmith
SENHA=SuperSecretPassword!


O código carrega essas informações através de:

from dotenv import load_dotenv

load_dotenv()


E depois utiliza:

import os

URL_LOGIN = os.getenv("URL_LOGIN")
URL_API = os.getenv("URL_API")
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")

Importante

O arquivo .env não deve ser enviado para um repositório público.

Adicione ao .gitignore:

.env

Selenium WebDriver

O Selenium é utilizado para controlar o navegador automaticamente.

O projeto cria o Chrome através de:

driver = webdriver.Chrome(options=opcoes)


O navegador pode ser executado de duas formas.

Modo normal

O navegador abre normalmente na tela:

iniciar_navegador(headless=False)

Modo Headless

O navegador executa sem interface gráfica:

iniciar_navegador(headless=True)


O modo Headless é útil para automações executadas em servidores, pipelines e ambientes onde não existe uma interface gráfica.

Fluxo de automação

O processo de automação Selenium segue estas etapas:

Verificar robots.txt
        
Iniciar navegador
        
Acessar página
        
Aguardar elementos
        
Preencher usuário
        
Preencher senha
        
Clicar no botão
        
Verificar autenticação
        
Ler mensagem
        
Encerrar navegador

Funções do Selenium
iniciar_navegador()

Inicializa o Google Chrome.

Também permite escolher se o navegador será executado em modo Headless.

iniciar_navegador(headless=False)

acessar_pagina()

Acessa uma URL utilizando:

driver.get(url)

localizar_elemento()

Localiza elementos da página utilizando os localizadores do Selenium.

Exemplos:

By.ID
By.NAME
By.CLASS_NAME
By.TAG_NAME
By.CSS_SELECTOR
By.XPATH

aguardar_elemento()

Utiliza uma espera explícita:

WebDriverWait


e aguarda o elemento ficar visível:

EC.visibility_of_element_located()


Isso evita depender apenas de pausas fixas durante a automação.

preencher_campo()

Localiza um campo, limpa seu conteúdo e envia um texto:

campo.clear()
campo.send_keys(texto)


A função retorna:

True


quando o preenchimento ocorre corretamente.

Ou:

False


quando ocorre um erro.

clicar_elemento()

Aguarda o elemento estar disponível para clique utilizando:

EC.element_to_be_clickable()


Depois executa:

elemento.click()

realizar_login()

Executa o processo de autenticação:

Usuário
   
Senha
   
Botão Login
   
Mensagem


A função interrompe o fluxo caso alguma etapa falhe.

verificar_login()

Verifica se o login foi realizado analisando:

driver.current_url


e:

driver.page_source

ler_mensagem()

Localiza a mensagem exibida pela página depois do login e mostra seu conteúdo.

robots.txt

O projeto também verifica o arquivo robots.txt antes de iniciar a automação.

Isso é feito através do módulo:

import urllib.robotparser


A função:

verificar_robots_txt()


consulta as regras disponíveis e utiliza:

parser.can_fetch()


para verificar se o acesso é permitido para um robô.

Fluxo:

URL
 
robots.txt
 
Verificação da regra
 
Permitido?
  Sim = Continua
  Não = Automação cancelada


A verificação de robots.txt é uma medida de respeito às regras de rastreamento publicadas pelo site; ela não substitui a análise dos termos de uso, autenticação ou outras restrições do serviço.

API REST

A segunda parte do projeto utiliza a biblioteca:

requests


para realizar uma requisição HTTP GET.

A API utilizada no exercício é:

https://jsonplaceholder.typicode.com/users


A requisição é realizada através de:

requests.get()


com tempo limite:

timeout=10

Tratamento de erros da API

O projeto trata diferentes situações:

Timeout
requests.exceptions.Timeout


O servidor demorou muito para responder.

Erro de conexão
requests.exceptions.ConnectionError


Não foi possível estabelecer conexão com a API.

Erro HTTP
requests.exceptions.HTTPError


A API retornou uma resposta HTTP de erro.

JSON inválido
ValueError


A resposta não pôde ser convertida para JSON.

Outros erros do Requests
requests.exceptions.RequestException


Captura outros problemas relacionados à requisição HTTP.

JSON

Depois da requisição:

dados = resposta.json()


o JSON recebido é convertido pelo Requests para estruturas do Python.

Neste projeto, os dados são representados principalmente por:

Lista
 
Dicionários
 
Dados dos usuários


Cada usuário possui informações como:

name
username
email
phone
address

Interpretação dos dados

A função:

interpretar_json()


percorre os usuários:

for usuario in dados:


e utiliza:

usuario.get()


para obter os dados.

Também acessa informações aninhadas, como a cidade:

endereco = usuario.get("address", {})
cidade = endereco.get("city")

Pesquisa de usuário

A função:

pesquisar_usuario()


permite pesquisar um usuário pelo nome.

O projeto utiliza:

lower()


para tornar a pesquisa independente de letras maiúsculas e minúsculas.

Exemplo:

Digite o nome do usuário: Leanne


O robô procura o termo dentro dos nomes retornados pela API.

Menu

O projeto possui um menu interativo.

1  - Iniciar navegador
2  - Acessar página
3  - Realizar login
4  - Ler mensagem da página
5  - Executar navegação completa

API REST E JSON

6  - Consultar API
7  - Interpretar JSON
8  - Pesquisar usuário

ROBÔ COMPLETO

9  - Executar robô completo

0  - Sair

Robô completo

A opção:

9 - Executar robô completo


A execução completa utiliza o Selenium em modo Headless:

executar_navegacao(headless=True)

Tratamento de exceções

O projeto utiliza mecanismos de tratamento de erros para evitar que uma falha encerre o programa de maneira inesperada.

Entre as exceções utilizadas estão:

TimeoutException
WebDriverException


Além das exceções específicas do Requests.

Também é utilizado:

try:
    
except:
    
finally:
    


O bloco finally garante que o navegador seja encerrado:

driver.quit()


mesmo quando ocorre algum erro durante a execução.

Como executar

Depois de instalar as dependências e configurar o .env, execute:

python Selenium_WebDriver_Automatizacao_Completa.py


O menu será exibido:

Escolha uma opção:


Digite:

9


para executar o robô completo.

Exemplo de execução

Uma execução poderá apresentar informações semelhantes a:

Automação do navegador.

robots.txt:
Acesso permitido.

Acessando:
https://the-internet.herokuapp.com/login

Campo preenchido:
username

Campo preenchido:
password

Clique realizado:
button[type='submit']

Login enviado.

Autenticação realizada.

Mensagem do sistema:
You logged into a secure area!

Robô concluiu a navegação.

Encerrando navegador...

Consultando API...

Método: GET
URL: https://jsonplaceholder.typicode.com/users
Código HTTP: 200

JSON recebido com sucesso.

Interpretação do JSON.

Nome: Leanne Graham
Usuário: Bret
E-mail: Sincere@april.biz
Cidade: Gwenborough


Robô finalizado.

Conceitos praticados

Este projeto permite praticar:

Python;
funções;
parâmetros;
retorno de funções;
if / elif / else;
for;
try / except / finally;
Selenium WebDriver;
ChromeOptions;
Headless Browser;
WebDriverWait;
Expected Conditions;
localizadores Selenium;
By.ID;
By.CSS_SELECTOR;
click();
send_keys();
clear();
tratamento de exceções;
HTTP;
método GET;
API REST;
Requests;
JSON;
listas;
dicionários;
.env;
variáveis de ambiente;
robots.txt;
criação de robôs de automação.
Evolução do projeto
Selenium WebDriver 01

Fundamentos da automação:

Selenium
 
Chrome
 
Acessar página
 
Localizar elementos
 
Interagir com elementos

Selenium WebDriver 02

Integração com APIs:

Selenium
 
Requests
 
JSON

Selenium WebDriver 03

Automação mais robusta:

Selenium
 
Requests
 
JSON
 
python-dotenv
 
robots.txt
 
WebDriverWait
 
Tratamento de exceções
 
Headless

Próximas evoluções

Algumas possibilidades para as próximas versões:

Separar o projeto em módulos;
Criar classes para o WebDriver;
Criar uma classe para consumo da API;
Utilizar requirements.txt;
Criar arquivos de configuração;
Implementar logging com logging;
Criar testes automatizados com pytest;
Criar screenshots em caso de erro;
Criar relatórios de execução;
Implementar Page Object Model (POM);
Criar uma estrutura de projeto profissional;
Executar o robô através de linha de comando;
Integrar com Git e GitHub;
Executar a automação em CI/CD.
Observação

Este projeto possui finalidade educacional e foi desenvolvido para praticar automação web, consumo de APIs e manipulação de dados.

Ao automatizar sites reais, é importante respeitar as regras do serviço, seus termos de uso, políticas de acesso e limites de requisições.

Autor

Projeto desenvolvido como parte dos estudos de Python, Selenium WebDriver, APIs REST e automação de processos.