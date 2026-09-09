from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 1. Configurar as opções do Chrome
chrome_options = Options()

# Caminho do executável do Chrome via Flatpak no Linux
# Geralmente fica em /var/lib/flatpak/exports/bin/com.google.Chrome 
# ou você pode usar o atalho de execução direta do flatpak:
chrome_options.binary_location = "/usr/bin/flatpak"

# Argumentos necessários para o Flatpak entender o comando de execução
chrome_options.add_argument("run")
chrome_options.add_argument("com.google.Chrome")

# Argumentos cruciais para evitar problemas de permissão dentro do container
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 2. Configurar o ChromeDriver (certifique-se de que a versão bate com a do Chrome)
# Baixe o chromedriver compatível e passe o caminho dele aqui:
service = Service(executable_path="/caminho/para/seu/chromedriver")

# 3. Iniciar o navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

# Testar o acesso
driver.get("https://google.com")

print(driver.title)
driver.quit()
