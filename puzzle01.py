# Example usage
from input_reader import download_aoc_input, parse_lines


input_file = download_aoc_input(
    year=2025,
    day=1,
    session_cookie=SESSION_COOKIE,
    output_path="inputs/input1.txt",
)

lines = parse_lines(input_file)

## Problem 1
def prob1_part1():
    number = 50
    ans = 0
    for line in lines:
        direction, dist = line[0], int(line[1:])
        if direction == "L":
            number = (number - dist + 100) % 100
        else: # direction == "R"
            number = (number + dist) % 100
        if number == 0:
            ans += 1


number = 50
ans = 0

for line in lines:
    direction, dist = line[0], int(line[1:])

    for _ in range(dist):
        if direction == "L":
            number = (number - 1 + 100) % 100
        else: # direction == "R"
            number = (number + 1) % 100

        if number == 0:
            ans += 1

print(ans)
