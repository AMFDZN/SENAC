import os

from dotenv import load_dotenv


load_dotenv()


URL_LOGIN = os.getenv("URL_LOGIN")
URL_API = os.getenv("URL_API")
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")
