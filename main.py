#!/usr/bin/python3

# imports random module
import random

# Create a function or class to print a matrix of size x * x.
# Fill it with y mines.
# Mark mines as 'x' and mark empty cells as '0'.
#
# e.g. a possible result of minesweeper_generator(size=4, mines=5) would be:
# [
#   ['0', '0', 'x', 'x'],
#   ['x', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', 'x', '0', 'x']
# ]


def minesweeper_generator(size, mines):
    if size*size < mines:
        print("To much mines!")
        return []

    mines_list = []
    rand_nums = 0
    while rand_nums < mines:
        num = random.randint(1, size*size)
        if num in mines_list:
            print("Position occupied")
        else:
            mines_list.append(num)
            rand_nums = rand_nums + 1
            print(num)

    num_rows = 0
    num_lines = 0
    temp_list = []
    output = []
    while num_rows < size:
        while num_lines < size:
            num_lines = num_lines + 1

            #index = num_rows+1 * num_lines

            #index = index+(num_rows+size)
            index = num_rows * size + num_lines

            print(f"1: {num_rows+1}")
            print(f"2: {num_lines}")
            print(f"Index: {index}")
            if index in mines_list:
                temp_list.append("X")
            else:
                temp_list.append("0")

        output.append(temp_list)
        temp_list = []
        num_lines = 0
        num_rows = num_rows + 1

    return output


if __name__ == "__main__":
    for line in minesweeper_generator(4, 17):
        print(line)
