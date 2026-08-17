print("=================================")
print("        EXPENSE TRACKER")
print("=================================")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n----- ADD EXPENSE -----")

        name = input("Enter expense name: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("\nExpense added successfully! ✅")

    elif choice == "2":
        print("\n----- ALL EXPENSES -----")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            for i, expense in enumerate(expenses, start=1):
                print("\nExpense No:", i)
                print("Name:", expense["name"])
                print("Category:", expense["category"])
                print("Amount: ₹", expense["amount"])

    elif choice == "3":
        print("\n----- TOTAL EXPENSES -----")

        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Spending: ₹", total)

    elif choice == "4":
        print("\n----- SEARCH BY CATEGORY -----")

        category = input("Enter category: ")

        found = False

        for expense in expenses:
            if expense["category"].lower() == category.lower():
                print("\nExpense Found! ✅")
                print("Name:", expense["name"])
                print("Category:", expense["category"])
                print("Amount: ₹", expense["amount"])

                found = True

        if found == False:
            print("No expenses found in this category.")

    elif choice == "5":
        print("\n----- DELETE EXPENSE -----")

        try:
            expense_no = int(input("Enter expense number to delete: "))

            if expense_no >= 1 and expense_no <= len(expenses):
                deleted = expenses.pop(expense_no - 1)

                print("\nExpense deleted successfully! ✅")
                print("Deleted:", deleted["name"])

            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "6":
        print("\nThank you for using Expense Tracker! 👋")
        break

    else:
        print("\nInvalid choice! Please try again.")