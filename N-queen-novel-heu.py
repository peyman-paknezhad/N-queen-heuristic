#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
import math
import time

class NQueen:
    def __init__(self, n=8, seed=1):
        self.queen = [i for i in range(n)]  # queens' positions
        self.n = n  # board size
        self.rand = seed  # seed for random
        self.seen = set()  # keep track of visited states
        self.p_dia = [[] for i in range(2 * (n - 1) + 1)]  # queens in each positive diagonal

    def __str__(self):  # print the row and column of queens
        for i in range(self.n):
            print(f"Q{i+1} >>> R: {i + 1}, C: {int(self.queen[i]) + 1}")
        return ""

    def print_board(self):
        black_square = "⬛"
        white_square = "⬜"
        queen = "👑"
        #print("    ♚ ♛ ♜ ♝ ♞ ♟️ ♔ ♕ ♖ ♗ ♘ ♙")
        print("➖➖➖➖Board➖➖➖➖\n")
        for i in range(self.n):
            print(f" {chr(65 + i)} ", end="")
            for j in range(self.n):
                if (i + j) % 2 == 0:
                    if self.queen[i] == j:
                        print(f"‌‌{queen}", end="")
                    else:
                        print(f"{white_square}", end="")
                else:
                    if self.queen[i] == j:
                        print(f"{queen}", end="")
                    else:
                        print(f"{black_square}", end="")
            print()


    def setup_board(self):  # setup board randomly
        random.seed(self.rand)  # set the seed
        self.queen = list(range(self.n))  # list of 0 to n
        random.shuffle(self.queen)  # shuffle the list
        self.seen.add(hash(self.board_to_state()))  # mark first state as seen

    def swap(self, x, y):  # swap the column of queens in row x and y
        self.queen[x], self.queen[y] = self.queen[y], self.queen[x]

    def check(self):  # check the goal state
        for x in range(self.n):
            for i in range(self.n):
                if i == x:  # don't check the queen with itself
                    continue
                if self.queen[x] == self.queen[i]:  # check the column
                    return False
                elif self.queen[x] - x == self.queen[i] - i:  # check the negative diagonal
                    return False
                elif self.queen[x] + x == self.queen[i] + i:  # check the positive diagonal
                    return False
        return True

    def attack_count(self, row, col):  # count the attacks for row R and column C
        counter = 0
        for i in range(self.n):
            if i == row:  # don't check the queen with itself
                continue
            if col == self.queen[i]:  # check the column
                counter += 1
                continue
            elif col - row == self.queen[i] - i:  # check the negative diagonal
                counter += 1
                continue
            elif col + row == self.queen[i] + i:  # check the positive diagonal
                counter += 1
                continue
        return counter

    def update_positive_diagonal(self):  # update the positive diagonal list
        self.p_dia = [[] for i in range(2 * (self.n - 1) + 1)]  # reset
        for i in range(self.n):
            self.p_dia[i + self.queen[i]].append(i)  # add the queen to its positive diagonal list
        return True

    def board_to_state(self):  # board to state
        str1 = ""
        for i in self.queen:
            str1 += str(i)
        return int(str1)  # return the self.queen as a string like "1,2,3,4,5,...,n"

    def total_count(self):  # count total attacks
        count = 0  # counter
        for i in range(self.n):
            count += self.attack_count(i, self.queen[i])  # attack_count function for every queen
        return count

    def heuristic(self):  # heuristic function
        self.update_positive_diagonal()  # update the positive diagonal list
        m = [len(i) for i in self.p_dia]  # number of queens in each positive diagonal
        dia = m.index(max(m))  # index of positive diagonal with the most queens
        Dia = {}  # a dict to keep the heuristics for each state

        for i in range(len(self.p_dia[dia])):
            for j in range(self.n):
                if j == self.p_dia[dia][i]:  # don't check the queen with itself
                    continue
                else:  # swap >>> find the heuristic >>> swap again
                    self.swap(self.p_dia[dia][i], j)
                    Dia[str(self.p_dia[dia][i]) + "," + str(j)] = self.total_count()
                    self.swap(self.p_dia[dia][i], j)

        while True:  # until we haven't found the next move
            Dia_v = list(Dia.values())  # list of heuristics
            Dia_k = list(Dia.keys())  # list of swap states
            x = Dia_k[Dia_v.index(min(Dia_v))]  # find the swap with the minimum heuristic
            a, b = x.split(",")
            self.swap(int(a), int(b))
            if hash(self.board_to_state()) in self.seen:  # if checked before
                Dia[x] = float('inf')   # set inf to not be the minimum anymore
                self.swap(int(a), int(b))  # reset the change
            else:
                self.swap(int(a), int(b))  # reset the change
                return int(a), int(b)  # return for swap

    def greedy_search(self):
        self.print_board()
        counter = 0  # counter for number of moves
        while True:
            self.update_positive_diagonal()  # update the positive diagonal list
            a, b = self.heuristic()  # next move by heuristic function
            counter += 1
            self.swap(a, b)  # next move
            self.seen.add(hash(self.board_to_state()))  # add to seen set
            if self.check():  # if it's the goal state
                self.print_board()
                print(counter)
                return True  # done!!!

s = time.time()
a = NQueen(16, seed=10)
a.setup_board()
a.greedy_search()
e = time.time()
print(e - s)


# In[ ]:




