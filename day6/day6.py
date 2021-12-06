#!/usr/bin/env python3
"""
Advent of Code - Day 6
"""
import os

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    puzzle_input = [int(fish) for line in puzzle_input for fish in line.split(',')]
    return puzzle_input


def sunrise_sunset(school, days):
    """
    >>> sunrise_sunset([3,4,3,1,2])
    [2, 3, 2, 0, 1]
    >>> sunrise_sunset([2,3,2,0,1])
    [1, 2, 1, 6, 0, 8]
    """
    current_schools = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    # Initial fish
    for fish in school:
        current_schools[fish] += 1

    for _ in range(days):
        todays_school = current_schools.copy()
        for fish_status in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            todays_fish_count = todays_school[fish_status]
            if fish_status == 0:
                zero_fish = todays_fish_count
                current_schools[8] = zero_fish
            else:
                current_schools[fish_status - 1] = todays_fish_count
        current_schools[6] += zero_fish
        todays_school = current_schools.copy()
    return current_schools

def part1(puzzle_input, max_days=80):
    """
    >>> part1([3,4,3,1,2], 18)
    26
    >>> part1([3,4,3,1,2])
    5934
    """
    final_fish = sunrise_sunset(puzzle_input, max_days)
    return sum(final_fish.values())


def part2(puzzle_input, max_days=256):
    """
    >>> part2([3,4,3,1,2])
    26984457539
    """
    final_fish = sunrise_sunset(puzzle_input, max_days)
    return sum(final_fish.values())


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
