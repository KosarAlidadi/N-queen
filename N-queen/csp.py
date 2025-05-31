# csp.py
# حل مسئله با استفاده از رویکرد CSP

def is_valid(state, row, col):
    for r in range(row):
        c = state[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def csp_dfs(n, row, state, initial):
    if row == n:
        return state
    if initial[row] != -1:
        if is_valid(state, row, initial[row]):
            state[row] = initial[row]
            return csp_dfs(n, row + 1, state, initial)
        return None
    for col in range(n):
        if is_valid(state, row, col):
            state[row] = col
            result = csp_dfs(n, row + 1, state, initial)
            if result:
                return result
    return None

def solve_csp(n, initial):
    state = [-1] * n
    return csp_dfs(n, 0, state, initial)
