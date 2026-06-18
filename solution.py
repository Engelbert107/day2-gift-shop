from pathlib import Path
from config import INPUT_FILE


def is_invalid_id(number: int) -> bool:
    """
    Check if an ID is made of a sequence of digits repeated twice.

    Examples:
        55 -> True
        6464 -> True
        123123 -> True
        1234 -> False
    """
    s = str(number)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    return s[:half] == s[half:]


def solve(puzzle_input: str) -> int:
    """
    Find and sum all invalid IDs in the given ranges.
    """
    total = 0

    for part in puzzle_input.strip().split(","):
        start, end = map(int, part.split("-"))

        for number in range(start, end + 1):
            if is_invalid_id(number):
                total += number

    return total



if __name__ == "__main__":
    input_data = Path(INPUT_FILE).read_text().strip()

    answer = solve(input_data)

    print(f"\n Answer: {answer}\n")
