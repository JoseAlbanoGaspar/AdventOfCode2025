from input_reader import download_aoc_input, parse_lines

# --- Load input ---
input_path = download_aoc_input(2025, 3, SESSION_COOKIE, "inputs/input3.txt")
banks = parse_lines(input_path)


def max_joltage(bank: str) -> int:
    digits = list(map(int, bank))
    best = 0
    n = len(digits)

    for i in range(n - 1):
        tens = digits[i]
        ones = max(digits[i + 1:])
        best = max(best, tens * 10 + ones)

    return best

def max_joltage_k(bank: str, k: int = 12) -> int:
    stack = []
    to_remove = len(bank) - k  # how many digits we are allowed to drop

    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return int("".join(stack[:k]))

part1 = sum(max_joltage(bank) for bank in banks)
part2 = sum(max_joltage_k(bank) for bank in banks)

print("Part1: ", part1)
print("Part2: ", part2)