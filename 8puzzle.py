#!/usr/bin/env python3
import random


def swap (list, position_a, position_b):
    list[position_a], list[position_b] = list[position_b], list[position_a]
class Graph:
    def __init__(self, root, size):
        self.root = root
        self.visited = [root]
        self.queue = []
        self.leaves = [root]
        self.size =size

    def bfs(self, goal):
        self.queue.append(self.root)
        while self.queue:
            s = self.queue.pop(0)
            if s.data == goal:
                return s
            if s not in self.visited:
                self.visited.append(s)
            for move in s.moves:
                self.queue.append(move)
        self.queue = []
        return None

    def new_level(self):
        count = len(self.leaves)
        for i in range(0, count):
            node = self.leaves.pop(0)
            node.new_moves(self.size)
            for n in node.moves:
                if n not in self.visited:
                    self.leaves.append(n)

    def print_path(self, node):
        path = [node]
        moves = []
        while node.parent is not None:
            path.append(node.parent)
            node = node.parent
        path.reverse()
        for node in path:
            print(node.data)

class Node:
    def __init__(self, data, position, previous, parent):
        self.moves = []
        self.data = data
        self.position = position
        self.previous = previous
        self.parent = parent

    def new_moves(self, size):
        if self.position % size != 0 and self.previous != 'r':
            left_move = self.data.copy()
            swap(left_move, self.position, self.position - 1)
            self.moves.append(Node(left_move, self.position - 1, 'l', self))
        if self.position % size != size-1 and self.previous != 'l':
            right_move = self.data.copy()
            swap(right_move, self.position, self.position + 1)
            self.moves.append(Node(right_move, self.position + 1, 'r', self))
        if self.position > size-1 and self.previous != 'd':
            up_move = self.data.copy()
            swap(up_move, self.position, self.position - size)
            self.moves.append(Node(up_move, self.position - size, 'u', self))
        if self.position < (len(self.data)-size) and self.previous != 'u':
            down_move = self.data.copy()
            swap(down_move, self.position, self.position + size)
            self.moves.append(Node(down_move, self.position + size, 'd', self))

    def __str__(self):
        return self.data


def solve(size):
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    puzzle = [1, 3, 4, 8, 0, 5, 7, 2, 6]
    print("Puzzle: {}".format(puzzle))

    if puzzle != goal:
        root = Node(puzzle, puzzle.index(0), "", None)
        graph = Graph(root, int(size**(1/2)))
        node = None
        while node is None:
            graph.new_level()
            node = graph.bfs(goal)
        graph.print_path(node)
        print("# of nodes: {}".format(len(graph.visited)))

if __name__ == '__main__':
    solve(9)
