from rush_model import RushModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import seaborn as sns
import argparse
import os
import sys
from code.classes.board import Board


list_of_colors = sns.color_palette(n_colors = 60)


def letter_to_color(letter):
    if len(letter) == 2:
        number = 26 + ord(letter[1]) - 65
    else:
        number = ord(letter) - 65
    
    return list_of_colors[number]


def agent_portrayal(agent):
    colorset = letter_to_color(agent._letter)
    r, g, b = int(colorset[0] * 255), int(colorset[1] * 255), int(colorset[2] * 255)
    color = "#%02x%02x%02x" % (r, g, b)

    portrayal = {"Shape": "circle",
                "Color": color,
                "Filled": "true",
                "Layer": 0,
                "r": 1}

    return portrayal


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
    # B = Rush(board_path, size)

    grid = CanvasGrid(agent_portrayal, size, size, 500, 500)

    server = ModularServer(RushModel,
                        [grid],
                        "Rush Model",
                        {"board_path": board_path, "size": size})

    server.port = 8521 # The default

    server.launch()

