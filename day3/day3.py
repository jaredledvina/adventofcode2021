#!/usr/bin/env python3
"""
Advent of Code - Day 3
"""
import os
from collections import Counter

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
    >>> part1(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    198
    """
    max_runs = len(puzzle_input[0])
    current_run = 0
    current_readings = []
    gamma = ''
    epsilon = ''
    while current_run < max_runs:
        for entry in puzzle_input:
            current_readings.append(entry[current_run])
        gamma = gamma + str(Counter(current_readings).most_common()[0][0])
        epsilon = epsilon + str(Counter(current_readings).most_common()[-1][0])

        current_readings = []
        current_run += 1
    return int(gamma, 2) * int(epsilon, 2)


def part2(puzzle_input):
    """
    >>> part2(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    230
    """
    current_co2_sensor_readings = []
    current_o2_sensor_readings = []
    current_o2_column = 0
    current_co2_column = 0
    oxygen_sensor_readings = puzzle_input.copy()
    co2_sensor_readings = puzzle_input.copy()
    while max(len(oxygen_sensor_readings), len(co2_sensor_readings)) > 1:
        if len(oxygen_sensor_readings) > 1:
            for reading in oxygen_sensor_readings:
                current_o2_sensor_readings.append(reading[current_o2_column])
            commons = Counter(current_o2_sensor_readings).most_common()
            print(commons)
            if len(commons) > 1 and commons[0][1] == commons[1][1]:
                most_common = '1'
            else:
                most_common = str(commons[0][0])
            for oxygen_sensor_reading in oxygen_sensor_readings.copy():
                if oxygen_sensor_reading[current_o2_column] != most_common and len(oxygen_sensor_readings) > 1:
                    oxygen_sensor_readings.remove(oxygen_sensor_reading)
            current_o2_sensor_readings = []
            if current_o2_column < len(puzzle_input[0])-1:
                current_o2_column += 1
            else:
                current_o2_column = 0
        if len(co2_sensor_readings) > 1:
            for reading in co2_sensor_readings:
                current_co2_sensor_readings.append(reading[current_co2_column])
            commons = Counter(current_co2_sensor_readings).most_common()
            if len(commons) > 1 and  commons[0][1] == commons[1][1]:
                least_common = '0'
            else:
                least_common = str(commons[-1][0])
            for co2_sensor_reading in co2_sensor_readings.copy():
                if co2_sensor_reading[current_co2_column] != least_common and len(co2_sensor_readings) > 1:
                    co2_sensor_readings.remove(co2_sensor_reading)
            current_co2_sensor_readings = []
            if current_co2_column < len(puzzle_input[0])-1:
                current_co2_column += 1
            else:
                current_co2_column = 0
    return int(co2_sensor_readings[0], 2) * int(oxygen_sensor_readings[0], 2)





def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
