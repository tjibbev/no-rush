import matplotlib.pyplot as plt
import numpy as np
import os
import imageio
import glob

def gif_maker(board, movepath):

    B = board
    counter = 1
    print(movepath)
    B._board_grid = B._starting_board
    
    for a in B._board_grid:
        print(a)

    for movement in movepath:

        image = []
        print(movement['car'])
        print(int(movement['move']))
        print(B.move_car(movement['car'],int(movement['move'])))
        B.move_car(movement['car'],int(movement['move']))
        

        for row in B.visualize():
            print(row, "row")
            row_list = []
            for position in row:
                if position in B._color:
                    position = B._color[position]
                else:
                    position = (248,248,255)
                row_list.append(position)
            image.append(row_list)
        counter += 1

        image_maker=np.array(image)
        plt.imshow(image_maker)
        plt.savefig(f'./test/test{counter}.png')
        plt.show()

    end_gif()


def end_gif():
    with imageio.get_writer('./test/mygif.gif', mode='I', fps = 1) as writer:
        pngs = glob.glob("./test/*.png")
        print(pngs)
        for filename in pngs:
            image = imageio.imread(filename)
            writer.append_data(image)
            os.remove(filename)