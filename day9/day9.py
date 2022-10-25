#!/usr/bin/env python3
"""
Advent of Code - Day 9
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

def generate_grid(puzzle_input):
    """
    Generates a grid from the input
    >>> generate_grid(['2199943210', '3987894921', '9856789892', '8767896789', '9899965678'])
    [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]]
    """
    grid = []
    for line in puzzle_input:
        grid.append([int(x) for x in list(line)])
    return grid


def part1(puzzle_input):
    """
    >>> part1(['2199943210', '3987894921', '9856789892', '8767896789', '9899965678'])
    15
    """
    low_points = 0
    grid = generate_grid(puzzle_input)
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            up, down, left, right = -1, -1, -1, -1
            if x > 0:
                left = grid[y][x - 1]
            if x < len(row) - 1:
                right = grid[y][x + 1]
            if y > 0:
                up = grid[y - 1][x]
            if y < len(grid) - 1:
                down = grid[y + 1][x]
            if up != -1 and point >= up:
                continue
            if down != -1 and point >= down:
                continue
            if left != -1 and point >= left:
                continue
            if right != -1 and point >= right:
                continue
            low_points += point + 1 
    return low_points


def part2(puzzle_input):
    """
    >>> part2(['2199943210', '3987894921', '9856789892', '8767896789', '9899965678'])
    1134
    """
    basins = []
    grid = generate_grid(puzzle_input)
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            up, down, left, right = -1, -1, -1, -1
            if x > 0:
                left = grid[y][x - 1]
            if x < len(row) - 1:
                right = grid[y][x + 1]
            if y > 0:
                up = grid[y - 1][x]
            if y < len(grid) - 1:
                down = grid[y + 1][x]
            if up != -1 and point >= up:
                continue
            if down != -1 and point >= down:
                continue
            if left != -1 and point >= left:
                continue
            if right != -1 and point >= right:
                continue
    return basins 


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
