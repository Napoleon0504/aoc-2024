import re


# Clean up the corrupted file and fin the sum of all multiplications
def main():    
    # Import file
    mul_sum1 = addition1()
    mul_sum2 = addition2()
    print("Part1: ", mul_sum1)
    print("Part2: ", mul_sum2)

def addition(s):
    #2 find all instances of the 'mul where there is only (number,number) in that order
    # else it is false
    # Filter everything into a list
    all_mul = s.split("mul")
    do_or_dont = True
    skip = False
    return_numb = 0
    for i in all_mul:
        if not do_or_dont:
            skip = True
        # For next round
        if "do()" in i:
            do_or_dont = True
        if "don't()" in i:
            do_or_dont = False
        #find index of first (
        first_bracket_i = i.find("(")
        if first_bracket_i != 0:
            # The bracket is not right after the mul
            continue
        #find index of first )
        last_bracket_i = i.find(")")
        # Extract everything inbetween
        res = i[first_bracket_i + 1: last_bracket_i]
        # Check if rs has only num and ,
        pattern = r'^[0-9,]+$'
        if not re.match(pattern, res):
            # Faulty
            continue
        else:
            # Correct
            if skip:
                # Skip this one and go to the next one
                continue
            numb = res.split(",")
            # Check if there are 2 numbers
            if len(numb) != 2:
                continue
            # Sum all multiplications
            else:
                # Maka all numb into intigers
                numb = [int(i) for i in numb]
                print(numb)
                line_mul = mul(numb[0],numb[1])
                return_numb += line_mul
                
    return return_numb
                
def mul(a, b):
    return a * b

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
