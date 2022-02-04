import matplotlib.pyplot as plt
import numpy as np
import os
import imageio
import copy

def gif_maker(board, move_path):

    movepath = copy.deepcopy(move_path)
    movepath.append({'car': 'X', 'move': 0})

    B = board
    counter = len(movepath)


    while movepath != []:
        movement = movepath.pop()

        image = []

        B.move_car(movement['car'],- int(movement['move']))
        

        for row in B.visualize():
            row_list = []
            for position in row:
                if position in B._color:
                    position = B._color[position]
                else:
                    position = (248,248,255)
                row_list.append(position)
            image.append(row_list)
        counter -= 1

        image_maker=np.array(image)
        plt.imshow(image_maker)
        plt.savefig(f'./code/visualisation/png_output/run{counter}.png')
        plt.show()

    end_gif(len(move_path))


def end_gif(frames):
    with imageio.get_writer('./output-gif.gif', mode='I', fps = 1) as writer:
        for frame in range(frames + 1):
            image = imageio.imread(f"./code/visualisation/png_output/run{frame}.png")
            writer.append_data(image)
            os.remove(f"./code/visualisation/png_output/run{frame}.png")
