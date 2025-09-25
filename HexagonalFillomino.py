from typing import Dict, Tuple, List
from functools import lru_cache
from sys import setrecursionlimit


class HexagonalFillomino:
    def __init__(self):
        self.solutions = []
        self.results = []
        setrecursionlimit(1000000)
        # Hexagonal neighbors: six directions
        self.directions = [
            (1, -1), (1, 0),
            (0, -1), (0, 1),
            (-1, 0), (-1, 1)
        ]

    #@lru_cache(None)
    def find_solves(self, board: Dict[Tuple[int, int], int]):
        visited = []
        start_pos = self.find_not_visited_valuable(board, visited)
        self.f(start_pos, visited, board)
        return self.results

    #@lru_cache(None)
    def f(self, coords: Tuple[int, int], visited: List[Tuple[int, int]], board: Dict[Tuple[int, int], int]):
        if board[coords] != 0:
            visited.append(coords)
        if self.size_of_region(coords, board) < board[coords]:
            neighbours = self.find_neighbours(coords, board)
            for neighbour in neighbours:
                if (board[neighbour] != 0 and board[neighbour] != board[coords]) or neighbour in visited:
                    continue
                board_copy = board.copy()
                board_copy[neighbour] = board[coords]
                self.f(neighbour, visited.copy(), board_copy)
        if self.size_of_region(coords, board) == board[coords]:
            if self.board_is_full(board):
                self.results.append(board.copy())
                return
            neighbour = self.find_not_visited_valuable(board, visited)
            if neighbour is None:
                self.fill_empty_cells(visited.copy(), board.copy())
                return
            self.f(neighbour, visited.copy(), board.copy())

        if board[coords] == 0: #ток если поле изначально из нулей
            self.fill_empty_cells(visited.copy(), board.copy())

        # if size_of_region(coords,board) > board[coords]:
        #    return

    #@lru_cache(None)
    def size_of_region(self, coords: Tuple[int, int], board: Dict[Tuple[int, int], int]) -> int:
        visited: List[Tuple[int, int]] = [coords]
        neighbours = self.find_neighbours(coords, board)
        for neighbour in neighbours:
            if neighbour not in visited:
                if board[neighbour] == board[coords]:
                    self.recursive_find_size(neighbour, board, visited)
        return len(visited)

    #@lru_cache(None)
    def recursive_find_size(self, coords: Tuple[int, int], board: Dict[Tuple[int, int], int],
                            visited: List[Tuple[int, int]]):
        neighbours = self.find_neighbours(coords, board)
        for neighbour in neighbours:
            if neighbour not in visited:
                if board[neighbour] == board[coords]:
                    self.recursive_find_size(neighbour, board, visited)

    #@lru_cache(None)
    def find_neighbours(self, coords: Tuple[int, int], board: Dict[Tuple[int, int], int]) -> List[Tuple[int, int]]:
        neighbours: list[tuple[int, int]] = []
        for direction in self.directions:
            if (coords[0] + direction[0], coords[1] + direction[1]) in board.keys():
                neighbours.append((coords[0] + direction[0], coords[1] + direction[1]))
        return neighbours

    @staticmethod
    def board_is_full(board: Dict[Tuple[int, int], int]) -> bool:
        for cell in board.values():
            if cell == 0:
                return False
        return True

    #@lru_cache(None)
    def fill_empty_cells(self, visited: List[Tuple[int, int]], board: Dict[Tuple[int, int], int]):
        neighbour: Tuple[int, int] = self.find_empty_cell(board)
        for n in range(self.size_of_region(neighbour, board), 0, -1):
            board_copy = board.copy()
            board_copy[neighbour] = n
            visited_copy = visited.copy()
            visited_copy.append(neighbour)
            self.f(neighbour, visited_copy, board_copy)

    @staticmethod
    def find_empty_cell(board: Dict[Tuple[int, int], int]):
        for cell in board.keys():
            if board[cell] == 0:
                return cell

    @staticmethod
    def find_not_visited_valuable(board: Dict[Tuple[int, int], int], visited: List[Tuple[int, int]]) -> Tuple[int, int]:
        for cell in board.keys():
            if cell not in visited:
                return cell
