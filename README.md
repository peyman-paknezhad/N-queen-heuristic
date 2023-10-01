# N-Queen Problem Solver

This is a Python code that solves the N-Queen problem using a greedy search algorithm. The N-Queen problem is a classic puzzle where the goal is to place N queens on an NxN chessboard in such a way that no two queens threaten each other. In other words, no two queens should share the same row, column, or diagonal.

## Getting Started

To use this code, follow the instructions below:

1. Clone the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Open the terminal and navigate to the project directory.
4. Run the code using the command `python nqueen.py`.

## Code Explanation

The code consists of a single class called `NQueen`, which represents the N-Queen problem solver. Here's a brief explanation of the class methods:

- `__init__(self, n=8, seed=1)`: Initializes the N-Queen solver with the board size `n` and a random seed for shuffling the queens' positions.
- `__str__(self)`: Prints the row and column of each queen.
- `print_board(self)`: Prints the chessboard with queens represented by 'Q' and empty spaces represented by '-'.
- `setup_board(self)`: Sets up the chessboard by shuffling the queens' positions randomly.
- `swap(self, x, y)`: Swaps the column of queens in row `x` and `y`.
- `check(self)`: Checks if the current board configuration is a valid solution.
- `attack_count(self, row, col)`: Counts the number of queens attacking the queen at position `(row, col)`.
- `update_positive_diagonal(self)`: Updates the list of queens in each positive diagonal.
- `board_to_state(self)`: Converts the board configuration to a unique state representation.
- `total_count(self)`: Counts the total number of queen attacks on the board.
- `heuristic(self)`: Applies a heuristic function to find the next move with the minimum number of attacks.
- `greedy_search(self)`: Performs a greedy search to find a solution to the N-Queen problem.

## Example Usage

```python
import random
import math
import time

# Create an instance of the NQueen class
a = NQueen(85, seed=10)

# Set up the chessboard
a.setup_board()

# Solve the N-Queen problem using greedy search
a.greedy_search()
```

## Performance

The performance of the code may vary depending on the board size and the initial configuration. The time taken to find a solution is printed at the end of the code execution.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
