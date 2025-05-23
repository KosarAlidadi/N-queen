import tkinter as tk
from tkinter import messagebox
from backtracking import solve_n_queens  # باید تمام جواب‌ها رو برگردونه
from Genetic import genetic_algorithm
from PIL import Image, ImageTk  # برای نمایش عکس وزیر

# متغیرهای عمومی
solutions = []
current_solution_index = 0
queen_base_img = None  # تصویر اصلی وزیر (PIL.Image)

# تابع برای رسم صفحه شطرنج و وزرا
def draw_board(board, canvas, n):
    global queen_base_img
    cell_size = 600 // n
    canvas.delete("all")

    # رسم صفحه شطرنج
    for row in range(n):
        for col in range(n):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    # مقیاس‌کردن عکس وزیر
    queen_size = int(cell_size * 0.8)
    resized = queen_base_img.resize((queen_size, queen_size), Image.Resampling.LANCZOS)
    queen_image = ImageTk.PhotoImage(resized)
    canvas.image = queen_image  # نگه‌داشتن رفرنس تصویر

    # رسم وزرا
    for row in range(n):
        col = board[row]
        x = col * cell_size + cell_size // 2
        y = row * cell_size + cell_size // 2
        canvas.create_image(x, y, anchor="center", image=queen_image)

# حل با الگوریتم بازگشتی
def solve_backtracking():
    global solutions, current_solution_index
    try:
        n = int(entry_n.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for N.")
        return

    all_solutions = solve_n_queens(n)
    if all_solutions:
        solutions = all_solutions
        current_solution_index = 0
        draw_board(solutions[0], canvas, n)
        label_info.config(text=f"Found {len(solutions)} solutions.")
        button_next_solution.config(state="normal")
    else:
        label_info.config(text="No solution found.")
        button_next_solution.config(state="disabled")

# راه‌حل بعدی
def show_next_solution():
    global current_solution_index
    if not solutions:
        return
    current_solution_index = (current_solution_index + 1) % len(solutions)
    n = int(entry_n.get())
    draw_board(solutions[current_solution_index], canvas, n)

# حل با الگوریتم ژنتیک
def solve_genetic():
    try:
        n = int(entry_n.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for N.")
        return

    solution, generation = genetic_algorithm(n)
    if solution and isinstance(solution, list):
        draw_board(solution, canvas, n)
        label_info.config(text=f"Solution found in {generation} generations.")
        button_next_solution.config(state="disabled")
    else:
        label_info.config(text="No solution found.")
        button_next_solution.config(state="disabled")

# رابط گرافیکی
root = tk.Tk()
root.title("N-Queens Solver")

# بارگذاری تصویر وزیر پس از ساخت root
try:
    queen_base_img = Image.open("queen.png")
except Exception as e:
    messagebox.showerror("Error", f"Cannot load image: {e}")
    root.quit()

frame_controls = tk.Frame(root)
frame_controls.pack()

label_n = tk.Label(frame_controls, text="Number of Queens (N):")
label_n.pack(side=tk.LEFT)

entry_n = tk.Entry(frame_controls, width=5)
entry_n.pack(side=tk.LEFT)

button_backtracking = tk.Button(frame_controls, text="Backtracking", command=solve_backtracking)
button_backtracking.pack(side=tk.LEFT, padx=5)

button_next_solution = tk.Button(frame_controls, text="Next Solution", command=show_next_solution, state="disabled")
button_next_solution.pack(side=tk.LEFT)

button_genetic = tk.Button(frame_controls, text="Genetic Algorithm", command=solve_genetic)
button_genetic.pack(side=tk.LEFT, padx=5)

label_info = tk.Label(root, text="")
label_info.pack()

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

root.mainloop()
