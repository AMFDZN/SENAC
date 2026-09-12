from selenium import webdriver


def iniciar_navegador(headless=False):
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--window-size=1920,1080")

    if headless:
        opcoes.add_argument("--headless=new")

    return webdriver.Chrome(options=opcoes)
