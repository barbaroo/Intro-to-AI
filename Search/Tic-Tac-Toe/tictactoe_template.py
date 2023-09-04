"""
Tic Tac Toe Player
"""

import copy

"""
copy is imported to clone the board, which ensures actions taken don't modify the original board.
"""


"""
EMPTY represents an empty spot on the board.
"""

X = "X"
O = "O"
EMPTY = None



def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Hint: Count all the empty cells in the board to determine the player.
    empty_cells = sum(row.count(EMPTY) for row in board)
    # Use a conditional expression to determine the player.
    return ___ if empty_cells % 2 == 0 else ___


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Hint: Go through every cell in the board.
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if ___:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Hint: Use the action's indices to update the board after creating a copy.
    new_board = copy.deepcopy(board)
    new_board[___][___] = ___
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Hint: Check all rows, columns, and both diagonals.
    for row in board:
        if ___ == ___ == ___ and ___ is not EMPTY:
            return ___
    # (Repeat similar logic for columns and diagonals)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Hint: The game ends if someone has won or if there are no empty spaces left.
    return ___ is not None or not any(EMPTY in row for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Hint: Use a series of if...elif...else conditions to check the board's state.
    ___
    ___
    ___


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Hint: Use the max_value and min_value helper functions to get the best move.
    best_move = None
    if player(board) == X:
        max_val = -float("inf")
        for action in actions(board):
            # Use min_value to get the utility of the resulting board.
            value = ___
            # Compare and store the best move.
            ___
    # (Repeat similar logic for player O)
    return best_move


def max_value(board):
    """
    Returns the max value for the maximizing player.
    Remember the recursion needs to stop for certain conditions....
    """
    # Initialize the value and then update based on results of each possible action.
    v = -float("inf")
    for action in actions(board):
        v = max(v, ___(result(board, action)))
    return v


def min_value(board):
    """
    This function calculates the min value for the minimizing player.
    Remember the recursion needs to stop for certain conditions....
    """
    # Similar to max_value but in reverse.
    v = float("inf")
    for action in actions(board):
        v = min(v, ___(result(board, action)))
    return v


# Example usage
if __name__ == "__main__":
    board = initial_state()
    print(minimax(board))
