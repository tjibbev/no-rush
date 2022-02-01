""" Runs breadth_first.py for TOTAL_RUN_TIME seconds and creates a text file with the solutions"""
""" The length of the file tells us how fast the algorithm is: the longer the faster """

import subprocess
import time
import csv

# total running time for each filter value
TOTAL_RUN_TIME = 10
# the maximum time available per run 
RUN_TIME = 5
# chosen board
BOARD = "Rushhour4x4_0"

start = time.time()
n_runs = 0

while time.time() - start < TOTAL_RUN_TIME:
    print(f"run: {n_runs}")
    f = open("results_random.txt", "a")

    subprocess.call(["timeout", f"{RUN_TIME}", "python3", "main.py", f"{BOARD}", "br", "--no-gif"], stdout=f)
    n_runs += 1
f.close()

# determine the length of the file
fr = open(f"results_random.txt", "r")
length = len(fr.readlines())
f.close()
print(f"number of runs: {length}")