import os
import time

# Função para limpar o terminal
def limpar_terminal():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')