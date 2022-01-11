# Auto eigenschappen

class Car:

    def __init__(self, id, orientation, column, row, length) -> None:
        self._id = id
        self._orientation = orientation
        self._coord = (int(row), int(column))
        self._length = int(length)

    def move(self, move):
        if self._orientation == 'H':
            self._coord = self._coord + (0, move) 
        else:
            self._coord = self._coord + (move, 0)

    
