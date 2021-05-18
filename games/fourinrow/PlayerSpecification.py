from Player import Player

class PlayerSpecification(Player):

    def move(self, player_code, board):
        #
        # O jogador sabe qual é o seu número (player_code)
        # e consegue visualizar o ambiente (tabuleiro) através da variável board.
        #
        # A implementação deste método deve identificar qual é a melhor jogada que o 
        # jogador deve fazer com o objetivo de ganhar o jogo
        #
        # O método sempre deve retornar um valor entre 0 e 6 - que significa o número
        # da coluna onde ele deverá jogar. 
        #
        # Além disso, não pode escolher uma coluna que já esteja completa. 
        #
        return None
    
    def name(self):
        # retorna o nome do jogador
        return None