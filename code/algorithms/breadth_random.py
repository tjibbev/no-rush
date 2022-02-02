from numpy import average
from code.classes.board import Board
import copy
from .breadth_first import Breadth
from .random_algo_long import random_move

class Breandom(Breadth):
    """ Trying to build a more efficient version of breadth-first search """
    def __init__(self, board, when_to_cut, cutback_val):
        """ Initializes the starting board """
        self.starting_board = board
        self.size = board._size
        self.state_archive = []
        self.breadth_start = []
        self.when_to_cut = when_to_cut
        self.cutback_val = cutback_val

    def custom_filter(self, list_of_states):
        scores = []
        for state in list_of_states:
            board = copy.deepcopy(state[0])
            random_lengths = []

            for i in range(2):
                movecount = 0
                while not(board.game_won()):
                    car, move = random_move(board)
                    movecount += 1
                
                random_lengths.append(movecount)
            
            state_score = average(random_lengths)
            scores.append((state, state_score))

        scores.sort(key=lambda item: item[1])

        del scores[self.cutback_val:]

        next_gen = [item[0] for item in scores]

        return next_gen


    def run(self):
        current_gen = [(copy.deepcopy(self.starting_board), [])]

        while not(self.found_solution(current_gen)):
            if len(current_gen) < self.when_to_cut:
                current_gen = self.next_generation(current_gen)
            else:
                current_gen = self.custom_filter(current_gen)

        
        solution = self.found_solution(current_gen)
        solution[0].after_win(solution[1], "semi-optimal")
        
        return solution
