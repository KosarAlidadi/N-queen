from backtracking import solve_n_queens

n = 5
solutions = solve_n_queens(n)

for sol in solutions:
    print(sol)
