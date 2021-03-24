# Refactoring da implementação Map.py

Este enunciado é referente ao projeto de número 2 do primeiro semestre de 2021. Ele está relacionado com a implementação do problema de melhor rota entre cidades que está no arquivo `Map.py`. O objetivo deste projeto é implementar algumas melhorias neste código. 

## Como executar o que já existe e verificar se está tudo funcionando? 

Sugere-se fortemente que todos façam uso de um ambiente virtual `virtualenv` para garantir que os pacotes utilizados e versão do python sejam os corretos. Para isto, se você ainda não configurou o ambiente virtual deste projeto, faça: 

* a partir do diretório principal do projeto, execute: 

````bash
virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

Se você já tem o virtualenv configurado, basta digitar `source venv/bin/activate`. 

O próximo passo é ir até o diretório `search` e digitar `pytest`. Você deverá ter como retorno da execução das rotinas de teste o seguinte resultado: 

````bash
================================================= test session starts ==================================================
platform darwin -- Python 3.7.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/fabricio/Dropbox/workspaces/ai_classes/search
collected 19 items                                                                                                     

test_Map.py .........                                                                                            [ 47%]
test_PlusOneTwo.py .......                                                                                       [ 84%]
test_VacuumWorld.py ...                                                                                          [100%]

================================================== 19 passed in 9.82s ==================================================
````

Ou seja, todos os testes devem executar corretamente. 

Para este projeto, você irá usar o arquivo `Map.py` e o arquivo `test_Map.py`. Você pode executar só o teste relacionado ao projeto **Map** com os seguintes comandos: 

* `pytest test_Map.py`, ou;
* `pytest test_Map.py --capture=tee-sys` par também visualizar as impressões. 

Estas implementaçòes de teste são muito úteis pois você terá que implementar diversas modificações no arquivo `Map.py` e a única forma de garantir que você não inseriu nenhum *bug* durante este processo e executando os testes já especificados e outros que por ventura você queira adicionar. 

Outra forma de verificar o funcionando do arquivo `Map.py` é executando o próprio arquivo: 

````bash
python Map.py
````

## Atividades

Uma vez garantido que tudo está funcionando, vamos para as atividades! 

A estrutura da class `Map` é muito similar as outras classes já estudadas nesta disciplina. 
Possui os métodos da interface `State` implementados, como você pode ver abaixo. 

````python
class Map(State):

    def __init__(self, city, cost, op, goal):
    
    def sucessors(self):

    def is_goal(self):
    
    def description(self):
    
    def cost(self):
    
    def print(self):
    
    def env(self):

    def h(self):

    @staticmethod
    def createArea():

    @staticmethod
    def createHeuristics():
````

No entanto, além destes métodos, a classe `Map` também possui outros dois métodos que são responsáveis pela inicialização do mapa entre cidades e da tabela de heurísticas utilizada na solução do problema: `createArea()` e `createHeuristics()`. Na declaração destes dois métodos você irá encontrar dois **TODO**. Faça o que está descrito nestes **TODO**. 

Depois de alterados estes dois métodos, faça a carga de um mapa (com a sua respectiva heurística) mais realista. Com uma quantidade maior de cidades, como nomes mais realistas para as cidades, distâncias, etc. Lembre-se da heurística utilizada. Utilize uma heurística admissível para o problema. 

Para testar a execução desta solução com este novo mapa, utilize também arquivos de teste. 

## Por que as soluções reportadas pela implementação não são ótimas? 

Como vimos em sala de aula, a implementação `Map.py` não retorna uma solução ótima para o cenário `state = Map('i', 0, 'i', 'x')`. Por que? Identifique o problema e implemente uma solução. 