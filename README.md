# Rush Hour
Welcome to the Rush Hour game, designed by the No-Rush team!

## Sumary
Using this program you can play the Rush Hour game on your own device. The goal is to get the red vehicle to the exit as soon as possible. The goal of this project is to implement several algorithms that can solve the puzzles on their own. This is a challenging task as boards will grow in size and so do the possible solutions. This means that it is our task to find the fastest working algorithm, which can be running for hours before a solution is found. With this project we aim to provide the user with those algorithms and enable them to compare the outputs.

## Requirements
This codebase is dependend on the following requirements that can be installed as follows:
- Run requirements.txt using `pip3 install -r requirements.txt`

## Working
Run the programm using the preferred command:
`python3 main.py board algorithm N --no-gif`

- In which board can be any of the boars under data/gameboards, for example: 'Rushhour9x9_4'
- In which algorithm can be 'cl' (command line), 'rl' (random solutions), 'r' (random - cuts off longer solutions), 'br' (breadth first), 'e' (efficient search), 'rbr' (combined Breadth/random) or 'A*' (Astar algorithm).
- (optional) In which N let's random algorithm run N times & chooses best solution, for example: '-N 5'
- - In which ' --no-gif' is highly suggested to add for larger boards. Only leave it out on the small ones.

## Algorithms
In the programm there are several algorithms that can be used as input.
- Random ()
- Random long ()
- Breadth first (In this algorithm the goal is to find the best possible solution to solve the puzzle, instead of the fastest. This means that the result in the same each time the same board is used as input.)
- Efficient search ()
- Combined Breadth/random ()
- A* ()

## Structure
These are the files used in our project, listed as follows:

- /code: all the project's code
    - /code/algorithms: all the used algorithms
    - /code/classes: the several classes used in the project
    - /code/visualisation: contains the visualisation code
- /data: contains the gameboards that can be used
- /presentation: contains several image outputs used in the presentation

## Automatic results
By running the auto script of an algorithm, the algorithm will automatically be run for a certain amount of time and the solution lengths will be saved to a file. The random algorithm will be filtered for the best result. The algorithms can now be compared. Run:
- auto_random_run.py
- auto_breadth_first.py
- auto_a_star.py

By running the the tune script of efficient_search.py, you find out what the best filter value is per board. Run:
- tune_efficient_search.py (TO DO: this is not working yet..)
