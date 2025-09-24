from typing import Dict, Tuple, List





class HexagonalFillomino:
    def __init__(self, board: Dict[Tuple[int, int], int]):
        self.board = board
        self.solutions = []
        self.visited = []
        self.results = []
        # Hexagonal neighbors: six directions
        self.directions = [
            (1, -1), (1, 0),
            (0, -1), (0, 1),
            (-1, 0), (-1, 1)
        ]

    def find_solves(self):
        print()

    def f(self, coords: Tuple[int, int], visited: List[Tuple[int, int]], board: Dict[Tuple[int, int], int]):
        if board[coords] != 0:
            visited.append(coords)
        if self.size_of_region(coords,board) < board[coords]:
            neighbours = self.find_neighbours(coords, board)
            for neighbour in neighbours:
                if (board[neighbour] != 0 or board[neighbour] != board[coords]) or neighbour in visited:
                    continue
                board_copy = board.copy()
                board_copy[neighbour] = board[coords]
                self.f(neighbour, visited.copy(), board_copy)
        if self.size_of_region(coords,board) == board[coords]:
            if self.board_is_full(board):
                self.results.append(board.copy())
                return
            neighbour = self.find_not_visited_valuable(board, visited)
            if neighbour == None:
                self.fill_empty_cells(board)
                return
            self.f(neighbour, visited, board.copy())

        if board[coords] == 0:
            for neighbour in neighbours:
                if neighbour in visited: continue
                self.f(neighbour, visited, board.copy())

        #if size_of_region(coords,board) > board[coords]:
        #    return

    def size_of_region(coords: Tuple[int, int], board: Dict[Tuple[int, int], int]) -> int:
        pass

    def find_neighbours(coords: Tuple[int, int], board: Dict[Tuple[int, int], int]) -> List[Tuple[int, int]]:
        pass

    def board_is_full(board: Dict[Tuple[int, int], int]) -> bool:
        for cell in board.values():
            if cell == 0:
                return False
        return True

    def fill_empty_cells(board: Dict[Tuple[int, int], int]):
        pass

    def find_not_visited_valuable(board: Dict[Tuple[int, int], int], visited: List[Tuple[int, int]]) -> Tuple[int, int]:
        for cell in board.keys():
            if cell not in visited:
                return cell
