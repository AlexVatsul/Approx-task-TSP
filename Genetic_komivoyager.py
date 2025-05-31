from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import random
import numpy as np


Graph = {
    0: {1: 3, 2: 11, 3: 1, 4: 6},
    1: {0: 3, 2: 1, 3: 13, 4: 4},
    2: {0: 11, 1: 1, 3: 8, 4: 7},
    3: {0: 1, 1: 13, 2: 8, 4: 8},
    4: {0: 6, 1: 4, 2: 7, 3: 8}
}

# Константы генетического алгоритма:
POPULATION_SIZE = 100
MAX_GENERATIONS = 200
HALL_OF_FAME_SIZE = 1
P_CROSSOVER = 0.9  # вероятность скрещивания
P_MUTATION = 0.1   # вероятность мутации особи


toolbox = base.Toolbox()

# определить единую цель, минимизируя фитнес-стратегию:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# создаем индивидуальный класс на основе списка целых чисел:
creator.create("Individual", list, fitness=creator.FitnessMin)

# здесь формируются значения вершин. Например, [0, 2, 1, 3] и тд
toolbox.register("randomOrder", random.sample, range(len(Graph)), len(Graph))


# создайте индивидуальный оператор создания, чтобы заполнить экземпляр Individual перетасованными индексами:
toolbox.register("individualCreator", tools.initIterate, creator.Individual, toolbox.randomOrder)

# создайте оператор создания популяции для создания списка особей:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# расчет фитнеса — вычисление общего расстояния списка городов, представленных индексами:
def Distance(individual):
    summa_puti = 0
    for i in range(len(individual)):
        if i == len(individual) - 1:
            summa_puti += Graph[individual[i]][individual[0]]

        else:
            summa_puti += Graph[individual[i]][individual[i + 1]]

    return (summa_puti,)


toolbox.register("evaluate", Distance)

# Генетические операторы:
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=1.0/len(Graph))

# Ход генетического алгоритма
# создаем начальную популяцию (поколение 0):
population = toolbox.populationCreator(n=POPULATION_SIZE)

# подготовьте объект статистики:
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("avg", np.mean)

# определите объект зала славы:
hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

# выполнить поток генетического алгоритма с добавленной функцией hof:
population, logbook = algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=False)

# распечатать лучшую индивидуальную информацию
best = hof.items[0]
print("Лучшее значение индивуума = ", best)
print("Лучшее значение приспособленности = ", best.fitness.values[0])
