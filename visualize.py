from rush_model import Rush
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
import argparse
import os
import sys
from board import Board
from cl_player import test_game
from algorithms import random_traffic_control

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
 #   B = Rush(board_path, size)

    def agent_portrayal(agent):
        if agent._letter == 'A':
            portrayal = {"Shape": "circle",
                        "Color": "green",
                        "Filled": "true",
                        "Layer": 0,
                        "r": 0.5}
        
        elif agent._letter == 'B':
            portrayal = {"Shape": "circle",
                        "Color": "red",
                        "Filled": "true",
                        "Layer": 0,
                        "r": 0.5}

        elif agent._letter == 'C':
            portrayal = {"Shape": "circle",
                        "Color": "blue",
                        "Filled": "true",
                        "Layer": 0,
                        "r": 0.5}

        elif agent._letter == 'D':
            portrayal = {"Shape": "circle",
                        "Color": "black",
                        "Filled": "true",
                        "Layer": 0,
                        "r": 0.5}

        return portrayal

    grid = CanvasGrid(agent_portrayal, 100, 100, 500, 500)

    server = ModularServer(Rush,
                        [grid],
                        "Rush Model",
                        {"board_path": board_path, "size": size})

    server.port = 8521 # The default

    server.launch()

