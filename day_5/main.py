from order import Order

def main():
    updates_file = "updates.txt"
    rules_file = "rules.txt"
    with open(updates_file, 'r') as f:
        txt = f.read()
    updates = txt.split("\n")
    sum = 0
    for update in updates:
        correct_order1 = Order(update, rules_file)
        if correct_order1.correct_order():
            sum += correct_order1.correct_order()
    print(sum)

main()