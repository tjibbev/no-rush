import copy
from ..classes.board import Board

class Breadth:
    """
    Class that searches for solutions breadth first
    """

    def __init__(self, board):
        """ Initializes the starting board """
        self.starting_board = board
        self.size = board._size
        self.state_archive = []


    def get_possibilities(self, state):
        """ Returns possible moves for some board """
        options = []

        for car in state[0]._cars.keys():
            length = state[0]._cars[car]._length
            for move in range(- self.size + length, self.size - length + 1):
                if state[0].is_valid_move(car, move):
                    options.append((car, move))
        
        return options


    def branching(self, state):
        """ Returns possible new states of board after 1 move """
        children = []
        for (car, move) in self.get_possibilities(state):
            child = copy.deepcopy(state)
            child[0].move_car(car, move)
            child[1].append({'car': car, 'move': move})
            if all(state != child[0] for state in self.state_archive):
                children.append(child)
                self.state_archive.append(child[0])

        return children


    def next_generation(self, generation):
        """ Returns the next generation of board states """
        next_gen = []
        for state in generation:
            for child in self.branching(state):
                next_gen.append(child)

        print(f"The next generation contains {len(next_gen)} states!")
        return next_gen


    def found_solution(self, current_gen):
        for state in current_gen:
            if state[0].game_won():
                return state

        return None
    

    def run(self):
        current_gen = [(copy.deepcopy(self.starting_board), [])]

        while not(self.found_solution(current_gen)):
            current_gen = self.next_generation(current_gen)

        solution = self.found_solution(current_gen)
        solution[0].after_win(solution[1], "optimal")
