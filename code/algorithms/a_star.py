from ..classes.board import Board
import copy
import heapq

def heuristiek(bord):
    reds_coords = bord._cars['X']._coord
    lane = bord._board_grid[reds_coords[0] - 1]

    count = 1
    for c in lane[reds_coords[1] + 1:]:
        if c != ' ':
            count += 1
        
    return count


class heap_prepare:
    def __init__(self, state) -> None:
        self.state = state
        self.heap_score = len(state[0]) + heuristiek(state[1])

    def __lt__(self, other):
        if self.heap_score == other.heap_score:
            if len(self.state[0]) == len(other.state[0]):
                return id(self) < id(other)
            
            return len(self.state[0]) < len(other.state[0])
        
        return self.heap_score < other.heap_score

    def __getitem__(self, __name: int):
        return [self.heap_score, self.state][__name]


class Astar:
    def __init__(self, board) -> None:
        self.starting_board = copy.deepcopy(board)
        self.size = board._size
        self.archive = {}
        self.winning_board = (board, [])


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
        selected = heapq.heappop(heap)

        if selected[1][1].game_won():
            self.winning_board = selected[1]
            return False

        self.archive[selected[1][1].convert_to_string()] = selected[1][0]

        self.expand(heap, selected)

        return True


    def expand(self, heap,  heapstate):
        state = heapstate[1]
        children = []

        for (car, move) in self.get_possibilities(state):
            child = copy.deepcopy(state)
            child[1].move_car(car, move)
            child[0].append({'car': car, 'move': move})

            string = child[1].convert_to_string()

            if not(string in self.archive):
                heapq.heappush(heap, heap_prepare(child))


    def run(self):
        heap = [heap_prepare(([], self.starting_board))]
        heapq.heapify(heap)

        while self.select(heap):
            pass

        self.winning_board[1].after_win(self.winning_board[0], "optimal")

        return self.winning_board
        