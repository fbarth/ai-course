from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from WorldWarcraftMap import WorldWarcraftMap
import time

WorldWarcraftMap.createArea()
WorldWarcraftMap.createHeuristics()

def test_BPI():
    print('Busca em profundidade iterativa: sair de Ahn Qiraj e chegar em Silvermoon')
    state = WorldWarcraftMap('Ahn Qiraj', 0, 'Ahn Qiraj', 'Silvermoon')
    algorithm = BuscaProfundidadeIterativa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Ahn Qiraj ; Gadgetzan ; Gurubashi Arena ; Gnomeregan ; Stormwind ; Kezan ; Orgrimmar ; Silvermoon"

def test_BPI2():
    print('Busca em profundidade iterativa: sair de Orgrimmar e chegar em Stormwind')
    state = WorldWarcraftMap('Orgrimmar', 0, 'Orgrimmar', 'Stormwind')
    algorithm = BuscaProfundidadeIterativa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Orgrimmar ; Kezan ; Stormwind"

def test_BCU():
    print('Busca em de custo uniforme: sair de Ahn Qiraj e chegar em Silvermoon')
    state = WorldWarcraftMap('Ahn Qiraj', 0, 'Ahn Qiraj', 'Silvermoon')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Ahn Qiraj ; Gadgetzan ; Gurubashi Arena ; Gnomeregan ; Stormwind ; Kezan ; Orgrimmar ; Silvermoon"

def test_BCU2():
    print('Busca de custo uniforme: sair de Orgrimmar e chegar em Stormwind')
    state = WorldWarcraftMap('Orgrimmar', 0, 'Orgrimmar', 'Stormwind')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Orgrimmar ; Kezan ; Stormwind"

def test_BCU3():
    print('Busca de custo uniforme: sair de Undercity e chegar em Darnassus')
    state = WorldWarcraftMap('Undercity', 0, 'Undercity', 'Darnassus')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Undercity ; Orgrimmar ; Thunder Bluff ; Darnassus"
    
def test_Gananciosa():
    print('Busca por algoritmo Ganancioso: sair de Orgrimmar e chegar em Stormwind')
    state = WorldWarcraftMap('Orgrimmar', 0, 'Orgrimmar', 'Stormwind')
    algorithm = BuscaGananciosa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Orgrimmar ; Kezan ; Stormwind"

def test_AEstrela():
    print('Busca por algoritmo A*: sair de Ahn Qiraj e chegar em Silvermoon')
    state = WorldWarcraftMap('Ahn Qiraj', 0, 'Ahn Qiraj', 'Silvermoon')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Ahn Qiraj ; Gadgetzan ; Gurubashi Arena ; Gnomeregan ; Stormwind ; Kezan ; Orgrimmar ; Silvermoon"

def test_AEstrela2():
    print('Busca por algoritmo A*: sair de Orgrimmar e chegar em Stormwind')
    state = WorldWarcraftMap('Orgrimmar', 0, 'Orgrimmar', 'Stormwind')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Orgrimmar ; Kezan ; Stormwind"

def test_AEstrela3():
    print('Busca por algoritmo A*: sair de Undercity e chegar em Darnassus')
    state = WorldWarcraftMap('Undercity', 0, 'Undercity', 'Darnassus')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "Undercity ; Orgrimmar ; Thunder Bluff ; Darnassus"