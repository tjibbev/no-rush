# Visualisering
import csv
from cars import Car

class Board:
    """The initialisation of the board"""

    def __init__(self, board_path, size):
        board_grid_row = []
        for i in range(size):
            board_grid_row.append('_')
        
        self._board_grid = []
        for i in range(size):
            self._board_grid.append(board_grid_row)

        self._cars = {}

        with open(board_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                self._cars[row['car']] = Car(row['car'], row['orientation'], row['col'], row['row'], row['length'])


    def visualize(self):
        """Load the Rush Hour board from the file."""

        for car in self._cars:
            auto = self._cars[car]
            auto_coords = []

            x, y = auto._coord
            if auto._orientation == 'H':
                for i in range(auto._length):
                    self._board_grid[x+1][y+1+i] = auto._id
            elif auto._orientation == 'V':
                for i in range(auto._length):
                    self._board_grid[x+1+i][y+1] = auto._id

        return self._board_grid
            
