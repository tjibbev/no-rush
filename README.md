# Rush Hour
Welcome to the Rush Hour game, designed by the No-Rush team!

## Sumary
Using this program you can play the Rush Hour game on your own device. The goal is to get the red vehicle to the exit as soon as possible.

## Requirements
This codebase is dependend on the following requirements that can be installed as follows:
- Run requirements.txt using `pip3 install -r requirements.txt`

## Working
Run the programm using the preferred command:
`python3 main.py board algoritme N`

- In which board can be any of the boars under data/gameboards, for example: 'Rushhour9x9_4'
- In which algoritme can be 'cl' (command line), 'rl' (random solutions), 'r' (random - cuts off longer solutions), 'br' (breadth first)
- In which N let's random algorithm run N times & chooses best solution, for example: '-N 5'

## Structure
These are the files used in our project, listed as follows:

- /code: all the project's code
    - /code/algorithms: all the used algorithms
    - /code/classes: the several classes used in the project
    - /code/visualisation: contains the visualisation code
- /data: contains the gameboards that can be used
