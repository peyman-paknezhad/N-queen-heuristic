# N-Queen Problem Solver

The N-Queen problem is a puzzle where the goal is to place N chess queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens should share the same row, column, or diagonal. It is a challenging problem because the number of possible configurations grows exponentially with the size of the board. Solving the N-Queen problem typically involves using search algorithms to explore different queen placements on the board and find a valid solution. The greedy search algorithm used in this implementation makes iterative moves to improve the queen placements based on a heuristic function, but it may not always find the optimal solution.

The N-Queen problem has practical applications in various areas of computer science, serving as a benchmark for evaluating search algorithms and providing insights into problem-solving strategies and combinatorial optimization. By studying and solving this problem, researchers and practitioners gain a deeper understanding of algorithmic techniques and the complexity of combinatorial problems.

## Usage

To use the N-Queen problem solver, follow these steps:

1. Import the required modules:
   ````python
   import random
   import math
   import time
   ```

2. Define an instance of the `NQueen` class, specifying the board size and an optional seed for randomness:
   ````python
   a = NQueen(n=8, seed=1)
   ```

3. Set up the initial board configuration:
   ````python
   a.setup_board()
   ```

4. Solve the N-Queen problem using a greedy search algorithm:
   ````python
   a.greedy_search()
   ```

5. The program will output the board configuration with the queens' positions and the number of moves taken to find a solution.

## Example

Here's an example usage of the N-Queen problem solver with a board size of 8:

```python
a = NQueen(8, seed=10)
a.setup_board()
a.greedy_search()
```

This will output the final board configuration and the number of moves taken to find a solution.

## Performance

The performance of the solver depends on the board size. Larger board sizes may require more time to find a solution. In the example above, the solver is set to solve the N-Queen problem for a board size of 8. The time taken to find a solution is printed at the end of the program.

## Note

This implementation uses a greedy search algorithm with a heuristic function to find the next move. The algorithm may not always find an optimal solution, but it provides a good approximation.

Feel free to modify the code and experiment with different board sizes and seed values to explore the N-Queen problem further.

---

*This code was developed as part of a project to solve the N-Queen problem using a greedy search algorithm. It is provided as-is without any warranty. Feel free to use and modify it for your own purposes.
