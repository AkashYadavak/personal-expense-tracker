from storage import load_expenses, save_expenses
from datetime import datetime


def add_expense():
    try:
        amount = float(input("Enter amount (INR): "))
        category = input("Enter category (Food/Travel/Bills/Shopping/Other): ").strip().title()
        description = input("Enter description: ").strip()
        date_str = datetime.now().strftime("%Y-%m-%d")

        expenses = load_expenses()
        new_id = max([e["id"] for e in expenses], default=0) + 1
        expenses.append({
            "id": new_id,
            "amount": amount,
            "category": category,
            "description": description,
            "date": date_str
        })
        save_expenses(expenses)
        print(f"Expenses added successfully (ID: {new_id}).")
    except ValueError:
        print("Invalid amount! Please enter a numeric value.")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'ID':<5} {'Date':<12} {'Category:<12'} {'Amount':<10} {'Description'}")
    print('-' * 60)
    for e in expenses:
        print(f"{e['id']:<5} {e['date']:<12} {e['category']:<12} {e['amount']:<10.2f} {e['description']}")





