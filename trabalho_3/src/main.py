import sys
import os

# Adiciona o diretório principal ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kit_busca.testa_solucao import *


def main():
    TestaSolucao.test_funcao_sucessor(self)

main()