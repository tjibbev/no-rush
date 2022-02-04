"""
Runs random_algo.py and creates a text file with the solution lengths
The length of the file tells us how fast the algorithm is: the longer the faster
"""

import subprocess
import time
import csv
import os

# total running time for each filter value
TOTAL_RUN_TIME = 60
# the maximum time available per run
RUN_TIME = 30
# chosen board
BOARD = "Rushhour6x6_1"

start = time.time()
n_runs = 0
os.chdir("../..")

while time.time() - start < TOTAL_RUN_TIME:
    print(f"run: {n_runs}")
    f = open("results_random.txt", "a")

    subprocess.call(["timeout", f"{RUN_TIME}", "python3", "main.py", f"{BOARD}", "r", "--no-gif"], stdout=f)
    n_runs += 1
f.close()

# determine the length of the file
fr = open("results_random.txt", "r")
length = len(fr.readlines())

rows = []
with open('results_random.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        print(row)
        rows.append(row[0])
fr.close()
best_sol = min(rows)

# print result
print(f"number of solutions: {length}")
print(f"best solution length: {best_sol}")
