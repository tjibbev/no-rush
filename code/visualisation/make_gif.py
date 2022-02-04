"""
Make a GIF from existing csv file.
Choose csv file and board path (see line 30) before running.
Run from main directory using python3 code/visualisation/make_gif.py
"""

import sys
from pathlib import Path

if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[3]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:  # Already removed
        pass

    __package__ = 'no_rush.code.visualisation'

    from ..visualisation.visualize_gif import gif_maker
    from ..classes.board import Board
    import csv

    # Choose the input files
    # WARNING: csv_file must contain solution of board given by board_path, size must also match
    csv_file = 'data/solutions/optimal_solution_1.csv'
    board_path = 'data/gameboards/Rushhour6x6_1.csv'
    size = 6

    board = Board(board_path, size)

    move_path = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            move_path.append({'car': row['car'], 'move': int(row['move'])})

    # Advance board to solvced state
    for turn in move_path:
        board.move_car(turn['car'], turn['move'])

    # Create gif
    gif_maker(board, move_path)
