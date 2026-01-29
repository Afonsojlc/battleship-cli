
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
        while len(self.navios) < self.num_navios:
            linha = random.randint(0, self.tamanho - 1)
            coluna = random.randint(0, self.tamanho - 1)

            if (linha, coluna) not in self.navios:
                self.navios.append((linha, coluna))

# 🔫 Fase 3: A Mecânica de Disparo

    def fazer_jogada(self, linha, coluna):
        if linha < 0 or linha >= self.tamanho or coluna < 0 or coluna >= self.tamanho:
            return "Fora dos limites! Tenta números entre 0 e 4."
        
        if self.grelha[linha][coluna] != "O":
            return "Já disparaste aqui! Tenta outro sítio."
        
        if (linha, coluna) in self.navios:
            self.grelha[linha][coluna] = "X" # X marca o tiro certeiro
            self.navios.remove((linha, coluna)) # Remove o navio da lista de alvos
            return "ACERTASTE! 🔥"
        else:
            self.grelha[linha][coluna] = "#" # # marca tiro na água
            return "Água... 🌊"
    
    def verificar_vitoria(self):
        # Se a lista de navios estiver vazia, o jogador ganhou
        return len(self.navios) == 0
    
# 🎮 Fase 4: O Loop do Jogo (Main)
def jogar():
    print("--- BEM-VINDO AO BATALHA NAVAL ---")
    print("Tenta afundar os navios escondidos do computador!")
    print("Legenda: O = Mar desconhecido | X = Navio Afundado | # = Tiro na Água")

    # Configurações do jogo
    tentativas = 10

    jogo = Tabuleiro()

    while tentativas > 0:
        jogo.print_tabuleiro()
        print(f"Tens {tentativas} tentativas restantes.")
        print(f"Navios restantes para afundar: {len(jogo.navios)}")
        try:
            # Pedir input ao utilizador
            entrada_linha = int(input("Escolha a LINHA (0-4): "))
            entrada_coluna = int(input("Escolha a COLUNA (0-4): "))
            
            # Fazer a jogada e guardar o resultado
            resultado = jogo.fazer_jogada(entrada_linha, entrada_coluna)
            print(f"\n---> {resultado}")
            
            # Só gasta tentativa se o tiro for válido (água ou navio)
            # Se for repetido ou fora dos limites, não gasta tentativa
            if "Fora" not in resultado and "Já disparaste" not in resultado:
                tentativas -= 1
                
            # Verifica se ganhou
            if jogo.verificar_vitoria():
                jogo.print_tabuleiro()
                print("\n🏆 PARABÉNS! Afundaste todos os navios inimigos!")
                break
                
        except ValueError:
            print("\n❌ Erro: Por favor introduz apenas NÚMEROS inteiros!")

    # Se sair do loop e ainda houver navios, perdeu
    if not jogo.verificar_vitoria():
        print("\n💀 Game Over! Ficaste sem tentativas.")
        print(f"Os navios estavam aqui: {jogo.navios}")

# Esta linha garante que o jogo só arranca se correres este ficheiro diretamente
if __name__ == "__main__":
    jogar()