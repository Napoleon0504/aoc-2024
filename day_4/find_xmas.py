# Find xmas:
# horizontal forwards
# horizontal backwards
# vertical up
# vertical down
# diagonal right down
# diagonal left down
# diagonal right up
# diagonal left up
# overlapping other words?

import textwrap
import re

def main():
    total_lenght = find_diagonal_pattern() + find_horizontal_pattern() + find_vertical_pattern()
    print(total_lenght)
    

# Find patterns horizontally 
def find_horizontal_pattern():
    length = 0
    with open("xmas.txt", 'r') as f:
        for line in f.readlines():
            # Find the pattern xmas or samx
            matches1 = re.findall(r'XMAS|SAMX',line)
            length += len(matches1)
    f.close()
    return length

def find_vertical_pattern():
    length = 0
    with open("xmas.txt", 'r') as f:
        text = f.read()

    list_of_strings = [''.join(chars) for chars in zip(*text.splitlines())]

    for line in list_of_strings:
        matches1 = re.findall(r'XMAS|SAMX',line)
        length += len(matches1)
    return length

def find_diagonal_pattern():
    length = 0
    with open("xmas.txt", 'r') as f:
        text = f.read()
    lines = text.split('\n')
    # The text file is 140 x 140 charcters
    dia_lines = []
    # Upper and lower triangle
    for hor_start in range(len(lines[0])):
        current_diagonal1 = []
        current_diagonal2 = []
        hor_line = hor_start
        ver_line = 0
        while True:
            if hor_line < 140 and ver_line < 140:
                if hor_start == 0:
                    current_diagonal1.append(lines[ver_line][hor_line])
                else:
                    current_diagonal1.append(lines[ver_line][hor_line])
                    current_diagonal2.append(lines[hor_line][ver_line])
                ver_line += 1
                hor_line += 1
            else:
                break
        dia_lines.append(current_diagonal1)
        dia_lines.append(current_diagonal2)

    # TODO
    # diagonal vänster 
    # Join lists into strings
    for i in range(len(dia_lines)):
        dia_lines[i] = ''.join(dia_lines[i])
        print(dia_lines[i])
    f.close()

    for line in dia_lines:
        matches1 = re.findall(r'XMAS|SAMX',line)
        length += len(matches1)
    print(length)
    return length


main()