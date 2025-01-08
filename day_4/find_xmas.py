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
    pass

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


print(find_vertical_pattern())
print(find_horizontal_pattern())