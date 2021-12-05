#!/usr/bin/env python3
"""
Advent of Code - Day 5
"""
import os
from collections import defaultdict

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    return puzzle_input


def parse_map(puzzle_input):
    vents = []
    for line in puzzle_input:
        start, end = line.split(' -> ')
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        vents.append((int(start_x), int(start_y), int(end_x), int(end_y)))
    return vents

def map_vents(vents, map_diagonals=False):
    map = defaultdict(lambda: defaultdict(int))
    for vent in vents:
        x1, y1, x2, y2 = vent[0], vent[1], vent[2], vent[3] 
        if x1 != x2 and y1 != y2:
            if map_diagonals: 
                marking_x = x1
                marking_y = y1
                while marking_x != x2 and marking_y != y2:
                    map[marking_x][marking_y] += 1
                    if marking_x < x2:
                        marking_x += 1
                    if marking_x > x2:
                        marking_x -= 1
                    if marking_y < y2:
                        marking_y += 1
                    if marking_y > y2:
                        marking_y -= 1
                map[x2][y2] += 1
        else:
            start_x = min(x1, x2)
            end_x = max(x1, x2)
            for x in range(start_x, end_x+1):
                start_y = min(y1, y2)
                end_y = max(y1, y2)
                for y in range(start_y, end_y+1):
                    map[x][y] += 1
    return map


def part1(puzzle_input):
    """
    >>> part1(['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2'])
    5
    """
    vents = parse_map(puzzle_input)
    map = map_vents(vents)
    dangerous_spots = 0
    for x in map:
        for y in map[x]:
            if map[x][y] >= 2:
                dangerous_spots += 1
    return dangerous_spots


def part2(puzzle_input):
    """
    >>> part2(['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2'])
    12
    """
    vents = parse_map(puzzle_input)
    map = map_vents(vents, map_diagonals=True)
    dangerous_spots = 0
    for x in map:
        for y in map[x]:
            if map[x][y] >= 2:
                dangerous_spots += 1
    return dangerous_spots


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
