#!/usr/bin/env python3
"""
Advent of Code - Day 4
"""
import os

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    puzzle_input = [line for line in puzzle_input if line.strip()]
    return puzzle_input


def parse_bingo(puzzle_input, board_height):
    """
    >>> parse_bingo(['1,1,1,1,1', '1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25'], 4)
    ([1, 1, 1, 1, 1], [[[[1, False], [2, False], [3, False], [4, False], [5, False]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]], [[21, False], [22, False], [23, False], [24, False], [25, False]]]])
    >>> parse_bingo(['1,1,1,1,1', '1 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25', '5 4 3 2 1', '10 9 8 7 6', '15 14 13 12 11', '20 19 18 17 16', '25 24 23 22 21'], 4)
    ([1, 1, 1, 1, 1], [[[[1, False], [2, False], [3, False], [4, False], [5, False]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]], [[21, False], [22, False], [23, False], [24, False], [25, False]]], [[[5, False], [4, False], [3, False], [2, False], [1, False]], [[10, False], [9, False], [8, False], [7, False], [6, False]], [[15, False], [14, False], [13, False], [12, False], [11, False]], [[20, False], [19, False], [18, False], [17, False], [16, False]], [[25, False], [24, False], [23, False], [22, False], [21, False]]]])
    """
    drawn_numbers = [int(number) for number in puzzle_input[0].split(',')]
    puzzle_input = puzzle_input[1:]
    all_boards = [[[]]]
    current_board_row = 0
    current_board = 0
    for line in puzzle_input:
        try:
            all_boards[current_board]
        except IndexError:
            all_boards.append([])
        for number in line.split():
            try:
                all_boards[current_board][current_board_row]
            except IndexError:
                all_boards[current_board].append([])
            all_boards[current_board][current_board_row].append([int(number), False])
        if current_board_row == board_height:
            current_board += 1
            current_board_row = 0
        else:
            current_board_row += 1
    return drawn_numbers, all_boards


def mark_drawn_numbers(drawn_number, all_boards):
    """
    >>> mark_drawn_numbers(1, [[[[1, False], [2, False], [3, False], [4, False], [5, False]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]]]])
    [[[[1, True], [2, False], [3, False], [4, False], [5, False]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]]]]
    """
    for current_board, board in enumerate(all_boards):
        for current_row, row in enumerate(board):
            for current_number, number in enumerate(row):
                if number[0] == drawn_number:
                    all_boards[current_board][current_row][current_number][1] = True
    return all_boards


def check_for_winner(all_boards):
    """
    >>> check_for_winner([[[[1, False], [2, False], [3, False], [4, False], [5, False]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]]]])
    (False, None, None)
    >>> check_for_winner([[[[1, True], [2, True], [3, True], [4, True], [5, True]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]]]])
    (True, [[[1, True], [2, True], [3, True], [4, True], [5, True]], [[6, False], [7, False], [8, False], [9, False], [10, False]], [[11, False], [12, False], [13, False], [14, False], [15, False]], [[16, False], [17, False], [18, False], [19, False], [20, False]]], 0)
    >>> check_for_winner([[[[1, False], [2, True], [3, False], [4, False], [5, False]], [[6, False], [7, True], [8, False], [9, False], [10, False]], [[11, False], [12, True], [13, False], [14, False], [15, False]], [[16, False], [17, True], [18, False], [19, False], [20, False]]]])
    (True, [[[1, False], [2, True], [3, False], [4, False], [5, False]], [[6, False], [7, True], [8, False], [9, False], [10, False]], [[11, False], [12, True], [13, False], [14, False], [15, False]], [[16, False], [17, True], [18, False], [19, False], [20, False]]], 0)
    >>> check_for_winner([[[[1, True], [2, True], [3, True], [4, True], [5, True]], [[6, True], [7, True], [8, True], [9, True], [10, True]], [[11, True], [12, True], [13, True], [14, True], [15, True]], [[16, True], [17, True], [18, True], [19, True], [20, True]]]])
    (True, [[[1, True], [2, True], [3, True], [4, True], [5, True]], [[6, True], [7, True], [8, True], [9, True], [10, True]], [[11, True], [12, True], [13, True], [14, True], [15, True]], [[16, True], [17, True], [18, True], [19, True], [20, True]]], 0)
    """
    for board_id, board in enumerate(all_boards):
        winning_board = False
        # winning row
        for row in board:
            if all([number[1] for number in row]):
                winning_board = True
        #winning column
        for column in range(len(board[0])):
            if all([row[column][1] for row in board]):
                winning_board = True
        if winning_board:
            return True, board, board_id
    return False, None, None


