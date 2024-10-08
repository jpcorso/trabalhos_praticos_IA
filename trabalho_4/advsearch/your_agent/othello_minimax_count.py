import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, 4, evaluate_count)

    #return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])


def evaluate_count(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on the number of pieces of each color.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    playerPieces = 0
    enemyPieces = 0
    
    for line in state.board.tiles:
        for tile in line:
            if tile == player:
                playerPieces += 1
            elif tile == state.board.opponent(player):
                enemyPieces += 1
    
    return int(playerPieces - enemyPieces) 

#    for tile in state.board.tiles:
#        print(tile)
#    myPlayer = Board.num_pieces(player)
#    opponentPlayer = state.board.num_pieces('B' if player == 'W' else 'W')
#
#    return float(myPlayer - opponentPlayer)