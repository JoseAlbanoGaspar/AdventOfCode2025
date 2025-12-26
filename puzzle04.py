from input_reader import download_aoc_input, parse_lines

# --- Load input ---
input_path = download_aoc_input(2025, 4, SESSION_COOKIE, "inputs/input4.txt")
grid_lines = parse_lines(input_path)


directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def count_accessible_rolls(grid: list[str]) -> int:
    """
    Part 1: Count rolls of paper (@) accessible by a forklift
    given the initial state. A roll is accessible if fewer than
    4 neighbors are rolls (@).
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        neighbors += 1

            if neighbors < 4:
                accessible += 1

    return accessible


def count_total_removable_rolls(grid: list[str]) -> int:
    """
    Part 2: Simulate repeated removal rounds. Each round,
    remove all rolls (@) with fewer than 4 neighbors. Return
    total number removed.
    """
    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0
    grid = [list(row) for row in grid]  # mutable copy

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue

                neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == "@":
                            neighbors += 1

                if neighbors < 4:
                    to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = "."

        total_removed += len(to_remove)

    return total_removed


# --- Run ---
print("Part 1:", count_accessible_rolls(grid_lines))
print("Part 2:", count_total_removable_rolls(grid_lines))
