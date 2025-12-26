from input_reader import download_aoc_input, parse_lines

# --- Load input ---
input_path = download_aoc_input(2025, 5, SESSION_COOKIE, "inputs/input5.txt")
lines = parse_lines(input_path, skip_empty=False)


def merge_ranges(range_list: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Merge overlapping or contiguous ranges.
    """
    range_list.sort()
    merged = []
    for start, end in range_list:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def count_fresh_available_ids(lines: list[str]) -> int:
    """
    Part 1: Count how many available ingredient IDs are fresh.
    """
    split_index = lines.index("")  # blank line separates ranges from available IDs
    range_lines = lines[:split_index]
    id_lines = lines[split_index + 1:]

    # Parse ranges
    ranges = []
    for r in range_lines:
        a, b = map(int, r.split("-"))
        ranges.append((a, b))

    # Merge ranges
    merged = merge_ranges(ranges)

    # Parse available IDs
    available_ids = list(map(int, id_lines))

    # Check if each ID is in any range
    def is_fresh(id_: int) -> bool:
        for start, end in merged:
            if start <= id_ <= end:
                return True
            if id_ < start:
                break
        return False

    return sum(1 for id_ in available_ids if is_fresh(id_))


def count_total_fresh_ids(lines: list[str]) -> int:
    """
    Part 2: Count total ingredient IDs considered fresh by the ranges,
    ignoring the available IDs section.
    """
    # Take only the range section
    range_lines = []
    for line in lines:
        if line == "":
            break
        range_lines.append(line)

    ranges = []
    for r in range_lines:
        a, b = map(int, r.split("-"))
        ranges.append((a, b))

    # Merge ranges
    merged = merge_ranges(ranges)

    # Sum all IDs covered by the merged ranges
    return sum(end - start + 1 for start, end in merged)


# --- Run ---
print("Part 1:", count_fresh_available_ids(lines))
print("Part 2:", count_total_fresh_ids(lines))
