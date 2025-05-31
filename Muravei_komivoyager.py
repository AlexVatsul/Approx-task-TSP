import random

Max_iter = 200
alpha = 1
beta = 1
Q = 1.0
pher = 0.2
N = 5  # число вершин и число муравьев
t = 0
ro = 0.4  # коэффициент испарения

dist = [[0,  3, 11,  1, 6],
            [3,  0,  1, 13, 4],
            [11, 1,  0,  8, 7],
            [1, 13,  8,  0, 8],
            [6,  4,  7,  8, 0]]

tau = [[pher for i in range(N)] for j in range(N)]


def random_num(random_number, itog):
    sum_p = 0
    j = 0
    for i in itog:
        sum_p += i
        if random_number > sum_p:
            j += 1
        else:
            break
    return j

# данная функция на вход получает вершину, а на выход выдает вершину, у которой наивысшая вреоятность перехода
def probability(node, xk):
    sum = 0
    j = 0
    lst_j = []
    itog = []

    for i in dist[node]:
        if i == 0:
            lst_j.append(0)
            j += 1
            continue
        else:
            b = ((1.0 / i) ** alpha) * (tau[node][j] ** beta)
            lst_j.append(b)
            sum += b
            j += 1

    for i in lst_j:
        itog.append(i / sum)

    random_number = random.random()
    index = random_num(random_number, itog)
    while index in xk:
        random_number = random.random()
        index = random_num(random_number, itog)

    return index

while t < Max_iter:
    xk = [[] for j in range(N)]
    for i in range(N):
        xk[i].append(i)
        while len(xk[i]) != N:
            z = probability(xk[i][-1], xk[i])
            xk[i].append(z)
        xk[i].append(i)

    total_distances = []
    for path in xk:
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += dist[path[i]][path[i + 1]]
        total_distances.append(total_distance)

    for i in range(N):
        for j in range(N):
            tau[i][j] = tau[i][j] * (1.0 - ro)

    for i in range(N):
        for j in range(N):
            tau[xk[i][j]][xk[i][j + 1]] += Q / total_distances[i]
    t += 1

print(xk)

print(total_distances)