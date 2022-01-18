# Visualisering
import csv
#from msilib.schema import SelfReg
from cars import Car
import copy
import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

class CarAgent(Agent):
    def __init__(self, unique_id, model, letter, orientation, column, row, length):
        super().__init__(unique_id, model)
        self._letter = letter 
        self._orientation = orientation
        self._coord = (int(row), int(column))
        self._length = int(length)

    def move(self, move):
        x, y = self._coord
        if self._orientation == 'H':
            self._coord = (x, y + move) 
        else:
            self._coord = (x + move, y)

class RushModel(Model):
    """Board containing multiple (moveable) cars on a grid"""
    def __init__(self, board_path, size):
        """
        Loads vehicles
        Creates empty board grid
        Loads vehicles onto board
        """
        self.grid = SingleGrid(size, size, True)
        self.schedule = RandomActivation(self)
        self.running = True 

        self._size = size
        self._cars = {}
        self._move_path = []
        self._board_grid = []
        self._empty_grid = []

        # open the gameboard file and intialize the CarAgents
        with open(board_path) as file:
            reader = csv.DictReader(file)
            
            id = 0
            for row in reader:
                id += 1
                car = CarAgent(id, self, row['car'], row['orientation'], row['col'], row['row'], row['length'])
                self.schedule.add(car)
                self.grid.place_agent(car, car._coord)
                
                #self._cars[row['car']] = Car(row['car'], row['orientation'], row['col'], row['row'], row['length'])

        # create empty board
        for i in range(size):
            row_list = []
            for i in range(size):
                row_list.append(' ')
            self._empty_grid.append(row_list)
        
        self.load_board()
        

    def load_board(self):
        """Loads all cars to current positions on the board"""
        self._board_grid = copy.deepcopy(self._empty_grid)

        for car in self._cars:
            auto = self._cars[car]

            x, y = auto._coord
            if auto._orientation == 'H':
                for i in range(auto._length):
                    self._board_grid[x-1][y-1+i] = auto._id
            elif auto._orientation == 'V':
                for i in range(auto._length):
                    self._board_grid[x-1+i][y-1] = auto._id


    def visualize(self):
        """Returns the board grid"""
        return self._board_grid
            

    def is_valid_move(self, carname, move):
        """Checks if car can be moved"""
        try:
            car = self._cars[carname]
        except KeyError:
            return False
            
        x, y = car._coord

        try:
            if car._orientation == 'H' and move < 0:
                if all(self._board_grid[x-1][y-1+i] == ' ' for i in range(move, 0)):
                    return True
            elif car._orientation == 'H' and move > 0:
                if y - 1 + move + car._length > len(self._empty_grid):
                    return False
                elif all(self._board_grid[x-1][y-1+i] == ' ' for i in range(car._length, car._length + move)):
                    return True
            elif car._orientation == 'V' and move < 0:
                if all(self._board_grid[x-1+i][y-1] == ' ' for i in range(move, 0)):
                    return True
            elif car._orientation == 'V' and move > 0:
                if x - 1 + move + car._length > len(self._empty_grid):
                    return False
                elif all(self._board_grid[x-1+i][y-1] == ' ' for i in range(car._length, car._length + move)):
                    return True
        except IndexError:
            return False
        
        return False

    
    def move_car(self, carname, move):
        """Move car if possible"""
        if self.is_valid_move(carname, move):
            self._cars[carname].move(move)
            self.load_board()

            return True

        return False

    def game_won(self):
        """Returns true if the red car has cleared traffic"""
        red = self._cars['X']

        if red._coord[1] == len(self._empty_grid) - 1:
            return True
        
        return False

    def after_win(self, movepath):
        """Prints winning status and makes output.csv"""
        if self.game_won():
            print()
            print("You completed the puzzle!")
            with open("output.csv", 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['car', 'move'])
                writer.writeheader()
                writer.writerows(movepath)

    def possibilities(self):
        """Creates & returns dict containing all possible car movements"""
        possibles = {}
        for car in self._cars.keys():
            length = self._cars[car]._length
            car_possibilities = []
            for move in range(- self._size + length, self._size - length + 1):
                if self.is_valid_move(car, move):
                    car_possibilities.append(move)
            
            # Add car only if moveable
            if car_possibilities != []:
                possibles[car] = car_possibilities

        return possibles


    def random_move(self):
        options = self.possibilities()

        car = random.choice(list(options.keys()))
        move = random.choice(options[car])

        self.move_car(car, move)

        return car, move


    def step(self):
        
        if not(self.game_won()):
            car, move = self.random_move()
            self._move_path.append({'car': car, 'move': move})
        else:
            self.after_win(self._move_path)

