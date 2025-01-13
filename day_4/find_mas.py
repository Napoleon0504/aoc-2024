import re

def main():
    print(a_index())

def a_index():
    # Read file
    txt = "xmas.txt"
    with open(txt, 'r') as f:
        # Row
        s = f.read()
    # Split rows into list
    row_list = s.split("\n")
    count = 0
    for line_index in range(1, len(row_list) - 1):
        # Index
        matches = re.finditer(r'A',row_list[line_index])
        for match in matches:
            if match.start() > 0 and match.start() < len(row_list[line_index]) - 1:
                # Find if the indexes around will match the pattern
                row_index = match.start()
                right_down = row_list[line_index - 1][row_index - 1] + row_list[line_index][row_index] + row_list[line_index + 1][row_index + 1]
                left_down = row_list[line_index - 1][row_index + 1] + row_list[line_index][row_index] + row_list[line_index + 1][row_index - 1]
                if right_down == "MAS" or right_down == "SAM":
                    if left_down == "MAS" or left_down == "SAM":
                        print(f"row: {line_index}, index: {row_index}")
                        print(f"right_down: {right_down}")
                        print(f"left_down: {left_down}\n")
                        count += 1
    return count
                                  
main()