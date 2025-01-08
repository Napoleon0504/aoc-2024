import re


# Clean up the corrupted file and fin the sum of all multiplications
def main():    
    # Import file
    mul_sum1 = addition1()
    mul_sum2 = addition2()
    print("Part1: ", mul_sum1)
    print("Part2: ", mul_sum2)


def addition1():
    with open("corrupted.txt", 'r') as f:
        mem = f.read()
    matches1 = re.findall(r'mul\((\d+),(\d+)\)',mem)
    sum_mul = 0
    for x,y in matches1:
        sum_mul += int(x) * int(y)
    return sum_mul

def addition2():
    with open("corrupted.txt", 'r') as f:
        mem = f.read()
    do_sum = True
    mul_sum = 0
    for i in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)',mem):
        # Check if the mul is not right after the do or don't
        if i[0] == 'do()':
            do_sum = True
            continue
        elif i[0] == 'don\'t()':
            do_sum = False
            continue
        else:
            # Check if skip: 
            if do_sum:    
                mul_sum += int(i[1]) * int(i[2])
    return mul_sum

main()
