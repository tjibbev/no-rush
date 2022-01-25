# Het input gedeelte, initialisatie programma.

import argparse
import os
import sys
from code.classes.board import Board
from code.algorithms.cl_player import test_game
from code.algorithms.random_algo import random_traffic_control
from code.algorithms.random_algo_long import random_traffic_control_long
from code.algorithms.breadth_first import Breadth
from code.visualisation.visualize_gif import gif_maker
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description='Solve Rush Hour.')
    parser.add_argument("board", help="The board to be solved.")
    parser.add_argument("algorithm", help="The algorithm to be used")
    parser.add_argument("-N", required=False, default=1, help="The number of times to run the algorithm.")
    parser.add_argument("--no-gif", dest="no_gif", action="store_const", const=True, default=False, help="Prevent making GIF (default: False")

    # Parse the command line arguments
    args = parser.parse_args()

    board_path = f"data/gameboards/{args.board}.csv"
    alg = args.algorithm.lower()
    N = int(args.N)
    if args.no_gif:
        def gif_maker(board, move_path):
            pass

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
    print()


    if alg == 'cl':
        # -------------------------------------------------- COMMAND LINE GAME ---------------------------------------------
        # Game using command line
        solution = test_game(B)
        gif_maker(solution[0], solution[1])

    elif alg == 'rl':
        # -------------------------------------------------- RANDOM ALGORITHM  (LONG VERSION) -------------------------------
        sol_list = []

        # Random solution generator
        for i in range(N):
            sol = random_traffic_control_long(B, i)
            sol_list.append(sol)
            best_sol = min(sol_list, key=lambda t: len(t[1]))

            # generate new board
            B = Board(board_path, size)
        
        print(f"Best solution: {len(best_sol[1])}")
        gif_maker(best_sol[0], best_sol[1])

    elif alg == 'r':
    # -------------------------------------------------- RANDOM ALGORITHM  ----------------------------------------------------
        sol_list = []
        # let the best solution temporarily be 100000
        best_sol = 0, '0' * 100000

        # Random solution generator
        for i in range(N):
            sol = random_traffic_control(B, i, best_sol)
            sol_list.append(sol)
            best_sol = min(sol_list, key=lambda t: len(t[1]))

            # generate new board
            B = Board(board_path, size)
        
        print(f"Best solution: {len(best_sol[1])}")
        gif_maker(best_sol[0], best_sol[1])

    elif alg == 'br':
        # --------------------------------------------------- BREADTH FIRST ----------------------------------------------
        # Initialize the board for a breadth-first algorithm
        board = Board(board_path, size)
        breadth_search = Breadth(board)

        # run the algorithm
        solution = breadth_search.run()

        gif_maker(solution[0], solution[1])

    else:
        print("Usage: python main.py board algorithm [N]")
        print("algorithm must be one of 'cl' (command line), 'rl' (random solutions), 'r' (random - cuts off longer solutions), 'br' (breadth first)")
        print("N let's random algorithm run N times & chooses best solution")
