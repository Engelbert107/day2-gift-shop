# Advent of Code 2025 - Day 2: Gift Shop 

## Problem Description

The gift shop database contains invalid product IDs created by an Elf.  
An invalid ID is a number made by repeating the same sequence of digits exactly twice.

Examples:

- `55` → `5` repeated twice
- `6464` → `64` repeated twice
- `123123` → `123` repeated twice

Numbers with leading zeros are not considered valid IDs.

The input consists of several ID ranges separated by commas:



The goal is to find all invalid IDs inside these ranges and return their total sum.

---

## Example

### Input

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

## Solution Approach

For each ID in every provided range:

1. Convert the ID into a string.
2. Split the string into two equal halves.
3. Check if both halves are identical.
4. If they match, the ID is invalid and is added to the total.

Example: 123123
- First half: 123
- Second half: 123
- => Invalid ID