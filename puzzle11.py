from functools import lru_cache
from input_reader import download_aoc_input, parse_lines



def parse_graph(lines):
    graph = {}
    for line in lines:
        src, rest = line.split(":")
        graph[src.strip()] = rest.strip().split()
    return graph


def day11_part1(lines):
    graph = parse_graph(lines)

    @lru_cache(None)
    def count_paths(node):
        if node == "out":
            return 1
        total = 0
        for nxt in graph.get(node, []):
            total += count_paths(nxt)
        return total

    return count_paths("you")

def day11_part2(lines):
    graph = parse_graph(lines)

    @lru_cache(None)
    def dfs(node, seen_dac, seen_fft):
        # Update flags if we hit dac or fft
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True

        # Base case
        if node == "out":
            return 1 if seen_dac and seen_fft else 0

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, seen_dac, seen_fft)
        return total

    return dfs("svr", False, False)

# ---- Run ----
input_path = download_aoc_input(2025, 11, SESSION_COOKIE, "inputs/input11.txt")
lines = parse_lines(input_path)

print("Day 11 - Part 1:", day11_part1(lines))
print("Day 11 - Part 2:", day11_part2(lines))
