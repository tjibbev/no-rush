# Het input gedeelte, initialisatie programma.

import argparse
import csv
import os
import sys
from board import Board
from collections import OrderedDict


def test_game(board):
    """Simple test game that moves cars on input"""

    # Creat list for the movement path
    move_path = []

    while not(board.game_won()):
        # Prompt for car input
        command = input("> ").upper()

        # Allows player to exit the game loop
        if command == "QUIT":
            break

        try:
            carname = command.split()[0]
            move = int(command.split()[1])

            if not(board.move_car(carname, move)):
                print("move not possible")
            else:
                print()
                for row in board.visualize():
                    print(row)
                print()
                move_path.append({'car': carname, 'move': move})
        except IndexError:
            print("Usage: X int")
            print("Make sure the car's initial and the movement integer are seperated by a space!")
        except ValueError:
            print("Usage: X int")
            print("Make sure the car's initial and the movement integer are seperated by a space!")


    if board.game_won():
        print()
        print("You completed the puzzle!")
        with open("output.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['car', 'move'])
            writer.writeheader()
            writer.writerows(move_path)


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

    # Present the Rush Hour board to the user
    print()
    for row in B.visualize():
        print(row)
    print()

    test_game(B)
