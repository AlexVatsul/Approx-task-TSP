import numpy as np
from python_tsp.exact import solve_tsp_brute_force, solve_tsp_dynamic_programming

distance_matrix = np.array([
    [0,  3, 11,  1, 6],
    [3,  0,  1, 13, 4],
    [11, 1,  0,  8, 7],
    [1, 13,  8,  0, 8],
    [6,  4,  7,  8, 0]
])

path, distance = solve_tsp_brute_force(distance_matrix)
print(path, distance)

from itertools import permutations

N = int(input("Числов вершин в графе"))
top = int(input(f"С какой вершины начинается путешествие? от 0 до {N - 1}"))


distance = [[0 for i in range(N)]for j in range(N)]

# distance = [[int(input(f"Введите расстояние между вершинами {i} и {j}:")) for i in range(N)]for j in range(N)]
distance = [[0,  3, 11,  1, 6],
            [3,  0,  1, 13, 4],
            [11, 1,  0,  8, 7],
            [1, 13,  8,  0, 8],
            [6,  4,  7,  8, 0]]

l = list(permutations(range(0, N)))
itog = [i for i in l if i[0] == top]


itog = [tuple(item + (top,)) for item in itog]
sum_itog = []
for i in range(len(itog)):
    sum = 0
    for j in range(1, N+1):
        sum += distance[itog[i][j-1]][itog[i][j]]
    sum_itog.append(sum)

min_al = min(sum_itog)
print(itog[sum_itog.index(min_al)], min_al)
print(f"Все пути с минимальным весом из вершины {top}")

for i in range(len(sum_itog)):
    if sum_itog[i] == min_al:
        print(itog[i], min_al)