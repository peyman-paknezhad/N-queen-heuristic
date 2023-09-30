#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import math

class NQueens:
    def __init__(self, n=8, seed=1):
        self.queen = [0 for _ in range(n)]  # queens' positions
        self.n = n
        self.rand = seed  # seed for randomization
        self.seen = set()  # keep track of visited states

    def __str__(self):
        for i in range(self.n):
            print(f"Queen {i+1} >>> Row: {i+1}, Column: {int(self.queen[i])+1}")
        return ""

    def print_board(self):
        print("    ________________Board________________\n")
        for i in range(self.n):
            print(f"Row {i+1}:   ", end="")
            for x in range(self.queen[i]):
                print("—  ", end="")  # empty before Queen
            print("Q ", end="")  # Q = Queen
            for y in range(self.n - self.queen[i] - 1):
                print("—  ", end="")  # empty after Queen
            print("\n")
        print("    ________________Board________________\n")

    def setup_board(self, randomize=True):
        if randomize:
            random.seed(self.rand)
            self.queen = list(range(self.n))
            random.shuffle(self.queen)
            self.seen.add(hash(self.board_to_string()))
        else:
            for i in range(self.n):
                x = int(input(f"Queen {i+1} >>> "))
                if x > self.n or x < 0:
                    raise ValueError("Invalid column")
                self.queen[i] = x - 1
            self.seen.add(hash(self.board_to_string()))

    def is_goal_state(self):
        for x in range(self.n):
            for i in range(self.n):
                if i == x:
                    continue
                if self.queen[x] == self.queen[i]:
                    return False
                elif self.queen[x] - x == self.queen[i] - i:
                    return False
                elif self.queen[x] + x == self.queen[i] + i:
                    return False
        return True

    def count_attacks(self, row, col):
        counter = 0
        for i in range(self.n):
            if i == row:
                continue
            if col == self.queen[i]:
                counter += 1
                continue
            elif col - row == self.queen[i] - i:
                counter += 1
                continue
            elif col + row == self.queen[i] + i:
                counter += 1
                continue
        return counter

    def make_move(self, row, col):
        self.queen[row] = col

    def board_to_string(self):
        return "".join(str(i) for i in self.queen)

    def calculate_heuristic(self):
        H = []
        H_state = []
        for i in self.queen:
            r = self.queen.index(i)
            c = i
            if c != 0:
                self.make_move(r, c-1)
                h = 0
                for j in range(self.n):
                    h += self.count_attacks(j, self.queen[j])
                H.append(h)
                H_state.append(self.board_to_string())
                self.make_move(r, c)
            else:
                H.append(1000)
                H_state.append("n")
            if c != self.n-1:
                self.make_move(r, c+1)
                h = 0
                for j in range(self.n):
                    h += self.count_attacks(j, self.queen[j])
                H.append(h)
                H_state.append(self.board_to_string())
                self.make_move(r, c)
            else:
                H.append(1000)
                H_state.append("n")

        while True:
            move = H.index(min(H))
            if hash(H_state[move]) in self.seen:
                H[move] = 1000
                continue
            else:
                move += 1
                if move % 2 == 0:
                    X = 1
                else:
                    X = -1
                row = math.ceil(move/2) - 1
                col = self.queen[row] + X
                return row, col

    def solve_greedy(self):
        counter = 0
        while True:
            m = self.calculate_heuristic()
            self.make_move(m[0], m[1])
            counter += 1
            self.seen.add(hash(self.board_to_string()))
            if self.is_goal_state():
                self.print_board()
                print(counter)
                return True

            
import time
start_time = time.time()

a = NQueens(16, seed=1)
a.setup_board(randomize=True)
a.print_board()
a.solve_greedy()

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
            


# In[ ]:




