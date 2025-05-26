# N-Queens Solver - Solving the N-Queens Problem with Python

This project is a graphical application that solves the well-known N-Queens problem (placing N queens on an N×N chessboard such that none threaten each other) using various algorithms.
It features a user-friendly GUI built with Tkinter and visualizes the solutions using a queen image.

---

## Features

- Exact solution using the **Backtracking Algorithm**
- Approximate solution using the **Genetic Algorithm**
- Step-by-step display of all solutions in Backtracking mode
- Simple and user-friendly graphical interface
- Visual representation of queens using an image
- Clean, modular, and extendable codebase

---

## File Structure

```
n_queens_project/
│
├── gui.py               # Main GUI application (Tkinter interface)
├── backtracking.py      # Backtracking algorithm implementation (returns all solutions)
├── Genetic.py           # Genetic algorithm implementation (returns one approximate solution)
├── queen.png            # Queen image used to render on the chessboard
└── README.md            # Project documentation
```

---

##  Installation & Running the Project

### Prerequisites:

- Python 3.10 or higher
- Required packages:

```bash
pip install pillow
```

### Running the Application:

```bash
python gui.py
```

---

## How to Use

1. Run the application.
2. Enter the number of queens (e.g., 8) in the input field.
3. Use the buttons:
   - **Backtracking**: Solves the problem using the backtracking algorithm and displays the first solution.
   - **Next Solution**: Shows the next available solution (in Backtracking mode).
   - **Genetic Algorithm**: Uses a genetic approach to find a solution.

> Note: If the queen image (`queen.png`) is missing in the project directory, the program will not run.

---

## Queen Image Instructions

The `queen.png` image must be located in the same directory as the project files. The image is dynamically resized based on the board cell size.

**Recommendation**: Use a PNG image with a transparent background for better visual integration with the chessboard.

---

##  Future Plans (Roadmap)

- [ ] Implement a csp Algorithm
- [ ] Display movement sequences for algorithms
- [ ] Support custom initial states
- [ ] Allow manual algorithm selection and animation speed control

---

## Developer

Kosar Alidadi

---

## License

This project is free for educational use. Feel free to use and modify it with proper attribution.lgorithms 3.  CSP 
