
# 🏗️ Fase 1: O Tabuleiro (A Base)
import random 

class Tabuleiro():
    def __init__(self, tamanho = 5, num_navios=3):
        self.tamanho = tamanho
        self.num_navios = num_navios

        self.grelha = [["O"] * tamanho for _ in range(tamanho)]

        self.navios = []

    def print_tabuleiro(self):
        print("\n  " + " ".join([str(i) for i in range(self.tamanho)]))
        # Imprime cada linha com o seu número à esquerda
        for indice, linha in enumerate(self.grelha):
            print(f"{indice} " + " ".join(linha))
        print("")
# 🛑 Checkpoint 1
# jogo = Tabuleiro()
# jogo.print_tabuleiro()

