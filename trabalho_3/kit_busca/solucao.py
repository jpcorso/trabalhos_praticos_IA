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
    
    def __eq__(self, other):
        return False

    #def __hash__(self):
    #    return hash(self.estado)

def moveNum(s, newPos, num):
    s = s.replace(num, "")    
    new_string = s[:newPos] + num + s[newPos:]
    
    return new_string

def move(s, newPos):
    s = s.replace("_", "")    
    new_string = s[:newPos] + "_" + s[newPos:]
    
    return new_string

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

    print(resposta)
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

    #    def __init__(self, estado:str, pai, acao:str, custo:int):

    for acao in acoes:
        mov, s = acao
        newCusto = 1 + nodo.custo
        newNodo = Nodo(s, nodo, mov, newCusto)
        newNodos.append(newNodo)

    return newNodos

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
