# Task: Check every line if it is safe
# Condtitions:
# - all must decrese or all must increase
import numbers
import math

def main():
    # Import the lists
    f = open("safety_list.txt", "r")
    all_num = f.read()

    # Seperate every line
    lines = all_num.split("\n")
    # Check if every line is compliant
    # All lines that are safe
    compl_lines = []
    safe_count = 0
    for line in lines:
        # Split into list
        line = line.split()
        # Make everything int
        int_line = [int(i) for i in line]
        # Check in positive dir
        if check(int_line, False) == True:
            compl_lines.append(int_line)
            print(int_line, "safe")
            safe_count += 1
        # Check in negative direction
        else: 
            reversed_line = int_line.copy()
            reversed_line.reverse()
            if check(reversed_line, False) == True:
                print(int_line, "safe reversed")
                compl_lines.append(int_line)
                safe_count += 1
            else:
                print(int_line, "Faulty")

    print(len(compl_lines))
    print(safe_count)

def check(a, fault):
    line = a.copy()
    """
    # check dir
    if line[1] - line[0] < 0: #Negative
        #Change to as if it were positive
        line.reverse()
    """
    # Loop thorugh every elem and find the difference
    dif_value = line[1] - line[0] # Difference for line[1]
    # Look at the difference behind line[i]
    for i in range(1, len(line)):
        # If line[i] safe 
        if dif_value <= 3 and dif_value >= 1:
            # Check if the last
            if i == len(line) - 1:
                # If last, return safe
                return True
            # dif_value for line[i+1]
            dif_value =  line[i+1] - line[i]
        # Not line[i] safe
        else:   
            # Would it work if removed?
            # Try to remove the term and redo the process
            # If first value is problem
            line = line.copy()
            if fault == False and i == 1:
                # Check if it would have worked to remove first value
                test_line = line.copy()
                del test_line[0]
                if check(test_line, True) == True:
                    return True
            # check if removing the last value works hello
            
            #If its the last value
            if fault == False and i == len(line) - 1:
                return True
            
            if fault == False:
                del line[i]
                return check(line, True)
            
            else:
                return False
           
      
main()

# 1,6,7,8,9

# TODO
#get a line
# if line:
# - Increase all out or decrease all out
# - change with between 1 and 3
# Safe

# diff value 

# Fault alternatives
# 