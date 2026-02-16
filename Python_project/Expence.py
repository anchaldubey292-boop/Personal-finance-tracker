expenses = []
print("Welcome to Expense Tracker")

while True:
    print("\n MENU ")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Khrcha")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Add expense
    if choice == 1:
        date = input("Enter date of expense: ")
        category = input("Type of Expense (FOOD, TRAVEL, MAKEUP, BOOKS): ")
        description = input("More Details: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("Expense added successfully!")

    # View all expenses
    elif choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            for exp in expenses:
                print(f"Date: {exp['date']}, Category: {exp['category']}, "
                      f"Description: {exp['description']}, Amount: {exp['amount']}")

    # View total expense
    elif choice == 3:
        total = sum(exp['amount'] for exp in expenses)
        print(f"Total Khrcha: {total}")

    # Exit
    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")