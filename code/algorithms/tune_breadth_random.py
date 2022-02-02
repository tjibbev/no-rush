""" Runs efficient_search.py for different filter values and creates a text file with the solution lengths"""
""" The length of the file tells us how fast the algorithm is: the longer the faster """

import subprocess
import time

# total running time for each filter value
TOTAL_RUN_TIME = 10
# the maximum time available per run 
RUN_TIME = 5
# chosen board
BOARD = "Rushhour4x4_0"

# list of lengths of the solution length files per filter
#lengths_list = []

for when_to_cut in range(800,1000,100):
    for cutback_val in range(5,8,1):
            start = time.time()
            n_runs = 0

            while time.time() - start < TOTAL_RUN_TIME:
                print(f"run: {n_runs}")
                f = open(f"results_efficient_{filter}.txt", "a")
                subprocess.call(["timeout", f"{RUN_TIME}", "python3", "main.py", f"{BOARD}", "rbr", "--no-gif", "-when-to-cut", f"{when_to_cut}", "-cutback-val", f"{cutback_val}"], stdout=f)
                n_runs += 1
            f.close()

            # determine the length of the file
            fr = open(f"results_efficient_{filter}.txt", "r")
            length = len(fr.readlines())
            fr.close()

            # append to list and print 
            #lengths_list.append(length)
            print(f"number of solutions: {length}")
            print("")
        
# determine the best combination of values
#max_value = max(lengths_list)
#index = lengths_list.index(max_value)
#filter_value = int(index) * 10

# print result
#print(f"The best filter value is: {filter_value}")

