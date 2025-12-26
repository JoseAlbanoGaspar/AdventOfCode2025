from input_reader import download_aoc_input, parse_lines

# --- Load input ---
input_path = download_aoc_input(2025, 7, SESSION_COOKIE, "inputs/input7.txt")
grid_lines = parse_lines(input_path)

def count_splits(grid: list[str]) -> int:
    """
    Part 1: Count the total number of splitters (^) encountered by beams.
    """
    rows = len(grid)
    cols = len(grid[0])
    start_col = grid[0].index("S")

    beams = set([start_col])
    split_count = 0

    for r in range(1, rows):
        new_beams = set()
        for c in beams:
            cell = grid[r][c]
            if cell == ".":
                new_beams.add(c)
            elif cell == "^":
                split_count += 1
                # spawn new beams left and right
                if c - 1 >= 0:
                    new_beams.add(c - 1)
                if c + 1 < cols:
                    new_beams.add(c + 1)
            # other cells (like S) stop beam
        beams = new_beams

    return split_count


def count_timelines(grid: list[str]) -> int:
    """
    Part 2: Count the total number of timelines for a single quantum particle.
    """
    rows = len(grid)
    cols = len(grid[0])
    start_col = grid[0].index("S")

    # dp[r][c] = number of timelines reaching this cell
    dp = [ [0] * cols for _ in range(rows) ]
    dp[0][start_col] = 1

    for r in range(rows - 1):
        for c in range(cols):
            if dp[r][c] == 0:
                continue
            cell = grid[r+1][c]
            if cell == ".":
                dp[r+1][c] += dp[r][c]
            elif cell == "^":
                if c - 1 >= 0:
                    dp[r+1][c-1] += dp[r][c]
                if c + 1 < cols:
                    dp[r+1][c+1] += dp[r][c]
            # other cells stop timelines

    return sum(dp[-1][c] for c in range(cols))


# --- Run ---
print("Part 1:", count_splits(grid_lines))
print("Part 2:", count_timelines(grid_lines))
