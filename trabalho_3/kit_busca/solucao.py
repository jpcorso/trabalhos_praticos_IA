from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    #pai:Nodo
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
    
    #def __eq__(self, other):
    #    return self.estado == other.estado
        
    def isFinal(self): 
        estadoFinal = "12345678_"
        return self.estado == estadoFinal


    def caminha(self):
        
        caminho = []

        nodo = self
        while nodo.pai != None:
            caminho.insert(0, nodo.acao)
            nodo = nodo.pai
        return caminho

    def hammingDistance(self): 
        #otimizar
        estadoFinal = "12345678_"        
        #return sum(1 for a, b in zip(self.estado, estadoFinal) if a != b)
        return sum(self.estado[i] != estadoFinal[i] for i in range(len(self.estado)))

    def manhattanDistance(self):
        coordenadas = {
            "1": (0, 0),
            "2": (0, 1),
            "3": (0, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "7": (2, 0),
            "8": (2, 1),
            "_": (2, 2)
        }
        manhattan = 0 

        for i in range (9):
            x,y = coordenadas[self.estado[i]]
            manhattan = manhattan + abs(x - (i // 3))  + abs(y - (i % 3))

        print(manhattan)
        return manhattan




# ====================
def moveNum(s, newPos, num):
    s = s.replace(num, "")    
    new_string = s[:newPos] + num + s[newPos:]
    
    return new_string

def move(s, newPos):
    s = s.replace("_", "")    
    new_string = s[:newPos] + "_" + s[newPos:]
    
    return new_string

        
def hammingDistance(s): 
    estadoFinal = "12345678_"        
    return sum(s[i] != estadoFinal[i] for i in range(len(s)))

def manhattanDistance(s):
    coordenadas = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "_": (2, 2)
    }
    manhattan = 0 

    for i in range (9):
        x,y = coordenadas[s[i]]
        manhattan = manhattan + abs(x - (i // 3))  + abs(y - (i % 3))

    return manhattan
# =====================

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    pos = estado.index('_')
    free = [0,1,2,3]

    #se esta em cima (0,1,2), nao vai pra cima
    #remove 0 
    #0 = acima
    if pos < 3:
        free[0] = -1 

    #se esta em baixo (6,7,8), nao vai pra baixo
    #remove 1
    #1 = abaixo
    if pos > 5:
        free[1] = -1

    dir = [2,5,8]
    #dir = 2
    if pos in dir:
        free[2] = -1


    esq = [0,3,6]
    #esq = 3
    if pos in esq:
        free[3] = -1

    resposta = []

    newPos = -1 
    for direction in free:
        if direction == 0:
            newPos = pos - 3 
            num = estado[newPos] 
            newString = moveNum (estado, pos, num)
            newString = move(newString, newPos)
            resposta.append(("acima", newString))

        if direction == 1:
            newPos = pos + 3 
            num = estado[newPos] 
            newString = moveNum (estado, pos, num)
            newString = move(newString, newPos)
            resposta.append(("abaixo", newString))

        if direction == 2:
            newPos = pos + 1
            newString = move(estado, newPos)
            resposta.append(("direita", newString))

        if direction == 3: 
            newPos = pos - 1
            newString = move(estado, newPos)
            resposta.append(("esquerda", newString))

    return resposta
    


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """

    acoes = sucessor(nodo.estado)
    newNodos = []

    for acao in acoes:
        mov, s = acao
        newCusto = 1 + nodo.custo
        newNodo = Nodo(s, nodo, mov, newCusto)
        newNodos.append(newNodo)

    return newNodos

#def heuristica_hamming(nodos):
#    melhorNodo = nodos[0]
#    value = melhorNodo.hammingDistance() + melhorNodo.custo
# 
#    for nodo in nodos:
#        candidato = nodo.hammingDistance()  + nodo.custo
#        if candidato < value:
#            value = candidato
#
#    return nodo
#
#
#
#def heuristica_manhattan(nodos): 
#    melhorNodo = nodos[0]
#    value = melhorNodo.manhattanDistance() + melhorNodo.custo
# 
#    for nodo in nodos:
#        candidato = nodo.manhattanDistance()  + nodo.custo
#        if candidato < value:
#            value = candidato
#
#    return nodo
# 


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    fronteiraDict = {
    }
    explorados = set()

    fronteiraDict[hammingDistance(estado)+1] = [Nodo(estado, None, None, 1)]

    while True:

        if len(fronteiraDict) == 0:
            return None
        
        index = min(fronteiraDict.keys())
        nodoV = fronteiraDict[index].pop(0)
        if len(fronteiraDict[index]) == 0:
            fronteiraDict.pop(index)

        if nodoV.isFinal():
            return nodoV.caminha()
        
        if nodoV.estado not in explorados:
            explorados.add(nodoV.estado)

            vizinhos = expande(nodoV)

            for vi in vizinhos:
                if vi.estado not in explorados:
                    if (vi.custo + hammingDistance(vi.estado)) not in fronteiraDict:
                        fronteiraDict[vi.custo + hammingDistance(vi.estado)] = [vi]
                    
                    else:
                        fronteiraDict[vi.custo + hammingDistance(vi.estado)].append(vi)


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    fronteiraDict = {
    }
    explorados = set()

    fronteiraDict[manhattanDistance(estado)+1] = [Nodo(estado, None, None, 1)]

    while True:

        if len(fronteiraDict) == 0:
            return None
        
        index = min(fronteiraDict.keys())
        nodoV = fronteiraDict[index].pop(0)
        if len(fronteiraDict[index]) == 0:
            fronteiraDict.pop(index)

        if nodoV.isFinal():
            return nodoV.caminha()
        
        if nodoV.estado not in explorados:
            explorados.add(nodoV.estado)

            vizinhos = expande(nodoV)

            for vi in vizinhos:
                if vi.estado not in explorados:
                    if (vi.custo + manhattanDistance(vi.estado)) not in fronteiraDict:
                        fronteiraDict[vi.custo + manhattanDistance(vi.estado)] = [vi]
                    
                    else:
                        fronteiraDict[vi.custo + manhattanDistance(vi.estado)].append(vi)


#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
