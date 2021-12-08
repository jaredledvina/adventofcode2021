#!/usr/bin/env python3
"""
Advent of Code - Day 7
"""
import os
import statistics
from collections import Counter, defaultdict

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    puzzle_input = [int(position) for line in puzzle_input for position in line.split(',')]
    return puzzle_input


def part1(puzzle_input):
    """
    >>> part1([16,1,2,0,4,2,7,1,2,14])
    37
    """
    total_fuel = 0
    median = statistics.median(puzzle_input)
    for crab in puzzle_input:
        total_fuel += abs(crab - median)
    return int(total_fuel)


def part2(puzzle_input):
    """
    >>> part2([16,1,2,0,4,2,7,1,2,14])
    168
    """
    possible_positions = defaultdict(int)
    for position in range(min(puzzle_input), max(puzzle_input) + 1):
        for crab in puzzle_input:
            number_of_steps = 0
            if crab != position:
                total_fuel = 0
                number_of_steps += abs(crab - position)
                for fuel in range(1, number_of_steps+1):
                    total_fuel += fuel
                possible_positions[position] += total_fuel
    return possible_positions[min(possible_positions, key=possible_positions.get)]



def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
