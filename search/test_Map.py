from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from Map import Map
import time

Map.createArea()
Map.createHeuristics()

def test_BPI():
    print('Busca em profundidade iterativa: sair de h e chegar em o')
    state = Map('h', 0, 'h', 'o')
    algorithm = BuscaProfundidadeIterativa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "h ; g ; c ; o"

def test_BPI2():
    print('Busca em profundidade iterativa: sair de i e chegar em x')
    state = Map('i', 0, 'i', 'x')
    algorithm = BuscaProfundidadeIterativa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "i ; e ; m ; x"

def test_BCU():
    print('Busca em de custo uniforme: sair de h e chegar em o')
    state = Map('h', 0, 'h', 'o')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "h ; g ; c ; o"

def test_BCU2():
    print('Busca de custo uniforme: sair de i e chegar em x')
    state = Map('i', 0, 'i', 'x')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "i ; h ; k ; n ; m ; x"

def test_BCU3():
    print('Busca de custo uniforme: sair de p e chegar em n')
    state = Map('p', 0, 'p', 'n')
    algorithm = BuscaCustoUniforme()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "p ; c ; g ; h ; k ; n"
    
def test_Gananciosa():
    print('Busca por algoritmo Ganancioso: sair de h e chegar em o')
    state = Map('h', 0, 'h', 'o')
    algorithm = BuscaGananciosa()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "h ; g ; c ; o"

def test_AEstrela():
    print('Busca por algoritmo A*: sair de h e chegar em o')
    state = Map('h', 0, 'h', 'o')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "h ; g ; c ; o"

def test_AEstrela2():
    print('Busca por algoritmo A*: sair de i e chegar em x')
    state = Map('i', 0, 'i', 'x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "i ; h ; k ; n ; m ; x"

def test_AEstrela3():
    print('Busca por algoritmo A*: sair de p e chegar em n')
    state = Map('p', 0, 'p', 'n')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    assert result.show_path() == "p ; c ; g ; h ; k ; n"