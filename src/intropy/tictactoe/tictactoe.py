"""Tic Tac Toe Player."""

from __future__ import annotations

import math
from typing import Literal

X = "X"
O = "O"
EMPTY = " "
_ = " "

Mark = Literal["X", "O", " "]
Player = Literal["X", "O", " "]
I = Literal[0, 1, 2]
J = Literal[0, 1, 2]
Board = tuple[tuple[Mark, Mark, Mark], tuple[Mark, Mark, Mark], tuple[Mark, Mark, Mark]]
Action = tuple[I, J]

MAX_DEPTH = 1000000


def initial_state() -> Board:
    """Return starting state of the board."""
    return ((_, _, _), (_, _, _), (_, _, _))


def player(board: Board) -> Player:
    """Return player who has the next turn on a board."""
    return X if tuple(mark for row in board for mark in row).count(EMPTY) % 2 else O


def actions(board: Board) -> list[Action]:
    """Returns set of all possible actions (i, j) available on the board."""
    if winner(board):
        return []

    return [
        (i, j)
        for i, row in enumerate(board)
        for j, mark in enumerate(row)
        if mark == EMPTY
    ]


def result(board: Board, action: Action) -> Board:
    """Returns the board that results from making move (i, j) on the board."""
    if action not in set(actions(board)):
        msg = f"Action {action} n'est pas admissible."
        raise ValueError(msg)

    current_player = player(board)

    i, j = action

    new_board = [list(row) for row in board]
    new_board[i][j] = current_player

    return tuple(tuple(row) for row in new_board)


def winner(board: Board) -> Player:
    """Returns the winner of the game, if there is one."""
    winning_lines = {
        (board[0][0], board[0][1], board[0][2]),
        (board[1][0], board[1][1], board[1][2]),
        (board[2][0], board[2][1], board[2][2]),

        (board[0][0], board[1][0], board[2][0]),
        (board[0][1], board[1][1], board[2][1]),
        (board[0][2], board[1][2], board[2][2]),

        (board[0][0], board[1][1], board[2][2]),
        (board[0][2], board[1][1], board[2][0]),
    }

    if (X, X, X) in winning_lines:
        return X
    if (O, O, O) in winning_lines:
        return O

    return EMPTY


def terminal(board: Board) -> bool:
    """Returns True if game is over, False otherwise."""
    return not actions(board)


def utility(board: Board) -> int:
    """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
    match winner(board):
        case "X":
            return 1
        case "O":
            return -1
        case _:
            return 0


def minimax(board: Board) -> Action:
    """Returns the optimal action for the current player on the board."""
    if terminal(board):
        msg = "Aucune action supplémentaire admissible."
        raise ValueError(msg)

    def _minimax(board: Board, remaining_depth: int) -> int:
        if not remaining_depth or terminal(board):
            return utility(board)

        value, comparison = (
            (-math.inf, max)
            if player(board) == X
            else (math.inf, min)
        )

        for action in actions(board):
            value = comparison(
                value,
                _minimax(result(board, action), remaining_depth - 1)
            )
        return value

    is_x = player(board) == X

    best_value = -math.inf if is_x else math.inf
    best_action = None

    for candidate_action in actions(board):
        # On évalue le score de chaque action possible
        score = _minimax(result(board, candidate_action), MAX_DEPTH)

        # On met à jour la meilleure action selon le joueur
        if (is_x and score > best_value) or (not is_x and score < best_value):
            best_value = score
            best_action = candidate_action

    return best_action
