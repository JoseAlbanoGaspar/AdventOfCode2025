import re
import z3
from input_reader import download_aoc_input, parse_lines


def day10_part2(lines):
    total = 0
    
    for line in lines:
        # Parse the line
        match = re.match(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$", line.strip())
        _, buttons, joltages = match.groups()
        
        # Parse buttons - each button is a set of counter indices it affects
        buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split()]
        
        # Parse target joltage values
        joltages = list(map(int, joltages.split(",")))
        
        # Create Z3 optimizer
        o = z3.Optimize()
        
        # Create integer variables for number of presses per button
        vars = [z3.Int(f"n{i}") for i in range(len(buttons))]
        
        # Constraint: each button must be pressed a non-negative number of times
        for var in vars:
            o.add(var >= 0)
        
        # Constraint: for each counter, the sum of presses must equal target joltage
        for i, joltage in enumerate(joltages):
            equation = 0
            for b, button in enumerate(buttons):
                if i in button:  # if this button affects counter i
                    equation += vars[b]
            o.add(equation == joltage)
        
        # Minimize total number of button presses
        o.minimize(sum(vars))
        
        # Solve and extract result
        o.check()
        total += o.model().eval(sum(vars)).as_long()
    
    return total


# ---- Run ----
input_path = download_aoc_input(2025, 10, SESSION_COOKIE, "inputs/input10.txt")
lines = parse_lines(input_path)

print("Day 10 Part 2:", day10_part2(lines))