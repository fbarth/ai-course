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
