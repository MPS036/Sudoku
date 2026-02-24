# 🧠 Sudoku Generator & Solver (Backtracking)

A Python implementation of a Sudoku generator and solver.
The project creates a valid Sudoku grid, removes a portion of numbers to form a puzzle, and then solves it using a classic backtracking algorithm.

## ✨ Features:

- Generates a valid 9×9 Sudoku solution grid
- Creates a puzzle by removing cells (empty cells are marked as 0 / displayed as .)
- Solves the puzzle using recursive backtracking
- Console-based output (no external dependencies)

## 📌 Notes:

- The generator creates valid puzzles by removing random cells.
- Uniqueness of the solution is not enforced (some generated puzzles may have multiple solutions).
- The solver modifies the board in-place.

## 🛠 Requirements:

- This project uses only Python’s standard library.