def part1(puzzle_input):
    """
    >>> part1(['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1', '22 13 17 11  0', '8  2 23  4 24', '21  9 14 16  7', '6 10  3 18  5', '1 12 20 15 19', '3 15  0  2 22', '9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4', '14 21 16 12  6', '14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', '2  0 12  3  7'] )
    4512
    """
    drawn_numbers, all_boards = parse_bingo(puzzle_input, 4)
    for drawn_number in drawn_numbers:
        all_boards = mark_drawn_numbers(drawn_number, all_boards)
        winner, winning_board, _ = check_for_winner(all_boards)
        if winner:
            undrawn_numbers = []
            for row in winning_board:
                for number in row:
                    if not number[1]:
                        undrawn_numbers.append(number[0])
            return sum(undrawn_numbers) * drawn_number


def get_last_winner(drawn_numbers, all_boards):
    """
    >>> get_last_winner([7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1], [[[[22, False], [13, False], [17, False], [11, False], [0, False]], [[8, False], [2, False], [23, False], [4, False], [24, False]], [[21, False], [9, False], [14, False], [16, False], [7, False]], [[6, False], [10, False], [3, False], [18, False], [5, False]], [[1, False], [12, False], [20, False], [15, False], [19, False]]], [[[3, False], [15, False], [0, False], [2, False], [22, False]], [[9, False], [18, False], [13, False], [17, False], [5, False]], [[19, False], [8, False], [7, False], [25, False], [23, False]], [[20, False], [11, False], [10, False], [24, False], [4, False]], [[14, False], [21, False], [16, False], [12, False], [6, False]]], [[[14, False], [21, False], [17, False], [24, False], [4, False]], [[10, False], [16, False], [15, False], [9, False], [19, False]], [[18, False], [8, False], [23, False], [26, False], [20, False]], [[22, False], [11, False], [13, False], [6, False], [5, False]], [[2, False], [0, False], [12, False], [3, False], [7, False]]]])
    (13, [[[3, False], [15, False], [0, True], [2, True], [22, False]], [[9, True], [18, False], [13, True], [17, True], [5, True]], [[19, False], [8, False], [7, True], [25, False], [23, True]], [[20, False], [11, True], [10, True], [24, True], [4, True]], [[14, True], [21, True], [16, True], [12, False], [6, False]]])
    """
    for drawn_number in drawn_numbers:
        more_winners = True
        all_boards = mark_drawn_numbers(drawn_number, all_boards)
        while more_winners:
            winner, winning_board, winning_board_index = check_for_winner(all_boards)
            if winner:
                if len(all_boards) == 1:
                    return drawn_number, winning_board
                else:
                    all_boards.pop(winning_board_index)
            else:
                more_winners = False


def part2(puzzle_input):
    """
    >>> part2(['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1', '22 13 17 11  0', '8  2 23  4 24', '21  9 14 16  7', '6 10  3 18  5', '1 12 20 15 19', '3 15  0  2 22', '9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4', '14 21 16 12  6', '14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', '2  0 12  3  7'] )
    1924
    """
    # 1735 / 5 = 347 / 2 = 173.5
    drawn_numbers, all_boards = parse_bingo(puzzle_input, 4)
    last_number, last_board = get_last_winner(drawn_numbers, all_boards)
    if last_board:
        undrawn_numbers = []
        for row in last_board:
            for number in row:
                if not number[1]:
                    undrawn_numbers.append(number[0])
        return sum(undrawn_numbers) * last_number
    print("No winner found")
    return None


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
