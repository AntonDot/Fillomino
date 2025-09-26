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
results_str = []

for result in results:
    result_str = str(result)
    if result_str not in results_str:
        results_str.append(result_str)
        draw_simple_hex_board(result)
        print()
print(len(results_str))
for res in results_str:
    print("\"" + res + "\"")
print("+_+")

draw_simple_hex_board(board)


