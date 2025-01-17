from order import Order

def main():
    updates_file = "updates.txt"
    rules_file = "rules.txt"
    with open(updates_file, 'r') as f:
        txt = f.read()
    updates = txt.split("\n")
    sum_correct = 0
    sum_wrong = 0
    for update in updates:
        correct_order1 = Order(update, rules_file)
        if correct_order1.find_correct_order():
            sum_correct += correct_order1.find_correct_order()
            #print("Correct Order: ", update)
        if  correct_order1.correct_wrong_order():
            sum_wrong += correct_order1.correct_wrong_order()
            #print("Wrong order: ", update)
    print("Sum_correct: ", sum_correct)
    print("Sum_wrong: ",sum_wrong)


main()