from time import process_time
import copy
import matplotlib.pyplot as plt
from code.algorithms.random_algo_long import random_traffic_control_long
from code.classes.board import Board

lengths = []
times = []
og_bord = Board('data/gameboards/Rushhour6x6_1.csv', 6)
N = 150

for i in range(N):
    bord = copy.deepcopy(og_bord)

    start = process_time()
    solution = random_traffic_control_long(bord, i)
    stop = process_time()

    elapsed = stop - start
    length = len(solution[1])
    
    lengths.append(length)
    times.append(elapsed)


plt.scatter(lengths, times)
plt.savefig('presentation/randoms1.png')
plt.show()