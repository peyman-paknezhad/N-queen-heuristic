# N-Queen Problem Solver
![photo_2023-10-01_20-43-37](https://github.com/peyman-paknezhad/N-queen-heuristic/assets/102018763/3718602f-8ddd-429e-b43d-38f035e56ea0)

The N-Queen problem is a puzzle where the goal is to place N chess queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens should share the same row, column, or diagonal. It is a challenging problem because the number of possible configurations grows exponentially with the size of the board. Solving the N-Queen problem typically involves using search algorithms to explore different queen placements on the board and find a valid solution. The greedy search algorithm used in this implementation makes iterative moves to improve the queen placements based on a heuristic function, but it may not always find the optimal solution.

The N-Queen problem has practical applications in various areas of computer science, serving as a benchmark for evaluating search algorithms and providing insights into problem-solving strategies and combinatorial optimization. By studying and solving this problem, researchers and practitioners gain a deeper understanding of algorithmic techniques and the complexity of combinatorial problems.

## Method
In this approach, we place restrictions on the rows and columns so that there is only one queen in each row and column. Therefore, we only need to consider the diagonals (positive diagonals, considering diagonals from left to right). We change the diagonal with the maximum number of queens. Based on the constraints, if we move a queen from position i in its row to position j, we move the queen from another row at position j to position i. We choose the movement from all possible movements in which the queens have the least threat to each other. If the queens are not in the same diagonal, we consider all possible movements for them. To prevent loops and repeated states, we store the checked states


## Example

Here's an example usage of the N-Queen problem solver with a board size of 8:

```python
a = NQueen(8, seed=10)
a.setup_board()
a.greedy_search()
```

This will output the final board configuration and the number of moves taken to find a solution.

## Performance

The performance of the solver depends on the board size. Larger board sizes may require more time to find a solution..

The output of the code that solves the N-queen problem can be very good, as it provides a solution to a complex puzzle. Based on the test conducted, the code was able to solve the problem for 150 queens in approximately 90 seconds. This demonstrates the efficiency and effectiveness of the code in finding solutions for a large number of queens.

Below is the picture of the result for the 16-queen problem:

![1](https://github.com/peyman-paknezhad/N-queen-heuristic/assets/102018763/06c50d72-148b-4389-b6fd-aa78f22ba1a8)


The picture showcases a valid configuration of 16 queens on a 16×16 chessboard, where no two queens threaten each other. This solution represents the successful outcome of the code in solving the N-queen problem for 16 queens.

## Note

This implementation uses a greedy search algorithm with a heuristic function to find the next move. The algorithm may not always find an optimal solution, but it provides a good approximation.

---
