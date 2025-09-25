from HexagonalFillomino import HexagonalFillomino
from sys import setrecursionlimit

setrecursionlimit(1000000)
board = {(0, 0): 3, (1, 0): 2, (0, 1): 0, (-1, 1): 0, (-1, 0): 0, (0, -1): 0, (1, -1): 0}
solver = HexagonalFillomino()
results = solver.find_solves(board)
results_str = []

for result in results:
    result_str = str(result)
    if result_str not in results_str:
        results_str.append(result_str)
print(len(results_str))
for res in results_str:
    print(res)
print("+_+")


