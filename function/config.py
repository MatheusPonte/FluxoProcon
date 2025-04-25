from dotenv import load_dotenv
import os
import sys
from end import endpoints


def load_environment():
    if getattr(sys, 'frozen', False):
        # Executável gerado pelo PyInstaller
        base_path = sys._MEIPASS
        dotenv_path = os.path.join(base_path, '.env')  # Caminho para o arquivo .env
    else:
        # Ambiente de desenvolvimento
        dotenv_path = os.path.join(os.getcwd(), '.env')  # Caminho normal para o arquivo .env durante o desenvolvimento
    print(f"Carregando .env de: {dotenv_path}")  # Imprime o caminho para verificar
    load_dotenv(dotenv_path)





