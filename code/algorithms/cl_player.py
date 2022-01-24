from code.classes.board import Board
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio
import glob

def test_game(board):
    """Simple test game that moves cars on input"""

    # Creat list for the movement path
    move_path = []
    image = []
    counter = 1

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
                
                    row_list = []
                    for position in row:
                        if position in board._color:
                            position = board.color()[position]
                        else:
                            position = (248,248,255)
                        row_list.append(position)
                    image.append(row_list)
                print()

                image_maker=np.array(image)
                plt.imshow(image_maker)
                plt.savefig(f'./test/test{counter}.png')
                plt.show()
                counter += 1
                image = []
                move_path.append({'car': carname, 'move': move})
        except IndexError:
            print("Usage: X int")
            print("Make sure the car's initial and the movement integer are seperated by a space!")
        except ValueError:
            print("Usage: X int")
            print("Make sure the car's initial and the movement integer are seperated by a space!")

    with imageio.get_writer('./test/mygif.gif', mode='I', fps = 1) as writer:
        pngs = glob.glob("./test/*.png")
        # print(pngs)
        for filename in pngs:
            image = imageio.imread(filename)
            writer.append_data(image)
            os.remove(filename)

    board.after_win(move_path, "cl")