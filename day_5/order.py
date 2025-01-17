class Order:

    def __init__(self, update, rules):
        self.update = update
        self.rules = rules
    
    def rules_list(self):
        # This is an order-method that takes in a rules-file and spits put an correct order
        # Get list with all rules
        with open(self.rules, 'r') as f:
            txt = f.read()
            rules = txt.split("\n")
            f.close 
        # Split ever element into lists
        for i in range(len(rules)):
            rules[i] = rules[i].split("|")
        return rules
    
    def update_list(self):
        # Put update in list
        update = self.update.split(",")
        return update

    def find_correct_order(self):
        update = self.update_list()
        rules = self.rules_list()
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
        
    def correct_wrong_order(self):
        update = self.update_list()
        rules = self.rules_list()
        any_swap = False    # Track if any swap was made during the 

        # Simple bubble sort
        n = len(update)
        for i in range(n):
            for j in range(0, n - i - 1):
                current = update[j]
                next_num = update[j + 1]

                # Check if this pair needs to be swaped
                for rule in rules:
                    if current in rule and update[j + 1] in rule:
                        # Check if they are in the right position
                        if rule[0] != update[j] and rule[1] != update[j + 1]:
                            update[j], update[j + 1] = update[j + 1], update[j]
                            any_swap = True
                            break

        # Check if update has been tampered with
        if any_swap:
            # Check middle element in update and 
            middle_term = update[len(update) // 2]
            return int(middle_term)
        return False

