"""
Runs efficient_search.py for different filter values and creates a text file with the solution lengths
The length of the file tells us how fast the algorithm is: the longer the faster
"""

import subprocess
import time
import gc


# total running time for each filter value
TOTAL_RUN_TIME = 1800
# the maximum time available per run
RUN_TIME = 1801
# chosen board
BOARD = "Rushhour6x6_1"

# list of lengths of the solution length files per filter
lengths_list = []

for filter in range(0, 100, 10):
    start = time.time()
    n_runs = 0
    f = open(f"results_efficient_{filter}.txt", "a")

    while time.time() - start < TOTAL_RUN_TIME:
        time_left = RUN_TIME - time.time() + start
        print(f"run: {n_runs}")

        subprocess.call(["timeout", f"{time_left}", "python3", "main.py", f"{BOARD}", "e",
                        "--no-gif", f"-F {filter}"], stdout=f)

        gc.collect()

        n_runs += 1

    f.close()

    # determine the length of the file
    fr = open(f"results_efficient_{filter}.txt", "r")
    length = len(fr.readlines())
    fr.close()

    # append to list and print
    lengths_list.append(length)
    print(f"number of solutions: {length}")
    print("")

# determine the best filter value,
# the index of a value times 10 gives you the filter value
max_value = max(lengths_list)
index = lengths_list.index(max_value)
filter_value = int(index) * 10

# print result
print(f"The best filter value is: {filter_value}")
