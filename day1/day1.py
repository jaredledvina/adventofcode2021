#!/usr/bin/env python3

from itertools import islice

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
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
    larger = 0
    result = tuple(islice(puzzle_input, 3))
    previous = False
    for elem in puzzle_input:
        result = result[1:] + (elem,)
        current = sum(result)
        if previous:
            if previous < current:
                larger += 1
        previous = current
    return larger


def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
