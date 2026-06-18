# Advent of Code 2025 - Day 2: Gift Shop 

## Problem Description

The gift shop database contains invalid product IDs created by an Elf.

An invalid ID is a number made by repeating the same sequence of digits **at least twice**.

Examples:

- `55` → `5` repeated 2 times
- `6464` → `64` repeated 2 times
- `123123` → `123` repeated 2 times
- `999` → `9` repeated 3 times
- `123123123` → `123` repeated 3 times
- `1212121212` → `12` repeated 5 times

Numbers with leading zeros are not considered valid IDs.

The input consists of several ID ranges separated by commas: stard-end, start-end, ...


The goal is to find all invalid IDs inside these ranges and return their total sum.

---

# Part One

## Rule

An invalid ID is a sequence of digits repeated **exactly twice**.

Examples:
55 = 5 + 5
6464 = 64 + 64
123123 = 123 + 123



---

# Part Two

## Updated Rule

The Elf was using more repeating patterns.

An ID is now invalid if it contains a sequence of digits repeated **two or more times**.

Examples:
999 = 9 repeated 3 times
123123123 = 123 repeated 3 times
1212121212 = 12 repeated 5 times
1111111 = 1 repeated 7 times


The pattern can be any length as long as it repeats completely.

---

# Example (Part One)

## Input

30-35,88-90,444-450,9999-10005,567567-567568

### Analysis 

| Range | Invalid IDs Found | Sum |
|---|---|---|
| `30-35` | `33` | 33 |
| `88-90` | `88` | 88 |
| `444-450` | None | 0 |
| `9999-10005` | `9999` | 9999 |
| `567567-567568` | `567567` | 567567 |

### Calculation

33 + 88 + 9999 + 567567 = 577687

### Output 

Answer: 577687

## Solution Approach (Part One)

For each ID in every provided range:

1. Convert the ID into a string.
2. Split the string into two equal halves.
3. Check if both halves are identical.
4. If they match, the ID is invalid and is added to the total.

Example: 123123

- First half: 123
- Second half: 123
- => Invalid ID


# Example (Part Two)

## Input

8-15,90-100,444-450,123123-123130,121212-121215

### Analysis 

| Range | Invalid IDs Found | Sum |
|---|---|---|
| `8-15` | `11` | 11 |
| `90-100` | `99` | 99 |
| `444-450` | None | 0 |
| `123123-123130` | `123123` | 123123 |
| `121212-121215` | `121212` | 121212 |

### Calculation

11 + 99 + 123123 + 121212 = 244889

### Output 

Answer: 244889


# Solution Approach (Part Two)

For each ID in every provided range:

1. Convert the ID into a string.
2. Try every possible repeating sequence length.
3. Check if the entire ID can be created by repeating that sequence.
4. If a valid repeating pattern is found, add the ID to the total.

Example: 123123123

- patten: 123
- repetitions: 3
- => Invalid ID



