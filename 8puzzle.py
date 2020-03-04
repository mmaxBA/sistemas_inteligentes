#!/usr/bin/env python3
import random


def swap (list, position_a, position_b):
    list[position_a], list[position_b] = list[position_b], list[position_a]
class Graph:
    def __init__(self, root):
        self.root = root
        self.visited = [root]
        self.queue = []
        self.leaves = [root]

    def bfs(self, goal):
        self.queue.append(self.root)
        while self.queue:
            s = self.queue.pop(0)
            print("S: {}".format(s.data))
            if s.data == goal:
                return True
            for move in s.moves:
                if move not in self.visited:
                    self.visited.append(move)
                    self.queue.append(move)
        self.queue = []
        return False

    def new_level(self):
        count = len(self.leaves)
        for i in range(0, count):
            node = self.leaves.pop(0)
            node.new_moves()
            for n in node.moves:
                self.leaves.append(n)

class Node:
    def __init__(self, data, position, previous):
        self.moves = []
        self.data = data
        self.position = position
        self.previous = previous

    def new_moves(self):
        if self.position % 3 != 0 and self.previous != 'r':
            left_move = self.data.copy()
            swap(left_move, self.position, self.position - 1)
            self.moves.append(Node(left_move, self.position - 1, 'l'))
        if self.position % 3 != 2 and self.previous != 'l':
            right_move = self.data.copy()
            swap(right_move, self.position, self.position + 1)
            self.moves.append(Node(right_move, self.position + 1, 'r'))
        if self.position > 2 and self.previous != 'd':
            up_move = self.data.copy()
            swap(up_move, self.position, self.position - 3)
            self.moves.append(Node(up_move, self.position - 3, 'u'))
        if self.position < 6 and self.previous != 'u':
            down_move = self.data.copy()
            swap(down_move, self.position, self.position + 3)
            self.moves.append(Node(down_move, self.position + 3, 'd'))


def solve(size):
    goal = []
    if size != 9 | size != 16 |size != 25:
        print("Not a valid size")
        return 0
    for i in range(1,size):
        goal.append(i)
    goal.append(0)
    puzzle = random.sample(range(size), size)
    print("Puzzle: {}".format(puzzle))

    if puzzle != goal:
        root = Node(puzzle, puzzle.index(0), " ")
        graph = Graph(root)
        solution_found = False
        while not solution_found:
            graph.new_level()
            solution_found = graph.bfs(goal)

    print(puzzle)
    print(graph)

if __name__ == '__main__':
    solve(9)
