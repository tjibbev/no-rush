# Het input gedeelte, initialisatie programma.

import argparse
import os
import sys
from board import Board, visualize


if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Solve Rush Hour.')
    parser.add_argument("board", help="The board to be solved.")

    # Parse the command line arguments
    args = parser.parse_args()

    board_path = f"gameboards/{args.board}.csv"

    # If the board does not exist, exit
    if not os.path.exists(board_path):
        print(f"board {args.board} does not exist")
        sys.exit(1)

    # Load the Rush Hour board
    board_visualised = visualize(board_path)

    # Present the Rush Hour board to the user
    print(board_visualised)
    print()