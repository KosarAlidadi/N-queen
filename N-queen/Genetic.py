# genetic.py
# حل تقریبی با الگوریتم ژنتیکی

import random

def fitness(state):
    n = len(state)
    score = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] != state[j] and abs(state[i] - state[j]) != abs(i - j):
                score += 1
    return score

def mutate(state, initial):
    n = len(state)
    i = random.randint(0, n - 1)
    if initial[i] == -1:
        state[i] = random.randint(0, n - 1)

def crossover(p1, p2, initial):
    n = len(p1)
    idx = random.randint(0, n - 1)
    child = [p1[i] if i < idx else p2[i] for i in range(n)]
    for i in range(n):
        if initial[i] != -1:
            child[i] = initial[i]
    return child

def solve_genetic(n, initial):
    population = []
    for _ in range(100):
        state = [initial[i] if initial[i] != -1 else random.randint(0, n - 1) for i in range(n)]
        population.append(state)

    for generation in range(1000):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == (n * (n - 1)) // 2:
            return population[0]
        next_gen = population[:10]
        while len(next_gen) < 100:
            p1, p2 = random.sample(population[:50], 2)
            child = crossover(p1, p2, initial)
            mutate(child, initial)
            next_gen.append(child)
        population = next_gen
    return population[0]
