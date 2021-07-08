# Projeto sobre uso de RL em Trading

## Introdução

O objetivo deste projeto é utilizar aprendizagem por reforço para implementar um robô de trading. 

Para esta finalidade, vamos utilizar uma extensão do OpenAI Gym chamada [gym-anytrading](https://github.com/AminHP/gym-anytrading).

Exemplos de utilização desta extensão podem ser vistos em:

* [trading.py](trading.py)
* [trading.ipynb](trading.ipynb)
* [trading_exemplo_completo.ipynb](trading_exemplo_completo.ipynb)

O arquivo [trading_exemplo_completo.ipynb](trading_exemplo_completo.ipynb) é o exemplo mais completo. Nele é possível visualizar a escolha aleatória de ações de *long* e *short*. Além disso, é possível entender a representação utilizada para o estado atual. 

```python
env.observation_space
```

Que utiliza a mesma estrutura do [MountainCar.py](MountainCar.py). Ou seja, um Box: 

```
Box(-inf, inf, (10, 2), float32)
```
com valores contínuos. 

## Objetivos

O principal objetivo deste trabalho é implementar um agente que usa aprendizagem por reforço para saber quando comprar e vender ações.

Para isso, você deve fazer: 

* Ler a documentação que está [aqui](https://github.com/AminHP/gym-anytrading).

* Executar e testar os arquivos listados acima. Se você executou a última versão do arquivo `requirements.txt` então você não precisa instalar via pip o `gym-anytrading`, nem o `jupyterlabs`. O pacote `gym-anytrading` é necessário para executar todos os códigos relacionados com trading e o `jupyterlabs` é necessário se você quiser usar o `jupyterlabs` para visualizar e editar os arquivos com formato `ipynb`. 

* Assim como o exemplo [MountainCar.py](MountainCar.py), neste projeto de trading você terá que discretizar o estado. Sendo assim, a próxima tarefa é encontrar um formato para discretizar a representação do `state` ou `observation`. Prazo máximo: 16/06/2021.

* Depois disso, temos que implementar o algoritmo **QLearning** e verificar o seu desempenho. 

* Por último. Utilize um dos algoritmos que estão em [Stable Baselines](https://stable-baselines.readthedocs.io/en/master/) para implementar um robô melhor que o implementado usando **QLearning**. 

## Regras relacionadas com as entregas

* Este projeto pode ser executado em equipes com até 3 integrantes;

* As equipes deverão criar um projeto no Github e informar ao professor via canvas toda vez que tiver uma atualização relevante no projeto. Ou seja, toda vez que tiver uma das entregas intermediárias;

* Teremos uma atividade aberta no canvas onde as equipes deverão informar o link para o Github e o nome dos participantes da equipe. Toda a troca de mensagens do professor da disciplina com a equipe deve acontecer via o sistema de mensagens desta atividade. 

## Resultados obtidos com os trabalhos dos alunos

TBD


