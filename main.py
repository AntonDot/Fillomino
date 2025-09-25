from HexagonalFillomino import HexagonalFillomino
from sys import setrecursionlimit

setrecursionlimit(1000000)
board = {(0, 0): 3, (1, 0): 2, (0, 1): 0, (-1, 1): 0, (-1, 0): 0, (0, -1): 0, (1, -1): 0}
solver = HexagonalFillomino()
results = solver.find_solves(board)
print(len(results))
for result in results:
    print(result)
print("+_+")


