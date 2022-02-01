import subprocess
import time
import csv


start = time.time()
n_runs = 0

while time.time() - start < 30:
    print(f"run: {n_runs}")
    f = open("results_random.txt", "a")

    subprocess.call(["timeout", "5", "python3", "main.py", "Rushhour6x6_2", "r", "--no-gif"], stdout=f)
    n_runs += 1
f.close()