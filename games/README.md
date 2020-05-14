# Implementações sobre Jogos de Tabuleiro e Busca Competitiva

Nesta pasta você irá encontrar arquivos que implementam o Jogo Liga4 (em inglês, *four in a row*). Este é um jogo de tabuleiro jogado por duas pessoas, sem variável aleatória e de soma zero. Ou seja, um jogador pode ganhar, empatar ou perder o jogo. 

O jogo é jogado em um tabuleiro com 7 colunas e 6 linhas colocado na vertical. Cada jogador tem peças de uma só cor. O jogo consiste em escolher em qual coluna colocar a sua peça. Quem alinhar 4 de suas peças na horizontal, vertical ou qualquer uma das diagonais vence. Neste site é possível jogar este jogo contra uma pessoa ou contra uma máquina: https://www.coolmathgames.com/0-4-in-a-row. 

Ao ver como o o jogo funciona em https://www.coolmathgames.com/0-4-in-a-row fica mais fácil entender as suas regras e objetivos. 

Nesta pasta temos cinco arquivos que estão relacionados com o jogo Liga4: 

* FourInRow.py: define todas as regras e gerencia o jogo. Para iniciar um jogo é necessário instanciar um objeto desta classe, passando dois jogadores, e executando o método **game()**:

`````
FourInRow(ManualPlayer(), RandomPlayer()).game()
`````
Neste caso, foi instanciado um jogo onde um jogador manual joga contra um robô que tem os seus movimentos definidos de forma aleatória. 

* Player.py: define uma classe abstrata que possui um único método: 

````   
@abstractmethod
def move(self, player_code, board):
    pass
````
Todos os jogadores precisam implementar o método *move* e o retorno deste método precisa ser um número entre 0 e 6 que é o índice da coluna onde será jogada a peça do jogador. 

* ManualPlayer.py: define um jogador manual. A implementação do método *move* nesta classe é apenas a leitura do índice da coluna pelo teclado: 

````
def move(self, player_code, board):
    g = input("Enter a column (0..6) : ") 
    return int(g)
````

* RandomPlayer.py: define um jogador que joga de forma aleatória. O método *move* deste jogador esta implementado da seguinte forma: 

````
def move(self, player_code, board):
        return randint(0, 6)
````

* PlayerSpecification.py: é um exemplo de como você deve começar a sua implementação. 

## Execução do campeonato

````
python3 Tournament.py > logs/competicao_results.log &
````

## Análise dos resultados

Para verificar quem venceu de quem:

````
cat logs/competicao_results.log | grep -e 'winner\|vs'  
````

Para identificar quem ultrapassou o limite de 15 segundos por jogada:

````
cat logs/competicao_results.log | grep -e 'duration' 
````


