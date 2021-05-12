# Implementações sobre Jogos de Tabuleiro e Busca Competitiva

Nesta pasta você irá encontrar arquivos que implementam o Jogo Liga4 (em inglês, *four in a row*) e o jogo da velha. 

## Jogo da velha (1o semestre de 2021)

O jogo da velha é um jogo extremamente simples e amplamente conhecido, não necessitando descrições. 

O escopo do projeto de busca competitiva do 1o semestre de 2021 será a implementação de um jogador para o jogo da velha. Cada equipe, formada com até duas pessoas, deverá implementar um jogador de jogo da velha para participar de um torneio. 

Cada implementação deverá respeitar o exemplo descrito em [PlayerSpecificationJV.py](PlayerSpecificationJV.py). A implementação do jogo está em [JogoVelha.py](JogoVelha.py) e o campeonato está codificado em [TournamentJV.py](TournamentJV.py). Estes arquivos seguem uma estrutura muito similar a implementação dos jogadores, jogo e campeonato de Liga4. As equipes poderão usar estas implementações como exemplo para implementar os seus jogadores de jogo da velha. 

As regras para a competição são:

* Cada jogador só pode realizar movimentos válidos. Se um jogador realizar qualquer movimento inválido então ele será desclassificado da competição e, consequentemente, ficará em último lugar na competição.

* Todos os movimentos precisam ter uma duração máxima de 2 segundos.

* Nenhum jogador pode perder do jogador aleatório.

* O campeonato será composto por jogos de ida e volta, ou seja, todo jogador jogará duas vezes contra o mesmo adversário. Sendo que em uma partida um jogador começa e na outra partida outro jogador começa. 

* Nenhum jogador poderá perder do jogador aleatório. Se perder do jogador aleatório então o competidor será posto em último lugar na competição.

### Resultados da competição do 1o semestre de 2021

Resultado da primeira execução: 

````json
{
    'Barth JV': 6.5, 
    'Random JV': 2.5, 
    'BiggerBrainBot': 10.5, 
    'Chad, from based department': 10.5, 
    'Astolfo': 1, 
    'Mari e Bia': 4, 
    'Caio e Samuel': 10.5, 
    'Tigas e Torto': 10.5
}
````

Resultado da segunda execução:

````json
{
    'Barth JV': 7.0, 
    'Random JV': 2, 
    'BiggerBrainBot': 10.5, 
    'Chad, from based department': 10.5, 
    'Astolfo': 1, 
    'Mari e Bia': 4, 
    'Caio e Samuel': 10.5, 
    'Tigas e Torto': 10.5
}
````


## Jogo Liga4 (1o semestre de 2020)

O Jogo Liga4 (em inglês, *four in a row*) é um jogo de tabuleiro jogado por duas pessoas, sem variável aleatória e de soma zero. Ou seja, um jogador pode ganhar, empatar ou perder o jogo. 

O jogo é jogado em um tabuleiro com 7 colunas e 6 linhas colocado na vertical. Cada jogador tem peças de uma só cor. O jogo consiste em escolher em qual coluna colocar a sua peça. Quem alinhar 4 de suas peças na horizontal, vertical ou qualquer uma das diagonais vence. Neste site é possível jogar este jogo contra uma pessoa ou contra uma máquina: https://www.coolmathgames.com/0-4-in-a-row. 

Ao ver como o o jogo funciona em https://www.coolmathgames.com/0-4-in-a-row fica mais fácil entender as suas regras e objetivos. 

Nesta pasta temos cinco arquivos que estão relacionados com o jogo Liga4: 

* FourInRow.py: define todas as regras e gerencia o jogo. Para iniciar um jogo é necessário instanciar um objeto desta classe, passando dois jogadores, e executando o método **game()**:

````python
FourInRow(ManualPlayer(), RandomPlayer()).game()
````
Neste caso, foi instanciado um jogo onde um jogador manual joga contra um robô que tem os seus movimentos definidos de forma aleatória. 

* Player.py: define uma classe abstrata que possui um único método: 

````python   
@abstractmethod
def move(self, player_code, board):
    pass
````
Todos os jogadores precisam implementar o método *move* e o retorno deste método precisa ser um número entre 0 e 6 que é o índice da coluna onde será jogada a peça do jogador. 

* ManualPlayer.py: define um jogador manual. A implementação do método *move* nesta classe é apenas a leitura do índice da coluna pelo teclado: 

````python
def move(self, player_code, board):
    g = input("Enter a column (0..6) : ") 
    return int(g)
````

* RandomPlayer.py: define um jogador que joga de forma aleatória. O método *move* deste jogador esta implementado da seguinte forma: 

````python
def move(self, player_code, board):
        return randint(0, 6)
````

* PlayerSpecification.py: é um exemplo de como você deve começar a sua implementação. 

### Execução do campeonato

````bash
python3 Tournament.py > logs/competicao_results.log &
````

### Análise dos resultados

Para verificar quem venceu de quem:

````bash
cat logs/competicao_results.log | grep -e 'winner\|vs'  
````

Para identificar quem ultrapassou o limite de 15 segundos por jogada:

````bash
cat logs/competicao_results.log | grep -e 'duration' 
````

### Resultado final do campeonato

O campeonato foi executado utilizando o comando abaixo:

````bash
cd games
python3 Tournament.py > logs/competicao_results_final.log &
````

Ao analisar o log é possível verificar que nenhum jogador cometeu infrações e todos os jogadores respeitaram os 15 segundos para cada jogada. O resultado da competição é apresentado ao final do arquivo de log:

````json
{
    'Barth': 3, 
    'Daniel/Lucas': 10, 
    'Cheddar Player': 1, 
    'Sushi': 7, 
    'Allan': 5, 
    'Bru_Jose': 4
}
````

Desta forma, a colocação final foi: 

* 1o lugar: Daniel/Lucas
* 2o lugar: Sushi player
* 3o lugar: Allan/Guilherme
* 4o lugar: Bruna/José
* 5o lugar: Cheddar player

### Comentários sobre o resultado do campeonato

O jogador Daniel/Lucas ganhou todos os jogos. É um jogador que faz uso de uma função de avaliação muito robusta, conseguindo também identificar situações de risco para o jogador. Faz uso de uma implementação de MinMax com poda alpha/beta que só inicia a busca se o estado atual não é um estado final. A profundidade utilizada por este jogador para o algotimo MinMax é 5.

O jogador Bruna/José faz uso de uma estrutura muito similar ao jogador Daniel/Lucas. No entanto, a profundidade para a rotina MinMax configurada neste jogador é de 1. Isto fez este jogador perder diversas partidas para os demais jogadores. 

Os jogadores Sushi player, Cheddar player e Barth implementam o algoritmo MinMax com poda alpha/beta e fazem uso de uma função de utilidade muito parecida. Esta função de utilidade tem uma falha ao não analisar bem o lado esquerdo do tabuleiro. Ou seja, é uma função de utilidade mais fraca que a implementada nos jogadores Daniel/Lucas e Bruna/José. 

O jogador Allan/Guilerme implementa o algoritmo MinMax sem poda e com profundidade 3. Faz uso da mesma função de utilidade que os jogadores Sushi player, Cheddar player e Barth. 

Os jogadores Sushi player, Cheddar player e Barth têm diferentes profundidades configuradas. Sushi player e Barth têm profundidade igual a 5. Cheddar tem profundidade igual a 6. 








