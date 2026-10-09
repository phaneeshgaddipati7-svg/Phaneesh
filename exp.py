
budget = float(input("Enter your monthly budget: ₹"))

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Check Remaining Budget")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Enter a valid amount!")
        else:
            expenses.append((name, amount))
            print("Expense added successfully!")

    elif choice == "2":
        total = 0
        print("\n--- Expense List ---")

        for name, amount in expenses:
            print(name, ":", "₹", amount)
            total += amount

        print("Total Spent: ₹", total)

    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        remaining = budget - total

        print("Monthly Budget: ₹", budget)
        print("Total Spent: ₹", total)
        print("Remaining Budget: ₹", remaining)

        if remaining < 0:
            print("Warning: You exceeded your budget!")

    elif choice == "4":
        print("Thank you for using Smart Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")