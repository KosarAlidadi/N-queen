import random

# تابع برازش (هر چه کمتر بهتر - تعداد برخوردها)
def fitness(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# ایجاد یک کروموزوم تصادفی معتبر (بدون تکرار)
def random_chromosome(n):
    return random.sample(range(n), n)

# انتخاب والدین با احتمال معکوس برخوردها
def select_parents(population, fitnesses):
    # از 1/(1+f) برای تبدیل برخورد کمتر به احتمال بیشتر
    adjusted = [(1 / (1 + f)) for f in fitnesses]
    parents = random.choices(population, weights=adjusted, k=2)
    return parents

# تابع اصلاح برای جلوگیری از تکرار در کروموزوم
def unique_chromosome(child):
    n = len(child)
    seen = set()
    missing = [i for i in range(n) if i not in child]
    for i in range(n):
        if child[i] in seen:
            child[i] = missing.pop()
        seen.add(child[i])
    return child

# Crossover چند نقطه‌ای ساده با اصلاح تکراری‌ها
def crossover(parent1, parent2):
    n = len(parent1)
    p1, p2 = sorted(random.sample(range(n), 2))
    child1 = parent1[:p1] + parent2[p1:p2] + parent1[p2:]
    child2 = parent2[:p1] + parent1[p1:p2] + parent2[p2:]
    return unique_chromosome(child1), unique_chromosome(child2)

# جابجایی تصادفی دو موقعیت برای جهش
def mutate(chromosome):
    n = len(chromosome)
    i, j = random.sample(range(n), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# الگوریتم ژنتیک اصلی
def genetic_algorithm(n, population_size=200, generations=5000, mutation_rate=0.2):
    population = [random_chromosome(n) for _ in range(population_size)]

    for generation in range(generations):
        fitnesses = [fitness(ind) for ind in population]

        if 0 in fitnesses:
            solution = population[fitnesses.index(0)]
            return solution, generation

        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                child1 = mutate(child1)
            if random.random() < mutation_rate:
                child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    # بازگرداندن بهترین جواب در صورت عدم موفقیت کامل
    fitnesses = [fitness(ind) for ind in population]
    best_solution = population[fitnesses.index(min(fitnesses))]
    return best_solution, generations
