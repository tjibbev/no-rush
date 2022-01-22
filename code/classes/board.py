# Visualisering
import csv
from string import whitespace
from code.classes.cars import Car
import copy

class Board:
    """Board containing multiple (moveable) cars on a grid"""

    def __init__(self, board_path, size):
        """
        Loads vehicles
        Creates empty board grid
        Loads vehicles onto board
        """

        self._size = size
        self._cars = {}
        self._color = {}
        list_of_colors = [(0,255,255),(118,238,198),(0,0,255),(255,97,3),(118,238,0),(139,136,120),(104,34,139),(255,20,147),(255,215,0),(3,3,3),(191,239,255),(255,182,193),(238,238,209),(224,102,255),(227,168,105),(255,222,173),(128,128,0),(205,55,0),(152,251,152),(139,139,0),(245,222,179),(255,255,0),(238,130,238),(0,128,128)]

        # Obtain cars from csv file
        with open(board_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self._cars[row['car']] = Car(row['car'], row['orientation'], row['col'], row['row'], row['length'])
        
        # Assign colors to the vehicles
        for key in self._cars:
            if key == "X":
                self._color[key] = (255,0,0)
            else:
                self._color[key] = list_of_colors.pop()

        self._board_grid = []
        self._empty_grid = []

        # create empty board grid
        for i in range(size):
            row_list = []
            for i in range(size):
                row_list.append(' ')
            self._empty_grid.append(row_list)
        
        # load cars onto board grid
        self.load_board()
        
    # TODO: define __eq__

    def __eq__(self, other):
        if isinstance(other, Board):
            return self._board_grid == other._board_grid
            
        return False

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


    def color(self):
        return self._color
            

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

    def after_win(self, movepath, run_number):
        """Prints winning status, makes an output.csv and returns the solution length"""
        sol_length = None

        if self.game_won():
            print()
            print("You completed the puzzle!")
            with open(f"output_{run_number}.csv", 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['car', 'move'])
                writer.writeheader()
                writer.writerows(movepath)
            sol_length = len(movepath)
            print(f"in {sol_length} steps!")
        
        return sol_length