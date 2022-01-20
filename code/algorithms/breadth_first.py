import copy
from classes.board import Board

class Breadth:
    """
    Class that searches for solutions breadth first
    """

    def __init__(self, board) -> None:
        """ Initializes the starting board """
        self.starting_board = board
        self.size = board._size
        self.state_archive = []


    def get_possibilities(self, state):
        """ Returns possible moves for some board """
        options = []

        for car in state._cars.keys():
            length = state._cars[car]._length
            for move in range(- self.size + length, self.size - length + 1):
                if state.is_valid_move(car, move):
                    options.append((car, move))
        
        return options


    def branching(self, state):
        """ Returns possible new states of board after 1 move """
        children = []
        for (car, move) in self.get_possibilities(state):
            child = copy.deepcopy(state)
            child.move_car(car, move)
            if not(child in self.state_archive):
                children.append(child)
                self.state_archive.append(child)

        return children


    def next_generation(self, generation):
        """ Returns the next generation of board states """
        next_gen = set()
        for state in generation:
            for child in self.branching(state):
                next_gen.add(child)

        return next_gen


    def found_solution(self, current_gen):
        for state in current_gen:
            if state.game_won():
                return True

        return False
    

    def run(self):
        current_gen = [copy.deepcopy(self.starting_board)]

        while not(self.found_solution(current_gen)):
            current_gen = self.next_generation(current_gen)

        # TODO: Add movepath to ech state (make tuple)

