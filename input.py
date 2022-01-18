# Het input gedeelte, initialisatie programma.

import argparse
import os
import sys
from board import Board
from cl_player import test_game
from algorithms import random_traffic_control
import matplotlib.pyplot as plt
import numpy as np

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

    # Figure out board size
    size = int(args.board[8])
    if size == 1:
        size = 12

    # Load the Rush Hour board
    B = Board(board_path, size)

    image = []

    # Present the Rush Hour board to the user
    print()
    for row in B.visualize():
        print(row)
        row_list = []
        for position in row:
            if position in B._color:
                position = B.color()[position]
            else:
                position = (248,248,255)
            row_list.append(position)
        image.append(row_list)
    print()

    board=np.array(image)
    plt.imshow(board)
    plt.savefig('test.png')
    plt.show()


    # Game using command line
    # test_game(B)

    # Random solution generator
    random_traffic_control(B)
