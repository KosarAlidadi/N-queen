import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from backtracking import solve_backtracking
from Genetic import solve_genetic
from csp import solve_csp

# متغیرهای عمومی
queen_img = None
solutions = []
current_solution_index = 0
sequence_label = None


def load_queen_image(cell_size):
    """بارگذاری تصویر وزیر با اندازه مناسب"""
    global queen_img
    try:
        img = Image.open("queen.png").resize((cell_size, cell_size))
        queen_img = ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Image Error", f"Cannot load queen.png: {e}")


def draw_board(canvas, board, n):
    """رسم صفحه شطرنج و جای‌گذاری وزیرها"""
    canvas.delete("all")
    cell_size = min(480 // n, 60)
    load_queen_image(cell_size)

    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
            if board[i] == j:
                canvas.create_image(x1, y1, anchor="nw", image=queen_img)


def parse_initial_input(text, n):
    """تجزیه حالت اولیه وارد شده توسط کاربر"""
    try:
        parts = text.strip().split(',')
        if len(parts) != n:
            raise ValueError
        return [int(p.strip()) for p in parts]
    except:
        messagebox.showerror("Input Error", f"Initial state must contain exactly {n} values (e.g., -1,-1,-1,...)")
        return None


def update_sequence_display(state):
    """نمایش مسیر حل (sequence)"""
    seq = ",".join(str(x) for x in state)
    sequence_label.config(text=f"Sequence: [{seq}]")


def on_backtracking(n, initial, canvas):
    """اجرای الگوریتم بازگشتی"""
    global solutions, current_solution_index
    solutions = solve_backtracking(n, initial)
    if not solutions:
        messagebox.showinfo("No Solution", "No solution found.")
        return
    current_solution_index = 0
    draw_board(canvas, solutions[0], n)
    update_sequence_display(solutions[0])


def on_next_solution(n, canvas):
    """مشاهده راه‌حل بعدی در الگوریتم بازگشتی"""
    global solutions, current_solution_index
    if not solutions:
        return
    current_solution_index = (current_solution_index + 1) % len(solutions)
    draw_board(canvas, solutions[current_solution_index], n)
    update_sequence_display(solutions[current_solution_index])


def on_genetic(n, initial, canvas):
    """اجرای الگوریتم ژنتیکی"""
    solution = solve_genetic(n, initial)
    if solution:
        draw_board(canvas, solution, n)
        update_sequence_display(solution)
    else:
        messagebox.showinfo("No Solution", "Genetic algorithm failed to find a solution.")


def on_csp(n, initial, canvas):
    """اجرای الگوریتم CSP"""
    solution = solve_csp(n, initial)
    if solution:
        draw_board(canvas, solution, n)
        update_sequence_display(solution)
    else:
        messagebox.showinfo("No Solution", "CSP algorithm failed to find a solution.")


def create_gui():
    """ساخت رابط گرافیکی برنامه"""
    root = tk.Tk()
    root.title("N-Queens Solver")

    tk.Label(root, text="Number of Queens (N):").grid(row=0, column=0, sticky="e")
    n_entry = tk.Entry(root)
    n_entry.insert(0, "8")
    n_entry.grid(row=0, column=1, pady=5)

    tk.Label(root, text="Initial State (-1 for empty, e.g. -1,-1,2,...):").grid(row=1, column=0, columnspan=2)
    init_entry = tk.Entry(root, width=40)
    init_entry.insert(0, "-1,-1,-1,-1,-1,-1,-1,-1")
    init_entry.grid(row=2, column=0, columnspan=2, pady=5)

    canvas = tk.Canvas(root, width=480, height=480)
    canvas.grid(row=3, column=0, columnspan=2, pady=10)

    def get_values():
        try:
            n = int(n_entry.get())
            initial = parse_initial_input(init_entry.get(), n)
            return n, initial
        except:
            messagebox.showerror("Error", "Invalid input.")
            return None, None

    # دکمه‌ها برای اجرای الگوریتم‌ها
    tk.Button(root, text="Backtracking", command=lambda: run_backtracking(canvas)).grid(row=4, column=0, sticky="ew", padx=5)
    tk.Button(root, text="Next Solution", command=lambda: on_next_solution(int(n_entry.get()), canvas)).grid(row=4, column=1, sticky="ew", padx=5)
    tk.Button(root, text="Genetic", command=lambda: run_genetic(canvas)).grid(row=5, column=0, sticky="ew", padx=5)
    tk.Button(root, text="CSP", command=lambda: run_csp(canvas)).grid(row=5, column=1, sticky="ew", padx=5)

    global sequence_label
    sequence_label = tk.Label(root, text="Sequence: []", fg="blue")
    sequence_label.grid(row=6, column=0, columnspan=2, pady=10)

    def run_backtracking(canvas):
        n, initial = get_values()
        if initial is not None:
            on_backtracking(n, initial, canvas)

    def run_genetic(canvas):
        n, initial = get_values()
        if initial is not None:
            on_genetic(n, initial, canvas)

    def run_csp(canvas):
        n, initial = get_values()
        if initial is not None:
            on_csp(n, initial, canvas)

    root.mainloop()


if __name__ == "__main__":
    create_gui()