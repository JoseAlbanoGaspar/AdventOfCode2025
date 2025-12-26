import re
from input_reader import download_aoc_input


def day12_part1(text):
    """
    Check if regions can fit all presents.
    Each present takes up at least 3x3 cells.
    """
    lines = text.split("\n\n")[-1].splitlines()
    total = 0
    
    for line in lines:
        x, y, *counts = list(map(int, re.findall(r"\d+", line)))
        if (x // 3) * (y // 3) >= sum(counts):
            total += 1
    
    return total


# ---- Run ----
input_path = download_aoc_input(2025, 12, SESSION_COOKIE, "inputs/input12.txt")
with open(input_path) as f:
    text = f.read()

print("Day 12 Part 1:", day12_part1(text))