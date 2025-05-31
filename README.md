# N-Queens Solver with GUI (Backtracking, Genetic, CSP)

This project is a Python-based application that solves the N-Queens problem using three different algorithms:
- Backtracking (exact search)
- Genetic Algorithm (approximate solution)
- CSP (Constraint Satisfaction Problem) approach

It features a Tkinter-based GUI, supports manual initial queen placement, and visualizes the step-by-step movements of each algorithm.

---

##  Features

- ✅ Backtracking: Explores all valid solutions recursively
- ✅ Genetic Algorithm: Heuristic search with crossover/mutation
- ✅ CSP : Forward-checking with constraints
- ✅ Manual input of initial board state
- ✅ Step-by-step move sequence display for each algorithm
- ✅ Scalable chessboard (queens resize with cell size)
- ✅ Modular codebase with clean architecture
- ✅ User-friendly graphical interface (Tkinter)

---

##  Project Structure

```
N_queen/
├── gui.py               # Main GUI interface
├── backtracking.py      # Backtracking algorithm implementation
├── Genetic.py           # Genetic algorithm implementation
├── csp.py               # CSP-based solver
├── queen.png            # Queen image for rendering
 README.md            # Project documentation
```

---

##  Requirements

- Python 3.10 or higher
- Pillow library for image rendering

Install required packages:
```bash
pip install pillow
```

---

##  How to Run

```bash
python gui.py
```

---

##  How to Use

1. Run the app.
2. Enter board size (e.g. 8 for 8×8).
3. (Optional) Use "Manual Input" to place queens before solving.
4. Choose your algorithm:
   - Backtracking
   - Genetic
   - CSP
5. The board will show step-by-step movement to the final solution.

---

##  Notes

- Ensure queen.png is in the same directory as gui.py.
- Manual input requires clicking on the board to place queens before running the algorithm.
- For Genetic and CSP, manual state must be valid (no conflicts).

---

##  Future Features

- [ ] Adjustable animation speed
- [ ] Save/load board states
- [ ] Export solution to file
- [ ] Enhanced CSP heuristics (e.g., MRV, degree heuristic)

---

##  Author

Kosar Alidadi  
For educational purposes – feel free to use and modify with attribution.

---

##  License

This project is free for academic and personal use. 
