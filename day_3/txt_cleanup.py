# Clean up the corrupted file and fin the sum of all multiplications
def main():    
    # Import file
    f = open("corrupted.txt", "r")
    s = f.read() # String
    #2 find all instances of the 'mul where there is only (number,number) in that order
    # else it is false
    # Filter everything into a list
    all_mul = s.split("mul")
    for i in all_mul:
        print(i)
    # Remove everything not a comma, parantheses or number
    

main()