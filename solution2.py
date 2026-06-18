from pathlib import Path
from config import INPUT_FILE


def is_invalid_id(number: int) -> bool:
    """
    Check if an ID is made of a sequence of digits repeated
    at least twice.

    Examples:
        55 -> True              (5 repeated 2 times)
        6464 -> True            (64 repeated 2 times)
        123123 -> True          (123 repeated 2 times)
        999 -> True             (9 repeated 3 times)
        123123123 -> True       (123 repeated 3 times)
        1212121212 -> True      (12 repeated 5 times)
        1234 -> False           (no repeating pattern)
    """
    s = str(number)
    length = len(s)

    # Try every possible size of the repeating sequence
    # Example: 123123 -> possible patterns: 1, 12, 123
    for size in range(1, length // 2 + 1):

        # The string length must be divisible by the pattern size
        # Example: 123123 (length 6) can be split into:
        # 1, 12, or 123, but not 2 digits like 12312
        if length % size != 0:
            continue

        # Extract the candidate repeating pattern
        pattern = s[:size]

        # Check if repeating the pattern recreates the full ID
        repetitions = length // size

        if pattern * repetitions == s:
            return True

    return False


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
