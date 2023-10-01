# N-Queen Problem Solver
![photo_2023-10-01_20-43-37](https://github.com/peyman-paknezhad/N-queen-heuristic/assets/102018763/3718602f-8ddd-429e-b43d-38f035e56ea0)

The N-Queen problem is a puzzle where the goal is to place N chess queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens should share the same row, column, or diagonal. It is a challenging problem because the number of possible configurations grows exponentially with the size of the board. Solving the N-Queen problem typically involves using search algorithms to explore different queen placements on the board and find a valid solution. The greedy search algorithm used in this implementation makes iterative moves to improve the queen placements based on a heuristic function, but it may not always find the optimal solution.

The N-Queen problem has practical applications in various areas of computer science, serving as a benchmark for evaluating search algorithms and providing insights into problem-solving strategies and combinatorial optimization. By studying and solving this problem, researchers and practitioners gain a deeper understanding of algorithmic techniques and the complexity of combinatorial problems.

## Method
In this approach, we place restrictions on the rows and columns so that there is only one queen in each row and column. Therefore, we only need to consider the diagonals (positive diagonals, considering diagonals from left to right). We change the diagonal with the maximum number of queens. Based on the constraints, if we move a queen from position i in its row to position j, we move the queen from another row at position j to position i. We choose the movement from all possible movements in which the queens have the least threat to each other. If the queens are not in the same diagonal, we consider all possible movements for them. To prevent loops and repeated states, we store the checked states


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
