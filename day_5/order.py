class Order:

    def __init__(self, update, rules):
        self.update = update
        self.rules = rules

    def correct_order(self):
        # This is an order-method that takes in a rules-file and spits put an correct order
        # Get list with all rules
        with open(self.rules, 'r') as f:
            txt = f.read()
            rules = txt.split("\n")
            f.close 
        # Split ever element into lists
        for i in range(len(rules)):
            rules[i] = rules[i].split("|")
        # Put update in list
        update = self.update.split(",")
        # Sort all nums
        
        for i in range(len(update)):
            for j in range(len(rules)):
                # Check if the number we are checking is in the rules[j]
                if update[i] in rules[j]:
                    if update[i] == rules[j][0]:
                        # The number we're checking is dominant
                        # Check if other number is before the one we're checking
                        for k in range(i - 1):
                            if update[k] == rules[j][1]:
                                return False
                    else:
                        # The number we're checking is not dominant
                        # Check if the other number is after the one we're checking
                        for k in range(i + 1, len(update)):
                            if update[k] == rules[j][0]:
                                return False
        # If the update made it through all the checks
        # Extract the middle-term and return
        middle_term = update[len(update) // 2]
        return int(middle_term)
        
    
        

                            
                        
        
