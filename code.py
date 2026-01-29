
# 🏗️ Fase 1: O Tabuleiro (A Base)
import random 

class Tabuleiro():
    def __init__(self, tamanho = 5, num_navios=3):
        self.tamanho = tamanho
        self.num_navios = num_navios

        self.grelha = [["O"] * tamanho for _ in range(tamanho)]

        self.navios = []

        self.colocar_navios()

    def print_tabuleiro(self):
        print("\n  " + " ".join([str(i) for i in range(self.tamanho)]))
        # Imprime cada linha com o seu número à esquerda
        for indice, linha in enumerate(self.grelha):
            print(f"{indice} " + " ".join(linha))
        print("")

# 🛑 Checkpoint 1
# jogo = Tabuleiro()
# jogo.print_tabuleiro()


# 🚢 Fase 2: Esconder os Navios
    def colocar_navios(self):
        while self.navios <= self.num_navios:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)

            if (linha, coluna) not in self.navios:
                self.navios.append((linha, coluna))

# 🔫 Fase 3: A Mecânica de Disparo

    def fazer_jogada(self, linha, coluna):
        if linha < 0 or linha >= self.tamanho or coluna < 0 or coluna >= self.tamanho:
            return "Fora dos limites! Tenta números entre 0 e 4."
        
        if "O" not in self.grelha:
            return "Já disparaste aqui! Tenta outro sítio."
        
        if (linha, coluna) in self.navios:
            self.grelha[linha][coluna] = "X" # X marca o tiro certeiro
            self.navios.remove((linha, coluna)) # Remove o navio da lista de alvos
            return "ACERTASTE! 🔥"
        else:
            self.grelha[linha][coluna] = "#" # # marca tiro na água
            return "Água... 🌊"
        
# 🎮 Fase 4: O Loop do Jogo (Main)