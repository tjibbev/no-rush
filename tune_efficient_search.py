""" Runs efficient_search.py for different filter values and creates a text file with the solutions"""
""" The length of the file tells us how fast the algorithm is: the longer the faster """

import subprocess
import time

# total running time for each filter value
TOTAL_RUN_TIME = 10
# the maximum time available per run 
RUN_TIME = 5
# chosen board
BOARD = "Rushhour4x4_0"

for filter in range(0,100,10):
        start = time.time()
        n_runs = 0

        while time.time() - start < TOTAL_RUN_TIME:
            print(f"run: {n_runs}")
            f = open(f"results_efficient_{filter}.txt", "a")
            subprocess.call(["timeout", f"{RUN_TIME}", "python3", "main.py", f"{BOARD}", "e", "--no-gif"], stdout=f)
            n_runs += 1
        
        f.close()
        fr = open(f"results_efficient_{filter}.txt", "r")
        print("")
        print(f"number of solutions: {len(fr.readlines())}")
        print("")
        f.close()


