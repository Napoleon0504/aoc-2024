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

import re

def main():
    txt = "xmas.txt"
    diagonal = find_diagonal_pattern(140, txt)
    horizontal = find_horizontal_pattern(txt)
    vertical = find_vertical_pattern(txt)
    total_lenght = diagonal + horizontal + vertical
    print("diagonal",diagonal)
    print("horizontal", horizontal)
    print("vertical", vertical)
    print("total",total_lenght)
    

# Find patterns horizontally 
def find_horizontal_pattern(txt):
    length = 0
    with open(txt, 'r') as f:
        for line in f.readlines():
            # Find the pattern xmas or samx
            #print(line)
            matches1 = re.findall(r'SAMX',line)
            matches2 = re.findall(r'XMAS',line)
            #print(len(matches1) + len(matches2))
            length += len(matches1) + len(matches2)
    f.close()
    return length

def find_vertical_pattern(txt):
    length = 0
    with open(txt, 'r') as f:
        text = f.read()

    list_of_strings = [''.join(chars) for chars in zip(*text.splitlines())]

    for line in list_of_strings:
        #print(line)
        matches1 = re.findall(r'XMAS',line)
        matches2 = re.findall(r'SAMX',line)
        #print(len(matches1) + len(matches2))
        length += len(matches1) + len(matches2)
    return length

def find_diagonal_pattern(l, txt):
    length = 0
    with open(txt, 'r') as f:
        text = f.read()
    lines = text.split('\n')
    # The text file is 140 x 140 charcters
    dia_lines = []
    # Upper and lower triangle
    for hor_start in range(len(lines[0])):
        # temporary lists
        current_diagonal1_right = []
        current_diagonal2_right = []
        current_diagonal1_left = []
        current_diagonal2_left = []
        hor_line = hor_start
        ver_line = 0
        while True:
            if hor_line < l and ver_line < l:
                if hor_start == 0:
                    # Mitt diagonal höger
                    current_diagonal1_right.append(lines[ver_line][hor_line])
                    # Mitt diagonal vänster
                    current_diagonal1_left.append(lines[ver_line][l - 1 - hor_line])
                else:
                    # Upper triangle right diagonal
                    current_diagonal1_right.append(lines[ver_line][hor_line])
                    # Lower triangle right diagonal
                    current_diagonal2_right.append(lines[hor_line][ver_line])
                    # Upper triangle left diagonal
                    current_diagonal1_left.append(lines[ver_line][l - 1 - hor_line])
                    # Lower triangle left diagonal
                    current_diagonal2_left.append(lines[l - 1 - ver_line][hor_line])
                ver_line += 1
                hor_line += 1
            else:
                break
        dia_lines.append(current_diagonal1_right)
        dia_lines.append(current_diagonal2_right)
        dia_lines.append(current_diagonal1_left)
        dia_lines.append(current_diagonal2_left)

    # Join lists into strings
    for i in range(len(dia_lines)):
        dia_lines[i] = ''.join(dia_lines[i])
    f.close()

    # Count instances of XMAS
    for line in dia_lines:
        #print(line)
        matches1 = re.findall(r'XMAS',line)
        matches2 = re.findall(r'SAMX',line)
        #print(len(matches1) + len(matches2))
        length += len(matches1) + len(matches2)
    
    return length


main()