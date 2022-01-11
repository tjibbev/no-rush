# Visualisering


class Board:
    """The initialisation of the board"""

    def __init__(self, board_grid):
        board_grid = board_grid


def visualize(board_input):
    """Load the Rush Hour board from the file."""

    board_grid = []

    with open(board_input) as f:
        for line in f:
            board_grid.append(line)

    return Board(board_grid)
