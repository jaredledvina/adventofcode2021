#!/usr/bin/env python3
"""
Advent of Code - Day 2
"""
import os

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    return puzzle_input

def part1(puzzle_input):
    """
    >>> part1(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
    150
    """
    horizontal = 0
    vertical = 0
    for movement in puzzle_input:
        direction, distance = movement.split()
        if direction == 'forward':
            horizontal += int(distance)
        elif direction == 'up':
            vertical -= int(distance)
        elif direction == 'down':
            vertical += int(distance)
    return horizontal * vertical


def part2(puzzle_input):
    """
    >>> part2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
    900
    """
    horizontal = 0
    vertical = 0
    aim = 0
    for movement in puzzle_input:
        direction, distance = movement.split()
        if direction == 'forward':
            horizontal += int(distance)
            vertical += aim * int(distance)
        elif direction == 'up':
            aim -= int(distance)
        elif direction == 'down':
            aim += int(distance)
    return horizontal * vertical


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
