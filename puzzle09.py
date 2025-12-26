from itertools import combinations
from input_reader import download_aoc_input, parse_lines


def parse_points(lines):
    return [tuple(map(int, line.split(","))) for line in lines]


def build_edges(points):
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        edges.append(((x1, y1), (x2, y2)))
    return edges


def point_inside(px, py, edges):
    # Ray casting to the right
    crossings = 0
    for (x1, y1), (x2, y2) in edges:
        if y1 == y2:
            continue  # horizontal edge
        if py < min(y1, y2) or py >= max(y1, y2):
            continue
        x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
        if x_int > px:
            crossings += 1
    return crossings % 2 == 1


def day9_part1(lines):
    points = parse_points(lines)
    best = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        best = max(best, area)
    return best

from collections import deque
from itertools import combinations


def day9_part2(lines):
    points = parse_points(lines)
    
    # Coordinate compression
    xs = sorted(set(x for x, y in points))
    ys = sorted(set(y for x, y in points))
    
    # Create grid with space between points (2x-1 size for edges)
    grid = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]
    
    # Mark edges of the polygon
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        
        cx1 = xs.index(x1) * 2
        cx2 = xs.index(x2) * 2
        cy1 = ys.index(y1) * 2
        cy2 = ys.index(y2) * 2
        
        # Fill all cells along the edge
        for cx in range(min(cx1, cx2), max(cx1, cx2) + 1):
            for cy in range(min(cy1, cy2), max(cy1, cy2) + 1):
                grid[cx][cy] = 1
    
    # Flood fill from outside to mark all outside cells
    outside = set([(-1, -1)])
    queue = deque([(-1, -1)])
    
    while queue:
        tx, ty = queue.popleft()
        
        for nx, ny in [(tx - 1, ty), (tx + 1, ty), (tx, ty - 1), (tx, ty + 1)]:
            # Skip if out of expanded bounds
            if nx < -1 or ny < -1 or nx > len(grid) or ny > len(grid[0]):
                continue
            # Skip if hitting a wall (edge)
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                continue
            # Skip if already visited
            if (nx, ny) in outside:
                continue
            
            outside.add((nx, ny))
            queue.append((nx, ny))
    
    # Mark all inside cells as valid (1)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x, y) not in outside:
                grid[x][y] = 1
    
    # Build 2D prefix sum array for fast rectangle queries
    psa = [[0] * len(grid[0]) for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            left = psa[x - 1][y] if x > 0 else 0
            top = psa[x][y - 1] if y > 0 else 0
            topleft = psa[x - 1][y - 1] if x > 0 and y > 0 else 0
            psa[x][y] = left + top - topleft + grid[x][y]
    
    # Check if rectangle from (x1,y1) to (x2,y2) is all valid
    def is_valid(x1, y1, x2, y2):
        cx1 = xs.index(x1) * 2
        cx2 = xs.index(x2) * 2
        cy1 = ys.index(y1) * 2
        cy2 = ys.index(y2) * 2
        
        if cx1 > cx2:
            cx1, cx2 = cx2, cx1
        if cy1 > cy2:
            cy1, cy2 = cy2, cy1
        
        # Query rectangle sum using prefix sum
        left = psa[cx1 - 1][cy2] if cx1 > 0 else 0
        top = psa[cx2][cy1 - 1] if cy1 > 0 else 0
        topleft = psa[cx1 - 1][cy1 - 1] if cx1 > 0 and cy1 > 0 else 0
        total = psa[cx2][cy2] - left - top + topleft
        
        # Check if all cells in rectangle are valid
        expected = (cx2 - cx1 + 1) * (cy2 - cy1 + 1)
        return total == expected
    
    # Find largest valid rectangle
    best = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        if is_valid(x1, y1, x2, y2):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            best = max(best, area)
    
    return best

# ---- Run ----
input_path = download_aoc_input(2025, 9, SESSION_COOKIE, "inputs/input09.txt")
lines = parse_lines(input_path)

print("Day 9 - Part 1:", day9_part1(lines))
print("Day 9 - Part 2:", day9_part2(lines))
