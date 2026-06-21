# Expense Tracker

total = 0

print("=== Expense Tracker ===")
print("Type 'quit' to stop.\n")

while True:
    expense = input("Enter expense amount: ")

    if expense.lower() == "quit":
        break

    try:
        expense = float(expense)
        total += expense
        print(f"Current Total: ₹{total}")
    except ValueError:
        print("Invalid input! Please enter a number.")

print("\n=== Summary ===")
print(f"Total Spent: ₹{total}")