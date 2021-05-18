from Player import Player

class PlayerSpecificationJV(Player):

    def move(self, player_code, position):
        #
        # O jogador sabe qual é o seu número (player_code)
        # e consegue visualizar o ambiente (tabuleiro) através da variável board.
        #
        # A implementação deste método deve identificar qual é a melhor jogada que o 
        # jogador deve fazer com o objetivo de ganhar o jogo
        #
        # O método sempre deve retornar um valor entre 0 e 8 - que significa a posição 
        # no tabuleiro do jogo da velha: 
        # 
        # | 0 | 1 | 2 |
        # | 3 | 4 | 5 |
        # | 6 | 7 | 8 | 
        #
        # Além disso, não pode escolher uma posição que já esteja completa. 
        #
        return None
    
    def name(self):
        # retorna o nome do jogador
        return None