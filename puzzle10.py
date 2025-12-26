import re
from itertools import product
from input_reader import download_aoc_input, parse_lines




def parse_machine(line):
    # indicator pattern
    pattern = re.search(r"\[([.#]+)\]", line).group(1)
    n = len(pattern)

    target = 0
    for i, ch in enumerate(pattern):
        if ch == "#":
            target |= 1 << i

    # button masks
    buttons = []
    for grp in re.findall(r"\(([^)]+)\)", line):
        mask = 0
        for idx in grp.split(","):
            mask |= 1 << int(idx)
        buttons.append(mask)

    return target, buttons


def min_presses_for_machine(target, buttons):
    m = len(buttons)
    best = None

    # try all subsets of buttons
    for choice in range(1 << m):
        state = 0
        presses = 0
        for i in range(m):
            if choice & (1 << i):
                state ^= buttons[i]
                presses += 1

        if state == target:
            if best is None or presses < best:
                best = presses

    return best


def day10_part1(lines):
    total = 0
    for line in lines:
        target, buttons = parse_machine(line)
        total += min_presses_for_machine(target, buttons)
    return total


# ---- Run ----
input_path = download_aoc_input(2025, 10, SESSION_COOKIE, "inputs/input10.txt")
lines = parse_lines(input_path)

print("Day 10:", day10_part1(lines))
