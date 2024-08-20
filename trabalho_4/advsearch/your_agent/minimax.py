import random
from typing import Tuple, Callable
from typing import Callable, Tuple


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    def minimax(state, depth, alpha, beta, maximizing_player):
        if state.is_terminal() or depth == 0:
            return eval_func(state, state.player), None

        best_move = None

        if maximizing_player:
            best_value = float('-inf')
            for move in state.legal_moves():
                next_state = state.next_state(move)
                value, _ = minimax(next_state, depth - 1, alpha, beta, False)
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            return best_value, best_move
        else:
            best_value = float('inf')
            for move in state.legal_moves():
                next_state = state.next_state(move)
                value, _ = minimax(next_state, depth - 1, alpha, beta, True)
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value, best_move

    # Initial call to the minimax function
    _, best_move = minimax(state, max_depth, float('-inf'), float('inf'), state.player == 'B')
    return best_move



# def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
#     """
#     Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
#     :param state: state to make the move (instance of GameState)
#     :param max_depth: maximum depth of search (-1 = unlimited)
#     :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
#                     This function should take a GameState object and a string identifying the player,
#                     and should return a float value representing the utility of the state for the player.
#     :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
#     """  

#     raise NotImplementedError()
