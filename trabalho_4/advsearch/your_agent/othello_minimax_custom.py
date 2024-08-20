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

    return minimax_move(state, 4, evaluate_custom)


def evaluate_custom(state: GameState, player: str) -> float:
    """
    Evaluates an Othello state from the point of view of the given player. 

    If the state is terminal, returns the utility (+1 for the winner, 
    -1 for the loser, 0 for a draw). 
    If non-terminal, returns an estimate of the state's value based on a 
    custom heuristic that considers the following factors:

    - Number of pieces of the player's color on the board
    - Number of pieces of the opponent's color on the board
    - Disc corner occupancy: Each corner piece contributes 4 points to 
    the score.
    - Disc stability: A disc is considered stable if it has another disc 
    of the same color adjacent to it in each direction (north, east, 
    south, and west). Each stable disc contributes 2 points to the score.
    - Disc mobility: The number of legal moves available to the player. 
    More legal moves indicate more options and potentially better 
    positioning.

    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    :return: float representing the heuristic score
    """

    board = state.get_board()


    playerPieces = 0
    enemyPieces = 0

    for line in state.board.tiles:
        for tile in line:
            if tile == player:
                playerPieces += 1
            elif tile == state.board.opponent(player):
                enemyPieces += 1

    # Pontuação básica com base na contagem de peças
    score = playerPieces - enemyPieces

    # Bônus de ocupação dos cantos
    corner_points = [(0, 0), (0, 7), (7, 0), (7, 7)]
    for point in corner_points:
        if board.tiles[point[0]][point[1]] == player:
            score += 4

    # Bônus de estabilidade das peças
    for x in range(8):
        for y in range(8):
            if board.tiles[x][y] == player:
                stable = True
                for dx, dy in Board.DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx <= 7 and 0 <= ny <= 7 and board.tiles[nx][ny] != player:
                        stable = False
                        break
                if stable:
                    score += 2


    # Verifica se o estado é terminal e ajusta a pontuação de acordo
    if state.is_terminal():
        if state.winner() == player:
            score = 1
        elif state.winner() == state.board.opponent(player):
            score = -1
        else:
            score = 0

    return score


