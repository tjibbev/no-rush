# Het input gedeelte, initialisatie programma.

import argparse
import os
import sys


if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Solve Rush Hour.')
    parser.add_argument("board", type=int, help="The board to be solved.")

    # Parse the command line arguments
    args = parser.parse_args()

    board_path = f"gameboards/{args.board}.csv"

    # If the puzzle does not exist, exit
    if not os.path.exists(board_path):
        print(f"puzzle {args.board} does not exist")
        sys.exit(1)