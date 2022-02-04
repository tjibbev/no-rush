""" Properties of a car on a Rush Hour board"""


class Car:
    """
    A car on a rush hour Board
    Cars can be of length 2 or 3
    """
    def __init__(self, id, orientation, column, row, length) -> None:
        self._id = id
        self._orientation = orientation
        self._coord = (int(row), int(column))
        self._length = int(length)

    def move(self, move):
        """ Move car by changing its coordinates """
        x, y = self._coord
        if self._orientation == 'H':
            self._coord = (x, y + move)
        else:
            self._coord = (x + move, y)
