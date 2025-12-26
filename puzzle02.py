from input_reader import download_aoc_input, parse_lines

def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def find_invalid_sum(ranges):
    total = 0

    for lo, hi in ranges:
        lo_len = len(str(lo))
        hi_len = len(str(hi))

        # Only even-length numbers can be invalid
        for length in range(lo_len, hi_len + 1):
            if length % 2 != 0:
                continue

            half_len = length // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len

            for x in range(start, end):
                s = str(x)
                candidate = int(s + s)

                if candidate < lo:
                    continue
                if candidate > hi:
                    break

                total += candidate

    return total

def is_invalid_part2(n: int) -> bool:
    s = str(n)
    L = len(s)

    for k in range(1, L // 2 + 1):
        if L % k != 0:
            continue
        if s[:k] * (L // k) == s:
            return True
    return False


def find_invalid_sum_part2(ranges):
    invalid_ids = set()

    for lo, hi in ranges:
        lo_len = len(str(lo))
        hi_len = len(str(hi))

        for length in range(lo_len, hi_len + 1):
            for pattern_len in range(1, length // 2 + 1):
                if length % pattern_len != 0:
                    continue

                repeats = length // pattern_len
                if repeats < 2:
                    continue

                start = 10 ** (pattern_len - 1)
                end = 10 ** pattern_len

                for x in range(start, end):
                    s = str(x)
                    candidate = int(s * repeats)

                    if candidate < lo:
                        continue
                    if candidate > hi:
                        break

                    if is_invalid_part2(candidate):
                        invalid_ids.add(candidate)

    return sum(invalid_ids)

input_file = download_aoc_input(
    year=2025,
    day=2,
    session_cookie=SESSION_COOKIE,
    output_path="inputs/input2.txt",
)

lines = parse_lines(input_file)

ranges = []
for part in lines[0].split(","):
    a, b = part.split("-")
    ranges.append((int(a), int(b)))

print(find_invalid_sum_part2(ranges))