from tasks import *
from blindMethods import *


task1 = FillJugsTask([0, 0], [[2, 0], [0, 2]])
IDS(task1)
# BFS(task1, modification=True)
#
# task2 = FillJugsTask([0, 0], [[2, 0], [0, 2]])
# DFS(task2, modification=True)

# task1 = Task([0, 0], _2JugsTask_operators(), [[2, 0], [0, 2]])
# path, b = BFS(task1)
# path.reverse()
# print("Basic BFS results:\npath:", path, "\nExpands:", b, "\n")
# task1.expands = 0
#
# path, b = BFS(task1, modification=True)
# path.reverse()
# print("Modified BFS results:\npath:", path, "\nExpands:", b, "\n")
# task1.expands = 0
#
# path, b = BFS(task1, modification=True, CLOSED=[])
# path.reverse()
# print("BFS with CLOSED results:\npath:", path, "\nExpands:", b, "\n")
# task1.expands = 0
#
# print("Modified DFS:")
# task2 = Task([0, 0], _2JugsTask_operators(), [[2, 0], [0, 2]])
# try:
#     path, b = DFS(task2, modification=True)
#     print("Goal:", path, "\nExpands:", b)
#     task2.expands = 0
# except RecursionError:
#     print("Failed!")

# try:
#     path, b = DFS(task2, modification=True)
#     path.reverse()
#     print("Modified DFS:\npath:", path, "\nExpands:", b)
#     task2.expands = 0
# except RecursionError:
#     print("Modified DFS failed!")
