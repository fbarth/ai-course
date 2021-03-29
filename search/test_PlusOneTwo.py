from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from PlusOneTwo import PlusOneTwo
from datetime import date, datetime

def test_largura():
    state = PlusOneTwo(1, '', 10)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; 2 ; 2 ; 2 ; 2 ; 1"

def test_profundidade():
    state = PlusOneTwo(1, '', 10)
    algorithm = BuscaProfundidade()
    inicio = datetime.now()
    result = algorithm.search(state, 50)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; 1 ; 1 ; 1 ; 1 ; 1 ; 1 ; 1 ; 1 ; 1"

def test_BPI():
    state = PlusOneTwo(1, '', 10)
    inicio = datetime.now()
    algorithm = BuscaProfundidadeIterativa()
    fim = datetime.now()
    print(fim - inicio)
    result = algorithm.search(state)
    assert result.show_path() == " ; 1 ; 2 ; 2 ; 2 ; 2"

def test_custoUniforme():
    state = PlusOneTwo(1, '', 10)
    inicio = datetime.now()
    algorithm = BuscaCustoUniforme()
    fim = datetime.now()
    print(fim - inicio)
    result = algorithm.search(state)
    assert result.show_path() == " ; 1 ; 2 ; 2 ; 2 ; 2"

def test_gananciosa():
    state = PlusOneTwo(1, '', 10)
    inicio = datetime.now()
    algorithm = BuscaGananciosa()
    fim = datetime.now()
    print(fim - inicio)
    result = algorithm.search(state)
    assert result.show_path() == " ; 2 ; 2 ; 2 ; 2 ; 1"

def test_AEstrela():
    state = PlusOneTwo(1, '', 10)
    inicio = datetime.now()
    algorithm = AEstrela()
    fim = datetime.now()
    print(fim - inicio)
    result = algorithm.search(state)
    assert result.show_path() == " ; 2 ; 2 ; 2 ; 2 ; 1"

def test_largura_bigger():
    state = PlusOneTwo(1, '', 40)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)

def test_largura_bigger_AEstrela():
    state = PlusOneTwo(1, '', 500)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    print(result.show_path())

