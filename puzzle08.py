import math
from itertools import combinations
from collections import Counter

from input_reader import download_aoc_input, parse_lines


def parse_input(lines):
    points = []
    for line in lines:
        x, y, z = map(int, line.strip().split(","))
        points.append((x, y, z))
    return points


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2 +
        (p1[2] - p2[2]) ** 2
    )


def day8_part1(lines):
    points = parse_input(lines)
    n = len(points)

    edges = []
    for (i, p1), (j, p2) in combinations(enumerate(points), 2):
        edges.append((distance(p1, p2), i, j))

    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)

    for k in range(1000):
        _, a, b = edges[k]
        uf.union(a, b)

    roots = [uf.find(i) for i in range(n)]
    counts = Counter(roots)
    sizes = sorted(counts.values(), reverse=True)

    return sizes[0] * sizes[1] * sizes[2]


def day8_part2(lines):
    points = parse_input(lines)
    n = len(points)

    edges = []
    for (i, p1), (j, p2) in combinations(enumerate(points), 2):
        edges.append((distance(p1, p2), i, j))

    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)

    for _, a, b in edges:
        merged = uf.union(a, b)
        if merged and uf.components == 1:
            # This edge completed the single circuit
            return points[a][0] * points[b][0]


# ---- Run ----
input_path = download_aoc_input(2025, 8, SESSION_COOKIE, "inputs/input8.txt")
lines = parse_lines(input_path)

print("Day 8 - Part 1:", day8_part1(lines))
print("Day 8 - Part 2:", day8_part2(lines))
