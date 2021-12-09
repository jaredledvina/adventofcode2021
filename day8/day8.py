#!/usr/bin/env python3
"""
Advent of Code - Day 8
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
    >>> part1(['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe', 'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc', 'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg', 'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb', 'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea', 'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb', 'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe', 'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef', 'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb', 'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'])
    26
    """
    all_digits = []
    for line in puzzle_input:
        _, four_digit_output_values = line.split(' | ')
        for digit in four_digit_output_values.split():
            all_digits.append(digit)
    return(len([digit for digit in all_digits if len(digit) in [2,3,4,7]]))


def evaluate_state(state):
    """
    >>> evaluate_state('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe')
    8394
    """
    digit_mapping = [x for x in range(10)]
    unique_signal_patterns, four_digit_output_values = state.split(' | ')
    for digit in unique_signal_patterns.split():
        num = ''
        if len(digit) == 2:
            num = '1'
        elif len(digit) == 3:
            num = '7'
        elif len(digit) == 4:
            num = '4'
        elif len(digit) == 7:
            num = '8'
        if num:
            digit_mapping[int(num)] = digit

    for digit in unique_signal_patterns.split():
        num = ''
        if len(digit) == 6: 
            remaining = ''.join([position for position in digit if position not in digit_mapping[1]])
            if len(remaining) == 4:
                remaining = ''.join([position for position in remaining if position not in digit_mapping[4]])
                if len(remaining) == 3:
                    num = '0'
                elif len(remaining) == 2:
                    num = '9'
                else:
                    print('FUCK 1:', digit, remaining)
            elif len(remaining) == 5:
                num = '6'
            else:
                print('FUCK 2:', digit, 'remaining', remaining)
        elif len(digit) == 5:
            remaining = ''.join([position for position in digit if position not in digit_mapping[7]])
            if len(remaining) == 2:
                num = '3'
            elif len(remaining) == 3:
                remaining = ''.join([position for position in remaining if position not in digit_mapping[4]])
                if len(remaining) == 2:
                    num = '2' 
                elif len(remaining) == 1:
                    num = '5'
                else:
                    print('FUCK 3:', digit, 'remaining', remaining)
            else:
                print('FUCK 4:', digit)
        if num:
            digit_mapping[int(num)] = digit
    answer = ''
    for four_bit in four_digit_output_values.split():
        for index, digit in enumerate(digit_mapping):   
            if ''.join(sorted(four_bit)) == ''.join(sorted(digit)):
                answer += str(index)
    return(int(answer))


        


def part2(puzzle_input):
    """
    >>> part2(['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe', 'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc', 'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg', 'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb', 'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea', 'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb', 'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe', 'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef', 'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb', 'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'])
    61229
    """
    digit_sum = 0
    for state in puzzle_input:
        digit_sum += evaluate_state(state)
    return digit_sum



def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == '__main__':
    main()
