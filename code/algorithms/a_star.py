from ..classes.board import Board
import copy
import heapq

def obstacle_count(bord):
    """" This heuristic gives a score to a board based on the amount of cars which are blocking the red cars exit. """
    reds_coords = bord._cars['X']._coord
    lane = bord._board_grid[reds_coords[0] - 1]

    count = 1
    for c in lane[reds_coords[1] + 1:]:
        if c != ' ':
            count += 1
        
    return count


def difference(bord, solution):
    """" 
    To be used when a solution of the board is given.
    This heuristic scores a board based on its difference compared to a solved board.
    """

    difference = 0

    for carname in bord._cars:
        car = bord._cars[carname]
        difference += abs(car._coord[0] - solution._cars[carname]._coord[0]) + abs(car._coord[1] - solution._cars[carname]._coord[1])
    
    return difference


class heap_prepare:
    """" 
    This class prepares a state (a movepath + a board) to put in in the heapq.
    There are two possible heuristics one can use.
    The heuristic is chosen through the Astar class
    """

    def __init__(self, state, solution=None) -> None:
        """ Initialise the heap_prepare class """
        self.state = state

        # Use the second heuristic if a solution is given
        if solution:
            self.heap_score = len(state[0]) + difference(state[1], solution)
        # Otherwise use the first heuristic
        else:
            self.heap_score = len(state[0]) + obstacle_count(state[1])

    def __lt__(self, other):
        if self.heap_score == other.heap_score:
            if len(self.state[0]) == len(other.state[0]):
                return id(self) < id(other)
            
            return len(self.state[0]) < len(other.state[0])
        
        return self.heap_score < other.heap_score

    def __getitem__(self, __name: int):
        return [self.heap_score, self.state][__name]


class Astar:
    """ 
    The A* algorithm can be regarded as a smartly expanding oil stain. 
    Makes the oil stain smart by using a heuristic
    """
    def __init__(self, board, solution=None) -> None:
        """ Initialise the A* algorithm """
        self.starting_board = copy.deepcopy(board)
        self.size = board._size
        self.archive = {}
        self.winning_board = (board, [])
        self.solution = solution


    def get_possibilities(self, state):
        """ Returns possible moves for some board """
        options = []

        for car in state[1]._cars.keys():
            length = state[1]._cars[car]._length
            for move in range(- self.size + length, self.size - length + 1):
                if state[1].is_valid_move(car, move):
                    options.append((car, move))
        
        return options


    def select(self, heap):
        """ Selects direction for oil stane to expand """
        selected = heapq.heappop(heap)

        if selected[1][1].game_won():
            self.winning_board = selected[1]
            return False

        self.archive[selected[1][1].convert_to_string()] = selected[1][0]

        self.expand(heap, selected)

        return True


    def expand(self, heap,  heapstate):
        """Expands the oil stane """
        state = heapstate[1]

        for (car, move) in self.get_possibilities(state):
            child = copy.deepcopy(state)
            child[1].move_car(car, move)
            child[0].append({'car': car, 'move': move})

            string = child[1].convert_to_string()

            if not(string in self.archive):
                heapq.heappush(heap, heap_prepare(child, self.solution))


    def run(self):
        """ Runs the A* algorithm """
        heap = [heap_prepare(([], self.starting_board), self.solution)]
        heapq.heapify(heap)

        while self.select(heap):
            pass

        self.winning_board[1].after_win(self.winning_board[0], "optimal")

        return self.winning_board
        