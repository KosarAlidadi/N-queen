# backtracking.py
# حل دقیق با استفاده از الگوریتم بازگشتی (Backtracking)

def is_safe(state, row, col):
    for r in range(row):
        c = state[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def backtrack(n, row, state, initial, solutions):
    if row == n:
        solutions.append(state.copy())
        return
    if initial[row] != -1:
        # اگر مقدار اولیه برای این سطر داده شده باشد
        if is_safe(state, row, initial[row]):
            state[row] = initial[row]
            backtrack(n, row + 1, state, initial, solutions)
        return
    for col in range(n):
        if is_safe(state, row, col):
            state[row] = col
            backtrack(n, row + 1, state, initial, solutions)

def solve_backtracking(n, initial):
    state = [-1] * n
    solutions = []
    backtrack(n, 0, state, initial, solutions)
    return solutions
