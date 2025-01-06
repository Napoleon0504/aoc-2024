# Task: Compare 2 lists in order and calculate the difference
import numbers
import math

def main():
    # Import the lists
    f = open("numbers.txt", "r")
    all_num = f.read()
    full_list1 = all_num.split()
    # List of all intigers 
    full_list2 = [int(item) for item in full_list1]

    left = []
    right = []

    # Create right and left-list 
    for i in range(0,len(full_list2),2):
        left.append(full_list2[i])
        right.append(full_list2[i + 1])

    difference = sum_li(left, right)
    simul_score = sim_score(left, right)
    print(f"sim-score: {simul_score}")

def sum_li(left, right):
    left.sort()
    right.sort()

    sum_list = []
    #substract right and left list
    for i in range(len(left)):
        sub = abs(left[i] - right[i])
        sum_list.append(sub)

    # Add all terms together
    difference = sum(sum_list)
    
    return difference

    # order the lists

    # Loop through the lists in order and calculate the difference between every index

def sim_score(left, right):
    # Loop through all in left list
    sim_score = 0
    for i in range(len(left)):
        occurance = right.count(left[i])
        sim_score += occurance * left[i]
    
    return sim_score

main()