from HexagonalFillomino import HexagonalFillomino
from CUI import *
from sys import setrecursionlimit

setrecursionlimit(1000000)
board = {
    (0, 0): 1,

    (1, 0): 3, (1, -1): 0, (0, -1): 0,
    (-1, 0): 4, (-1, 1): 3, (0, 1): 2,

    (2, 0): 3, (2, -1): 0, (2, -2): 0,
    (1, -2): 0, (0, -2): 0, (-1, -1): 4,
    (-2, 0): 4, (-2, 1): 4, (-2, 2): 3,
    (-1, 2): 3, (0, 2): 2, (1, 1): 3
}

solver = HexagonalFillomino()
results = solver.find_solves(board)
uni_results = []
for result in results:
    if result not in uni_results:
        uni_results.append(result)


draw_simple_hex_board(board)
print("-----------------------------------------------------")

for result in uni_results:
    draw_simple_hex_board(result)
    print()





