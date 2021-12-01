#!/usr/bin/env python3

def read_input():
    with open('input.txt') as f:
        puzzle_input = f.read().splitlines()
    puzzle_input = [int(entry) for entry in puzzle_input]
    return puzzle_input

def part1(puzzle_input):
    """
    >>> part1()
    """
    pass


def part2(puzzle_input):
    """
    >>> part2()
    """
    pass


def main():
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
