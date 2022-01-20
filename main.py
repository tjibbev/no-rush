# Het input gedeelte, initialisatie programma.

import argparse
import os
import sys
from code.classes.board import Board
from code.algorithms.cl_player import test_game
from code.algorithms.random_algo import random_traffic_control
from code.algorithms.random_algo_long import random_traffic_control_long
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Solve Rush Hour.')
    parser.add_argument("board", help="The board to be solved.")
    parser.add_argument("N", help="The number of times to run the algorithm.")

    # Parse the command line arguments
    args = parser.parse_args()

    board_path = f"data/gameboards/{args.board}.csv"
    N = int(args.N)

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

    sol_list = []
    # let the best solution temporarily be 1500
    best_sol = 1500

    # Random solution generator
    for i in range(N):
        sol = random_traffic_control_long(B, i, best_sol)
        sol_list.append(sol)
        print(sol_list)
        best_sol = int(min(sol_list))
        print(best_sol)

        # generate new board
        B = Board(board_path, size)
