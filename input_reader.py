import requests
from pathlib import Path

def download_aoc_input(
    year: int,
    day: int,
    session_cookie: str,
    output_path: str | Path,
):
    
    output_path = Path(output_path)

    # Skip download if file already exists
    if output_path.exists():
        print(f"Input already exists: {output_path}")
        return output_path
    
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "github.com/yourname/aoc-scripts by you@example.com",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    Path(output_path).write_text(response.text)

    return output_path


from pathlib import Path
from typing import Callable

def parse_lines(
    input_path: str | Path,
    transform: Callable[[str], object] | None = None,
    strip: bool = True,
    skip_empty: bool = True,  # new parameter
) -> list:
    """
    Read a file line by line and optionally transform each line.

    :param input_path: Path to input file
    :param transform: Function applied to each line (e.g. int, str.split)
    :param strip: Whether to strip whitespace/newlines
    :param skip_empty: Whether to skip empty lines
    :return: List of parsed lines
    """
    input_path = Path(input_path)
    results = []

    with input_path.open() as f:
        for line in f:
            if strip:
                line = line.strip()

            if skip_empty and not line:
                continue  # skip empty lines if requested

            results.append(transform(line) if transform else line)

    return results



