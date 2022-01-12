# Visualisering
import csv
from cars import Car

class Board:
    """Board containing multiple (moveable) cars on a grid"""

    def __init__(self, board_path, size):
        """
        Loads vehicles
        Creates empty board grid
        Loads vehicles onto board
        """

        self._cars = {}

        with open(board_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self._cars[row['car']] = Car(row['car'], row['orientation'], row['col'], row['row'], row['length'])
        
        self._board_grid = []
        for i in range(size):
            row_list = []
            for i in range(size):
                row_list.append(' ')
            self._board_grid.append(row_list)
        
        self.load_board()
        

    def load_board(self):
        """Loads all cars to current positions on the board"""
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
        car = self._cars[carname]
        x, y = car._coord

        if car._orientation == 'H' and move < 0:
            if all(self._board_grid[x-1][y-1+i] == ' ' for i in range(move, 0)):
                return True
        elif car._orientation == 'H' and move > 0:
            if all(self._board_grid[x-1][y-1+i] == ' ' for i in range(car._length, car._length + move)):
                return True
        elif car._orientation == 'V' and move < 0:
            if all(self._board_grid[x-1+i][y-1] == ' ' for i in range(move, 0)):
                return True
        elif car._orientation == 'V' and move > 0:
            if all(self._board_grid[x-1+i][y-1] == ' ' for i in range(car._length, car._length + move)):
                return True
        
        return False

    
    def move_car(self, carname, move):
        """Move car if possible"""
        if self.is_valid_move(carname, move):
            self._cars[carname].move(move)
            self.load_board()
