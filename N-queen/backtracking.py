def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    
    # سه مجموعه برای ردیف‌های پرشده، ستون‌های پرشده و قطرهای پرشده
    cols = set()  # ستون‌ها
    diag1 = set()  # قطرهای اصلی
    diag2 = set()  # قطرهای فرعی

    def backtrack(row=0):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            # اگر ستون یا قطرها تداخل دارند، ادامه نده
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # افزودن ستون و قطرها به مجموعه‌ها
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            board[row] = col
            backtrack(row + 1)
            
            # حذف ستون و قطرها از مجموعه‌ها (برگشت به حالت قبلی)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack()
    return solutions
