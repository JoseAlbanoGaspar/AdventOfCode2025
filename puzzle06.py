from functools import reduce
from input_reader import download_aoc_input, parse_lines
import operator

# --- Load input ---
input_path = download_aoc_input(2025, 6, SESSION_COOKIE, "inputs/input6.txt")
lines = parse_lines(input_path)

op_map = {
    '+': operator.add,
    '*': operator.mul,
}

for i in range(len(lines)):
    lines[i] = lines[i].split()

lines = [list(row) for row in zip(*lines)] # transpose rows to columns

def part1(lines):
    res = 0
    for line in lines:
        *nums, op = line
        res += reduce(op_map[op], map(int, nums))
    return res




print("Part 1:", part1(lines))
