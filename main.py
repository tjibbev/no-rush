# Het input gedeelte, initialisatie programma.

import argparse
import os
import sys
from code.classes.board import Board
from code.algorithms.cl_player import test_game
from code.algorithms.random_algo import random_traffic_control
from code.algorithms.random_algo_long import random_traffic_control_long
from code.algorithms.breadth_first import Breadth
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Solve Rush Hour.')
    parser.add_argument("board", help="The board to be solved.")
    parser.add_argument("algorithm", help="The algorithm to be used")
    parser.add_argument("-N", required=False, default=1, help="The number of times to run the algorithm.")

    # Parse the command line arguments
    args = parser.parse_args()

    board_path = f"data/gameboards/{args.board}.csv"
    alg = args.algorithm.lower()
    N = int(args.N)

    # If the board does not exist, exit
    if not os.path.exists(board_path):
        print(f"board {board_path} does not exist")
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
    plt.savefig('./test/test.png')
    plt.show()

    if alg == 'cl':
        # -------------------------------------------------- COMMAND LINE GAME ---------------------------------------------
        # Game using command line
        test_game(B)

    elif alg == 'rl':
        # -------------------------------------------------- RANDOM ALGORITHM  (LONG VERSION) -------------------------------
        sol_list = []

        # Random solution generator
        for i in range(N):
            sol = random_traffic_control_long(B, i)
            sol_list.append(sol)
            best_sol = int(min(sol_list))

            # generate new board
            B = Board(board_path, size)
        
        print(f"Best solution: {best_sol}")

    elif alg == 'r':
    # -------------------------------------------------- RANDOM ALGORITHM  ----------------------------------------------------
        sol_list = []
        # let the best solution temporarily be 100000
        best_sol = 100000

        # Random solution generator
        for i in range(N):
            sol = random_traffic_control(B, i, best_sol)
            sol_list.append(sol)
            best_sol = int(min(sol_list))

            # generate new board
            B = Board(board_path, size)
        
        print(f"Best solution: {best_sol}")

    elif alg == 'br':
        # --------------------------------------------------- BREADTH FIRST ----------------------------------------------
        # Initialize the board for a breadth-first algorithm
        board = Board(board_path, size)
        breadth_search = Breadth(board)

        # run the algorithm
        breadth_search.run()

    else:
        print("Usage: python main.py board algorithm [N]")
        print("algorithm must be one of 'cl' (command line), 'rl' (random solutions), 'r' (random - cuts off longer solutions), 'br' (breadth first)")
        print("N let's random algorithm run N times & chooses best solution")
