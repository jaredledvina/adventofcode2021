#!/usr/bin/env python3
"""
Advent of Code - Day 1
"""
import os


def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    puzzle_input = [int(entry) for entry in puzzle_input]
    return puzzle_input

def part1(puzzle_input):
    """
    >>> part1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    7
    """
    larger = 0
    previous = False
    for current in puzzle_input:
        if previous:
            if int(previous) < int(current):
                larger += 1
        previous = current
    return larger


def part2(puzzle_input):
    """
    >>> part2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    5
    """
    first = 0
    last = 3
    larger = 0
    while last < len(puzzle_input):
        if puzzle_input[first] < puzzle_input[last]:
            larger += 1
        first += 1
        last += 1
    return larger


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
