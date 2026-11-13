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



