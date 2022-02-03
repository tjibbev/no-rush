""" Runs random_algo.py and creates a text file with the solution lengths"""
""" The length of the file tells us how fast the algorithm is: the longer the faster """

import subprocess
import time
import csv
import os

# total running time for each filter value
TOTAL_RUN_TIME = 60
# the maximum time available per run 
RUN_TIME = 30
# chosen board
BOARD = "Rushhour4x4_0"

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
fr = open(f"results_random.txt", "r")
length = len(fr.readlines())

rows = []
reader = csv.reader(fr, delimiter=" ")
for row in reader:
    rows.append(row)
fr.close()
best_sol = min(rows)

# print result
print(f"number of solutions: {length}")
print(f"best solution length:{best_sol}")