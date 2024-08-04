import json
import os

# File to store expenses
EXPENSES_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from a file."""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to a file."""
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Add a new expense."""
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }

    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses to display.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: ${expense['amount']:.2f}, Category: {expense['category']}, Description: {expense['description']}")

def expense_summary(expenses):
    """Show summary of expenses by category."""
    summary = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f"Category: {category}, Total: ${total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            expense_summary(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
