from code.classes.board import Board
import copy
from code.algorithms.random_algo import possibilities
from .breadth_first import Breadth


def heuristiek(board):
    """ Returns a number that indicates how many moves are possible """
    valid_moves = possibilities(board)

    total_valids = 0
    for moves in valid_moves.values():
        total_valids += len(moves)

    return total_valids


class Efficient(Breadth):
    """ Trying to build a more efficient version of breadth-first search """
    def __init__(self, board):
        """ Initializes the starting board """
        self.starting_board = board
        self.size = board._size
        self.state_archive = [set(), set(), set(board.convert_to_string())]
        self._generations = []
        self._filter = 50
        self._backtrack_number = 2


    def back_track(self):
        for i in range(self._backtrack_number):
            prev_gen = self._generations.pop()
        
        self._backtrack_number = self._backtrack_number * 2
        self._filter = self._filter / 2

        return prev_gen

    def branching(self, state):
        """ Returns possible new states of board after 1 move """
        children = []

        for (car, move) in self.get_possibilities(state):
            child = copy.deepcopy(state)
            child[0].move_car(car, move)
            child[1].append({'car': car, 'move': move})

            string = child[0].convert_to_string()

            if all(not(string in self.state_archive[i]) for i in [0, 1, 2]):
                children.append(child)

        children.sort(key=lambda t: heuristiek(t[0]))

        number_of_drops = int(len(children) * self._filter / 100)
        del children[:number_of_drops]

        self.state_archive.pop()
        self.state_archive.append(set([bord[0].convert_to_string() for bord in children]))

        return children


    def run(self):
        current_gen = [(copy.deepcopy(self.starting_board), [])]

        while not(self.found_solution(current_gen)):
            self._generations.append(current_gen)
            current_gen = self.next_generation(current_gen)
            if current_gen == []:
                print("backtracking...")
                current_gen = self.back_track()
        
        solution = self.found_solution(current_gen)
        solution[0].after_win(solution[1], "semi-optimal")
        
        return solution
