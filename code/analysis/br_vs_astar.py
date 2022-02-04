"""
Runs breadth_first.py for TOTAL_RUN_TIME seconds and creates a text file with the solution lengths
The length of the file tells us how fast the algorithm is: the longer the faster
"""

import subprocess
import time
import os

# total running time max (10h)
TOTAL_RUN_TIME = 18000

# The first three boards
BOARDS = ["Rushhour6x6_1", "Rushhour6x6_2", "Rushhour6x6_3"]

os.chdir("../..")
f = open("data/br_vs_a.txt", "w")

for board_path in BOARDS:
    f.write(f"{board_path}, br:")
    start = time.time()
    subprocess.call(["timeout", f"{TOTAL_RUN_TIME}", "python3", "main.py", board_path, "br", "--no-gif"], stdout=f)
    stop = time.time()
    f.write(f"time: {stop - start}")

    print("completed br algorithm")
    f.write("----------------------------")

    f.write(f"{board_path}, a:")
    start = time.time()
    subprocess.call(["timeout", f"{TOTAL_RUN_TIME}", "python3", "main.py", board_path, "a",
                    "--no-gif", "--use-random"], stdout=f)
    stop = time.time()
    f.write(f"time: {stop - start}")

    print("completed a* algorithm")
    f.write("----------------------------")

f.close()
