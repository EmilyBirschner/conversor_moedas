import sys
import os

# Adiciona o diretório atual ao caminho do Python para ele achar seus arquivos
sys.path.append(os.getcwd())

# Importa a aplicação Flask definida no arquivo app.py
from app import app as application
